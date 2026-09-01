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
  berücksichtigt nur die unverstärkte Holz-Querdrucksteifigkeit
  `c_c,90,plate`; die axiale Schraubensteifigkeit ist als paralleler
  Beitrag noch nicht eingerechnet (siehe R2-COMMON-ASS-005). Die
  tatsächliche Querdrucksteifigkeit könnte dadurch höher liegen als
  aktuell berechnet.
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
