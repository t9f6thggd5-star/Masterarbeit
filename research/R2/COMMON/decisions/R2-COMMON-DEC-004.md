---
decision_id: R2-COMMON-DEC-004
scope:
  connection: R2
  material: COMMON
type: DECISION
question: >
  Wirkt die Schubfeld-Komponente `c_v` (R2-GL24h-CALC-003,
  R2-COMMON-ASS-003) nur am Zugpfad des Federmodells, oder auch am
  Druckpfad? Wie ist der Druckpfad (c_C) grundsätzlich verschaltet?
decision: >
  `c_v` wirkt AUSSCHLIESSLICH im Zugpfad, in Serie mit den beiden
  parallelen Stangenzweigen (Rod 1 / Rod 2). Der Druckpfad besteht nur
  aus zwei Holzfedern in Serie: `1/c_C = 1/c_c,90 + 1/c_c,0`. Kein
  Stahl-/Stangenanteil und kein `c_v`-Anteil auf der Druckseite.
reason: >
  Bestätigt durch ein vom Nutzer geteiltes Federmodell-Diagramm (Fig. 7
  aus FragiacomoBatchelar2012a, "Proposed modeling of extended column/
  beam semirigid moment connections with the component method"), das
  die vollständige Sechs-Komponenten-Topologie zeigt — siehe
  R2-COMMON-CLAIM-031 für die Herkunft und Zitatgenauigkeit. Die
  Topologie (WAS in Serie/parallel steht) wird als strukturelles
  Vorbild übernommen; die konkreten Steifigkeitswerte der Quelle NICHT
  (abweichende Geometrie/Material, siehe CLAIM-002/003/031).
alternatives_considered: >
  Vor dieser Entscheidung standen zwei Lesarten offen (siehe Diskussion
  im Chat vom 2026-09-17): (1) c_v nur Zugpfad, da nur die
  Gewindestangen ihre Kraft per Schub "umlenken" müssen — jetzt
  bestätigt; (2) c_v als gemeinsames Element für die gesamte Eckzone,
  das beide Pfade teilen (Doppelzählungs-Risiko, falls in c_T UND c_C
  einzeln angesetzt) — durch das Diagramm widerlegt, da c_v dort
  eindeutig nur im Zugpfad-Zweig liegt.
date: "2026-09-17"
---

Löst den in der Antwort vom 2026-09-17 aufgeworfenen offenen Punkt zur
Verschaltung von `c_v`. Ermöglicht jetzt die Berechnung von `c_C`
(Druckseiten-Gesamtsteifigkeit) als einfache Serienschaltung der
bereits vorliegenden `c_c,90`- und `c_c,0`-Werte, siehe
R2-GL24h-CALC-020.

Materialunabhängig geführt (R2/COMMON), da die Topologie des
Federmodells primär von der Rahmeneck-Konstruktion (Stangenanordnung,
Kontaktgeometrie), nicht vom Holzwerkstoff abhängt — analog zu
R2-COMMON-DEC-002/003.

**Was diese Entscheidung NICHT klärt:** Wie `c_T` (Zugseite) und `c_C`
(Druckseite) über den Hebelarm `z` zur Rotationssteifigkeit der
gesamten Rahmenecke kombiniert werden (Bild zeigt `T`/`C`/`z`/`φ` als
nächsten Schritt) — das bleibt Teil von R2-COMMON-OPQ-006.
