---
calculation_id: R3-GL24h-CALC-018
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: 
  literature: Buchholz2025
  experimental_data:
  assumptions: 
method: >
  Wie R3-GL24h-CALC-014 (Buchholz2025 Gl. 12) mit c_v nach R3-GL24h-CALC-017.
equations: >
  1/c_t,tot = 1/(2 · 19,357) + 1/131,13 = 0,025831 + 0,007626 = 0,033457 mm/kN;
  c_t,tot = 29,89 kN/mm
result:
  quantity: Gesamtsteifigkeit der Zugseite c_t,tot (ohne Druckkontakt, ohne Vorspannung, ohne C_v,f,rot)
  value: 29.89
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" I152 (per openpyxl geprüft, 2026-09-30).
certainty: CALCULATED
superseded_by:
---

Ersetzt R3-GL24h-CALC-014 (31,02 kN/mm). Anteil Schubfeld an 1/c_t,tot jetzt ≈ 23 %.
