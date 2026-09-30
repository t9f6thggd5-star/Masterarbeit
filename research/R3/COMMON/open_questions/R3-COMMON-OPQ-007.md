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
related_sources: Buchholz2025, ScheibmairQuenneville2014, VDI-2230-1-2015
options_considered: >
  Für die Übersichtstabelle (Besprechung 2026-09-30) vorerst der Zustand nach
  dem Öffnen der Fuge (untere Grenze der Anfangssteifigkeit); danach
  stückweise Kontaktrechnung für den vorgespannten Bereich.
date_opened: "2026-09-30"
date_resolved:
resolution:
---

**Beobachtung in der Literatur (SOURCE_CLAIM, 2026-09-30):**
ScheibmairQuenneville2014 (S. 04013022-8) berichten für den Versuch Holz auf
Holz des Quick Connect (LVL, Querschnitt 105 × 1050 mm) eine erhöhte
Anfangssteifigkeit bis ≈ 59 kNm, "at which point the tension force in the
rods has overcome the elastic compression in the sleeves and the tension
sleeves begin to separate at the beam–column interface"; danach etwa
linear-elastisch bis zum Versagen (Längsschub im Riegel) bei ≈ 588 kNm und
0,0987 rad. Die Autoren führen die Steifigkeitswechsel auf ungleichmäßig
angezogene Stangen und die vorhandene Vorspannung zurück; eine leichte
Versteifung zwischen ≈ 120 und 220 kNm deuten sie als Setzen auf der
Druckseite bis zum vollen Kontakt. Stützt den oben beschriebenen Kraftfluss
(Vorpressung der Fuge Riegel/Stütze, Öffnen an der Zugseite) qualitativ;
Übertragung auf GL24h/R3-Geometrie nicht belegt, n = 1 Versuch je
Konfiguration.

**Update (2026-09-30), Kontakt der Laschenhälften:** Nach R3-COMMON-DEC-011
schließt sich die Vorspannung über die Stoßfuge der Laschen; nach
R3-COMMON-DEC-014 teilt sie sich nach Steifigkeit auf diesen Weg und den Weg
über ASSY und Holzkontakt Riegel/Stütze auf (Nutzer). Der oben beschriebene
Kraftfluss ohne Kontakt gilt damit nicht mehr als Hauptvariante.
Überschlag (Claude, ohne Aufteilung, Laschen starr gekoppelt über die
Stoßfuge, gleiche Reihenlast F/8): Lastanteil der Stange Φ ≈ 0,12, Öffnen der
Stoßfuge bei T ≈ F_V/(1 − Φ) ≈ 113 kN je Lasche (≈ 227 kN für beide, etwa
56 % der Stangentragfähigkeit 406 kN); davor ist die Zugseite etwa doppelt
so steif wie nach dem Öffnen. Die Excel-Blätter "VSP … ohne Druckkontakt"
sind entsprechend neu aufzubauen.

