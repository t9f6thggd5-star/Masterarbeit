---
decision_id: R3-GL24h-DEC-005
scope:
  connection: R3
  material: GL24h
type: DECISION
question: >
  Darf die volle Laschenlänge (800 mm) als wirksame Verformungslänge der
  Holzseitenlasche angesetzt werden, obwohl die ASSY-Schrauben die Lasche
  über ihre Länge verteilt abstützen?
decision: >
  Nein — die volle 800-mm-Verformungslänge ist für eine über die Länge
  verteilte ASSY-Abstützung zu weich angesetzt; die ASSY-Schrauben
  verändern die wirksame Steifigkeit der Holzlasche.
reason: >
  Die ASSY-Schrauben stützen die Seitenlasche über ihre gesamte Länge
  verteilt ab, wodurch die tatsächliche wirksame Verformungslänge kürzer
  ist als die volle Laschenlänge.
alternatives_considered: >
  Volles EA/800-Modell ohne Berücksichtigung der ASSY-Abstützung (verworfen
  als zu weich/unrealistisch).
date: "UNKNOWN (chat-1, Steifigkeits-Verfeinerung; kein genaues Datum überliefert)"
---

Übernommen aus chat-1, DECISIONS.md Punkt 6, dort als `[Fact]`/„Active"
markiert. Motiviert die vereinfachte Modellierung in
R3-GL24h-ASS-002 (Annahme gleicher Kraftanteile je Schraubenreihe,
Ergebnis `L_eff = 450 mm`).
