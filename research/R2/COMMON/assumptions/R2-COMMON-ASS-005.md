---
assumption_id: R2-COMMON-ASS-005
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Die axiale/versteifende Wirkung der ASSY-Querdruckverstärkungsschrauben
  wird im ersten Phase-2-Steifigkeitsmodell der Zugseite (noch) nicht
  berücksichtigt; nur die unverstärkte Holz-Querdrucksteifigkeit
  `c_c,90,plate` geht in die Steifigkeitskette ein. Auf der
  Festigkeitsseite wird die Verstärkung dagegen bereits berücksichtigt
  (siehe R2-GL24h-CALC-006).
reason: >
  Vereinfachung für die erste lineare Steifigkeitsabschätzung, solange
  unklar ist, ob/wie die Schrauben von Beginn an (ab Laststufe 0)
  mittragen.
basis: chat-3 / STATE.md Abschnitt 4; TASKS.md "P2 — Evaluate ASSY reinforcement effect on stiffness"
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Übernommen aus chat-3, STATE.md ("ASSY cross-grain reinforcement is not
included in the stiffness at this stage; the unreinforced timber
stiffness is used first"). Konsequenz laut chat-3: die tatsächliche
Querdrucksteifigkeit könnte höher liegen als hier abgeschätzt — siehe
R2-COMMON-OPQ-... (offene Frage zur ASSY-Steifigkeitswirkung,
R2-GL24h-OPQ-002, da die ASSY-Verstärkung im R2-Excel bisher nur für
GL24h überhaupt modelliert ist).

Materialunabhängig als Modellierungsprinzip geführt (R2/COMMON); die
konkrete Umsetzung existiert bisher ausschließlich für R2/GL24h, da für
GL75 im R2-Excel gar kein ASSY-Verstärkungsblock vorliegt (siehe
R2-GL75-OPQ-002).
