# Master Thesis Research Wiki

## 1. Purpose

This repository is the research knowledge base for a master thesis
investigating three rigid timber frame corner connections.

The research investigates:

- R1 – Frame Corner 1
- R2 – Frame Corner 2
- R3 – Frame Corner 3

Each connection is investigated using two materials:

- GL24h
- GL75

The research includes component tests, full connection tests, analytical
calculations, normative approaches, scientific literature, observations,
experimental results, interpretations, hypotheses and conclusions.

Sources are **not** treated as unconditional facts. A source is a
document that makes a claim, states a norm, reports a result, or shows a
plan. Whether that claim holds for a given scope is a separate question
the wiki and the researcher answer explicitly — see Section 10.

**Original source files (norms, literature, books, plans, raw measurement
exports, scans) are not stored in this Git repository.** They live in a
separate external sources folder (outside this repository, e.g. in
OneDrive), kept apart deliberately: those files can be large and are
unrelated to the version history that matters for this repository, and
keeping the two physically separate avoids sync conflicts between a
cloud-sync tool and Git. The external sources folder mirrors the same
categorization used throughout this document — `common/norms/`,
`common/literature/`, `common/books/`, `common/general/`, and per
connection `R1/R2/R3` × `GL24h/GL75` × `experiments/components/`,
`experiments/full_connection/`, `plans/`. All rules in this file about
"sources" (never modify them, cite them by ID, distinguish source types,
etc.) apply identically regardless of where the files physically live —
only the storage location changed, not the rules. Every source is still
registered with a stable ID in `bibliography/sources.yaml`, which records
its location in the external folder; claims and templates reference that
ID, never a raw file path.

All controlled vocabulary referenced below (source types, research types,
status values, certainty levels, ID pattern) is defined once in
`schema.yaml`. Do not invent new values ad hoc — extend `schema.yaml`
first, then use the new value consistently.

Not all content in this repository is about a specific connection.
`research/` and `wiki/` each have a `thesis/` category alongside `common/`
and `R1/R2/R3/` for the non-connection-specific chapters of the thesis
itself — abstract, introduction, fundamentals, state of the art,
methodology, discussion, limitations, conclusion, outlook, and a `general/`
catch-all for anything not yet fitting one of these. `common/` is
technical knowledge that applies across all three connections (norms,
cross-cutting methods, literature feeding into claims/calculations);
`thesis/` is the narrative synthesis of the thesis document itself.

The external sources folder has no separate `thesis/` category: a source
is not tied to a single chapter — the same paper or norm can be cited in
the introduction, the state of the art, and as evidence for an
R1-specific claim at once. Which chapter cites a source follows from the
`source` field of the relevant claim, not from where the file is stored.
All sources used for `thesis/` chapters live in the external folder's
`common/`, categorized by source type as usual. See the `README.md` in
each of `research/thesis/` and `wiki/thesis/` for the chapter list.

---

## 2. Scope

Every project-specific statement must be associated with a scope. The
scope has three dimensions, defined in `schema.yaml`:

- **Connection**: COMMON, R1, R2, R3
- **Material**: COMMON, GL24h, GL75
- **Experiment level**: COMMON, COMPONENT, FULL_CONNECTION

Content under `thesis/` (Section 1) is, by its nature, above this scope
system — it is not scoped to a connection or material at all rather than
scoped to `COMMON`. It does not need the `scope` field used elsewhere.

---

## 3. Structural Symmetry — No Default Connection or Material

**R1, R2 and R3 must be treated as structurally identical and must be
represented with exactly the same sub-structure and the same categories
in the external sources folder, `research/` and `wiki/`.** The same
applies to GL24h and GL75 within each connection. This symmetry
requirement applies only to the `R1/R2/R3` branches — it does not apply
to `common/` or `thesis/` (the latter existing only under `research/` and
`wiki/`, not in the external sources folder), which exist exactly once
and are not connection-specific by design.

No connection and no material may be treated as a "standard case" or
default:

- Do not give R1 additional folders, fields, or shortcuts that R2 and R3
  do not also have.
- Do not assume information is generally valid just because it was first
  entered under R1, or under GL24h.
- If a folder or category exists for one connection or material, it must
  exist — even if currently empty — for all others.
- When creating new categories later in the thesis, add them under
  `common/` first if they could plausibly apply to all connections, and
  only add them per-connection if they are genuinely connection-specific
  — and then add the identical category to R1, R2 **and** R3 at the same
  time.

This symmetry exists to prevent Claude (and the researcher) from
unconsciously privileging whichever connection was documented first.

---

## 4. Scope Isolation

Information must never be transferred between different connections,
materials or experiment levels without explicit evidence.

Never assume:

- R1 = R2 = R3
- GL24h = GL75
- COMPONENT = FULL_CONNECTION

Never use an experimental result from one connection as evidence for
another connection unless the relationship is explicitly established and
documented (see Section 12, Cross-Connection Analysis).

If the scope of a piece of information is unclear, use `UNKNOWN` and do
not guess.

---

## 5. Source Types

See `schema.yaml -> source_type` for the full definition. Summary:

- **NORMATIVE** — standards and regulations.
- **LITERATURE** — scientific papers, books, journals, conference papers.
- **PRIMARY_DATA** — original experimental data produced by this research.
- **PLAN** — drawings, test plans, technical plans.
- **MANUFACTURER_DATA** — manufacturer datasheets/claims.
- **REPORT** — expert reports / Gutachten.

---

## 6. Research Types

See `schema.yaml -> research_type`. These are **not** sources — they are
outputs of the researcher's own process:

CALCULATION, PROCESSED_DATA, EXPERIMENTAL_RESULT, RAW_MEASUREMENT,
OBSERVATION, ASSUMPTION, HYPOTHESIS, INTERPRETATION, CONCLUSION, DECISION.

---

## 7. Data Provenance

Always distinguish, and never blur, the following chain:

```
RAW MEASUREMENT
      ↓
PROCESSED DATA
      ↓
EXPERIMENTAL RESULT
      ↓
INTERPRETATION
      ↓
CONCLUSION
```

- Never describe a derived result as measured.
- Never describe an interpretation as an observation.
- Never describe a calculation result as experimental data.
- Every derived entry must reference the entry/entries (by ID, see
  Section 14) it was derived from.

---

## 8. Experimental Data

Experimental measurements are primary project data (`PRIMARY_DATA`). They
do not require an external publication to be valid, but measured values
and interpretations must be kept strictly separate.

A directly recorded numerical measurement is `RAW_MEASUREMENT`; a value
derived from it through processing is `PROCESSED_DATA` or
`EXPERIMENTAL_RESULT`, never described as directly measured. A statement
about the cause of an observed effect (e.g. attributing a failure to a
specific mechanism) is an `INTERPRETATION`, unless it is directly and
unambiguously established by the raw observation itself — in which case
it is an `OBSERVATION`, not an interpretation.

---

## 9. Calculations

Calculations are research outputs, not sources. Every calculation entry
should identify: calculation ID, scope, input data, normative basis,
literature basis, assumptions used, calculation method, result, and
units. Never present an own calculation as a normative statement.

---

## 10. Uncertainty and Claims

The wiki must preserve uncertainty rather than resolve it prematurely.
Use the `certainty_level` values from `schema.yaml`: ESTABLISHED,
MEASURED, CALCULATED, ASSUMED, HYPOTHESIZED, INTERPRETED, UNKNOWN. Never
increase the certainty of a statement during synthesis.

Every factual claim recorded in the wiki should be expressed as a
structured claim (see `templates/claim.md`), not as an unattributed
sentence: text of the claim, the source it comes from (an id from
`bibliography/sources.yaml`), page reference, source type, claim status
and confidence — never a bare assertion without these fields filled in.

`claim_status` distinguishes four kinds of statement (schema.yaml):
NORMATIVE (a standard requires it), SOURCE_CLAIM (a source reports it,
not independently verified), EVIDENCE (supported by empirical/
experimental data, with sample size/methodology noted where relevant),
and SYNTHESIS (the researcher's own synthesis across sources — must never
be mixed into the same block as an original source claim).

---

## 11. Contradictions

Never silently resolve contradictions. If two sources or two results
disagree:

1. Preserve both claims.
2. Identify their scopes.
3. Identify their source/research types.
4. Identify the evidence supporting each.
5. Explain possible reasons for the difference (methodology, boundary
   conditions, scope, sample size, etc.).
6. Do not arbitrarily select one as correct — record both under
   `wiki/.../contradictions` (or the relevant `common/` equivalent) if
   such a category is added.

---

## 12. Cross-Connection Analysis

R1, R2 and R3 may only be combined or compared when:

- explicitly requested by the researcher, or
- the information is located in `wiki/cross_connection/`.

The same restriction applies to GL24h vs. GL75 comparisons. When
comparing variants, always label the corresponding connection and
material explicitly in the output — never present a cross-connection
conclusion as if it were scoped to a single connection.

---

## 13. Research State vs. Established Knowledge

Files under `research/` represent the current working state and may
contain provisional assumptions, hypotheses and decisions that later
turn out to be wrong. Working assumptions must never be presented as
established scientific facts, either in the wiki or in conversation.
When an assumption in `research/.../assumptions/` is superseded, do not
delete or silently overwrite it — mark its status and add the
superseding entry, so the evolution remains traceable.

---

## 14. Authorship and Review Status

Interpretations, conclusions and hypotheses vary in how much of the
actual scientific judgement is Claude's proposal versus the researcher's
own. To keep this traceable, every entry in `research/.../interpretations/`,
`research/.../conclusions/` and `research/.../hypotheses/` carries an
`authored_by` field (`RESEARCHER` or `CLAUDE_DRAFT`, see `schema.yaml`)
and a `reviewed` field (`true`/`false`).

- A new entry that Claude proposes during a conversation is always
  created with `authored_by: CLAUDE_DRAFT` and `reviewed: false`.
- `reviewed` is set to `true` only by the researcher's own decision —
  never by Claude itself, even if the researcher appears to agree in
  conversation. Claude may point out that an entry is still unreviewed,
  but does not change the field itself.
- An entry the researcher writes or edits directly is `authored_by:
  RESEARCHER`; `reviewed` does not apply and may be left empty.
- An unreviewed `CLAUDE_DRAFT` entry must never be cited elsewhere (e.g.
  in a `CONCLUSION`, in another chapter, or in the thesis text) as if it
  were confirmed. Claude flags this explicitly whenever such an entry is
  used as input elsewhere.

---

## 15. Sample Size and Statistical Weight

Every `EXPERIMENTAL_RESULT` entry records `n`, the number of specimens or
repetitions the result is based on. A result with `n = 1` is a single
observation, not a characteristic or typical value, and must never be
described using generalizing language ("typically", "the connection
shows...") — it is reported as a single data point with this limitation
stated explicitly. Aggregating statistics (mean, scatter, a
normatively-derived characteristic value) may only be computed and
presented as such once `n > 1`, and the aggregation method must be
documented in the corresponding `PROCESSED_DATA` or `EXPERIMENTAL_RESULT`
entry.

---

## 16. Units

Before entering real measurement or calculation data, define one fixed
unit per physical quantity in `schema.yaml -> unit_convention` (e.g. one
unit for force, one for length, one for stress, and so on) and apply it
consistently across all entries of that quantity, regardless of scope or
source. Do not decide the unit per entry — that is exactly what causes
silent mismatches between sources, own measurements and calculations.

If a source (a paper, a norm, a datasheet) or a measurement system
originally reports a value in a different unit, convert it to the
thesis's unit convention and record both: the converted `value`/`unit`
used throughout the repository, and the `original_value`/`original_unit`
as reported by the source, so the conversion stays traceable and
reviewable.

---

## 17. Identifiers and Provenance

Use the ID pattern defined in `schema.yaml -> id_pattern`:
`<CONNECTION>-<MATERIAL>-<CATEGORY>-<NUMBER>`. IDs are never reused and
never renumbered, even if an entry is later superseded or found to be
wrong.

Whenever possible, preserve: source ID, experiment ID, calculation ID,
page number, figure number, table number, measurement file reference,
and processing method. Never invent source information. If provenance is
unavailable, explicitly set status to `PROVENANCE_UNKNOWN` rather than
guessing.

---

## 18. Answering Questions

Before answering a research question:

1. Determine the required connection scope (R1/R2/R3/COMMON).
2. Determine the material scope (GL24h/GL75/COMMON).
3. Determine the experiment level (COMPONENT/FULL_CONNECTION/COMMON).
4. Load COMMON information where applicable.
5. Load only the relevant project-specific information — do not pull in
   other connections/materials "for context" unless asked.
6. Check for known contradictions in the relevant scope.
7. Distinguish sources, measurements, calculations, interpretations and
   conclusions explicitly in the answer.
8. State uncertainty/claim_status where relevant.

If the user asks about R1/GL24h, do not silently use R2/GL75 information,
even as a plausibility check, without saying so explicitly.

---

## 19. General Rules

1. Never modify original sources, wherever they are stored (the external
    sources folder, not this repository).
2. Never present an interpretation as an established fact.
3. Every factual claim must have a source reference.
4. Preserve page numbers whenever possible.
5. Distinguish normative requirement, source claim, empirical evidence,
   interpretation and synthesis (Section 10).
6. Never silently resolve contradictions (Section 11).
7. When sources disagree, preserve both positions and explain the
   disagreement.
8. Prefer primary sources over secondary sources.
9. Never invent citations.
10. If evidence is insufficient, explicitly state "insufficient evidence"
    rather than filling the gap.
11. R1, R2 and R3 must be treated as structurally and epistemically
    equal — no connection or material is a default (Section 3).
12. Use only the controlled vocabulary in `schema.yaml`; extend it there
    before using a new value.
13. Mark every Claude-proposed interpretation, conclusion or hypothesis
    as `CLAUDE_DRAFT` and unreviewed until the researcher confirms it
    (Section 14).
14. Never describe a single-specimen result (`n = 1`) as typical or
    characteristic (Section 15).
15. Define each quantity's unit once in `schema.yaml` and apply it
    consistently; always preserve the original value/unit when
    converting (Section 16).
