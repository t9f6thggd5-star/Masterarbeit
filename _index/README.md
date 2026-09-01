# _index/

Auto-generated catalog and lint report for this repository. Nothing here
is hand-written or hand-edited — every file in this folder is regenerated
from the real frontmatter in `research/` and `wiki/` by the scripts in
`scripts/`. This replaces the `_index/` catalog + operation-log idea from
[le0nce/LLM-Wiki](https://github.com/le0nce/LLM-Wiki), rebuilt against
this repository's own `schema.yaml` instead of a generic entities/
concepts model.

- `catalog.yaml` — machine-readable: every entry's ID, type, scope,
  status, authored_by/reviewed, and file path. This is what Claude should
  read first when asked "what exists for R2/GL75" instead of walking
  every folder by hand.
- `INDEX.md` — the same data, rendered as tables grouped by
  connection/material, for quick human browsing.
- `lint_report.md` — structural findings: R1/R2/R3 symmetry violations,
  duplicate or scope-mismatched IDs, missing required fields, values not
  covered by `schema.yaml`'s controlled vocabulary, and any unreviewed
  `CLAUDE_DRAFT` entry cited elsewhere as if confirmed.

## Regenerating

This happens automatically on every `git commit` via the pre-commit hook
in `.githooks/` (see "One-time setup" below). To run it manually anytime:

```
python3 scripts/build_index.py
python3 scripts/lint.py
```

`lint.py` exits with status 1 if it found any ERROR-level finding (0 for
WARNING/INFO only) — that's what makes the pre-commit hook able to block
a commit on a real problem.

## One-time setup per clone/machine

Hooks under `.git/hooks/` are never tracked by Git, so a hook shipped
*inside* the repository (here: `.githooks/pre-commit`) only takes effect
once you point Git at it — once per clone/machine:

```
git config core.hooksPath .githooks
```

Without this step, commits still work, but nothing regenerates the
catalog or blocks a broken commit automatically — you're back to the
manual-only situation this hook exists to avoid.

To skip the check for one commit in an emergency: `git commit --no-verify`
(not recommended — it's exactly the check you'd want on a commit you're
in a hurry with).

## Checking the external sources folder

The external sources folder (outside this Git repository, see
`EXTERNAL_SOURCES.md`) is invisible to these scripts by default — with
one opt-in exception: `lint.py` can cross-check that every
`RAW_MEASUREMENT.experiment_id` actually corresponds to a real
`experiment_metadata.md` registered there (catching a typo'd or
never-registered experiment ID, which nothing else would catch).

To enable it, create a file named `.external_sources_path` at the repo
root (already in `.gitignore` — it's a per-machine path, never shared)
containing just the absolute path to your external sources folder, e.g.
on Windows:

```
C:\Users\Lukas\OneDrive\Masterarbeit\Claude Masterarbeit\sources
```

Without this file, `lint.py` reports a single INFO line noting the check
was skipped, rather than failing — a missing local config file is not a
defect in the repository itself.

## What this still does not cover

- The external sources folder's own R1/R2/R3/COMMON symmetry (separate
  from the experiment-ID cross-check above) — check that separately by
  hand, or extend `lint.py` further if that becomes worth automating.
- Scientific correctness. This only checks the repository's own
  structural rules (CLAUDE.md, `schema.yaml`) — not whether a claim,
  calculation or interpretation is actually right.
