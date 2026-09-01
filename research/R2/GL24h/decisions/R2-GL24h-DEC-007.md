---
decision_id: R2-GL24h-DEC-007
scope:
  connection: R2
  material: GL24h
type: DECISION
question: >
  Mit welcher Einklebelänge wird der ETA/Würth-Vergleichs-
  (Sensitivitäts-)Nachweis für die Querdruckverstärkung geführt?
decision: >
  Für den ETA/Würth-Vergleich wird `l_ef = 580 mm` verwendet (statt eines
  früheren Zwischenwerts von 545 mm), konsistent zur FprEN-Geometrie
  (R2-GL24h-DEC-005).
reason: >
  Konsistenz zwischen den beiden verglichenen Modellen (FprEN vs.
  ETA/Würth-Ansatz).
alternatives_considered: l_ef = 545 mm (verworfen, aus einer alten Berechnung).
date: "UNKNOWN (chat-3, seq 192-197; kein genaues Datum überliefert)"
---

Übernommen aus chat-3, DECISIONS.md "Seq 192-197 — ETA/Würth comparison".
Laut chat-3 ergibt sich damit: ETA-Ausziehwiderstand (`ρ_mean=420 kg/m³`)
`F_ax ≈ 64,42 kN`, weiterhin Knicken `F_c=11,73 kN` maßgebend,
ETA/Würth-verstärkter Widerstand `≈356,27 kN` (`k_c,90=1,75`,
1. Modus), 2. Modus `≈413,79 kN`.

**Verifikationshinweis:** Diese Vergleichsrechnung (mit dem alten
`k_c,90=1,75`) ist im aktuell abgelegten R2-Excel nicht als eigenes
Berechnungsblatt auffindbar — die genannten Zahlenwerte stammen
ausschließlich aus chat-3 und sind bisher nicht unabhängig gegen eine
Excel-Quelle verifiziert (siehe R2-COMMON-OPQ-002).
