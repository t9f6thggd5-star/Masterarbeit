---
hypothesis_id:            # <CONNECTION>-<MATERIAL>-HYP-<NUMMER>
scope:
  connection:              # R1 | R2 | R3
  material:                # GL24h | GL75
type: HYPOTHESIS
statement:
motivated_by:
tested_by:
certainty: HYPOTHESIZED     # siehe schema.yaml -> certainty (später: CONFIRMED | REJECTED)
superseded_by:             # ID der neueren Hypothese, falls diese hier überholt ist (Abschnitt 13)
authored_by:               # RESEARCHER | CLAUDE_DRAFT
reviewed:                  # true | false — nur relevant bei CLAUDE_DRAFT, wird ausschließlich vom Forschenden gesetzt
---
