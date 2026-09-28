---
calculation_id: R1-GL24h-CALC-011
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: Buchholz2025
  experimental_data:
  assumptions: R1-COMMON-ASS-002, R1-COMMON-ASS-003
method: >
  Werte der Übersichtstabelle nach COMMON-COMMON-DEC-008 (linear):
  M_R über das Kräftepaar mit dem mittleren F_max der Zugversuche,
  elastische Eckverdrehung φ_el = M_R / C_rot,tot (R1-GL24h-CALC-009),
  Anfangsschlupf φ_S = 2·v0,mittel / z (Riegel- und Stützengruppe in Reihe,
  Druckseite starr), Zylinderkraft F = M_R / a und Maschinenweg u_M = Φ · a
  mit dem Hebelarm a nach R1-COMMON-ASS-003.
equations: >
  v0 = v01 − F01 / K_ser je Kurve (EN 26891; K_ser = Sekante F01–F04 =
  Zelle M21/S21 der Versuchsblätter); φ_el = M_R / C_rot,tot;
  φ_S = 2·v0,mittel / z; Φ_ges = φ_el + φ_S; F = M_R / a; u_M = Φ · a.
result:
  quantity: Übersichtswerte R1/GL24h – F = 170,2 kN; φ_el = 2,364 mrad; φ_S = 1,022 mrad; Φ_ges = 3,386 mrad; u_M = 5,55 mm ohne / 7,95 mm mit Anfangsschlupf
  value: 2.364 / 3.386
  unit: mrad
  original_value:
  original_unit:
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Stand 2026-09-28 (vom Nutzer angelegt): C110 M_R =
  399,49 kNm (=C101*C107*10^-3, C107 = 2·I7 = 726,35 kN), N40 C_rot,tot =
  168.996,9 kNm/rad, C101 z = 550 mm, C115 a = 2,3476 m
  (=(2842-800/(2*COS(RADIANS(36))))*10^-3), C118 F = 170,17 kN, I46–I55
  v0 je Kurve, I57 v0,mittel = 0,2810 mm, I59 φ_S, I64 φ_el, I66 Φ_ges,
  I68/I69 u_M.
certainty: CALCULATED
superseded_by:
---

**Rechnung:**

```
φ_el  = 399,49 / 168.996,9 · 1000        = 2,364 mrad
v0    = (0,361 + 0,185 + 0,332 + 0,216 + 0,291 + 0,301) / 6 = 0,281 mm
φ_S   = 2 · 0,281 / 550 · 1000            = 1,022 mrad
Φ_ges = 2,364 + 1,022                     = 3,386 mrad
F     = 399,49 / 2,3476                   = 170,2 kN
u_M   = 2,364 · 2,3476 = 5,55 mm (ohne) ; 3,386 · 2,3476 = 7,95 mm (mit Schlupf)
```

v0 je Kurve (28-1/-2/-3, oben/unten) aus den Versuchsblättern der
Auswertungsdatei (M11, S11, P11, M21, S21), vom Nutzer im Excel
eingetragen und von Claude gegen die Blätter geprüft (2026-09-28).

**Vorbehalte:** Druckseite starr (R1-COMMON-ASS-002) → Φ und u_M sind
Untergrenzen; bei c_c,tot = c_t,tot wäre φ_el ≈ 3,15 mrad (+33 %).
Anfangsschlupf nur Zugseite, Addition zu φ_el vereinfachend; ob er
angesetzt wird, ist offen (R1-COMMON-OPQ-008). u_M nur aus der
Anschlussverdrehung (COMMON-COMMON-OPQ-004). M_R nur Kräftepaar
(R1-COMMON-OPQ-007).

**Vergleich nichtlinear:** Die Mittelkurve nach R1-GL24h-CALC-010 ergibt
2,373 mrad (+0,4 %). Für die Übersicht wird die lineare Variante verwendet,
die nichtlineare M-φ-Kurve erst in Phase 4 (Nutzerentscheidung 2026-09-28).
