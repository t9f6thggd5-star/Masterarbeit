---
open_question_id: R2-GL24h-OPQ-004
scope:
  connection: R2
  material: GL24h
status: OPEN
question: >
  Die Excel-Formel für die "maßgebende Zug/Druckkomponente" (Zelle H111,
  Sheet "Rahmenecke GL24h SD", Basis von M_max) lautet `=MIN(L16;H87)` —
  sie vergleicht das Gewindestangen-Zugversuchsmittel (`L16=285,77 kN`)
  nur mit der verstärkten Querdrucktragfähigkeit der **Druckseite**
  (`H87=384,124 kN`, R2-GL24h-CALC-011). Der neu berechnete, niedrigere
  Zugseiten-Wert (`L87=356,273 kN`, R2-GL24h-CALC-017) ist in dieser
  MIN-Formel nicht als dritter Kandidat enthalten. Sollte die Formel um
  `L87` ergänzt werden, damit auch ein rechnerisches Versagen auf der
  Zugseite (verstärkter Querdruck) als möglicher maßgebender Mechanismus
  erfasst wird?
context: >
  Aktuell ändert das Fehlen von `L87` in der MIN-Formel nichts am
  Ergebnis: `MIN(285,77; 384,124)=285,77=MIN(285,77; 384,124; 356,273)`,
  da `356,273 kN` ohnehin über dem Gewindestangen-Zugversuchsmittel
  liegt. Die Lücke ist also aktuell numerisch folgenlos, aber
  strukturell: bei zukünftigen Änderungen (z. B. anderer
  Gewindestangen-Versuchswert, andere Schraubengeometrie) könnte sich das
  ändern, ohne dass die Formel den dann ggf. maßgebenden Zugseiten-
  Querdruckwert erfassen würde.
related_sources:
options_considered: >
  (a) Formel unverändert lassen, da aktuell ohne numerische Auswirkung;
  (b) Formel um `L87` zu `=MIN(L16;H87;L87)` ergänzen, für Robustheit
  gegenüber künftigen Eingabeänderungen.
date_opened: "2026-09-17"
date_resolved:
resolution:
---

Eigener Fund (Claude) beim Verifizieren der neu getrennten Zug-/
Druckseiten-Werte (R2-GL24h-CALC-017/018) gegen die tatsächliche
Excel-Formel für `M_max`. Blockiert keinen der dokumentierten Werte, da
rein numerisch folgenlos (siehe `context`) — wird hier nur als
Konsistenz-Hinweis für eine mögliche spätere Formel-Ergänzung
festgehalten.
