---
assumption_id: R3-GL24h-ASS-001
scope:
  connection: R3
  material: GL24h
type: ASSUMPTION
statement: >
  Die Kopf-/Endplatten werden für das aktuelle Modell als starr angenommen
  (Steifigkeit → unendlich); die Verformung unter der Kopfplatte wird
  vernachlässigt.
reason: >
  Vereinfachung für das erste Steifigkeits-/Vorspannungsmodell, bis eine
  genauere Behandlung nötig/möglich ist.
basis:
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Übernommen aus chat-1, DECISIONS.md Punkt 3 ("End plates rigid for now"),
dort abweichend von den übrigen Punkten bereits im Ursprungsmaterial als
`[Assumption]` (nicht `[Fact]`) markiert — deshalb hier als eigenständige
Annahme statt als Entscheidung geführt. Siehe auch `STATE.md`: "End-plate
stiffness currently infinite; deformation under head plate neglected."
