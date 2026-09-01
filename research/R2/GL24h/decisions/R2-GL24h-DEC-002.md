---
decision_id: R2-GL24h-DEC-002
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Welche Federmodell-Topologie wird für die Rahmenecke mit eingeklebten
  Gewindestangen verwendet?
decision: >
  Zwei Zugpfade (je 2 Gewindestangen), eine gemeinsame Schubfeder `c_v`
  für das gesamte Holz-/Sperrholz-Schubfeld, je Stange eine Serienkette
  aus Stangendehnung `c_t`, Verbundsteifigkeit `c_ax,f,par`,
  Querdrucksteifigkeit unter der Ankerplatte `c_c,90,rod` und
  Plattensteifigkeit `c_t,ep`; auf der Druckseite separat `c_c,90` und
  `c_c,0`.
reason: >
  Bildet den tatsächlichen Lastpfad besser ab als frühere vereinfachte
  Vorschläge.
alternatives_considered: >
  Frühere, stärker vereinfachte Federvorschläge (Details nicht mehr
  im Ursprungsmaterial nachvollziehbar).
date: "UNKNOWN (chat-3, seq 040-055; kein genaues Datum überliefert)"
---

Übernommen aus chat-3, DECISIONS.md "Seq 040-055 — Correct spring model".
Umgesetzt in R2-GL24h-CALC-002 (Zugseite) und R2-COMMON-OPQ-001/006
(Druckseite, noch offen).
