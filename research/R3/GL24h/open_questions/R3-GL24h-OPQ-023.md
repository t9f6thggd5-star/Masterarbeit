---
open_question_id: R3-GL24h-OPQ-023
scope:
  connection: R3
  material: GL24h
status: RESOLVED
question: >
  Ist III-PO-S-SC-44-C-2 im Lastfenster 10–20 % F_est ein Ausreißer, und
  soll er in das Verhältnis B/C der Rekonstruktion (R3-GL24h-CALC-010)
  eingehen?
context: >
  Im Fenster 10–20 % F_est: 44-C-1 106,8, 44-C-2 56,0, 44-C-3
  105,0 kN/mm je Scherfuge. 44-C-2 geht wie in der Auswertungsdatei in den
  Mittelwert (89,29) ein. Ohne 44-C-2 wäre B/C kleiner und der rekonstruierte
  c16,Beam läge bei etwa 66 kN/mm statt 78,8 kN/mm.
related_sources: 
options_considered: >
  Vorerst mit allen drei Prüfkörpern; Frage für die Besprechung.
date_opened: "2026-09-28"
date_resolved: "2026-09-30"
resolution: >
  C-2 bleibt im Hauptwert (alle drei Prüfkörper); die Variante ohne C-2 wird
  als Empfindlichkeit geführt (R3-GL24h-CALC-015). Nutzerentscheidung
  (Chat, 2026-09-30). Grundlage: keine Auswertungsfehler im Blatt, keine
  statistische Ausschlussgrundlage (n = 3), Wiederbelastung und Höchstlast
  unauffällig; Einfluss auf c_t,tot nur +1,4 % bei Ausschluss.
---

**Update (2026-09-30), Prüfung des Blatts III-PO-S-SC-44-C-2:** Kein Fehler
gefunden. Formeln in C-1, C-2 und C-3 identisch; von Hand eingetragene
Zeilenverweise V12:V17 in C-2 treffen die Laststufen (29,0 / 115,1 / 112,0 /
28,9 / 30,0 / 116,2 kN); Rohdaten ohne Lücken (Zeitschritt 0,2 s) und ohne
Sprünge der Wegaufnehmer (≤ 0,005 mm); gleiche Prüfgeschwindigkeit wie C-1/C-3
(Maschinenweg ≈ 1,2 mm/min). Dabei in C-1 ein falscher Zeilenverweis für
v11/F11 gefunden (ohne Einfluss auf K_ser/K_e), siehe R3-GL24h-OPQ-024.

**Befund zu C-2 (Messdaten, Sekanten der Erstbelastung, ganzer Prüfkörper
L/R in kN/mm):** 3–29 kN 129/137 (C-1 201/217, C-3 217/214); 29–58 kN
111/113 (198/229, 193/227); 58–87 kN 164/184 (236/302, 195/253); 87–110 kN
254/232 (285/323, 204/251). Beide Seiten und alle vier Wegaufnehmer gleich
weich, Maschinenweg ebenfalls weicher; C-2 versteift sich mit der Last.
Wiederbelastung K_e 429/431 (C-1 459/563, C-3 416/484) und F_max 338 kN
(331, 312) unauffällig. Streuung der Anfangssteifigkeit in allen GL24h-Push-
Out-Serien deutlich größer als die der Höchstlast (VK K_ser 9–22 %, F_max
0–4 %, Blatt "Überblick").

**Deutung (von Claude vorgeschlagen, nicht geprüft):** C-2 ist elastisch
nicht weicher, sondern setzt sich in der Erstbelastung stärker und bis in
das Auswertefenster hinein (z. B. Fuge Lasche/Mittelholz, geringere
Anpressung und Reibung, Eindrehen). Ursache nur über Versuchsprotokoll oder
Fotos zu klären. Ob ein solches Setzen auch in der Rahmenecke zu erwarten
ist (dort ggf. teilweise durch die Vorspannung vorweggenommen), bleibt offen.

**Korrektur des Kontexts oben:** Die ≈ 66 kN/mm entstehen nur, wenn C-2 im
Fenster 10–20 % ausgeschlossen, im Normfenster (K_C,norm = 104,97) aber
behalten wird — inkonsistent. Konsequent in beiden Fenstern ausgeschlossen:
c16,Beam = 74,46 kN/mm, c32,Beam unverändert 137,9 kN/mm (R3-GL24h-CALC-015).
