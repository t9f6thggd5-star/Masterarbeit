---
assumption_id: R2-COMMON-ASS-002
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Alle vier eingeklebten Gewindestangen (M16, 2 je Zugpfad) erhalten im
  vereinfachten linearen Zugseiten-Federmodell eine gleich große Kraft;
  die Querdrucksteifigkeit unter der gemeinsamen Ankerplatte wird dazu zu
  gleichen Teilen auf die vier Stangen aufgeteilt
  (`c_c,90,rod = c_c,90,plate / 4`).
reason: >
  Vereinfachung für die erste lineare Phase-2-Steifigkeitsabschätzung, um
  ohne vollständiges Rotations-/Momentenmodell eine erste Zugseiten-Feder
  aufstellen zu können.
basis: chat-3 / DECISIONS.md "Seq 100-108 — Equal load on four rods"; REQUIREMENTS.md "Accepted modeling assumptions"
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Übernommen aus chat-3, REQUIREMENTS.md ("All four bonded-in threaded rods
receive equal load in the current simplified tension-side model"; "The
cross-grain stiffness beneath the common end plate is split equally over
four rods"). Im Ursprungsmaterial sowohl als `[Decision]`
(DECISIONS.md) als auch als `[Assumption: active]` (REQUIREMENTS.md)
markiert — hier gemäß Charakter (vereinfachende Modellannahme, kein
methodischer Grundsatzbeschluss) als ASSUMPTION geführt, analog zur
Behandlung der vergleichbaren R3-Vereinfachung "F/8 je Schraubenreihe"
(siehe R3-GL24h-ASS-002).

Materialunabhängig geführt (R2/COMMON), da die Geometrie der vier
Gewindestangen und der Ankerplatte unabhängig vom Holzwerkstoff ist;
bisher jedoch nur für GL24h tatsächlich in einer Steifigkeitskette
verwendet (siehe R2-GL24h-CALC-002) — für GL75 liegt noch keine
entsprechende Berechnung vor (siehe R2-GL75-OPQ-001).

**Bekannte Einschränkung** (chat-3, OPEN_QUESTIONS.md Punkt 9): Die
tatsächliche Kraftverteilung unter Rahmeneckenrotation dürfte von der
Gleichverteilung abweichen; das vollständige Moment-Rotations-Modell mit
Hebelarmen steht noch aus.
