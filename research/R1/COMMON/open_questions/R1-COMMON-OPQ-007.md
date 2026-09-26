---
open_question_id: R1-COMMON-OPQ-007
scope:
  connection: R1
  material: COMMON
status: OPEN
question: >
  Wie wird die Momententragfähigkeit der R1-Rahmenecke konsistent zum
  Federmodell nach Buchholz2025 Gl. (5) nachgewiesen, wenn Kräftepaar und
  Gruppendrehung dieselben Dübel beanspruchen? Welche Tragreserve aus der
  Gruppendrehung darf angesetzt werden (insbesondere bei sprödem Versagen
  wie dem Blockscheren bei GL24h)?
context: >
  Nach Gl. (5) tragen die vier Drehfedern etwa die Hälfte des Moments
  (GL24h: 84.444 von 168.997 kNm/rad). M_R wird bisher nur über das
  Kräftepaar gerechnet (M_R = T_max·z = 399,49 kNm); bei diesem Moment sind
  die Zuggruppen im Modell erst bei ≈ 181 kN je 2×8-Gruppe (≈ 50 % von
  F_max) (R1-GL24h-CALC-010). Die Gruppendrehung ist eine reale Reserve
  (Dübelkreis-Prinzip), ist aber nur nutzbar, wenn die kombinierte
  Dübelbeanspruchung (Kräftepaar + Drehung, vektoriell an den äußeren Dübeln)
  nachgewiesen ist. Ein reines Addieren (Kurve bis F_max ausgenutzt ergäbe
  M ≈ 927 kNm) ist keine Tragfähigkeit. Nutzer (2026-09-26): gerade das
  Ausnutzen solcher Reserven ist Ziel der Komponentenmethode.
related_sources: Buchholz2025
options_considered: >
  (a) M_R nur Kräftepaar (bisher, konservativ); (b) Aufteilung von M nach
  Steifigkeitsanteilen und Nachweis des am stärksten beanspruchten Dübels
  bzw. der Gruppe unter kombinierter Beanspruchung; (c) Summe der vier
  Drehfedern in Gl. (5) mit der Reihenschaltung Träger/Stütze abgleichen.
date_opened: "2026-09-26"
date_resolved:
resolution:
---

Wird in der E-Mail an die Betreuung vom 2026-09-26 (Punkt 1) gefragt.
