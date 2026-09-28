---
calculation_id: R3-GL24h-CALC-013
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: Buchholz2025
  experimental_data: R3-GL24h-III-PO-S-SC-44-C-RES-004, R3-GL24h-III-PO-S-SC-44-B-RES-001
  assumptions: R3-GL24h-ASS-002, R3-GL24h-ASS-003
method: >
  Zugsteifigkeit einer Lasche (sleeve) nach Buchholz2025 Gl. (11),
  Komponentenzuordnung nach R3-COMMON-DEC-005: Reihenschaltung aus
  Gewindestange (R3-GL24h-CALC-011), 2 × c_c,ep = ∞, ASSY-Gruppe Stütze
  (R3-GL24h-CALC-007), ASSY-Gruppe Riegel (R3-GL24h-DEC-015 / CALC-010),
  c_br,par = c_br,perp = ∞, 2 × c_c,0 = c_H,Lasche
  (E_0,mean·A_netto/L_eff = 11500 · 11678 / 450).
equations: >
  1/c_t,sleeve = 1/30,994 + 1/183,682 + 1/137,900 + 2/298,438
  = 0,032264 + 0,005444 + 0,007252 + 0,006702 = 0,051662 mm/kN;
  c_t,sleeve = 19,36 kN/mm
result:
  quantity: Zugsteifigkeit einer Lasche (c_t,sleeve), Variante ohne Druckkontakt, ohne Vorspannung
  value: 19.36
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD", Block ab I96 (I139 laut Nutzerformel).
certainty: CALCULATED
superseded_by:
---

Ersetzt R3-GL24h-CALC-005 (27,09 kN/mm, mit normativem c_ASSY,S und c_t mit
Faktor 1,6). c_H,Lasche hier mit A_netto = 11678 mm² aus dem Excel
(298,44 kN/mm); R3-GL24h-CALC-001 nennt mit 11700 mm² gerundet 299,0 kN/mm.

Anteile an 1/c_t,sleeve: Stange 62 %, ASSY Riegel 14 %, Lasche (2×) 13 %,
ASSY Stütze 11 %. Empfindlichkeit c32,Beam 130–147 kN/mm: c_t,sleeve etwa
19,2–19,5 kN/mm.
