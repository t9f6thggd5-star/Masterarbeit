---
open_question_id: R3-COMMON-OPQ-006
scope:
  connection: R3
  material: COMMON
status: OPEN
question: >
  Wie wird in der schriftlichen Ausarbeitung begründet, dass Sprödversagen
  (br,par, br,perp) der ASSY-Schraubengruppen bei R3 nicht maßgebend wird
  (R3-COMMON-DEC-008)?
context: >
  Die Annahme beruht bisher auf der Einschätzung des Nutzers, nicht auf einem
  Nachweis. Mögliche Bausteine: (1) FprEN 11.5/11.6 mit Mittelwerten
  (γ_M = 1, k_mod = 1) gegen die Stangentragfähigkeit 203 kN (GL24h) bzw.
  293 kN (GL75) je Lasche (R3-COMMON-DEC-003); (2) Push-Out-Versuche 4×4 als
  Kalibrierung des Normmodells, sofern dort kein br-Versagen auftrat
  (Versagensmodi 44-C bisher nicht im Wiki; GL75-44er noch nicht ausgewertet,
  R3-GL75-ASS-001); (3) qualitativ: Bruchflächen für Block- und Reihenscheren
  wachsen mit der Gruppenlänge (8 statt 4 Reihen), die Schraubentragfähigkeit
  wegen des Gruppeneffekts etwas weniger. Offen außerdem, welche Norm-
  regel für axial beanspruchte, 45° geneigte Schrauben passt: 11.5 ist auf
  quer belastete Verbindungsmittel formuliert (11.5.1 (4)); für axial
  beanspruchte Gruppen nennt 11.6.1 (7) Rollschub entlang des Gruppenumfangs
  (n_0 > 2). Buchholz2025 ordnet Nr. 13 trotzdem 11.5 zu.
related_sources: Buchholz2025, FprEN-1995-1-1-2024
options_considered: >
  Vorerst keine Rechnung; Begründung spätestens bei der Ausarbeitung
  (Nutzerentscheidung 2026-09-30). Ggf. Frage an die Betreuung.
date_opened: "2026-09-30"
date_resolved:
resolution:
---

**Update (2026-09-30), Literaturrecherche:** Keine Quelle mit eigener
Steifigkeitsfeder für br,par/br,perp gefunden; die Kataloge (Buchholz2025
Tab. 1, Gauß 2024 Tab. 6.1) führen nur die Tragfähigkeit. Steifigkeitsbasierte
Tragfähigkeitsmodelle (Zarnani & Quenneville 2014; Mahlknecht & Brandner 2019)
bilden den Holzblock elastisch als Federsystem ab, nutzen das aber nur zur
Lastaufteilung. Argument für "starr" (Claude, zu prüfen): Die elastische
Blockverformung steckt in K_ser der Push-Out-Versuche und in c_H; eine eigene
Feder würde doppelt zählen. Für die Tragfähigkeit relevant: Scheibmair 2012
(Block tear-out beim Quick Connect, S. 65–66), Mahlknecht & Brandner 2019 und
Blaß/Flaig/Meyer 2019 (axial beanspruchte Schraubengruppen), Meyer 2020
(Buchen-FSH), Jockwer & Dietsch 2018 (quer zur Faser). Zusammenstellung im
Projektdokument claude/R3-Sproedversagen_br_Literatur.md. Die Quellen sind
noch nicht in bibliography/sources.yaml eingetragen; mehrere sind nur über den
Abstract geprüft.

