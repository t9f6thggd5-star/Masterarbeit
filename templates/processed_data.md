---
processing_id:            # <CONNECTION>-<MATERIAL>-<EXPERIMENT-ID>-PROC-<NUMMER>
scope:
  connection:              # R1 | R2 | R3
  material:                # GL24h | GL75
  experiment_level:        # COMPONENT | FULL_CONNECTION
type: PROCESSED_DATA
input:                    # ID(s) der zugrundeliegenden RAW_MEASUREMENT-Einträge
method:
filtering:
correction:
evaluation_range:
output:
  quantity:
  value:
  unit:                    # gemäß schema.yaml -> unit_convention
  original_value:          # nur falls die Eingangsdaten in einer anderen Einheit vorlagen
  original_unit:
status: PROCESSED
---
