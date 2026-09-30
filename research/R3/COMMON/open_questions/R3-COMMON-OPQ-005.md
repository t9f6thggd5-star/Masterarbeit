---
open_question_id: R3-COMMON-OPQ-005
scope:
  connection: R3
  material: COMMON
status: OPEN
question: >
  Ist das einfache Schubfeldmodell c_v = G·b·h_v/l_v (Holz + Platten
  parallel) für R3 ausreichend, insbesondere weil die Verstärkungsplatten
  (l = 460 mm) kürzer sind als das Holzfeld (800 mm)?
context: >
  Rechenweg aus R2 übernommen (R3-COMMON-DEC-007). Die Parallelschaltung
  nimmt gleiche Verformung von Holz und Platte an; eine kürzere Platte
  überbrückt nur einen Teil des Feldes, das Ergebnis ist eher zu steif. Anteil
  der Platten klein (2 · 26 von 156 kN/mm GL24h). G_P = 500 N/mm² ist eine
  Annahme ("KLH ETA Scheibenbeanspruchung", Quelle nicht registriert). Für
  Holz gibt es keine Katalogformel (Nr. 5 nennt nur G nach EN 14080); im
  Stahlbau genauer k_1 = 0,38·A_vc/(β·z) mit Übertragungsparameter β.
  Gilt sinngemäß auch für R2.
related_sources: Buchholz2025
options_considered: >
  Vorerst einfaches Modell (Nutzerentscheidung 2026-09-28).
date_opened: "2026-09-28"
date_resolved:
resolution:
---
