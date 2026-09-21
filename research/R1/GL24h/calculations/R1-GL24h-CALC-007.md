---
calculation_id: R1-GL24h-CALC-007
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature: Buchholz2025
  experimental_data:
  assumptions: R1-COMMON-ASS-001
method: >
  Drehfeder C_rot,v,f je Dübelgruppe nach Buchholz2025 Gl. (4):
  C_rot,v,f = I_p · K_ser, mit I_p als polarem Trägheitsmoment der
  Dübelanordnung um den Gruppenschwerpunkt (Koordinaten aus R1-COMMON-ASS-001)
  und K_ser,Dübel nach FprEN Tab. 11.12 (Entscheidung R1-GL24h-DEC-010).
equations: >
  I_p = Σ(x_i² + y_i²) = 1.075.200 + 100.000 = 1.175.200 mm² (32 Dübel);
  K_ser,Dübel = ρ_mean^1,5 · d / 23 · 2 (Stahl-Holz) · m = 420^1,5 · 12 / 23 ·
  2 · 2 = 17,963 kN/mm; C_rot,v,f = K_ser,Dübel · I_p (Buchholz2025 Gl. 4).
  Probe: c_T · r_g² mit r_g² = I_p / 32 = 36.725 mm² (r_g = 191,6 mm).
result:
  quantity: Drehfeder C_rot,v,f je 4×8-Dübelgruppe (GL24h)
  value: 21110.5
  unit: kNm/rad
  original_value: 21110529.2
  original_unit: kN·mm/rad
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Zellen I18 (K_ser,Dübel), I20:I25 (Koordinaten),
  I26:I29 (I_p, r_g), I31 (C_rot,v,f); Stand der Datei am 2026-09-21 (per
  openpyxl ausgelesen, in Excel geöffnet und vom Nutzer bearbeitet). Die
  Einheit in H31 steht dort als "kNmm/rad", der Wert ist in kNm/rad.
certainty: CALCULATED
superseded_by:
---

Nachgerechnet gegen die Zellen I26 bis I31 des Blattes (Abweichung nur in
der Rundung). Das Federmodell (Buchholz2025 Abb. 3) führt vier Drehfedern,
je eine je Dübelgruppe; alle vier haben hier denselben Wert, weil die
Geometrie identisch ist (R1-COMMON-ASS-001) und K_ser auf der Druckseite wie
auf der Zugseite angesetzt wird (Annahme des Nutzers, keine Druckversuche).

**Empfindlichkeit auf K_ser,Dübel** (R1-GL24h-OPQ-013, R1-GL24h-OPQ-014):
17,47 kN/mm (Versuch, c_T / 32) ergibt 20.531 kNm/rad; 23,29 kN/mm (Versuch
mit Reihendeckel, c_T / 12) 27.374 kNm/rad; mit ρ = 385 kg/m³ 18.527 kNm/rad.

**Kombination der vier Drehfedern (offen):** Gl. (5) wörtlich: 4 · 21.111 =
84.442 kNm/rad. Physikalische Lesart (Zug- und Druckgruppe je Bauteil
parallel, Träger und Stütze in Reihe): 21.111 kNm/rad. Die Entscheidung des
Nutzers steht aus. Zum Vergleich: die obere Grenze des Kräftepaar-Glieds
C_rot,t+c = z² · c_t,tot (Druckseite starr) ist 84.555 kNm/rad mit
z = 550 mm (Blatt C89, für GL24h mit demselben Wert gerechnet, nicht getrennt
geprüft); mit c_c,tot = c_t,tot 42.277 kNm/rad.
