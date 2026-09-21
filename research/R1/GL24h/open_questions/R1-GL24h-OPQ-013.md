---
open_question_id: R1-GL24h-OPQ-013
scope:
  connection: R1
  material: GL24h
status: RESOLVED
question: >
  Darf für die Drehfeder c_v,f,rot der Dübelgruppen (Buchholz2025 Gl. 4:
  C_rot,v,f = K_ser · Σr² über alle Dübel der Gruppe) die Steifigkeit eines
  einzelnen Stabdübels (Ø12, zweischnittig, Stahl-Holz, GL24h) als
  K_ser,Dübel = c_T / 32 = 559,04 / 32 = 17,47 kN/mm angesetzt werden,
  obwohl dieser Wert aus Gruppenversuchen (2×8) abgeleitet ist und für
  GL24h Ø12 kein Einzeldübelversuch vorliegt?
context: >
  Anlass (Claude, 2026-09-21): c_v,f,rot ist im Blatt "Rahmenecke GL24h SD"
  (Zelle I18) bisher nur ein Platzhalter (1E+99, "Annahme wird
  vernachlässigt") und soll berechnet werden. Nach Buchholz2025 Gl. (4) und
  (5) geht je Dübelgruppe K_ser je Verbindungsmittel [N/mm] mit dem
  polaren Trägheitsmoment der Dübelanordnung Σr² [mm²] ein. Der Nutzer
  benötigt dafür K_ser eines einzelnen Dübels, nicht das K_ser der
  Gruppenversuche.
  Herleitung des Werts: K_ser (Mittel der drei Zugversuche I-T-S-SD-28-1/2/3,
  Blatt "Diagramme Steifigkeiten" H6) = 279,52 kN/mm je getesteter 2×8-Gruppe
  (16 Dübel), Lastfenster 0,1 bis 0,4·F_est mit vorläufig F_est = 480 kN
  (R1-COMMON-OPQ-004). Die reale Gruppe je Bauteil ist 4×8 (32 Dübel), also
  c_T = 2 · 279,52 = 559,04 kN/mm (Zelle I15 im Blatt). Je Dübel
  (zwei Scherfugen, Stahl-Holz): 559,04 / 32 = 279,52 / 16 = 17,47 kN/mm.
  Der Nutzer hat diese Rechnung am 2026-09-21 als Arbeitsannahme gewählt
  ("559,04/32 als Annahme für K_ser Einzeldübel").
  Plausibilität: Die Formel ρ_m^1,5 · d / 23 (EC5/FprEN-Tab. 11.12) ergibt
  mit ρ_m = 420 kg/m³ und d = 12 mm 4,49 kN/mm je Scherfläche; mit Faktor 2
  (Stahl-Holz) und 2 Scherfugen 17,96 kN/mm je Dübel (Blatt "Diagramme
  Steifigkeiten", C19 = 287,414 kN/mm für 16 Dübel). Der Versuchswert liegt
  bei 97 % davon. Streuung der Versuche: Standardabweichung 53,3 kN/mm,
  Variationskoeffizient 0,19 (sechs Werte OBEN/UNTEN der drei Versuche, laut
  Blatt). Die im Blatt geführten Werte mit Gruppenabminderung liegen für 16
  Dübel niedriger (prEN mit n_ef = 12: 215,6; Buchholz: 198,2; Gauß: 205,6;
  SIA 265: 268,9 kN/mm; Werte aus dem Blatt, von Claude nicht nachgerechnet);
  eine solche Abminderung ist im Versuchswert nicht sichtbar.
  Grenzen der Annahme: (1) 17,47 kN/mm ist ein effektiver Gruppenwert, kein
  gemessener Einzeldübel; Gruppenwirkung, Lochspielanteil im gewählten
  Lastfenster (vgl. R1-GL24h-DEC-007, u_0 und u_el getrennt) und die
  Messbasis der Wegaufnehmer (R1-COMMON-OPQ-003) stecken im Wert.
  (2) Der Wert hängt am Lastfenster: bei F_est = 313,6 kN wäre das Mittel
  238 kN/mm, also 14,9 kN/mm je Dübel (R1-COMMON-OPQ-004; Neuauswertung der
  Rohdaten durch Claude). (3) Einzeldübelversuche in der Auswertedatei
  ("Auswertung Steifigkeiten_0703_Zugversuche_Stahl-Holz-Stabdübel"): fünf
  Blätter "HO-SD8 11 0 1 t2 2/3, t3 1/2/3", d = 8 mm, ρ_m = 800 kg/m³
  (Hartholz), ein Dübel, Faktor Stahl 2, zwei Scherfugen. K_ser (Mittel aus
  OBEN und UNTEN) 20,2 / 27,9 / 21,8 / 15,0 / 20,3 kN/mm, Mittelwert 21,1
  kN/mm (Streuung ca. 22 %), das sind etwa 0,67 · K_ser,EC5 (31,48 kN/mm).
  Für GL24h Ø12 nicht übertragbar (anderes Material und Durchmesser). Die
  Zeilen "HO-SD12 …" in der Überblick-Tabelle sind #REF!, Blätter dafür
  fehlen in der Kopie; die Bedeutung der Kürzel "11 0 1" und "t2/t3" ist im
  Arbeitsbuch nicht erklärt. (4) Der IGF-Bericht 20625 N (Gauß) enthält nach
  Claudes Durchsicht Einzeldübelversuche mit d = 12, 16 und 20 mm, darunter
  BSH GL24h; er ist nicht in bibliography/sources.yaml geführt, die Werte
  sind nicht ausgewertet.
  Nicht Gegenstand dieser Frage, aber verwandt: Wie C_rot,v,f mit dem
  Zugpfad kombiniert wird. Die Abbildung des Federmodells zeigt c_v,f,rot,
  c_v,f und c_br,par in Reihe (siehe R1-COMMON-OPQ-003), Buchholz2025
  Gl. (5) addiert die Drehfedern dagegen; Claudes Lesart (Drehung der
  Gruppe um den eigenen Schwerpunkt als paralleler Zusatz zum Kräftepaar
  je Bauteil) ist nicht bestätigt.
related_sources: Buchholz2025, FprEN-1995-1-1-2024
options_considered: >
  (a) K_ser,Dübel = 17,47 kN/mm (Versuch, c_T / 32) als Arbeitsannahme;
  konsistent mit der Translationsfeder c_T, die denselben Dübelwert enthält;
  der EC5-Wert 17,96 kN/mm dient als Gegenprobe. (b) K_ser,Dübel =
  17,96 kN/mm (Formelwert, unabhängig von Versuchsfenster und Messbasis).
  (c) Einzeldübelversuche für GL24h Ø12 heranziehen (IGF-Bericht Gauß oder
  eigene Versuche) und K_ser,Dübel daraus bestimmen; Quelle noch nicht
  erschlossen. (d) Einfluss als Sensitivität ausweisen: C_rot,v,f ist linear
  in K_ser, die Spanne 14,9 bis 17,96 kN/mm (F_est-Basis und EC5) ergibt
  etwa minus 15 % bis plus 3 % gegenüber 17,47 kN/mm.
date_opened: "2026-09-21"
date_resolved: "2026-09-21"
resolution: >
  Der Nutzer hat am 2026-09-21 entschieden, für die Drehfeder den Normwert
  anzusetzen: K_ser,Dübel = 17,96 kN/mm (ρ_m^1,5 · d / 23 nach FprEN Tab.
  11.12 mit ρ_m = 420 kg/m³ und d = 12 mm, also 4,49 kN/mm je Scherfläche,
  verdoppelt für Stahl-Holz und mal 2 Scherfugen). Der aus dem Versuch
  abgeleitete effektive Wert 17,47 kN/mm (c_T / 32) dient als Gegenprobe
  (Abweichung 2,8 %); die Lesart B (23,29 kN/mm mit Reihendeckel) wird nicht
  verwendet. Damit ist C_rot,v,f je 4×8-Gruppe 21.111 kNm/rad (I_p =
  1.175.200 mm²). Festgehalten in R1-GL24h-DEC-010. Nicht entschieden ist
  die Kombination der vier Drehfedern (Gl. 5 wörtlich oder Träger/Stütze in
  Reihe). Zur Herkunft des Normwerts siehe R1-GL24h-OPQ-014.
---

Aufgenommen auf Wunsch des Nutzers (2026-09-21) und am selben Tag vom
Nutzer entschieden (siehe `resolution`, R1-GL24h-DEC-010). Zwischenstand
vor der Entscheidung: Arbeitsannahme (a), K_ser,Dübel = 17,47 kN/mm.
Geometrie der Dübelgruppen: a_1 = 80 mm und a_2 = 50 mm vom Nutzer als
Annahme bestätigt (4×8 je Gruppe); die Druckgruppe ist laut Nutzer
(2026-09-21) geometrisch identisch mit der Zuggruppe. Die Frage, ob der
Normwert selbst versuchsgestützt ist, steht in R1-GL24h-OPQ-014.

**Update (2026-09-21):** Der Nutzer hat bestätigt, dass es auch auf der
Druckseite eine Dübelgruppe gibt und dass K_ser,Dübel dort gleich dem der
Zugseite angesetzt wird (Annahme des Nutzers, für die Druckseite liegen
keine Versuche vor). Das Federmodell (Buchholz2025, Abb. 3) führt damit
vier Drehfedern C_v,f,rot: Träger-Zugzone, Stütze-Zugzone, Träger-Druckzone,
Stütze-Druckzone, je eine je Dübelgruppe. Damit wird für die Drehfeder nur
K_ser,Dübel und die Geometrie (Σr²) jeder der vier Gruppen benötigt; die
fehlenden Druckseitenversuche betreffen die Translationsfeder des
Druckpfads, nicht C_v,f,rot.

**Update 2 (2026-09-21), Nachfrage des Nutzers, ob c_T/32 wirklich K_ser
ist:** Nein, nicht im Sinn der Norm. 559,04 / 32 = 17,47 kN/mm ist ein
effektiver Dübelwert der getesteten Gruppe (Gruppensteifigkeit geteilt
durch die Dübelzahl), kein K_ser eines Einzeldübels. Nach FprEN 1995-1-1
Abschn. 11.3.8.2, Gl. (11.26) ist die Gruppensteifigkeit nicht n · K:
K_SLS,v = Σ (Reihen i) min{n_0,i; 6} · m · K_SLS,v,i, mit K_SLS,v,i je
Scherfläche und Dübel nach Tab. 11.12 und Verdopplung bei Stahl-Holz
(11.3.8.2 (5)). Für die getestete 2×8-Gruppe (m = 2) sind das 2 · 6 · 2 ·
(2 · 4,49) = 215,6 kN/mm (Blatt: K_ser,prEC5 = 215,56), für die reale 4×8-
Gruppe 431,1 kN/mm. Die Versuchswerte 279,52 bzw. 559,04 kN/mm liegen
30 % darüber und nur 3 % unter dem Wert ohne Reihendeckel (287,4 bzw.
574,8 kN/mm). Meine frühere Aussage, der Versuch stimme gut mit EC5 überein,
gilt nur gegen den Wert ohne Reihendeckel; gegen die prEN-Gruppenformel ist
der Versuch deutlich steifer. Zwei Lesarten sind mit dem Versuch vereinbar:
(A) kein Reihendeckel wirksam, K_Dübel = 279,52/16 = 17,47 kN/mm; (B) der
Reihendeckel gilt, dann wäre K_Dübel = 279,52/12 = 23,29 kN/mm (1,30 · Tab.
11.12 mit Verdopplung). Ob der Versuchswert außerdem Holz- und
Blechverformung zwischen den Messpunkten (R1-COMMON-OPQ-003) und
Lochspiel im Lastfenster (R1-COMMON-OPQ-004) enthält, ist offen. Die
Translationsfeder c_T ist als gemessene Gruppensteifigkeit davon nicht
betroffen; nur die daraus abgeleitete Einzeldübelsteifigkeit ist es.
Buchholz2025 nennt für Gl. (4) das "lateral slip modulus K_ser ... e.g.
according to Tab. 11.12", also den Normwert je Verbindungsmittel.
Auswirkung auf C_rot,v,f je 4×8-Gruppe (I_p = 1.175.200 mm², a_1 = 80 mm,
a_2 = 50 mm): (A) 17,47 kN/mm ergibt 20.531 kNm/rad; Normwert 17,96 kN/mm
(Tab. 11.12, doppelt für Stahl-Holz, m = 2) 21.111 kNm/rad (+2,8 %);
(B) 23,29 kN/mm 27.374 kNm/rad (+33 %).
