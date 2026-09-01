---
calculation_id:           # <CONNECTION>-<MATERIAL>-CALC-<NUMMER>
scope:
  connection:              # R1 | R2 | R3
  material:                # GL24h | GL75
type: CALCULATION
inputs:
  normative_sources:       # ID(s) aus bibliography/sources.yaml
  literature:              # ID(s) aus bibliography/sources.yaml
  experimental_data:       # ID(s) aus research/.../experimental_results/
  assumptions:             # ID(s) aus research/.../assumptions/
method:
equations:
result:
  quantity:
  value:
  unit:                    # gemäß schema.yaml -> unit_convention
  original_value:          # nur falls ein verwendeter Eingangswert in einer anderen Einheit vorlag
  original_unit:
certainty: CALCULATED    # siehe schema.yaml -> certainty
---

Herleitung / Nachvollziehbarkeit der Berechnung. Nicht als normative
Aussage formulieren — es ist eine eigene Berechnung (siehe CLAUDE.md
Abschnitt 9).
