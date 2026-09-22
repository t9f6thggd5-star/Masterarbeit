---
assumption_id: R1-COMMON-ASS-001
scope:
  connection: R1
  material: COMMON
type: ASSUMPTION
statement: >
  Alle vier Dübelgruppen des R1-Federmodells (Träger und Stütze, jeweils Zug-
  und Druckzone) haben dieselbe Geometrie: 4 Reihen zu je 8 Dübeln Ø12
  (n_90 = 4, n_0 = 8), a_1 = 80 mm in Faserrichtung, a_2 = 50 mm quer dazu.
  Dübelkoordinaten je Gruppe, Ursprung im Gruppenschwerpunkt: x = ±40, ±120,
  ±200, ±280 mm und y = ±25, ±75 mm. Die Geometrie gilt für GL24h und GL75
  gleichermaßen.
reason: >
  Vorgabe des Nutzers für die Berechnung der Drehfeder C_rot,v,f (Buchholz2025
  Gl. 4), die Geometrie nicht aus dem Plan abzulesen. Die Druckgruppe hat
  nach Aussage des Nutzers dieselbe Geometrie wie die Zuggruppe; die
  Anschlussgeometrie von GL75 ist identisch mit GL24h.
basis: >
  Nutzer, 2026-09-21 (Bestätigung a_1 = 80 mm und a_2 = 50 mm; Druckgruppe
  identisch; GL75 identisch). n_0 = 8, n_90 = 4 und a_1 = 80 mm stehen im
  Blatt "Rahmenecke GL75 SD" (C25, C24, C26); a_2 = 50 mm entspricht der
  getesteten Gruppe (Angabe des Nutzers). Nicht Teil der Annahme: der
  innere Hebelarm z (550 mm, Abstand der resultierenden Zug- und Druckkraft,
  R1-GL24h-OPQ-003) und die Lage der Gruppenschwerpunkte
  zueinander.
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Grundlage der Berechnungen R1-GL24h-CALC-007 und R1-GL75-CALC-004
(Σx² = 1.075.200 mm², Σy² = 100.000 mm², I_p = 1.175.200 mm² je Gruppe).
Die Blätter "Rahmenecke GL24h SD" und "Rahmenecke GL75 SD" führen die
Koordinaten in I20 bis I25 (GL24h).
