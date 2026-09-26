---
open_question_id: R1-COMMON-OPQ-009
scope:
  connection: R1
  material: COMMON
status: OPEN
question: >
  Ist die Summe der vier Drehfedern in Buchholz2025 Gl. (5) so gemeint,
  obwohl Träger- und Stützengruppe bei der Zugfeder (Gl. 2) in Reihe liegen?
  Kinematisch setzt sich die Eckverdrehung aus Träger gegenüber Blech und
  Stütze gegenüber Blech zusammen (φ = θ_Träger + θ_Stütze), was auch für die
  Drehfedern eine Reihenschaltung von Träger und Stütze nahelegen würde.
context: >
  Frage für die Besprechung mit der Betreuung am Mittwoch, 2026-09-30
  (Nutzer, 2026-09-26; bewusst nicht in die E-Mail aufgenommen). Zug- und
  Druckgruppe desselben Bauteils drehen gemeinsam (parallel); der Druckkontakt
  legt den Drehpunkt fest, verhindert aber nicht die Drehung der Druckgruppe
  gegenüber dem Blech. Annahme dabei: das Blech stellt sich frei zwischen
  Träger und Stütze ein. Gerechnet wird nach Gl. (5) wie gedruckt
  (R1-COMMON-DEC-004). GL24h: Gl. (5) Σ C_rot,v,f = 84.444 kNm/rad,
  C_rot,tot = 168.997 kNm/rad, Φ(399,5 kNm) = 2,36 mrad, u_M(a = 3,03 m) =
  7,2 mm; Träger/Stütze in Reihe Σ = 21.111 kNm/rad, C_rot,tot = 105.666
  kNm/rad, Φ = 3,78 mrad, u_M = 11,5 mm.
related_sources: Buchholz2025
options_considered: >
  (a) Gl. (5) wie gedruckt (aktuell); (b) je Bauteil Zug-/Druckgruppe
  parallel, Träger und Stütze in Reihe (ergibt einmal C_rot,v,f).
date_opened: "2026-09-26"
date_resolved:
resolution:
---
