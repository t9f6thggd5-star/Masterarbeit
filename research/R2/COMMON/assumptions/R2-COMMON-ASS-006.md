---
assumption_id: R2-COMMON-ASS-006
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Der im R2-Excel für alle drei Blätter ("Rahmenecke GL24h SD" C90/C92,
  "Rahmenecke GL24h HD" I92/I94, "Rahmenecke GL75 SD" I54/I56) identisch
  verwendete innere Hebelarm `z = 560 mm` ergibt sich geometrisch aus der
  Stützenbreite (Rahmeneck-Querschnittshöhe) von 800 mm abzüglich des
  Abstands vom Stützenrand zum jeweiligen Kraftangriffspunkt auf Zug- und
  Druckseite. Die Zug- bzw. Druckresultierende wird dabei als jeweils
  mittig in ihrer Stahlplatte (160×240×25 mm) angreifend angenommen, d. h.
  120 mm (= 240/2) vom Stützenrand entfernt auf jeder Seite:
  `z = 800 - 2·(240/2) = 800 - 240 = 560 mm`.
reason: >
  Erklärt die bisher als "reiner Zahlen-Input ohne Formelherleitung"
  dokumentierte Herkunft von z=560mm (siehe R2-GL24h-CALC-022,
  R2-COMMON-OPQ-008 Punkt 3) durch die Annahme eines mittigen
  Kraftangriffs in der jeweiligen Stahlplatte, symmetrisch für Zug- und
  Druckseite.
basis: Chat mit dem Nutzer (Lukas), 2026-09-18.
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

**Nutzerangabe (Lukas), 2026-09-18:** "die 560 kommen aus 800-2*240/2 das
ist die Stützenbreite - jeweils die Hälfte der Stahlplatten da wir davon
ausgehen, dass die Druck bzw. Zugkomponente immer mittig angreifen."

**Rechnerische Prüfung:** `800 - 2·(240/2) = 800 - 240 = 560 mm` ✓ —
konsistent mit dem Excel-Zahlenwert (R2-GL24h-CALC-022).

Materialunabhängig geführt (R2/COMMON), da dieselbe Stützenbreite
(800 mm) und dieselbe Stahlplattengeometrie (160×240×25 mm) für GL24h und
GL75 gelten (siehe Zwischenstand-Notiz zur R2-Druckseite,
2026-09-17) und `z=560mm` im Excel identisch in allen drei
material-/versuchsspezifischen Blättern auftaucht.

**Verhältnis zu `h_d` (Druckzonenhöhe, R2-COMMON-DEC-002/OPQ-006) —
richtiggestellt, 2026-09-18:** Eine erste Fassung dieses Eintrags stellte
hier fälschlich einen Konflikt mit `h_d` dar, als müsse `h_d = 240 mm`
gelten, damit `z=560mm` mit DEC-002 vereinbar ist. Das ist nicht korrekt:
`h_d` ist eine eigenständige, aus der Pressungsverteilung/dem
Gleichgewicht abzuleitende Größe (unabhängig von der hier getroffenen
Lage-Annahme) und bleibt über R2-COMMON-OPQ-006 weiterhin offen — sie
wird durch diese Annahme weder festgelegt noch vorausgesetzt.

Der Kraftangriffspunkt bei 120 mm (= halbe Plattentiefe) wird hier —
ebenso wie bei `c_c,0` in R2-GL24h-CALC-019 — direkt aus der
Plattengeometrie als pragmatischer Ersatz für `h_d` angesetzt (Option 1
in R2-COMMON-OPQ-011), gerade um die Berechnung nicht von der noch
offenen `h_d`-Bestimmung abhängig zu machen (Option 2 dort, bewusst
nicht gewählt). `z=560mm` und `c_c,0` (`l=240mm`) beruhen damit auf
derselben, bereits in R2-COMMON-OPQ-011 dokumentierten und noch nicht
mit der Betreuerin abgestimmten Modellierungsannahme — kein neuer,
separater Klärungsbedarf, aber ein zusätzlicher Grund, weshalb eine
Änderung dort auch `z` und nicht nur `c_c,0` betreffen würde.
