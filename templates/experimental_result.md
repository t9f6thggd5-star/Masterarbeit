---
result_id:                # <CONNECTION>-<MATERIAL>-<EXPERIMENT-ID>-RES-<NUMMER>
scope:
  connection:              # R1 | R2 | R3
  material:                # GL24h | GL75
  experiment_level:        # COMPONENT | FULL_CONNECTION
type: EXPERIMENTAL_RESULT
derived_from:             # ID(s) der zugrundeliegenden RAW_MEASUREMENT/PROCESSED_DATA-Einträge
n:                        # Anzahl der zugrundeliegenden Prüfkörper/Wiederholungen
method:
result:
  quantity:
  value:
  unit:                    # gemäß schema.yaml -> unit_convention
  original_value:          # nur falls die Eingangsdaten in einer anderen Einheit vorlagen
  original_unit:
status: DERIVED
---

Bei n = 1 ist dieses Ergebnis ein Einzelbefund und wird nicht als
typisches oder charakteristisches Verhalten formuliert (siehe CLAUDE.md,
Abschnitt zu Sample Size).
