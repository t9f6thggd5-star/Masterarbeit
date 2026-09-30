---
decision_id: R3-COMMON-DEC-014
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Wie werden Kraftfluss und Federkomponenten von R3 mit Kontakt der
  Laschenhälften an der Stoßfuge (R3-COMMON-DEC-011) für die Vorbemessung
  abgebildet?
decision: >
  Druckseite (spiegelbildlich zur Zugseite, ohne Vorspannung): zwei Wege
  parallel, (1) Holzkontakt Riegel/Stütze wie R3-COMMON-DEC-009 (dreieckige
  Druckzone, Nulllinie aus Gleichgewicht) und (2) Laschen: ASSY-Gruppe Riegel
  → Laschenhälfte auf Druck → Stoßfuge → Laschenhälfte → ASSY-Gruppe Stütze,
  wirksam in der Stangenlinie 80 mm vom gedrückten Rand. ASSY-Gruppen der
  Druckseite mit derselben Steifigkeit wie auf der Zugseite (137,9 / 183,7
  kN/mm). Stoßfuge (Hirnholz auf Hirnholz) starr. Gewindestange der
  Druckseite unbelastet (Ankerplatte hebt von der Mutter ab).
  Zugseite (vorgespannt): Vorspannung teilt sich nach Steifigkeit auf den Weg
  über die Stoßfuge der Laschen und den Weg über ASSY und Holzkontakt
  Riegel/Stütze auf. Bis zum Öffnen der Stoßfuge wirkt das Laschenstück
  zwischen Schraubengruppe und Stoßfuge parallel zum Weg über die Stange;
  danach gilt die bisherige Zugkette (R3-GL24h-CALC-018).
reason: >
  Nutzerentscheidungen (Chat, 2026-09-30): Druckseite spiegelbildlich, dort
  keine Vorspannung, Stoß in derselben Fuge; ASSY gleiche Steifigkeit wie
  Zugseite; Stoßfuge starr; Stange Druckseite unbelastet; Vorspannung nach
  Steifigkeit aufteilen. Kraftfluss von Claude vorgeschlagen, vom Nutzer so
  übernommen. Festlegung für die Vorbemessung nach COMMON-COMMON-DEC-011.
alternatives_considered: >
  Stellschrauben für den Versuchsvergleich: ASSY auf Druck (Einschieben)
  weicher als auf Zug (z. B. ohne Reibanteil in der Fuge); Setzen der
  Stoßfuge (Hirnholzkontakt, Passung) als Schlupf oder Feder; Vorspannung
  vollständig in den Laschen (einfacher, etwas steifer); Stange der
  Druckseite mit Kontermutter (auf Druck mittragend).
date: "2026-09-30"
superseded_by:
---

Geometrie nach Plan 2685085-003-01-03 (Außenlasche GL 24h) und
2685085-003-V1, Detail Z/Y: Laschenhälfte 800 mm = 170 mm (Ankerplatte bis
erste Schraubenreihe) + 7 × 80 mm + 70 mm (letzte Reihe bis Stoßfuge),
Laschenquerschnitt 80 × 160 mm, A_netto = 11 678 mm², Stange in
Laschenmitte (80 mm vom Rand).

Offen: welche Laschenlänge in die Stauchungsfedern eingeht (Zug- und
Druckseite, R3-COMMON-OPQ-003). Ersetzt R3-COMMON-DEC-009 nicht, sondern
ergänzt die Druckseite um den Laschenweg; die Berechnung folgt.

Überschlag GL24h (Claude, 2026-09-30, Laschenlänge wie bisher 450 mm Zug /
350 mm Druck, Bettung des Holzkontakts konstant gehalten): Laschen der
Druckseite zusammen ≈ 112 kN/mm (Holzkontakt 110,5 kN/mm), Nulllinie
≈ 170 statt 253 mm, S_j,ini nach dem Öffnen der Stoßfuge ≈ 10 660 statt
8 878 kNm/rad.

**Abgleich mit Buchholz2025, Bild 5 / Gl. (11), (12), (6), (3), (5) (2026-09-30):**

| Komponente (Buchholz) | Buchholz | Festlegung Vorbemessung | Abweichung / Stellschraube |
|---|---|---|---|
| c_t (Nr. 0S) | Stange auf Zug | E·A_s/L_b = 30,99 kN/mm, ohne Faktor 1,6 (R3-COMMON-DEC-006) | – |
| 2 · c_c,ep (Nr. 15) | Ankerplatte auf Hirnholz | starr, kein Setzen (R3-COMMON-DEC-005, OPQ-002) | Setzen der Platten |
| 2 · c_ax,v,f,α (Nr. 11) | ein Wert je Gruppe | Push-Out: Stütze 183,7, Riegel 137,9 kN/mm (Spanne 130–147) | Riegelwert n = 1 |
| c_br,perp, c_br,par (Nr. 13/14) | nur Tragfähigkeit | starr (R3-COMMON-DEC-008) | – |
| 2 · c_c,0 (Nr. 3) | Deutung offen | (a) Laschenstauchung c_H und (b) Stoßfuge starr | Laschenlänge (OPQ-003), Setzen Stoßfuge |
| Hülsen ①, ② parallel | ja | 2 · c_t,sleeve | – |
| c_v (Nr. 5) | Holz auf Schub | Holz + 2 BFU-Platten, G_v = 520, κ = 1 (OPQ-005) | Modell Schubfeld, z statt l_v (OPQ-008) |
| C_v,f,rot (Nr. 11, Gl. 4/5) | je Gruppe I_p · K_ser, parallel addiert | **noch nicht angesetzt** | R3-COMMON-OPQ-009 |
| Druckzone c_c,90 + c_c,0 (Gl. 6) | nur Kontakt Riegel/Stütze („wahrscheinlich auch über die Hülsen“) | Kontakt nach FprEN Gl. (9.31) mit h_ef, l_0 = x, dreieckige Druckzone | – |
| Hülsen der Druckseite | nicht im Modell | parallel zum Kontakt, 80 mm vom Rand | ASSY auf Druck, Laschenlänge |
| Hebelarm z, Gl. (3) | Abstand der Resultierenden | Nulllinie aus Gleichgewicht, S = Σ c_i · a_i² um die Nulllinie (gleichwertig zu Gl. 3 mit c_c,eq = ¾ c_c,tot) | – |
| Vorspannung | nur über c_c,ep erwähnt | eigene Phase bis zum Öffnen der Stoßfuge, Aufteilung nach Steifigkeit (OPQ-007) | Höhe F_V, Verluste |
| Schubdübel | nicht im Federmodell | nicht im Federmodell | Einfluss auf Rotation |
