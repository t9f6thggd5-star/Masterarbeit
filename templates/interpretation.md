---
interpretation_id:        # <CONNECTION>-<MATERIAL>-INT-<NUMMER>
scope:
  connection:              # R1 | R2 | R3
  material:                # GL24h | GL75
type: INTERPRETATION
based_on:
  experimental_results:    # ID(s) aus research/.../experimental_results/
  observations:            # ID(s) von Beobachtungen, falls vorhanden
interpretation:
certainty: INTERPRETED     # siehe schema.yaml -> certainty
superseded_by:             # ID der neueren Interpretation, falls diese hier überholt ist (Abschnitt 13)
authored_by:               # RESEARCHER | CLAUDE_DRAFT
reviewed:                  # true | false — nur relevant bei CLAUDE_DRAFT, wird ausschließlich vom Forschenden gesetzt
---
