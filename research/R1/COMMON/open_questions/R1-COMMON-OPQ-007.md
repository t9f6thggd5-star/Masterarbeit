---
open_question_id: R1-COMMON-OPQ-007
scope:
  connection: R1
  material: COMMON
status: RESOLVED
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
date_resolved: "2026-09-30"
resolution: >
  M_R wird über das Kräftepaar nachgewiesen (M_R = T_max · z); die Drehfedern
  gehen nur in die Steifigkeit ein. In einer späteren Phase, z. B. beim Vergleich
  der berechneten mit den gemessenen Last-Verschiebungskurven, kann die
  Umlagerung durch die Gruppendrehung erneut Thema werden. Nutzer, 2026-09-30.
---

Wird in der E-Mail an die Betreuung vom 2026-09-26 (Punkt 1) gefragt.

**Update (2026-09-26), Diskussion mit dem Nutzer:** Wie in der
Komponentenmethode des Stahlbaus wird die Momententragfähigkeit über das
Kräftepaar nachgewiesen (M_R = T_max·z = 399,49 kNm, unabhängig von den
Steifigkeiten); die Drehfedern gehen nur in die Steifigkeit ein. Die
abweichende Lastaufteilung (elastisch für die Steifigkeit, plastisch für die
Tragfähigkeit) ist dort methodisch üblich. Konservative elastische
Kontrollrechnung (Claude): Moment nach Steifigkeiten verteilt, Dübelkraft
aus Kräftepaar (T/32) und Gruppendrehung vektoriell addiert, Tragfähigkeit
je Dübel 22,7 kN (726,35/32), quer zur Faser mit k_90 = 1,53 abgemindert;
maßgebend der Eckdübel (x = 280, y = 75 mm). Ergebnis: Gl. (5) M ≈ 398 kNm
(±0 %), Träger/Stütze in Reihe ≈ 364 kNm (−9 %); die Übereinstimmung bei
Gl. (5) ist geometrieabhängig und nicht verallgemeinerbar. Einwand des
Nutzers: Die Zugversuche wurden nur zentrisch gefahren, Drehsteifigkeit und
Tragfähigkeit der Gruppe bei Drehung (Belastung quer zur Faser, Spalten
br,perp) sind nicht versuchsgestützt. Voraussetzungen für M_R = 399,49 kNm
bleiben: übrige Komponenten nicht schwächer (Druckseite, Blech, br,perp),
Hochrechnung 2×8 → 4×8 beim Blockscheren (E-Mail Frage 6). In der E-Mail
vom 2026-09-26 als Frage 1 ("Tragfähigkeit über Kräftepaar, Drehfedern nur
Steifigkeit – so gedacht?"). Summe der Drehfedern: R1-COMMON-OPQ-009.
