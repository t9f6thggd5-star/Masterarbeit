---
decision_id: R1-COMMON-DEC-003
scope:
  connection: R1
  material: COMMON
type: DECISION
question: >
  Wird das innenliegende Schlitzblech im Federmodell von R1 als eigene
  Feder berücksichtigt oder als starr angesetzt?
decision: >
  Das Schlitzblech wird als starr angesetzt. Es erhält keine eigene Feder
  im Zug- oder Druckpfad; die Stahlkomponente plate in compression (c,p)
  geht mit unendlicher Steifigkeit ein.
reason: >
  Entscheidung des Nutzers (2026-09-26). Deckt sich mit Buchholz2025,
  Abschn. 4.2: die Komponente c,p wird dort nicht berücksichtigt, weil ihre
  Steifigkeit als unendlich anzunehmen ist (Verweis auf EN 1993-1-8).
alternatives_considered: >
  Eigene Feder für die Blechverformung (Längsdehnung/Schub des Blechs),
  siehe R1-GL24h-OPQ-009 — nicht gewählt.
date: "2026-09-26"
---

Gilt für GL24h und GL75, da das Schlitzblech materialunabhängig ist.
Löst R1-GL24h-OPQ-009. Bei GL75 ist in den Zugversuchen der
Nettoquerschnitt des Schlitzblechs versagt (R1-GL75-CALC-003); das betrifft
die Tragfähigkeit, nicht die Annahme der Blechsteifigkeit.
