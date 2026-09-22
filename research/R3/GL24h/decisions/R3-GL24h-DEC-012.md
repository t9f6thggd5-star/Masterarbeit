---
decision_id: R3-GL24h-DEC-012
scope:
  connection: R3
  material: GL24h
type: DECISION
question: >
  Sind die Wegaufnehmer-Paare "LINKS" (VL+HL) und "RECHTS" (VR+HR) bei den
  R3-Push-Out-Komponentenversuchen (Serien SC-11-B/-C, SC-44-B/-C, SD-36,
  WD-36) zwei unabhängige Verbindungen (wie R2-BR-22 oben/unten) oder zwei
  Messstellenpaare derselben einen Verbindung am Prüfkörper?
decision: >
  Zwei unabhängige Verbindungen. Für jede betroffene R3-Push-Out-Serie
  werden LINKS- und RECHTS-Einzelwerte künftig zu einem gemeinsamen
  Stichprobenmittel gepoolt (n=6, bzw. n=4 wenn ein Prüfkörper wegen
  Nichtverwertbarkeit ausgeschlossen ist), analog zur bereits etablierten
  Poolung von "oben"/"unten" bei R2-BR-22 (R2-GL24h-II-T-S-BR-22-RES-003).
reason: >
  Nutzerangabe im Chat, 2026-09-22, direkte Bestätigung auf Rückfrage
  ("Zwei unabhängige Verbindungen").
alternatives_considered: >
  LINKS/RECHTS als zwei Messstellenpaare derselben einen Verbindung
  behandeln (n=3, LINKS als Primärwert) — bisherige Praxis in den
  betroffenen RES-002-Einträgen, jetzt korrigiert.
date: "2026-09-22"
---

## Anlass

Der in den betroffenen RES-002-Einträgen dokumentierte Beschreibungstext
("zwei getrennte Messstellenpaare am selben Prüfkörper ... nicht zwei
unterschiedliche Prüfkörper") steht im Widerspruch zu dieser Entscheidung
— er wurde vermutlich unbesehen von der ursprünglichen (später korrigierten)
BR-11/BR-22-Formulierung übernommen, ohne für die Push-Out-Serien eigens
geprüft zu werden. Diese Entscheidung korrigiert das für die betroffenen
R3/GL24h-Serien; die RES-002-Einträge selbst bleiben als Rohdaten-
Dokumentation unverändert stehen (CLAUDE.md Abschnitt 13 — kein
Überschreiben), erhalten aber je einen Verweis-Zusatz auf die neuen,
gepoolten RES-003-Einträge.

## Betroffene Einträge

Neue, gepoolte RES-003-Einträge angelegt für: R3-GL24h-III-PO-S-SC-11-B,
R3-GL24h-III-PO-S-SC-11-C, R3-GL24h-III-PO-S-SC-44-C,
R3-GL24h-III-PO-S-SD-36 (n=4, Prüfkörper 1 weiterhin ausgeschlossen, siehe
R3-GL24h-III-PO-S-SD-36-RES-001/002), R3-GL24h-III-PO-S-WD-36.
R3-GL24h-III-PO-S-SC-44-B bleibt unberührt (nur 1 von 3 Prüfkörpern
verwertbar, R3-GL24h-OPQ-021 — keine sinnvolle Poolung möglich).

## Geltungsbereich

Diese Entscheidung gilt zunächst nur für R3/GL24h. Ob dieselbe
Poolungs-Korrektur auch für R1 und R2 (z. B. R2-GL24h-II-PO-S-SD-34/
WD-34, dieselbe LINKS/RECHTS-Konvention) rückwirkend angewendet werden
soll, ist eine gesonderte, vom Nutzer ausdrücklich noch nicht getroffene
Entscheidung (Rückfrage 2026-09-22: "nur R3 jetzt") — R1/R2 bleiben bis zu
einer eigenen Prüfung unverändert (CLAUDE.md Abschnitt 3/4 — keine
Übertragung ohne Beleg).
