---
calculation_id: R3-GL24h-CALC-009
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data: R3-GL24h-III-PO-S-SC-44-B-RES-001
  assumptions:
method: >
  Querdruckwiderstand des Mittelholzes am Lasteinleitungsquerschnitt
  (Kopffläche) des Push-Out-Prüfkörpers III-PO-S-SC-44-B
  (Plan-Bezeichnung III-BSH-VG-R-G-4x4, R = Riegel). Beim R-Prüfkörper
  verläuft die Faser des Mittelholzes in Tiefenrichtung (senkrecht zur
  Zeichenebene), die Prüflast wird oben über die volle Kopffläche
  160 × 160 mm quer zur Faser eingeleitet (Nutzerangabe 2026-09-25).
  Keine Lastausbreitung möglich (Breite und Faserlänge = 160 mm = volle
  Abmessung), daher k_c,90 = 1. Mittelwertbetrachtung mit gamma = 1
  (COMMON-COMMON-DEC-001), f_c,90,mean wie in R2-GL24h-CALC-005/010.
equations: >
  FprEN 1995-1-1:2024, Gl. (8.5)/(8.6): F_c,90 = k_mat · k_c,90 · f_c,90 · A;
  Gl. (8.7): k_c,90 = sqrt(A_ef/A) = 1,0 (A_ef = A);
  A = b_90,c · l_90,c = 160 · 160 = 25.600 mm²;
  k_mat = 1,0 (8.1.6.1(2), Grundwert):
  F_c,90,mean = 1,0 · 1,0 · 3,3156 · 25.600 = 84.879 N ≈ 84,88 kN.
  Vergleichswerte: k_mat = 1,4 (Tab. 8.1, SWB Fall A) → 118,83 kN;
  charakteristisch (f_c,90,k = 2,5 N/mm², k_mat = 1,0) → 64,00 kN.
result:
  quantity: Querdruckwiderstand Mittelholz am Lasteinleitungsquerschnitt, Push-Out III-PO-S-SC-44-B (Gesamtkraft, k_mat = 1,0, Mittelwert)
  value: 84.88
  unit: kN
  original_value:
  original_unit:
source_file: >
  R3/GL24h/calculations/R3_44B_Querdruck_und_Steifigkeit.xlsx, Blatt
  "Querdruck Mittelholz" (erstellt 2026-09-25, Zelle B15). Kraft-Weg-Kurve von PK1 aus
  common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx,
  Blatt "III-PO-S-SC-44-B-1" (Stand 16.09.2026).
certainty: CALCULATED
superseded_by:
---

**Geometrie** (Nutzer, Skizzen III-BSH-VG-R-G-4x4 und Chat 2026-09-25):
Mittelholz 160 mm breit × 160 mm tief, Höhe 680 mm, oben 100 mm über
den Laschen (je 80 mm dick, 580 mm hoch), unten 100 mm frei; Laschen
unten aufgelagert (je F/2), Last oben auf das Mittelholz über die volle
Kopffläche.

**Vergleich mit der Kraft-Weg-Kurve PK1** (Maschinenweg, Blatt
"III-PO-S-SC-44-B-1"): Sekantensteigung ≈ 20,9 kN/mm zwischen 10 und
50 kN, danach 14,4 (50–60 kN), 8,4 (60–70 kN), 5,3 (70–80 kN) und
≈ 1,0 kN/mm (80–85 kN); Plateau ab ≈ 80–83 kN, anschließend langsamer
Anstieg bis F_max = 93,97 kN bei 20,4 mm Maschinenweg, kein spröder
Lastabfall. Das Plateau liegt nahe am hier berechneten Mittelwert
(84,88 kN), der Beginn der Abflachung nahe am charakteristischen Wert
(64,0 kN). Die Deutung als Versagensmechanismus steht in
R3-GL24h-INT-001 (nicht hier — eigene Berechnung, keine Interpretation).

**Einordnung:** Die Serie war mit F_est = 290 kN (Gesamtkraft)
ausgewertet; der hier berechnete Querdruckwiderstand des Mittelholzes
liegt bei rund 29 % davon. Die Variante S (Stütze, Faser des
Mittelholzes parallel zur Last, III-PO-S-SC-44-C) ist davon nicht
betroffen.
