---
open_question_id: R3-GL24h-OPQ-024
scope:
  connection: R3
  material: GL24h
status: OPEN
question: >
  Fehler in der übernommenen Push-Out-Auswertung: Im Blatt
  "III-PO-S-SC-44-C-1" zeigt der von Hand eingetragene Zeilenverweis für
  v11/F11 (Zelle V15 = 847) nicht auf den Punkt 0,1 · F_est nach der
  Entlastung, sondern auf einen Punkt mitten in der Entlastung
  (F11 = 36,02 kN statt ≈ 29 kN). Mit der Betreuung zu besprechen; Korrektur
  in der Datei durch den Nutzer.
context: >
  Gefunden am 2026-09-30 bei der Prüfung von III-PO-S-SC-44-C-2 (Anlass
  R3-GL24h-OPQ-023) nach COMMON-COMMON-DEC-007. Datei
  common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx.
  Die Punkte v01, v04, v14, v11, v21, v24 (EN 26891) werden über
  INDIRECT aus den Zeilennummern in V12:V17 gelesen (M = links, S = rechts,
  P = Kraft). In C-1 liegt Zeile 847 in der Entlastung (Kraft fällt weiter:
  37,4 → 35,0 kN um diese Zeile); 0,1 · F_est = 29,0 kN wird erst in Zeile
  879 unterschritten (28,98 kN), Minimum Zeile 880 (28,92 kN).
  Richtiger Verweis: V15 = 879 (erste Zeile mit F ≤ 0,1 · F_est, gleiche
  Regel wie bei V12/V16) oder 880 (Minimum, wie bei C-2 und C-3); beide
  liefern praktisch dieselben Werte. Damit ändern sich v11 links
  0,401 → 0,359 mm, rechts 0,336 → 0,303 mm, F11 36,02 → 28,98 kN.
  Geprüft und richtig: V12:V17 in "III-PO-S-SC-44-C-2" (V15 = 1148, 28,85 kN)
  und "III-PO-S-SC-44-C-3" (V15 = 893, 29,03 kN); Formeln der drei Blätter
  identisch. Auswirkung: keine auf die Ergebnisse. v11/F11 (M15, P15, S15)
  gehen in keine Formel ein: K_ser (M22/S22) nutzt v01/v04, K_e (M23/S23)
  v21/v24; keine Verweise aus "Überblick" oder anderen Blättern; die
  Diagramme des Blatts nutzen nur Zeilen 12/13, 14/15 der Spalten AD:AE,
  16/17 und die Messreihen. Betroffen wäre nur eine Auswertung der
  bleibenden Verschiebung v11 − v01 (links 0,258 → 0,216 mm, −16 %;
  rechts 0,208 → 0,175 mm). Weitere Blätter der Datei (andere Serien) sind
  auf diesen Punkt noch nicht geprüft.
related_sources:
options_considered: >
  V15 in "III-PO-S-SC-44-C-1" auf 879 (bzw. 880) ändern. Übrige Blätter bei
  Gelegenheit auf dieselbe Art prüfen (Zeilenverweise V12:V17 gegen die
  Messdaten).
date_opened: "2026-09-30"
date_resolved:
resolution:
---
