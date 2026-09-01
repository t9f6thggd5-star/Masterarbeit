"""
_repo_lib.py

Shared helpers for build_index.py and lint.py. Not a template, not a
schema extension — just parsing/walking logic so both scripts agree on
what an "entry" is and how to read one.

Nothing in here is repository content. It only reads research/ and
wiki/ (never the external sources folder, never bibliography/sources.yaml
as an entry source — that file is handled separately where needed).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any, Iterator

import yaml

ROOT = Path(__file__).resolve().parent.parent

# Folders that hold structured entries. templates/ holds templates (no
# real IDs, frontmatter values are placeholders/comments), so it is
# deliberately excluded. bibliography/ has its own format and is read
# directly by lint.py where needed.
CONTENT_ROOTS = ["research", "wiki"]

# Files that are never entries, wherever they occur. current_state.md is a
# rolling narrative summary (one per connection/material, always named the
# same) rather than a uniquely-ID'd registry entry, so it is structural
# like README.md, not something build_index/lint should expect an *_id in.
SKIP_NAMES = {"README.md", ".gitkeep", "current_state.md"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n?(.*)$", re.DOTALL)


def load_schema() -> dict[str, Any]:
    with open(ROOT / "schema.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def iter_markdown_files() -> Iterator[Path]:
    for root_name in CONTENT_ROOTS:
        root = ROOT / root_name
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if path.name in SKIP_NAMES:
                continue
            yield path


def parse_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str, str | None]:
    """Returns (frontmatter_dict, body, error). frontmatter_dict is None
    if the file has no '---' frontmatter block at all (e.g. a stray file
    that isn't a structured entry)."""
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text, None
    raw_fm, body = m.group(1), m.group(2)
    try:
        fm = yaml.safe_load(raw_fm)
        if fm is None:
            fm = {}
        if not isinstance(fm, dict):
            return None, body, f"frontmatter did not parse to a mapping (got {type(fm).__name__})"
        return fm, body, None
    except yaml.YAMLError as e:
        return None, body, f"YAML parse error: {e}"


ID_FIELD_CANDIDATES = [
    "claim_id", "assumption_id", "calculation_id", "conclusion_id",
    "decision_id", "experiment_id", "result_id", "hypothesis_id",
    "interpretation_id", "open_question_id", "processing_id",
    "measurement_id",
]


def find_id_field(fm: dict[str, Any]) -> tuple[str | None, Any]:
    for key in ID_FIELD_CANDIDATES:
        if key in fm:
            return key, fm[key]
    # fallback: any key ending in _id, in case the frontmatter uses one
    # we don't yet know about (e.g. a future template).
    for key, value in fm.items():
        if isinstance(key, str) and key.endswith("_id"):
            return key, value
    return None, None


# Maps the id-field name to the entry "type" when the frontmatter has no
# explicit `type:` field of its own (claim.md and open_question.md).
ID_FIELD_TO_TYPE = {
    "claim_id": "CLAIM",
    "open_question_id": "OPEN_QUESTION",
}


def entry_type(fm: dict[str, Any], id_field: str | None) -> str | None:
    if fm.get("type"):
        return str(fm["type"])
    if id_field in ID_FIELD_TO_TYPE:
        return ID_FIELD_TO_TYPE[id_field]
    return None


def get_path(d: dict[str, Any], dotted: str) -> Any:
    cur: Any = d
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def is_blank(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    if isinstance(value, (list, dict)) and len(value) == 0:
        return True
    return False


def collect_reference_ids(fm: dict[str, Any]) -> list[str]:
    """Collects every ID-like string referenced from cross-reference
    fields (based_on, derived_from, input, supported_by, ...), so lint.py
    can check whether an entry cites an unreviewed CLAUDE_DRAFT."""
    ref_fields = [
        "based_on", "derived_from", "input", "supported_by",
        "contradicted_by", "superseded_by", "tested_by", "motivated_by",
        "related_sources", "normative_sources", "literature",
        "experimental_data", "assumptions",
    ]
    found: list[str] = []

    def walk(value: Any):
        if value is None:
            return
        if isinstance(value, str):
            # split on commas in case someone wrote "ID1, ID2" in one string
            for token in re.split(r"[,\s]+", value.strip()):
                if token:
                    found.append(token)
        elif isinstance(value, list):
            for item in value:
                walk(item)
        elif isinstance(value, dict):
            for item in value.values():
                walk(item)

    for field in ref_fields:
        if field in fm:
            walk(fm[field])
        # `inputs.normative_sources` etc. (calculation.md nests under `inputs:`)
        if field in fm.get("inputs", {}) if isinstance(fm.get("inputs"), dict) else False:
            walk(fm["inputs"][field])
    if isinstance(fm.get("based_on"), dict):
        # interpretation.md nests based_on.experimental_results / .observations
        for item in fm["based_on"].values():
            walk(item)
    return found


class Entry:
    def __init__(self, path: Path, fm: dict[str, Any], body: str):
        self.path = path
        self.rel_path = path.relative_to(ROOT).as_posix()
        self.fm = fm
        self.body = body
        self.id_field, self.id = find_id_field(fm)
        self.type = entry_type(fm, self.id_field)
        self.scope = fm.get("scope") if isinstance(fm.get("scope"), dict) else {}
        # `certainty` is the one unified field (schema.yaml -> certainty) used by
        # every entry type except OPEN_QUESTION, which keeps its own `status`
        # (OPEN | RESOLVED, schema.yaml -> open_question_status) — a question's
        # resolution state is not a certainty judgement. self.status therefore
        # only ever holds a real value for OPEN_QUESTION entries.
        self.certainty = fm.get("certainty")
        if self.certainty is None and isinstance(fm.get("claim"), dict):
            # claim.md nests it under claim.certainty rather than top-level
            self.certainty = fm["claim"].get("certainty")
        self.status = fm.get("status") if self.type == "OPEN_QUESTION" else None
        self.authored_by = fm.get("authored_by")
        self.reviewed = fm.get("reviewed")


def load_entries() -> tuple[list[Entry], list[tuple[Path, str]]]:
    """Returns (entries, parse_errors). parse_errors is a list of
    (path, message) for files under research/ or wiki/ that could not be
    read as structured entries at all."""
    entries: list[Entry] = []
    errors: list[tuple[Path, str]] = []
    for path in iter_markdown_files():
        fm, body, err = parse_frontmatter(path)
        if err:
            errors.append((path, err))
            continue
        if fm is None:
            errors.append((path, "no YAML frontmatter block found"))
            continue
        entries.append(Entry(path, fm, body))
    return entries, errors
