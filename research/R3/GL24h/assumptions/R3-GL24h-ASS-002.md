---
assumption_id: R3-GL24h-ASS-002
scope:
  connection: R3
  material: GL24h
type: ASSUMPTION
statement: >
  Jede der 8 ASSY-Schraubenreihen (in Lastrichtung) überträgt einen
  gleichen Kraftanteil F/8 der Holzlaschen-Zugkraft F ("Equal-row-load"-
  Vereinfachung).
reason: >
  Erste Näherung, um die durch die verteilte ASSY-Abstützung reduzierte
  wirksame Verformungslänge der Holzlasche greifbar zu machen (siehe
  R3-GL24h-DEC-005), ohne ein vollständiges diskretes Feder-Modell pro
  Schraube aufzustellen.
basis: R3-GL24h-DEC-005
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Übernommen aus chat-1, DECISIONS.md Punkt 7 ("Equal row load
simplification"), dort bereits im Ursprungsmaterial als `[Assumption]`
markiert. Ergebnis der Vereinfachung (siehe `R3-GL24h-CALC-001` für die
zugehörige Berechnung): mit Geometrie 170 mm bis Reihe 1, danach 7×80 mm,
danach 70 mm ergibt sich eine wirksame Länge `L_eff = 450 mm` und daraus
`c_H,eff = 299,0 kN/mm` (gegenüber `c_H,800 = 168,19 kN/mm` bei voller
Laschenlänge ohne ASSY-Abstützung).

`OPEN_QUESTIONS.md` Punkt 6 hält ausdrücklich fest, dass die Genauigkeit
dieser Annahme (gleicher Kraftanteil F/8 je Reihe) noch nicht abschließend
geklärt ist — siehe den zugehörigen offenen-Frage-Eintrag.

**Hinweis zur Materialabhängigkeit (2026-09-01):** In der zugrundeliegenden
Exceltabelle (`R3-GL24h-CALC-001` bzw. deren `source_file`) ergibt sich
`L_eff = 450 mm` für dieses konkrete Geometrie-Layout sowohl bei GL24h als
auch bei GL75 identisch. Das ist jedoch **kein** Beleg dafür, dass diese
Annahme generell materialunabhängig (COMMON) wäre: Anzahl der
Verbindungsmittel, Laschengrößen und Anzahl der Querkraftdorne variieren
zwischen den Materialvarianten der Rahmenecke teilweise, sodass Geometrie
und damit `L_eff` bei anderen Konfigurationen durchaus abweichen können.
Diese Annahme bleibt deshalb bewusst bei R3/GL24h geführt, nicht bei
COMMON/COMMON — siehe CLAUDE.md Abschnitt 4 (Scope Isolation: GL24h ≠
GL75 nie pauschal annehmen).
