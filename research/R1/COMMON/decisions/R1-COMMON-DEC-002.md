---
decision_id: R1-COMMON-DEC-002
scope:
  connection: R1
  material: COMMON
type: DECISION
question: >
  Können die Hauptrahmenstäbe in RFEM als "Rigid Member / Starrstab"
  modelliert werden, wenn klassische Stabschnittgrößen benötigt werden?
decision: >
  Nein. Der Rigid-Member-Typ lieferte nicht die gewünschte klassische
  Stabschnittgrößen-Darstellung. Stattdessen werden reguläre Stabelemente
  verwendet; Steifigkeit/Starrheit wird über einen gemeinsamen Knoten ohne
  Endgelenke bzw. über Rigid-Offset-/Rigid-Link-Konzepte abgebildet.
reason: >
  Der Rigid-Member-Typ in RFEM gab die gewünschte Stabergebnis-Darstellung
  nicht her.
alternatives_considered: >
  Ein regulärer Stab mit sehr hoher Steifigkeit zur Annäherung an
  Starrheit (als Vorschlag notiert) — beeinflusst in einem statisch
  unbestimmten System jedoch ggf. die Kraftverteilung und wurde deshalb
  nicht als Standardlösung festgelegt.
date: "UNKNOWN (chat-2, seq 021-030; kein genaues Datum überliefert)"
---

Übernommen aus chat-2, DECISIONS.md D07. Als reine
Modellierungs-/Softwarenotiz materialunabhängig für R1 geführt
(Nutzerentscheidung vom 2026-09-01) — die Beobachtung betrifft die
RFEM-Handhabung des Rahmenmodells, nicht eine materialabhängige
Kenngröße.
