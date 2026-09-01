---
open_question_id: R2-COMMON-OPQ-001
scope:
  connection: R2
  material: COMMON
status: OPEN
question: >
  Wie ist die genaue Druckzonenlänge/-verteilung am Rahmeneck-Innenknoten
  anzusetzen (rechteckige vs. dreieckige Pressungsverteilung), und wo
  liegt der resultierende Kraftangriffspunkt/Hebelarm?
context: >
  Bestimmt `A_c`, `c_c,90`, `c_c,0` sowie die Lage des
  Druckresultierenden und damit den Hebelarm `z` für das
  Momenten-Rotations-Modell der Druckseite. Ohne diese Geometrie können
  die Druckseiten-Federn `c_c,90`/`c_c,0` und die daraus kombinierte
  Rotationssteifigkeit nicht berechnet werden.
related_sources:
options_considered: >
  Aktuelle Druckverteilungsannahme aus dem Festigkeitsmodell übernehmen,
  oder ein gewähltes Dreiecks-/Rechtecks-Kontaktmodell mit eigener
  Herleitung ansetzen.
date_opened: "2026-09-01"
date_resolved:
resolution:
---

Übernommen aus chat-3, OPEN_QUESTIONS.md Punkt 1, und TASKS.md
("Blocked / needs input — P1 — Compression-zone length"). Diese Frage
blockiert laut TASKS.md direkt die Bearbeitung von `c_c,90`, `c_c,0` und
der finalen Rotationssteifigkeit (siehe auch R2-COMMON-OPQ-006).
Materialunabhängig geführt, da die Druckzonen-Geometrie primär von der
Rahmeneck-Konstruktion, nicht vom Holzwerkstoff abhängt.
