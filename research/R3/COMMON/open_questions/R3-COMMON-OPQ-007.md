---
open_question_id: R3-COMMON-OPQ-007
scope:
  connection: R3
  material: COMMON
status: OPEN
question: >
  Wie wirkt die Vorspannung der zugseitigen Stangen (F_V = 100 kN je Stange)
  auf das Momenten-Rotations-Verhalten von R3, und wie groß ist der
  Lastanteilsfaktor Φ, wenn zum verspannten Teil nicht nur die Lasche,
  sondern auch die ASSY-Gruppen und die Kontaktfuge Riegel/Stütze gehören?
context: >
  Nur die Laschen der Zugseite werden vorgespannt (R3-COMMON-DEC-001; Nutzer
  2026-09-30). Ohne Druckkontakt der Laschenhälften schließt sich die
  Vorspannkraft über Stange → Laschenhälften → ASSY → Riegel/Stütze →
  Kontaktfuge (Kraftfluss vom Nutzer bestätigt 2026-09-30). Überschlag
  (starre Körper, Bettung): Resultierende der Vorpressung auf der
  Stangenlinie 80 mm vom äußeren Rand, Exzentrizität zur Querschnittsmitte
  320 mm > Kern L/6 = 133 mm, nur ≈ 240 mm Kontakt außen; unter dem
  schließenden Moment wandert die Resultierende nach innen, die Kontaktzone
  ändert sich mit dem Moment (nichtlinear), bis die Fuge außen öffnet
  (F_sep). Danach gilt R3-COMMON-DEC-009 / R3-GL24h-CALC-016. F_sep ≈
  F_V/(1 − Φ) liegt grob bei der Hälfte der Stangentragfähigkeit (203 kN,
  GL24h), der vorgespannte Bereich ist damit für S_j,ini maßgebend.
  Excel "VSP GL24h ohne Druckkontakt": Φ = c_t/(c_t + c_H-ges) (C20) enthält
  als verspannte Teile nur die Lasche; C9 (c_t) verweist auf
  'Rahmenecke GL24h HD'!I78 = 0 (Wert steht im SD-Blatt jetzt in I108),
  daher Φ = 0 und #DIV/0! ab C17/C29; C10 nutzt noch den normativen
  c_ASSY,S = 199,15 kN/mm statt der Versuchswerte (R3-COMMON-DEC-005).
related_sources: Buchholz2025
options_considered: >
  Für die Übersichtstabelle (Besprechung 2026-09-30) vorerst der Zustand nach
  dem Öffnen der Fuge (untere Grenze der Anfangssteifigkeit); danach
  stückweise Kontaktrechnung für den vorgespannten Bereich.
date_opened: "2026-09-30"
date_resolved:
resolution:
---
