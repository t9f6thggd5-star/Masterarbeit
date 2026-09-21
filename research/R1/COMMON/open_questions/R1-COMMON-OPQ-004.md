---
open_question_id: R1-COMMON-OPQ-004
scope:
  connection: R1
  material: COMMON
status: OPEN
question: >
  Welche F_est-Basis legt das Lastfenster (0,1 bis 0,4·F_est) fest, in dem
  K_ser der Zugversuche I-T-S-SD-28 (GL24h) und I-T-B-SD-28 (GL75)
  ausgewertet wird: der in den Auswerteblättern verwendete Planungswert
  (480 kN bzw. 800 kN) oder der Wert aus der Berechnungs-Excel (Zelle C30,
  für die getestete 2×8-Gruppe halbiert: 313,6 kN bzw. 471,8 kN)?
context: >
  Befund (Claude, 2026-09-21) aus der Analyse der Datei "Auswertung
  Steifigkeiten_0703_Zugversuche_Stahl-Holz-Stabdübel.xlsx" und ihrer
  Kopie (R1/COMMON/calculations). K_ser ist nicht unabhängig von F_est.
  In den Versuchsblättern steht F_est in M5 (S5 = M5); direkt verwendet
  wird es in M8/S8 (0,1·F_est), M9/S9 (0,4·F_est), M19/S19 (K_i) und
  M20/S20 (K_ser nach Normformel) sowie in AD11/AE11 (F_est-Linie der
  LVK-Diagramme). Die K_ser-Werte, die das Blatt "Diagramme Steifigkeiten"
  verwendet (B6:G6 und B35:G35), stammen aus M21/S21
  (=(P12-P11)/(M12-M11)) und enthalten kein F_est in der Formel; F_est
  wirkt nur indirekt über die von Hand gewählten Zeilen V11 und V12
  (Punkte bei etwa 0,1 und 0,4·F_est). Dasselbe gilt für K_e (M22/S22,
  Zeilen V15/V16). Weil die Kraft-Schlupf-Kurve zu Beginn nichtlinear
  ansteigt (Spielausgleich, dann steiferer Ast), hängt die
  Sekantensteifigkeit vom gewählten Lastfenster ab.
  Zahlen (je 2×8-Gruppe, Mittel der drei Versuche): GL24h 279,5 kN/mm bei
  F_est = 480 kN (Fenster 48–192 kN) gegenüber 238 kN/mm bei
  F_est = 313,6 kN (Fenster 31–125 kN, Neuauswertung derselben Rohdaten
  durch Claude); GL75 727,7 kN/mm bei 800 kN gegenüber 547 kN/mm bei
  471,8 kN (Neuauswertung durch Claude, nicht im Wiki als Ergebnis
  abgelegt). Beide Werte sind aus Messdaten abgeleitet und beziehen sich
  nur auf unterschiedliche Lastniveaus. Die 192 kN (0,4 · 480 kN) sind die
  Umkehrlast im ersten Zyklus des Prüfprotokolls; die Erstbelastung ist
  bis dahin gemessen, das Fenster 31–125 kN liegt darin.
  Weitere Gesichtspunkte: (1) Gemessene F_max (GL24h Mittel 362 kN)
  liegt 13 % über 313,6 kN, aber 25 % unter 480 kN; nach Erinnerung von
  Claude soll F_est nach EN 26891 innerhalb von etwa ±20 % von F_max
  liegen (DIN EN 26891 liegt nicht im Quellenordner, nicht verifiziert).
  (2) In der realen 4×8-Gruppe entspricht 0,4·F_est (627 kN, C30) je
  2×8-Anteil 125 kN, also dem Fenster der C30-Basis. (3) Die F_est-Linie
  in den LVK-Diagrammen (480 kN bzw. 800 kN) lässt alle Versuche unter
  F_est erscheinen; gegen C30/2 liegen sie darüber (GL24h Faktor
  1,13–1,19, GL75 Faktor 1,23–1,37). Das ist auch für die Abschätzung der
  theoretischen Höchstlast bei GL75 relevant. Auswirkung auf die
  Zugpfadfeder c_T (GL24h): 279,5 kN/mm gegenüber 238 kN/mm.
related_sources:
options_considered: >
  (a) Planungswerte 480 kN / 800 kN beibehalten (Tabelle unverändert,
  K_ser 279,5 bzw. 727,7 kN/mm); (b) F_est aus C30 halbiert verwenden
  (313,6 kN / 471,8 kN) und K_ser aus den Rohdaten neu bestimmen (238 bzw.
  547 kN/mm) — im Blatt reicht dazu eine Änderung von M5 nicht, die
  Zeilen V11–V16 sind neu zu wählen; (c) ein festes, von F_est
  unabhängiges Kraftfenster festlegen oder die Steifigkeit als Funktion
  der Last angeben. Zu klären durch den Nutzer; Verwandt:
  R1-COMMON-OPQ-003 (LVDT-Bezugspunkte) für die Zugpfadfeder.
date_opened: "2026-09-21"
date_resolved:
resolution:
---

Aufgenommen auf Wunsch des Nutzers (2026-09-21). Bis zur Klärung sind alle
daraus abgeleiteten Zugpfad-Steifigkeiten als vorläufig zu kennzeichnen;
Claude rechnet vorläufig mit den K_ser-Werten der Tabelle (F_est = 480 kN
bei GL24h).

**Update (2026-09-21):** Für GL75 hat sich die C30-Basis geändert. Nach der
Bestätigung von n_ef = 7,308 (R1-GL75-OPQ-002, R1-GL75-CALC-003) ist
C30 = C72 = 1254,16 kN (4×8), je getesteter 2×8-Gruppe 627,08 kN; der
Nutzer verwendet diesen Wert für F_est. Die oben genannten Zahlen für GL75
"471,8 kN / 547 kN/mm" beruhen auf dem früheren n_ef und sind überholt. Die
Versuchsblätter I-T-B-SD-28-1 bis -3 rechnen weiter mit F_est = 800 kN (M5;
K_ser-Mittel 727,74 kN/mm), die Zeilen V11-V16 sind nicht neu gewählt und
K_ser wurde für das Fenster 0,1 bis 0,4 · 627,08 kN (63 bis 251 kN) noch
nicht ausgewertet. Höchstlasten der Versuche laut Excel 581,0 / 640,2 /
645,7 kN (Mittel 622,3 kN), also 0,93 bis 1,03 · 627,08 kN. Für GL24h
unverändert (Arbeitsstand F_est = 480 kN). Die Frage bleibt für GL75 OPEN.
