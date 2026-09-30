---
calculation_id: R3-GL75-CALC-002
scope:
  connection: R3
  material: GL75
type: CALCULATION
inputs:
  normative_sources: DIN-EN-1993-1-8-2025
  literature:
  experimental_data:
  assumptions: >
    Eine Gewindestange M24 je Lasche (A_s = 353 mm²), L_b = 1660 mm,
    E_s = 210000 N/mm² (R3-COMMON-DEC-006).
method: >
  c_t = E_s·A_s/L_b, ohne Faktor 1,6 (R3-COMMON-DEC-006).
equations: >
  c_t = 210000 · 353 / 1660 = 44657 N/mm = 44,66 kN/mm
result:
  quantity: Axiale Steifigkeit der Gewindestange je Lasche
  value: 44.66
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx, Sheet "Rahmenecke GL75 SD" (bisher H74 = 71,45 kN/mm mit Faktor 1,6).
certainty: CALCULATED
superseded_by:
---

Bisheriger Excelwert 71,45 kN/mm (mit Faktor 1,6) war nicht als eigener
Wiki-Eintrag geführt.
