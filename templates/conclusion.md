---
conclusion_id:            # <CONNECTION>-<MATERIAL>-CON-<NUMMER>
scope:
  connection:              # R1 | R2 | R3
  material:                # GL24h | GL75
type: CONCLUSION
based_on:                 # ID(s) der zugrundeliegenden Ergebnisse/Berechnungen/Interpretationen
statement:
limitations:
certainty:                 # siehe schema.yaml -> certainty (z. B. ESTABLISHED | MEASURED | INTERPRETED | SYNTHESIS —
                            # je nachdem, worauf die Schlussfolgerung tatsächlich beruht)
superseded_by:             # ID der neueren Schlussfolgerung, falls diese hier überholt ist (Abschnitt 13)
authored_by:               # RESEARCHER | CLAUDE_DRAFT
reviewed:                  # true | false — nur relevant bei CLAUDE_DRAFT, wird ausschließlich vom Forschenden gesetzt
---
