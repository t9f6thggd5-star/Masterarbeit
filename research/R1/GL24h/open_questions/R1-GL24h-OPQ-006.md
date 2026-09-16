---
open_question_id: R1-GL24h-OPQ-006
scope:
  connection: R1
  material: GL24h
status: RESOLVED
question: >
  Gilt der Faktor "2" für die zweischnittige Johansen-Tragfähigkeit exakt
  so, wie er sich aus den Excel-Zellwerten rekonstruieren lässt
  (R1-GL24h-CALC-003), oder ist eine andere normative Kombination korrekt?
context: >
  Übernommen aus chat-2, OPEN_QUESTIONS.md Q6 und DECISIONS.md D04
  (R1-GL24h-DEC-004). Die aus den Zellwerten rekonstruierte Rechnung
  (F_D,k × n_ef × n_90 × m) liefert einen plausiblen Wert (≈494.77 kN
  bzw. ≈627 kN), ist aber keine bestätigte Formel-Einsicht — in der
  Excel-Datei ist keine Formel, nur der Ergebniswert sichtbar.
related_sources:
options_considered:
date_opened: "2026-09-01"
date_resolved: "2026-09-03"
resolution: >
  Vom Nutzer bestätigt (2026-09-03): Der R1-Anschluss hat ein mittig im
  Holzquerschnitt eingeschlitztes Stahlblech (Schlitzblech), wodurch jeder
  Stabdübel zweischnittig beansprucht wird — zwei Scherfugen je
  Verbindungsmittel (m=2), symmetrisch je eine auf jeder Seite des
  Blechs. Der Faktor "m=2" in der rekonstruierten Formel
  (F_D,k × n_ef × n_90 × m) entspricht damit genau dieser Anzahl
  Scherfugen bei mittigem, symmetrischem Schlitzblech-Anschluss (nicht
  einer pauschalen Sicherheitszahl) — keine andere normative Kombination
  erforderlich.
---

Übernommen aus chat-2, OPEN_QUESTIONS.md Q6 und DECISIONS.md D04
(R1-GL24h-DEC-004).

**Update (2026-09-03):** Vom Nutzer im Gespräch bestätigt — siehe
`resolution`-Feld oben. Der Faktor m=2 zählt die Scherfugen der
zweischnittigen Verbindung bei mittig eingeschlitztem Stahlblech im Holz
(Holz–Stahl–Holz-Anordnung), nicht eine pauschale Sicherheitszahl.
