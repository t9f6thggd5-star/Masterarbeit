#!/usr/bin/env python3
"""
lint.py

Consistency checks across schema.yaml, templates/ and every real entry
under research/ and wiki/. This is the replacement for the "/wiki lint"
idea from le0nce/LLM-Wiki, rewritten against this repository's own
CLAUDE.md rules instead of a generic wiki model. It checks things a
human (or Claude, mid-conversation) would otherwise have to remember to
check by hand every time:

  - structural symmetry between R1/R2/R3 and between GL24h/GL75
    (CLAUDE.md section 3)
  - every entry's ID prefix matches its own declared scope
  - ID category codes actually used are covered by schema.yaml
  - required fields (per templates/*.md) are filled in
  - controlled-vocabulary fields actually appear in schema.yaml
    (CLAUDE.md rule 12)
  - no unreviewed CLAUDE_DRAFT entry is cited elsewhere as if confirmed
    (CLAUDE.md section 14)
  - duplicate IDs

It does NOT check the external sources folder (outside this repository,
not guaranteed reachable from wherever this script runs) and does NOT
try to judge scientific correctness — only the repository's own
structural rules.

Usage:
    python3 scripts/lint.py

Exit code is 1 if any ERROR-level finding exists, 0 otherwise (WARNING/
INFO findings never fail the run).
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _repo_lib import (  # noqa: E402
    ROOT, load_entries, load_schema, get_path, is_blank,
    collect_reference_ids,
)


class Finding:
    def __init__(self, severity: str, area: str, location: str, message: str):
        self.severity = severity  # ERROR | WARNING | INFO
        self.area = area
        self.location = location
        self.message = message

    def line(self) -> str:
        return f"[{self.severity}] ({self.area}) {self.location}: {self.message}"


REQUIRED_FIELDS: dict[str, list[str]] = {
    "ASSUMPTION": ["assumption_id", "scope.connection", "scope.material",
                   "statement", "reason", "certainty"],
    "CALCULATION": ["calculation_id", "scope.connection", "scope.material",
                     "method", "result.quantity", "result.value",
                     "result.unit", "certainty"],
    "CONCLUSION": ["conclusion_id", "scope.connection", "scope.material",
                    "based_on", "statement", "certainty",
                    "authored_by"],
    "DECISION": ["decision_id", "scope.connection", "scope.material",
                  "question", "decision", "reason", "date"],
    "EXPERIMENTAL_RESULT": ["result_id", "scope.connection", "scope.material",
                              "scope.experiment_level", "derived_from", "n",
                              "method", "result.quantity", "result.value",
                              "result.unit", "certainty"],
    "HYPOTHESIS": ["hypothesis_id", "scope.connection", "scope.material",
                    "statement", "certainty", "authored_by"],
    "INTERPRETATION": ["interpretation_id", "scope.connection", "scope.material",
                         "interpretation", "certainty", "authored_by"],
    "PROCESSED_DATA": ["processing_id", "scope.connection", "scope.material",
                         "scope.experiment_level", "input", "method",
                         "output.quantity", "output.value", "output.unit",
                         "certainty"],
    "RAW_MEASUREMENT": ["measurement_id", "scope.connection", "scope.material",
                          "scope.experiment_level", "experiment_id", "quantity",
                          "value", "unit", "certainty"],
    "CLAIM": ["claim_id", "scope.connection", "scope.material", "claim.text",
               "claim.source", "claim.source_type", "claim.certainty"],
    "OPEN_QUESTION": ["open_question_id", "scope.connection", "scope.material",
                        "status", "question"],
}

# Which id-field implies which category-code token(s) to look for in the ID.
ID_FIELD_TO_CATEGORY = {
    "assumption_id": ["ASS"],
    "calculation_id": ["CALC"],
    "conclusion_id": ["CON"],
    "decision_id": ["DEC"],
    "hypothesis_id": ["HYP"],
    "interpretation_id": ["INT"],
    "open_question_id": ["OPQ"],
    "claim_id": ["CLAIM"],
    "experiment_id": ["FULL", "CMP"],
    "measurement_id": ["RAW"],
    "processing_id": ["PROC"],
    "result_id": ["RES"],
}

GENERALIZING_WORDS = [
    "typically", "typical", "usually", "generally shows", "characteristic behavior",
    "typisch", "typischerweise", "in der regel", "üblicherweise", "generell zeigt",
]


def parse_schema_category_codes(schema_text: str) -> set[str]:
    # The CATEGORY list in schema.yaml's comment block wraps across
    # multiple '#'-prefixed lines before the next labelled line (NUMBER:).
    m = re.search(r"CATEGORY:\s*(.*?)\n\s*#\s*NUMBER:", schema_text, re.DOTALL)
    if not m:
        return set()
    raw = m.group(1)
    # strip leading '#' comment markers from continuation lines
    raw = re.sub(r"\n\s*#\s*", " ", raw)
    codes = set()
    for token in raw.split("|"):
        token = token.strip()
        code = token.split()[0] if token else ""
        code = code.strip()
        if code:
            codes.add(code)
    return codes


def check_required_fields(entries) -> list[Finding]:
    findings = []
    for e in entries:
        if e.type not in REQUIRED_FIELDS:
            findings.append(Finding(
                "WARNING", "unknown-type", e.rel_path,
                f"entry type '{e.type}' has no known required-field list in lint.py "
                f"(new template added since lint.py was written? extend REQUIRED_FIELDS)."
            ))
            continue
        for field in REQUIRED_FIELDS[e.type]:
            value = get_path(e.fm, field)
            if is_blank(value):
                findings.append(Finding(
                    "ERROR", "required-field", e.rel_path,
                    f"required field '{field}' is empty/missing for a {e.type} entry."
                ))
        # reviewed is only mandatory when authored_by == CLAUDE_DRAFT
        if e.authored_by == "CLAUDE_DRAFT" and e.reviewed is None:
            findings.append(Finding(
                "ERROR", "required-field", e.rel_path,
                "authored_by is CLAUDE_DRAFT but 'reviewed' is not set "
                "(must be explicit true/false, CLAUDE.md section 14)."
            ))
    return findings


def check_controlled_vocabulary(entries, schema: dict) -> list[Finding]:
    findings = []
    connections = set(schema["scope_dimensions"]["connection"])
    materials = set(schema["scope_dimensions"]["material"])
    exp_levels = set(schema["scope_dimensions"]["experiment_level"])
    authored_by_values = set(schema["authored_by"].keys()) if isinstance(schema["authored_by"], dict) else set(schema["authored_by"])
    source_type_values = set(schema["source_type"].keys())
    certainty_values = set(schema["certainty"])
    open_question_status_values = set(schema.get("open_question_status", []))

    for e in entries:
        conn = e.scope.get("connection")
        mat = e.scope.get("material")
        lvl = e.scope.get("experiment_level")
        if conn is not None and conn not in connections:
            findings.append(Finding("ERROR", "vocabulary", e.rel_path,
                f"scope.connection '{conn}' is not in schema.yaml scope_dimensions.connection {sorted(connections)}."))
        if mat is not None and mat not in materials:
            findings.append(Finding("ERROR", "vocabulary", e.rel_path,
                f"scope.material '{mat}' is not in schema.yaml scope_dimensions.material {sorted(materials)}."))
        if lvl is not None and lvl not in exp_levels:
            findings.append(Finding("ERROR", "vocabulary", e.rel_path,
                f"scope.experiment_level '{lvl}' is not in schema.yaml scope_dimensions.experiment_level {sorted(exp_levels)}."))
        if e.authored_by is not None and e.authored_by not in authored_by_values:
            findings.append(Finding("ERROR", "vocabulary", e.rel_path,
                f"authored_by '{e.authored_by}' is not in schema.yaml authored_by {sorted(authored_by_values)}."))
        # certainty: the one unified field, on every type except OPEN_QUESTION
        # (which keeps its own status field, checked separately below).
        if e.type != "OPEN_QUESTION" and e.certainty is not None and e.certainty not in certainty_values:
            findings.append(Finding("ERROR", "vocabulary", e.rel_path,
                f"certainty '{e.certainty}' is not in schema.yaml certainty {sorted(certainty_values)}."))
        if e.type == "OPEN_QUESTION" and e.status is not None and e.status not in open_question_status_values:
            findings.append(Finding("ERROR", "vocabulary", e.rel_path,
                f"status '{e.status}' is not in schema.yaml open_question_status {sorted(open_question_status_values)}."))
        claim = e.fm.get("claim") if isinstance(e.fm.get("claim"), dict) else {}
        if claim.get("source_type") and claim["source_type"] not in source_type_values:
            findings.append(Finding("ERROR", "vocabulary", e.rel_path,
                f"claim.source_type '{claim['source_type']}' is not in schema.yaml source_type {sorted(source_type_values)}."))
    return findings


def check_ids(entries, schema_text: str) -> list[Finding]:
    findings = []
    known_categories = parse_schema_category_codes(schema_text)
    seen_ids: dict[str, str] = {}

    for e in entries:
        if not e.id:
            findings.append(Finding("ERROR", "id", e.rel_path,
                "no *_id field found in frontmatter at all."))
            continue

        # duplicate check
        if e.id in seen_ids:
            findings.append(Finding("ERROR", "id", e.rel_path,
                f"ID '{e.id}' is also used by {seen_ids[e.id]} — IDs must be unique "
                f"and are never reused (CLAUDE.md section 17)."))
        else:
            seen_ids[e.id] = e.rel_path

        # ID prefix must match the entry's own declared scope
        conn = e.scope.get("connection")
        mat = e.scope.get("material")
        if conn and mat:
            expected_prefix = f"{conn}-{mat}-"
            if not e.id.startswith(expected_prefix):
                findings.append(Finding("ERROR", "id", e.rel_path,
                    f"ID '{e.id}' does not start with '{expected_prefix}', which is "
                    f"what this entry's own scope (connection={conn}, material={mat}) implies."))

        # category code must be one schema.yaml documents
        if e.id_field in ID_FIELD_TO_CATEGORY:
            expected_codes = ID_FIELD_TO_CATEGORY[e.id_field]
            tokens = e.id.split("-")
            if not any(code in tokens for code in expected_codes):
                findings.append(Finding("WARNING", "id", e.rel_path,
                    f"ID '{e.id}' does not contain the expected category code "
                    f"{expected_codes} as a '-'-separated token — check against "
                    f"schema.yaml's id_pattern."))
            if known_categories and not (set(expected_codes) & known_categories):
                findings.append(Finding("ERROR", "schema-consistency", "schema.yaml",
                    f"category code {expected_codes} (used by '{e.id_field}' in "
                    f"templates/) is not listed in schema.yaml's own CATEGORY comment "
                    f"{sorted(known_categories)}. Extend schema.yaml first (CLAUDE.md rule 12) "
                    f"before this ID pattern is used further — first seen at {e.rel_path}."))

        # trailing running number should be 3 digits
        last_token = e.id.split("-")[-1]
        if not re.fullmatch(r"\d{3}", last_token):
            findings.append(Finding("WARNING", "id", e.rel_path,
                f"ID '{e.id}' does not end in a 3-digit running number as schema.yaml's "
                f"id_pattern specifies (got '{last_token}')."))
    return findings


def check_claude_draft_citations(entries) -> list[Finding]:
    findings = []
    by_id = {e.id: e for e in entries if e.id}
    for e in entries:
        for ref in collect_reference_ids(e.fm):
            target = by_id.get(ref)
            if target is None:
                continue
            if target.authored_by == "CLAUDE_DRAFT" and target.reviewed is not True:
                findings.append(Finding("ERROR", "unreviewed-citation", e.rel_path,
                    f"cites '{ref}' ({target.rel_path}), which is authored_by=CLAUDE_DRAFT "
                    f"and not yet reviewed:true. Per CLAUDE.md section 14 this must be "
                    f"flagged explicitly wherever it is used, not cited as confirmed."))
    return findings


def check_symmetry() -> list[Finding]:
    findings = []
    for base in ["research", "wiki"]:
        base_path = ROOT / base
        if not base_path.exists():
            continue
        for group_name, conns in [("connections", ["R1", "R2", "R3"])]:
            existing = [c for c in conns if (base_path / c).exists()]
            if len(existing) < 2:
                continue
            # compare, for each material, the recursive set of subfolder
            # names relative to <base>/<connection>/<material>/
            materials = set()
            for c in existing:
                for child in (base_path / c).iterdir():
                    if child.is_dir():
                        materials.add(child.name)
            for mat in sorted(materials):
                subfolder_sets = {}
                for c in existing:
                    mat_dir = base_path / c / mat
                    if not mat_dir.exists():
                        subfolder_sets[c] = None
                        continue
                    subfolder_sets[c] = frozenset(
                        p.relative_to(mat_dir).as_posix()
                        for p in mat_dir.rglob("*") if p.is_dir()
                    )
                reference_conn = existing[0]
                reference_set = subfolder_sets.get(reference_conn)
                for c in existing[1:]:
                    this_set = subfolder_sets.get(c)
                    if this_set is None and reference_set is not None:
                        findings.append(Finding("ERROR", "symmetry", f"{base}/{c}",
                            f"'{base}/{c}/{mat}/' is missing entirely, but "
                            f"'{base}/{reference_conn}/{mat}/' exists (CLAUDE.md section 3: "
                            f"R1/R2/R3 must be structurally identical)."))
                        continue
                    if this_set != reference_set:
                        only_in_ref = (reference_set or set()) - (this_set or set())
                        only_in_this = (this_set or set()) - (reference_set or set())
                        detail = []
                        if only_in_ref:
                            detail.append(f"missing here: {sorted(only_in_ref)}")
                        if only_in_this:
                            detail.append(f"extra here (not in {reference_conn}): {sorted(only_in_this)}")
                        findings.append(Finding("ERROR", "symmetry", f"{base}/{c}/{mat}",
                            f"subfolder structure differs from {base}/{reference_conn}/{mat} — " + "; ".join(detail)))
    return findings


def check_n1_language(entries) -> list[Finding]:
    findings = []
    for e in entries:
        if e.type != "EXPERIMENTAL_RESULT":
            continue
        n = e.fm.get("n")
        if n == 1 or n == "1":
            lower_body = e.body.lower()
            for word in GENERALIZING_WORDS:
                if word in lower_body:
                    findings.append(Finding("WARNING", "n1-language", e.rel_path,
                        f"n=1 but the entry text contains '{word}', which reads as "
                        f"generalizing language. CLAUDE.md section 15: a single "
                        f"specimen must be reported as one data point, not as typical "
                        f"or characteristic. (Heuristic word match — please confirm "
                        f"by reading the sentence in context.)"))
    return findings


def render_report(findings: list[Finding], entry_count: int) -> str:
    lines = ["# Lint report (auto-generated — do not edit by hand)", ""]
    lines.append(f"Generated by `scripts/lint.py` against {entry_count} entries under "
                 f"`research/` and `wiki/`. Regenerate with `python3 scripts/lint.py`.")
    lines.append("")
    lines.append("Does **not** cover the external sources folder (outside this "
                 "repository) or scientific correctness — only this repository's own "
                 "structural rules from CLAUDE.md and schema.yaml.")
    lines.append("")
    by_severity = defaultdict(list)
    for f in findings:
        by_severity[f.severity].append(f)
    lines.append(f"**{len(by_severity['ERROR'])} error(s), "
                 f"{len(by_severity['WARNING'])} warning(s), "
                 f"{len(by_severity['INFO'])} info.**")
    lines.append("")
    if not findings:
        lines.append("No findings.")
        return "\n".join(lines)
    for severity in ["ERROR", "WARNING", "INFO"]:
        items = by_severity[severity]
        if not items:
            continue
        lines.append(f"## {severity} ({len(items)})")
        lines.append("")
        for f in items:
            lines.append(f"- **{f.area}** — `{f.location}` — {f.message}")
        lines.append("")
    return "\n".join(lines)


def run() -> int:
    schema = load_schema()
    schema_text = (ROOT / "schema.yaml").read_text(encoding="utf-8")
    entries, parse_errors = load_entries()

    findings: list[Finding] = []
    for path, msg in parse_errors:
        findings.append(Finding("ERROR", "parse", path.relative_to(ROOT).as_posix(), msg))

    findings += check_required_fields(entries)
    findings += check_controlled_vocabulary(entries, schema)
    findings += check_ids(entries, schema_text)
    findings += check_claude_draft_citations(entries)
    findings += check_symmetry()
    findings += check_n1_language(entries)

    report = render_report(findings, len(entries))
    out_path = ROOT / "_index" / "lint_report.md"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"\nWrote {out_path.relative_to(ROOT)}")

    return 1 if any(f.severity == "ERROR" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(run())
