---
calculation_id: R3-GL24h-CALC-011
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: DIN-EN-1993-1-8-2025
  literature:
  experimental_data:
  assumptions: >
    Eine Gewindestange M20 je Lasche (A_s = 245 mm²), Dehnlänge L_b = 1660 mm,
    E_s = 210000 N/mm², starre Ankerplatte ohne Abstützkräfte
    (R3-COMMON-DEC-006).
method: >
  Axiale Dehnsteifigkeit einer Gewindestange, c_t = E_s·A_s/L_b (ohne den
  Faktor 1,6 aus DIN EN 1993-1-8:2025-04 Gl. (A.40), der sich auf eine
  Schraubenreihe mit zwei Schrauben bezieht).
equations: >
  c_t = 210000 · 245 / 1660 = 30994 N/mm = 30,99 kN/mm
result:
  quantity: Axiale Steifigkeit der Gewindestange je Lasche
  value: 30.99
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" I98 (vom Nutzer am 2026-09-28 korrigiert).
certainty: CALCULATED
superseded_by:
---

Ersetzt R3-GL24h-CALC-004 (49,59 kN/mm mit Faktor 1,6).
