---
assumption_id: R2-COMMON-ASS-001
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Die S355-Stahl-Ankerplatte (160×240×25 mm) wird für die
  Verformungsberechnung als starr angenommen (`c_t,ep → ∞`, in Excel als
  `1E+99 N/mm` umgesetzt).
reason: >
  Volle Auflagerung, kurze Lastausbreitungswege und hohe Biegesteifigkeit
  der Stahlplatte gegenüber den weicheren Holz-/Verbindungsfedern lassen
  eine eigene endliche Plattenbiegefeder als vernachlässigbar erscheinen.
basis: chat-3 / DECISIONS.md "Seq 070-085 — Rigid end plate"
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Übernommen aus chat-3, DECISIONS.md ("Rationale: full bearing, short
load-spread distances, high bending stiffness relative to softer
timber/connection springs"). Materialunabhängig geführt (R2/COMMON), da
die Stahlplatte und ihre Geometrie unabhängig vom verwendeten
Holzwerkstoff (GL24h/GL75) dieselbe bleibt; im R2-Excel als
`c_t,ep = 1E+99` (Zelle C129, Sheet "Rahmenecke GL24h SD") verifiziert.

Alternative (nicht gewählt): endliche Plattenbiegefeder modellieren —
laut TASKS.md ("P3 — Plate-bending sensitivity") als spätere
Sensitivitätsrechnung vorgesehen, aber noch nicht durchgeführt.
