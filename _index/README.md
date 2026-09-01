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

Run both after every change to `research/` or `wiki/` (new entry, edited
frontmatter, renamed file):

```
python3 scripts/build_index.py
python3 scripts/lint.py
```

`lint.py` exits with status 1 if it found any ERROR-level finding (0 for
WARNING/INFO only), so it can be wired into a pre-commit hook later if
useful.

## What this does not cover

- The external sources folder (outside this Git repository) is not
  read by these scripts. Its own R1/R2/R3/COMMON symmetry needs to be
  checked separately (by hand, or with a small variant of `lint.py`
  pointed at that folder, if that becomes worth automating later).
- Scientific correctness. This only checks the repository's own
  structural rules (CLAUDE.md, `schema.yaml`) — not whether a claim,
  calculation or interpretation is actually right.
