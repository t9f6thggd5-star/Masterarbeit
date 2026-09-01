---
decision_id: R2-GL24h-DEC-005
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Welche Geometrie wird für die 9 ASSY-Querdruckverstärkungsschrauben
  (3×3-Anordnung) endgültig angesetzt?
decision: >
  `ASSY plus VG 4 CSMP 8×580`, `n=9` (3×3), `d=8 mm`, `d_1=5,0 mm`,
  `l_w = l_r = 580 mm`, `n_0=3`, `a_1=80 mm`, `a_3,c=40 mm`.
reason: >
  Endgültige, konsistente Geometrie nach Korrektur früherer fehlerhafter
  Zwischenstände.
alternatives_considered: >
  Frühere Einklebelänge 545 mm (verworfen); ein zwischenzeitlich
  fehlerhafter Gewindeinnendurchmesser `d_1=6,2 mm` (verworfen, korrekt
  `5,0 mm`).
date: "UNKNOWN (chat-3, seq 175-182; kein genaues Datum überliefert)"
---

Übernommen aus chat-3, DECISIONS.md "Seq 175-182 — ASSY geometry"
("Supersedes: earlier 545 mm embedded length and a temporary mistaken
`d1 = 6.2 mm`"). Gegen R2-Excel verifiziert (Sheet "Rahmenecke GL24h SD",
Zellen H76-H92: `d=8` (H76), `d_1=5` (H77), `l_w=580` (H87), `l_r=580`
(H88), `n=9` (H81), `n_0=3` (H82), `a_1=80` (H79), `a_3,c=40` (H80)).
Effektive Längen: `l_1,ef=270 mm` (H91, Gl. 8.13), `l_2,ef=780 mm` (H92,
Gl. 8.15). Nur für GL24h im R2-Excel modelliert — für GL75 existiert kein
entsprechender Verstärkungsblock (siehe R2-GL75-OPQ-002).
