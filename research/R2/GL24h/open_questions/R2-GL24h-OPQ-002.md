---
open_question_id: R2-GL24h-OPQ-002
scope:
  connection: R2
  material: GL24h
status: OPEN
question: >
  Wie groß ist der versteifende Beitrag der 9 ASSY-Verstärkungsschrauben
  zur Querdrucksteifigkeit, und ab welcher Laststufe darf er angesetzt
  werden (sofortige Mittragswirkung ab Last null, oder erst nach
  Kontaktaktivierung)?
context: >
  Das erste Zugseiten-Steifigkeitsmodell (R2-GL24h-CALC-001–004)
  berücksichtigte nur die unverstärkte Holz-Querdrucksteifigkeit
  `c_c,90,plate`; die axiale Schraubensteifigkeit war als paralleler
  Beitrag zunächst nicht eingerechnet (siehe R2-COMMON-ASS-005).

  **Update (2026-09-22, Nutzerhinweis — Status/Text war veraltet):**
  Die ASSY- Schraubensteifigkeit ist inzwischen über das Bejtka-Modell
  (R2-COMMON-CALC-001) eingerechnet und produktiv in `c_T` übernommen
  (R2-GL24h-CALC-021, `c_c,90` ASSY-verstärkt statt unverstärkt). Offen
  bleibt diese Frage trotzdem — aus zwei anderen, weiterhin gültigen
  Gründen: (1) die Frage nach der Laststufe (sofortige Mittragswirkung
  ab Last null vs. erst nach Kontaktaktivierung) ist nicht Teil der
  Bejtka-Herleitung und bleibt unbeantwortet; (2) die generelle
  Bejtka-Übernahme in `c_T`/`c_C` ist laut R2-COMMON-CALC-001 fachlich
  noch nicht mit der Betreuerin abgestimmt.
related_sources:
options_considered: >
  Axiale Schraubensteifigkeit als parallele Feder ergänzen, mit
  Annahme zur Kontaktaktivierung.
date_opened: "2026-09-01"
date_resolved:
resolution:
---

Übernommen aus chat-3, OPEN_QUESTIONS.md Punkt 5 und TASKS.md "P2 —
Evaluate ASSY reinforcement effect on stiffness".
