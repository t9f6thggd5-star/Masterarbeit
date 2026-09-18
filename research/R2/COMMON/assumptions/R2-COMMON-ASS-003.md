---
assumption_id: R2-COMMON-ASS-003
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Als globales Schubfeld für die Zugseiten-Steifigkeit wird die gesamte
  800×800 mm-Eckzone angesetzt; zwei vollflächig verklebte
  Furniersperrholzplatten (BFU-BU F50/25, 12 mm) sitzen auf der linken
  und rechten Seitenfläche des Trägers, symmetrisch flankierend um die
  eingeklebten Gewindestangen (nicht auf Vorder-/Rückseite des
  Trägerquerschnitts, siehe Skizze vom Nutzer, 2026-09-18). Sie wirken
  parallel zum Holzschubfeld mit einem angenommenen Schubmodul
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

**Klarstellung (2026-09-18, in zwei Schritten):** Die ursprüngliche
Formulierung ("beidseitig ... je Seite") war missverständlich. Erster
Korrekturversuch (Chat) — "beide Platten auf derselben Trägerseite,
links/rechts auf dem Schubfeld angeordnet" — war noch falsch. Per vom
Nutzer bereitgestellter Skizze (Ansicht auf den Trägerquerschnitt,
Plattenbreite oben mit "160" bemaßt, passend zur Stahlplattenbreite)
jetzt korrekt geklärt: die zwei Platten sitzen auf der LINKEN und
RECHTEN Seitenfläche des Trägers (den schmalen Querschnittsseiten,
symmetrisch flankierend um die eingeklebten Gewindestangen) — nicht auf
Vorder-/Rückseite, und nicht beide auf derselben Fläche. Keine
Auswirkung auf die Rechnung selbst (`c_v,P` je Platte bleibt eine
unabhängige Einzelfeder, Parallelschaltung `c_v,ges = c_v,H + Σc_v,P`
unverändert gültig) — reine Präzisierung der Geometriebeschreibung.
Gilt jetzt auch für GL75, mit `9mm` statt `12mm` Plattendicke (siehe
R2-GL75-CALC-009/010) — seit 2026-09-18 auch für GL75 als eigener Block
im R2-Excel nachgebildet (Sheet "Rahmenecke GL75 SD", Zellen K71:M80).

**Neue Quellenangabe für `G_r,mean=500 N/mm²` (2026-09-18):** Im
R2-Excel findet sich bei der GL75-Umsetzung dieser Annahme (Zelle N77,
Sheet "Rahmenecke GL75 SD") erstmals eine konkrete technische Notiz:
"Annahme Schubmodul 500 N/mm^2 KLH ETA Scheibenbeanspruchung" — d. h.
der Wert wurde vom Nutzer in Anlehnung an eine ETA für KLH-
Brettsperrholz (Scheibenbeanspruchung) gewählt, nicht willkürlich.
Ergänzt (aber ersetzt nicht) die bisherige Herkunftsangabe aus chat-3
oben; welche konkrete KLH-ETA (Produkt/Ausgabejahr) gemeint ist, ist
damit noch nicht abschließend dokumentiert — bei Bedarf beim Nutzer
nachfragen, bevor dies als vollwertige Normquelle zitiert wird.
