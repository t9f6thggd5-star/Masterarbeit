---
open_question_id: R2-COMMON-OPQ-006
scope:
  connection: R2
  material: COMMON
status: OPEN
question: >
  Wie werden Zugseiten-Steifigkeit `c_T` und Druckseiten-Steifigkeit
  `c_C` über die richtigen Hebelarme/Federpositionen zu einer
  Rotationssteifigkeit der gesamten Rahmenecke kombiniert?
context: >
  Voraussetzung für die Umrechnung in erwartete
  Last-Verformungs-/Moment-Rotations-Bereiche für die Versuchsplanung
  (TASKS.md "P1 — Define load–deformation ranges for planned tests").
  Blockiert durch die noch offene Druckseiten-Geometrie
  (R2-COMMON-OPQ-001), da `c_C` bisher gar nicht berechnet ist.
related_sources:
options_considered:
date_opened: "2026-09-01"
date_resolved:
resolution:
---

Übernommen aus chat-3, OPEN_QUESTIONS.md Punkt 9 und STATE.md Abschnitt 9
("Immediate next state" / "Next"). Die Zugseiten-Steifigkeit `c_T` selbst
liegt für GL24h bereits vor (R2-GL24h-CALC-004); die Druckseite und damit
das vollständige Rotationsmodell fehlen noch vollständig.
