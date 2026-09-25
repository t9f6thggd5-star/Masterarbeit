---
calculation_id: R3-GL24h-CALC-010
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data: R3-GL24h-III-PO-S-SC-44-B-RES-001, R3-GL24h-III-PO-S-SC-44-C-RES-004, R3-GL24h-III-PO-S-SC-11-B-RES-004, R3-GL24h-III-PO-S-SC-11-C-RES-004
  assumptions: R3-GL24h-ASS-003, R3-GL24h-ASS-004
method: >
  Rekonstruktion der Anfangssteifigkeit der Beam-seitigen 4×4-Schraubengruppe
  (je Scherfuge) aus der Erstbelastung von III-PO-S-SC-44-B-1 (n = 1).
  Sekante K = (F2 − F1)/(v2 − v1) wie in der Auswertungsdatei, je Seite
  (LINKS VL+HL, RECHTS VR+HR) mit der Gesamtkraft, Mittel L/R, halbiert je
  Scherfuge (R3-GL24h-DEC-013); Punkte = erste Messzeile mit Kraft ≥
  Grenze. Hauptwert im Lastfenster 10–20 % F_est = 29–58 kN
  (R3-GL24h-DEC-014). Dieselbe Rechnung für 44-C-1…3 im gleichen Fenster;
  Übertragung auf das Normfenster über das Verhältnis B/C mal K_ser,C
  (EN 26891). Hochrechnung auf 32 Schrauben mit 2^α (α = 0,807,
  CALC-007). Methodenkontrolle an 1×1 (Abweichung zur Datei meist < 3 %).
equations: >
  K_SF = ½ · (K_L + K_R)/2 mit K = (F2 − F1)/(v2 − v1);
  44-B-1, 29–58 kN: K_L = 131,87, K_R = 136,22 → K_SF = 67,02 kN/mm;
  44-C (Mittel n=3) im selben Fenster: 89,29 kN/mm → B/C = 0,7506;
  übertragen: c16,Beam = 0,7506 · 104,97 = 78,79 kN/mm;
  c32,Beam = 78,79 · 2^0,807 = 137,9 kN/mm.
  Vergleich: Faktor 0,8028 (CALC-008) 84,3 / 147,5 kN/mm → −6,5 %.
  Weitere Fenster (Vergleich, direkt je Scherfuge): 3–13 % F_est 58,85;
  10–28 % F_est 57,72 kN/mm.
result:
  quantity: Rekonstruierte Anfangssteifigkeit der Beam-seitigen 4×4-Schraubengruppe je Scherfuge, übertragen auf das Normfenster (Hauptwert, Lastfenster 10–20 % F_est)
  value: 78.79
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/GL24h/calculations/R3_44B_Querdruck_und_Steifigkeit_2.xlsx, Blatt
  "Steifigkeit" (vom Nutzer überarbeitete Fassung, Stand 2026-09-25); Messpunkte aus
  common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx,
  Blätter "III-PO-S-SC-44-B-1" (Zeilen 490/882) und "III-PO-S-SC-44-C-1…3",
  Spalten A, I, J; K_ser aus "Überblick" B31:C36, B40:C42.
certainty: CALCULATED
superseded_by:
---

**Einschränkungen:** n = 1 auf der Trägerseite (CLAUDE.md Abschnitt 15),
kein K_ser nach EN 26891 im strengen Sinn (obere Fenstergrenze 20 statt
40 % F_est). Die Übertragung setzt voraus, dass Träger- und Stützenseite
sich zwischen Ersatz- und Normfenster gleich stark versteifen. Geprüft an
den 1×1-Serien: Im Lastfenster 10–20 % F_est weicht das Verhältnis B/C
um etwa +5 % vom Normfenster ab (0,854 statt 0,810), im Fenster
3–13 % F_est um etwa −7 %; die Stärke der Versteifung der 4×4-Kurven
(Stützenseite Faktor ≈ 1,18) lässt sich an 1×1 nicht prüfen. Die
Hochrechnung 16 → 32 nutzt das an der Stützenseite kalibrierte α
(ASS-003/004).

Direkter Wert ohne Übertragung (10–20 % F_est): 67,02 kN/mm je Scherfuge.
Welcher Wert in die Zugpfadkette eingeht, ist offen (R3-GL24h-OPQ-022).

**Empfindlichkeit: Fensterkorrektur aus den 1×1-Serien (2026-09-25):**
Verhältnis Träger/Stütze bei 1×1 im Lastfenster 10–20 % F_est (je
Prüfkörper sein eigenes F_est; SC-11-B-1 wurde mit F_est = 8 kN geprüft,
alle anderen mit 20 kN): B = 7,128, C = 8,351 kN/mm je Scherfuge,
B/C = 0,854; im Normfenster (K_ser „Überblick“) B/C = 0,803 (= Faktor
ASS-004). Korrekturfaktor 0,803 / 0,854 = 0,940 → c16,Beam = 78,79 · 0,940
= **74,1 kN/mm** je Scherfuge (c32,Beam 129,7 kN/mm; −12,1 % gegenüber dem
Faktorwert). Nur als Empfindlichkeit, nicht als Hauptwert: Die Korrektur
ersetzt die Annahme „gleiche Kurvenform von Träger und Stütze“ durch die
Annahme „gleiche Verschiebung des Verhältnisses bei 1×1 und 4×4“; die
1×1-Kurven sind zwischen den Fenstern fast linear (Faktor 1,00–1,05),
die 4×4-Stützenseite versteift sich dagegen deutlich (Faktor ≈ 1,18);
die Einzelwerte der 1×1-Prüfkörper streuen stark (bei SC-11-B-1 liegt das
Fenster nur bei 0,8–1,6 kN, K LINKS 17,3 gegenüber RECHTS 10,6 kN/mm).
Rekonstruktion damit 74–79 kN/mm je Scherfuge, zusammen mit dem Faktorwert
Spanne für die Parameterstudie etwa 74–84 kN/mm. Rechnung im Blatt
"Steifigkeit", Zeilen 56–74 und Zeile 49.
