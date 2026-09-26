---
calculation_id: R1-GL75-CALC-004
scope:
  connection: R1
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature: Buchholz2025
  experimental_data:
  assumptions: R1-COMMON-ASS-001
method: >
  Drehfeder C_rot,v,f je Dübelgruppe (BauBuche/GL75) nach Buchholz2025
  Gl. (4): C_rot,v,f = I_p · K_ser, mit I_p aus der identischen Geometrie
  R1-COMMON-ASS-001 und K_ser,Dübel nach FprEN Tab. 11.12 mit ρ_mean =
  800 kg/m³ (Entscheidung R1-GL75-DEC-001).
equations: >
  I_p = 1.175.200 mm² (wie R1-GL24h-CALC-007); K_ser,Dübel = ρ_mean^1,5 ·
  d / 23 · 2 (Stahl-Holz) · m = 800^1,5 · 12 / 23 · 2 · 2 = 47,222 kN/mm;
  C_rot,v,f = K_ser,Dübel · I_p.
result:
  quantity: Drehfeder C_rot,v,f je 4×8-Dübelgruppe (GL75)
  value: 55495.8
  unit: kNm/rad
  original_value: 55495806.2
  original_unit: kN·mm/rad
source_file: >
  Eigene Nachrechnung (Claude, 2026-09-21) mit den Eingaben aus
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL75 SD" (C5 = 800 kg/m³ aus "Holzkennwerte" F21, C6 = 2,
  C22 = 12 mm). Der Rotationsblock des GL75-Blattes ist zu diesem Stand noch
  nicht angelegt (I18 = 1E+99 als Platzhalter).
certainty: CALCULATED
superseded_by:
---

**Empfindlichkeit** (R1-GL75-OPQ-001, R1-GL75-OPQ-003): mit ρ = 730 kg/m³
K_ser = 41,16 kN/mm und C_rot,v,f = 48.374 kNm/rad; mit dem aus dem Versuch
abgeleiteten c_T / 32 = 45,48 kN/mm 53.453 kNm/rad; mit Reihendeckel
(c_T / 24 = 60,65 kN/mm) 71.270 kNm/rad.

**Kombination der vier Drehfedern (offen):** Gl. (5) wörtlich 4 · 55.496 =
221.983 kNm/rad, physikalische Lesart 55.496 kNm/rad. Die Entscheidung des
Nutzers steht aus. Die obere Grenze des Kräftepaar-Glieds z² · c_t,tot
(Druckseite starr, z = 550 mm nach R1-GL24h-OPQ-003, Blatt C91) ist 220.141 kNm/rad, mit c_c,tot = c_t,tot
110.070 kNm/rad.

**Update (2026-09-26):** Die Kombination der vier Drehfedern ist
entschieden: Buchholz2025 Gl. (5) wie gedruckt, also Summe der vier
Drehfedern (4 · 55.496 = 221.983 kNm/rad) plus C_rot,t+c (R1-COMMON-DEC-004).

**Update (2026-09-26), Zellbezüge:** Nach der Neugliederung des Blattes
stehen die Werte jetzt in I27 (K_ser = 47,222 kN/mm), I29:I38, I40 (C_rot,v,f = 55.495,8 kNm/rad); der Rotationsblock ist inzwischen angelegt. Zahlenwert unverändert. Weiterverwendet
in R1-GL75-CALC-006.
