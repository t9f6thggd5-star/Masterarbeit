---
calculation_id: R3-GL24h-CALC-019
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature: Buchholz2025, ScheibmairQuenneville2014
  experimental_data:
  assumptions: R3-COMMON-DEC-009
method: >
  Wie R3-GL24h-CALC-016 (R3-COMMON-DEC-009, Nulllinie aus Gleichgewicht, Iteration),
  mit c_t,tot = 29,889 kN/mm nach R3-GL24h-CALC-018.
equations: >
  x = 252,8 mm; c_c,90 = 117,56 kN/mm; c_c,0 = 1 840 kN/mm; c_c,tot = 110,50 kN/mm;
  z = 720 − 252,8/3 = 635,7 mm; S_j,ini = 29 889 · (720 − 252,8) · 635,7 =
  8,878·10⁹ Nmm/rad; Kontrolle Gl. (3) mit c_c,eq = ¾ · 110,50 = 82,87 kN/mm:
  635,7² / (1/29,889 + 1/82,87) = 8 878 kNm/rad
result:
  quantity: Anfangsrotationssteifigkeit S_j,ini R3/GL24h nach dem Öffnen der Fuge (ohne Vorspannung, ohne C_v,f,rot)
  value: 8878
  unit: kNm/rad
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" I179–I188 (per openpyxl geprüft, 2026-09-30).
certainty: CALCULATED
superseded_by:
---

Ersetzt R3-GL24h-CALC-016 (9 115 kNm/rad, −2,6 %). Vorbehalte wie dort.
Übersicht linear (M_R = 238,19 kNm nach R3-COMMON-DEC-004, a = 3,0293 m):
Φ = 238,19/8 878 = 26,83 mrad, u_M = 81,3 mm, F = 78,63 kN.

**Update (2026-09-30), Hebelarm nach R3-COMMON-DEC-013:** Mit z = 635,7 mm auch für M_R: M_R = 2 · 203 · 0,6357 = 258,11 kNm (statt 238,19), Φ = 258,11/8 878 = 29,07 mrad, u_M = 88,1 mm, F = 85,20 kN. Im Excel noch nicht umgestellt (Sheet "Rahmenecke GL24h SD" C80 = I96/3 mit I96 = 400 mm). Die Werte gelten für die Variante ohne Druckkontakt der Laschen, die nach R3-COMMON-DEC-011 überarbeitet wird.
