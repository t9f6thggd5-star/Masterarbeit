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

**Update (2026-09-17):** Mit `c_T` (R2-GL24h-CALC-021) und `c_C`
(R2-GL24h-CALC-020) liegen inzwischen beide Teilsteifigkeiten vor. Für
die Kombination wurde eine erste Kombinationsformel hergeleitet und als
eigene Hypothese dokumentiert: `S_j,ini = z²/(1/c_T+1/c_C)`
(R2-COMMON-HYP-001, `CLAUDE_DRAFT`, `reviewed: false`), angewendet mit
dem bereits im R2-Excel für die Tragfähigkeitskette verwendeten
Hebelarm `z=560mm` — Ergebnis `S_j,ini≈12.540,8 kNm/rad`
(R2-GL24h-CALC-022). Status bleibt bewusst `OPEN`: sowohl die
Kombinationsformel selbst als auch die Wiederverwendung von `z=560mm`
für die Steifigkeits- (statt nur Tragfähigkeits-)Kette sind noch nicht
mit der Betreuerin abgestimmt — siehe R2-COMMON-HYP-001 für die
Herleitung und die offenen Punkte im Detail. Erst nach dieser
fachlichen Absicherung sollte diese Frage als `RESOLVED` markiert
werden.
