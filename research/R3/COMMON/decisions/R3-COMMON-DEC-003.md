---
decision_id: R3-COMMON-DEC-003
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Mit welcher Zugtragfähigkeit der Gewindestangen (8.8, GL24h M20, GL75 M24)
  wird die geschätzte Höchstlast bzw. M_max der R3-Rahmenecke angesetzt,
  solange kein Komponentenversuch an den Stangen vorliegt?
decision: >
  F_t = Mindestbruchkraft F_m,min nach DIN EN ISO 898-1:2013, Tab. 4
  (= A_s,nom · R_m,min, R_m,min = 830 MPa für 8.8 bei d > 16 mm, Tab. 3 Nr. 1):
  M20 (A_s = 245 mm²) 203 kN, M24 (A_s = 353 mm²) 293 kN, je Laschenseite.
  Kein Zuschlag für Überfestigkeit.
reason: >
  Nutzerentscheidung (Chat, 2026-09-28). Der bisherige Excel-Wert
  0,9 · f_ub · A_s (EN 1993-1-8, k₂ = 0,9, f_ub = 800 MPa; 176,4 bzw. 254,16 kN)
  ist ein Bemessungsansatz und für eine Abschätzung der Höchstlast zu niedrig;
  die übrigen Tragfähigkeiten werden mit Mittelwerten geschätzt. F_m,min wird
  an der fertigen Schraube inkl. Gewinde geprüft, eine zusätzliche Abminderung
  entfällt. Ein Überfestigkeitszuschlag (bei R2 BR-11, M16 4.6: gemessen
  72,34 kN = 1,15 · F_m,min) ist für 8.8-Stangen nicht durch Versuche belegt.
alternatives_considered: >
  0,9 · f_ub · A_s nach EN 1993-1-8 (bisher, verworfen); F_m,min · 1,15 mit
  Überfestigkeit analog R2 (verworfen, nicht belegt, höchstens als Obergrenze).
date: "2026-09-28"
superseded_by:
---

Quelle: DIN-EN-ISO-898-1-2013, Tab. 3 (S. 13) und Tab. 4 (S. 15). Folge
(z = 586,7 mm, zwei Laschenseiten, Stange bleibt maßgebend gegenüber
ASSY-Gruppe und Holzpressung): M_max GL24h ≈ 238,2 kNm (bisher 206,98),
GL75 ≈ 343,8 kNm (bisher 298,21), je +15 %. Holzpressung bei GL75 im Blatt
noch zu prüfen. Der Hebelarm z selbst ist noch nicht festgelegt
(Excel 586,7 mm, R3-GL24h-DEC-007 vorläufig 640 mm).
