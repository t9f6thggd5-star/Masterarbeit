---
assumption_id: R2-COMMON-ASS-003
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Als globales Schubfeld für die Zugseiten-Steifigkeit wird die gesamte
  800×800 mm-Eckzone angesetzt; zwei beidseitig vollflächig verklebte
  Furniersperrholzplatten (BFU-BU F50/25, 12 mm, je Seite) wirken parallel
  zum Holzschubfeld mit einem angenommenen Schubmodul
  `G_r,mean = 500 N/mm²`.
reason: >
  Praktikable Phase-2-Näherung für das Schubfeld; `G_r,mean = 500 N/mm²`
  wurde als expliziter Annahmewert gewählt, nachdem ein früherer,
  unbelegter Wert von 700 N/mm² aus EN 12369-2 verworfen wurde.
basis: chat-3 / DECISIONS.md "Seq 118-132" und "Seq 125-138"
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Übernommen aus chat-3. `G_r,mean = 500 N/mm²` ist laut chat-3
(REQUIREMENTS.md, "Rejected or superseded approaches") ausdrücklich
**nicht** als direkt aus EN 12369-2 abgelesener Wert zu verstehen, sondern
als eigene Annahme des Nutzers — siehe auch die bereits registrierte
Quelle `DIN-EN-12369-2-2011` (siehe COMMON-COMMON-OPQ zur
Ausgabenversion) und den Hinweis, dass die dort dokumentierten
BFU-BU-F50/25-Kennwerte nicht direkt für `G_r` in Scheibenbeanspruchung
übernommen wurden.

Materialunabhängig geführt (R2/COMMON), da Schubfeld-Geometrie und
Sperrholz-Verstärkung unabhängig vom Hauptholzwerkstoff (GL24h/GL75)
sind; im R2-Excel bisher nur für GL24h tatsächlich gerechnet (Sheet
"Rahmenecke GL24h SD", Zellen C150-C166 — siehe R2-GL24h-CALC-003).
