---
calculation_id: R3-GL24h-CALC-014
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
  Gesamtsteifigkeit der Zugseite nach Buchholz2025 Gl. (12): zwei Laschen
  (vorne/hinten, gleicher Hebelarm) parallel, Schubfeld c_v in Reihe
  (R3-COMMON-DEC-005/007). Eingänge R3-GL24h-CALC-013 und R3-GL24h-CALC-012.
equations: >
  Σc_t,sleeve = 2 · 19,357 = 38,713 kN/mm;
  1/c_t,tot = 1/38,713 + 1/156,174 = 0,025831 + 0,006403 = 0,032234 mm/kN;
  c_t,tot = 31,02 kN/mm
result:
  quantity: Gesamtsteifigkeit der Zugseite c_t,tot (Variante ohne Druckkontakt, ohne Vorspannung, ohne C_v,f,rot)
  value: 31.02
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" (Nutzerformel =1/(1/(2*I139)+1/I136)).
certainty: CALCULATED
superseded_by:
---

Anteile an 1/c_t,tot: Gewindestange 50 %, Schubfeld 20 %, ASSY Riegel 11 %,
Lasche (2×) 10 %, ASSY Stütze 8 %. Geht in S_j,ini = z²/(1/c_t,tot +
1/c_c,tot) ein; Druckseite c_c,tot steht noch aus.
