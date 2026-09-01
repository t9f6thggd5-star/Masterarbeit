---
open_question_id: R2-GL24h-OPQ-003
scope:
  connection: R2
  material: GL24h
status: RESOLVED
question: >
  Ist die Kontaktfläche der Ankerplatte für den Verstärkungsnachweis
  (Gl. 8.12) als Endauflager (FprEN 1995-1-1:2024, Gl. 8.13, mit
  `l_e`-Begrenzungsterm) oder als Zwischenauflager (Gl. 8.14, ohne
  `l_e`-Term) zu behandeln — und ist `l_1,ef=300 mm` (aktueller
  Excel-Wert) damit korrekt, oder müsste mit einem `l_e`-Term
  (randnahe Kontaktfläche) ein kleinerer Wert (z. B. `270 mm`, wie im
  vorherigen Zwischenstand) angesetzt werden?
context: >
  Die Zelle `H91` ("l_1,ef") in der R2-Excel ist mit "Gl. 8.13" (Spalte
  I) beschriftet, ihre tatsächliche Formel (`=H58+(MIN(30,H90/2)+
  MIN(30,H90/2))`) enthält aber keinen `l_e`-Term und entspricht damit
  strukturell eher Gl. 8.14 (Zwischenauflager). In einer früheren
  Version des Arbeitsblatts existierte eine eigene `l_e`-Zeile
  (`l_e=0 mm`), die beim Einfügen der neuen `k_mat Holz`-Zeile
  (Korrektur zu R2-GL24h-CALC-011) offenbar entfallen ist. Mit `l_e=0`
  (randnahe Kontaktfläche, wie zuvor hinterlegt) ergäbe Gl. 8.13
  `l_1,ef = 240+0+30 = 270 mm` statt der aktuellen `300 mm`. Der genaue
  Wert wirkt sich unmittelbar auf den Holzanteil-Term in Gl. 8.12 (und
  damit auf `F_c,90`, R2-GL24h-CALC-011) aus.
related_sources: FprEN-1995-1-1-2024
options_considered: >
  (a) Kontaktfläche ist randnah (Endauflager) — `l_e`-Zeile wieder
  einführen und Gl. 8.13 korrekt mit `l_e` rechnen, `l_1,ef` sinkt
  vermutlich auf `≈270 mm`; (b) Kontaktfläche ist bewusst als
  Zwischenauflager zu behandeln — `l_1,ef=300 mm` bleibt korrekt, nur
  die Normverweis-Beschriftung in Spalte I ist von "Gl. 8.13" auf
  "Gl. 8.14" zu korrigieren.
date_opened: "2026-09-01"
date_resolved: "2026-09-01"
resolution: >
  Option (b): Nutzerentscheidung, die Kontaktfläche der Ankerplatte
  bewusst als Zwischenauflager zu behandeln. Die Normverweis-Beschriftung
  in Zelle `I91` wurde entsprechend vom Nutzer von "Gl. 8.13" auf
  "Gl. 8.14" korrigiert; die Formel in `H91` (`=H58+(MIN(30,H90/2)+
  MIN(30,H90/2))`, kein `l_e`-Term) entsprach dieser Auslegung ohnehin
  bereits. `l_1,ef=300 mm` war damit korrekt und bleibt unverändert —
  keine Auswirkung auf den in R2-GL24h-CALC-011 dokumentierten Wert
  `F_c,90=384,124 kN`.
---

Eigener Fund (Claude) beim Verifizieren von R2-GL24h-CALC-011 gegen die
Excel-Formeln (nicht nur die Werte). Blockierte keine der beiden bereits
dokumentierten Korrekturen (R2-GL24h-CALC-010/011), da deren Werte in
sich konsistent waren — betraf nur die korrekte Normbeschriftung/
-begründung von `l_1,ef`, nicht dessen Wert.
