---
decision_id: R3-COMMON-DEC-002
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Soll Kriechverlust/Schwindverlust der Vorspannung im initialen
  analytischen Modell abgeschätzt oder experimentell bestimmt werden?
decision: >
  Kriechen, Schwinden und Vorspannungsverlust werden experimentell über
  geplante Kriechversuche bestimmt. Das initiale analytische Modell trifft
  dazu keine Annahmen/Spekulationen.
reason: "Im Ursprungsmaterial (chat-1) nicht dokumentiert."
alternatives_considered:
date: "UNKNOWN (chat-1, Abschnitt Kriechversuch-Diskussion; kein genaues Datum überliefert)"
superseded_by:
---

Nachträglich angelegt am 2026-09-22, um die zuvor dangling Referenz
"R3-COMMON-DEC-002" aus `R3-GL24h/current_state.md` aufzulösen (Audit-
Punkt 5, Nutzerentscheidung: R3-COMMON soll nachträglich angelegt
werden). Inhaltlich identisch übernommen aus `R3-GL24h-DEC-003`
(chat-1, DECISIONS.md Punkt 4, dort als `[Fact]`/„Active" markiert).

**Materialunabhängigkeit:** Die Entscheidung ist methodisch (Kriechen/
Schwinden werden generell experimentell statt rechnerisch erfasst),
nicht die daraus resultierenden Zahlenwerte — diese dürfen je Material
durchaus unterschiedlich ausfallen (GL24h vs. GL75/BauBuche), ohne dass
das die hier getroffene methodische Festlegung selbst berührt. Analog
zu R1-COMMON-DEC-001 (Federmodell-Phasenlogik, ebenfalls eine
materialunabhängige Methodik-Entscheidung) daher materialunabhängig für
R3 geführt, gilt damit auch für GL75.

`R3-GL24h-DEC-003` bleibt als historischer Eintrag erhalten (siehe dort,
`superseded_by: R3-COMMON-DEC-002`), damit keine Referenz auf die alte
ID ins Leere zeigt.
