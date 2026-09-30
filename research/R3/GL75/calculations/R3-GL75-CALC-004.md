---
calculation_id: R3-GL75-CALC-004
scope:
  connection: R3
  material: GL75
type: CALCULATION
inputs:
  normative_sources: DIN-EN-12369-2-2011
  literature: Buchholz2025
  experimental_data:
  assumptions: R3-COMMON-DEC-010, COMMON-COMMON-DEC-010
method: >
  Wie R3-GL75-CALC-003, korrigiert nach R3-COMMON-DEC-010 (eine 15-mm-Platte je
  Seite, G_v = 520 N/mm²); G_mean Holz = 850 N/mm², b = 160 mm.
equations: >
  c_v,H = 850 · 160 · 800 / 800 = 136,00 kN/mm; c_v,P = 520 · 15 · 800 / 460 =
  13,57 kN/mm je Seite; c_v = 136,00 + 2 · 13,57 = 163,13 kN/mm
result:
  quantity: Schubsteifigkeit des Schubfelds im Riegel (Holz + 2 Verstärkungsplatten)
  value: 163.13
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  Gerechnet im Chat 2026-09-30.
certainty: CALCULATED
superseded_by:
---

Ersetzt R3-GL75-CALC-003 (188,17 kN/mm).
