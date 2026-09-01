---
assumption_id: R2-COMMON-ASS-004
scope:
  connection: R2
  material: COMMON
type: ASSUMPTION
statement: >
  Der Schub-Korrekturbeiwert wird zunächst mit `κ = 1` angesetzt (keine
  zusätzliche Abminderung der Schubfeldsteifigkeit).
reason: >
  Einfachste erste Näherung für die Phase-2-Steifigkeitsabschätzung.
basis: chat-3 / DECISIONS.md "Seq 138-145 — Shear correction factor"
supported_by:
contradicted_by:
certainty: ASSUMED
superseded_by:
---

Übernommen aus chat-3. Alternative `κ = 5/6` oder ein literatur-/FE-
kalibrierter Wert wurde ausdrücklich als spätere Sensitivitätsrechnung
vorgesehen, aber noch nicht durchgeführt — siehe R2-COMMON-OPQ-004 und
TASKS.md "P3 — Shear correction sensitivity".

Materialunabhängig geführt (R2/COMMON); bisher nur für GL24h tatsächlich
verwendet (siehe R2-GL24h-CALC-003).
