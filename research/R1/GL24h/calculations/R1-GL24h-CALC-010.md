---
calculation_id: R1-GL24h-CALC-010
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: Buchholz2025
  experimental_data:
  assumptions: R1-COMMON-ASS-002
method: >
  Nichtlineare Verdrehung der Rahmenecke bei M_R aus der Mittelkurve der
  sechs Zugversuchsgruppen (Aufbereitung nach R1-GL24h-DEC-011):
  Mittelkurve F–v je 2×8-Gruppe ohne Anfangsschlupf, umgerechnet auf den
  Anschluss (4×8: T = 2F; Träger und Stütze in Reihe, Druckseite starr:
  φ = 2v/z), plus vier Drehfedern nach Buchholz2025 Gl. (5) linear
  (R1-COMMON-DEC-004): M = T·z + 4·C_rot,v,f·φ. Φ bei M_R abgelesen;
  Anfangsschlupf getrennt (+2·v0,mittel/z).
equations: >
  v(F) = F / mean_i(F/v_i(F)); T = 2F; φ = 2v/z;
  M = T·z + 4·C_rot,v,f·φ; φ_Schlupf = 2·v0/z.
result:
  quantity: Verdrehung Φ der Rahmenecke R1 (GL24h) bei M_R = 399,49 kNm (ohne / mit Anfangsschlupf)
  value: 2.373 / 3.395
  unit: mrad
  original_value:
  original_unit:
source_file: >
  Skript R1/GL24h/calculations/R1_GL24h_Mittelkurve_Mphi.py mit Ergebnis
  R1_GL24h_Mittelkurve_Mphi.csv und Grafiken R1_GL24h_Mittelkurve.png,
  R1_GL24h_Zugversuche_bis_Fmax.png (Stand 2026-09-26). Rohdaten:
  R1/COMMON/calculations/"Kopie von Auswertung Steifigkeiten_0703_Zugversuche_Stahl-Holz-Stabdübel kopie.xlsx", Blätter I-T-S-SD-28-1 bis -3, Spalten B (Kraft), I (v_oben =
  (VO+HO)/2), J (v_unten = (VU+HU)/2); F01/F04-Zeilen wie im Blatt (z. B.
  28-1: Zeile 534 / 1174). Eingänge aus dem R1-Excel: z = 550 mm (C101),
  C_rot,v,f = 21.110,5 kNm/rad (I40), M_R = 399,49 kNm (C109).
certainty: CALCULATED
superseded_by:
---

**Normbezug:** Schlupfabzug und Lastfenster nach DIN EN 26891 (nicht in
bibliography/sources.yaml registriert, Norm liegt nicht im Quellenordner).

**Kontrollen:** K_ser je Gruppe exakt wie Auswerteblatt (247,09 / 208,91 /
276,25 / 294,97 / 368,60 / 281,32; Mittel 279,52 kN/mm). Mittelkurve:
Sekantensteifigkeit 279,52 kN/mm bis 48 kN, 278,3 kN/mm bei 191,5 kN, 222
kN/mm bei 355 kN (Ende = kleinste Höchstlast 355,08 kN). Anfangsschlupf je
Gruppe v0 = 0,361 / 0,185 / 0,332 / 0,216 / 0,291 / 0,301 mm, Mittel
0,281 mm → φ_Schlupf = 1,02 mrad.

**Ergebnis und Spanne von M_R** (M_R = 2·F_max·z, F_max je Prüfkörper aus
dem Versuchsblatt, Zelle M6):

| M_R | Φ ohne Schlupf | Φ mit Schlupf | F je 2×8-Gruppe bei M_R |
|---|---|---|---|
| 390,6 kNm (28-1, 355,08 kN) | 2,33 mrad | 3,35 mrad | 177 kN |
| 393,4 kNm (28-2, 357,62 kN) | 2,34 mrad | 3,36 mrad | 178 kN |
| 399,49 kNm (R1-Excel C109) | 2,37 mrad | 3,40 mrad | 181 kN |
| 412,0 kNm (28-3, 374,52 kN) | 2,44 mrad | 3,46 mrad | 187 kN |

Linear mit C_rot,tot = 168.996,9 kNm/rad (R1-GL24h-CALC-009): 2,36 mrad.
Die Nichtlinearität wirkt kaum, weil nach Gl. (5) die Drehfedern etwa die
Hälfte des Moments tragen und M_R schon bei ≈ 181 kN je Gruppe (≈ 0,4·F_est)
erreicht ist; siehe R1-COMMON-OPQ-007.

**Maschinenweg (vorläufig):** u_M = Φ·a, nur Starrkörperdrehung, a noch
ungeklärt (R1-GL24h-OPQ-010). Mit a = 3,03 m: 7,2 mm ohne, 10,3 mm mit
Anfangsschlupf.

**Offen/Hinweise:** Das R1-Excel (I2:I4) führt als Höchstlasten 356,18 /
358,16 / 375,18 kN (Mittel 363,17), das Versuchsblatt (MAX der Kraftspalte)
355,08 / 357,62 / 374,52 kN (Mittel 362,41); Herkunft der Differenz ≈ 1 kN
ungeklärt. K_ser oder K_e: R1-COMMON-OPQ-008.
