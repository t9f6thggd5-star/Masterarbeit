---
open_question_id: R3-COMMON-OPQ-001
scope:
  connection: R3
  material: COMMON
status: OPEN
question: >
  Wie groß ist die Druckzone der R3-Rahmenecke tatsächlich? Nach Ansicht des
  Nutzers ist sie der Bereich auf der Druckseite des Rotationspunkts
  (Nulllinie), also nicht fest 400 mm, sondern aus Gleichgewicht und
  Steifigkeiten zu bestimmen.
context: >
  Aktuell z = 720 − 400/3 = 586,7 mm mit angenommener Druckzonenbreite 400 mm
  (Excel N95, Herkunft nicht dokumentiert; R3-COMMON-DEC-004). Bei elastischer,
  dreieckförmiger Kontaktpressung ergibt sich die Lage der Nulllinie x aus dem
  Gleichgewicht Zugkraft = Druckkraft (analog gerissener Querschnitt im
  Stahlbetonbau): c_T·φ·(d − x) = ½·k·b·φ·x² mit d = Abstand Zugkraft zum
  gedrückten Rand (720 mm), b = Kontaktbreite, k = Kontaktsteifigkeit je
  Fläche (z. B. E_90 bzw. E_0 bezogen auf eine wirksame Tiefe); damit
  z = d − x/3 und S_j,ini = c_T·(d − x)·(d − x/3). x hängt von c_T und k ab
  und ist damit an die noch offene Zug- und Druckseitenkette gekoppelt.
related_sources:
options_considered: >
  (a) Druckzonenbreite 400 mm beibehalten (Arbeitsstand); (b) Nulllinie aus
  Gleichgewicht mit Kontaktsteifigkeit bestimmen (Nutzervorschlag).
date_opened: "2026-09-28"
date_resolved:
resolution:
---
