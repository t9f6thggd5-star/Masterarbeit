---
calculation_id: R3-GL24h-CALC-017
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: DIN-EN-12369-2-2011
  literature: Buchholz2025
  experimental_data:
  assumptions: R3-COMMON-DEC-010, COMMON-COMMON-DEC-010
method: >
  Wie R3-GL24h-CALC-012, korrigiert nach R3-COMMON-DEC-010: eine Platte je Seite
  (t_P = 15 mm), G_v = 520 N/mm² (COMMON-COMMON-DEC-010).
equations: >
  c_v,H = 650 · 160 · 800 / 800 = 104,00 kN/mm; c_v,P = 520 · 15 · 800 / 460
  = 13,57 kN/mm je Seite; c_v = 104,00 + 2 · 13,57 = 131,13 kN/mm
result:
  quantity: Schubsteifigkeit des Schubfelds im Riegel (Holz + 2 Verstärkungsplatten, je Seite eine 15-mm-Platte)
  value: 131.13
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" I135, I143, I146
  (vom Nutzer am 2026-09-30 angepasst, per openpyxl geprüft).
certainty: CALCULATED
superseded_by:
---

Ersetzt R3-GL24h-CALC-012 (156,17 kN/mm, Platten doppelt gezählt, G_P = 500).
