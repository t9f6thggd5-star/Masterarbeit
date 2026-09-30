---
decision_id: R3-COMMON-DEC-013
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Mit welchem Hebelarm z werden Momententragfähigkeit M_R und
  Anfangsrotationssteifigkeit S_j,ini gerechnet?
decision: >
  Mit dem Hebelarm aus der Nulllinie, z = d − x/3 (R3-COMMON-DEC-009), für M_R
  und S_j,ini. z hängt von den Steifigkeiten ab und wird angepasst, sobald
  sich Werte ändern.
reason: >
  Nutzerentscheidung (Chat, 2026-09-30).
alternatives_considered: >
  z = 586,7 mm aus fester Druckzone 400 mm (R3-COMMON-DEC-004).
date: "2026-09-30"
superseded_by:
---

Ersetzt R3-COMMON-DEC-004. Beantwortet den offenen Punkt "z für M_R" aus
R3-COMMON-DEC-009.

Aktueller Wert GL24h (Variante ohne Druckkontakt, R3-GL24h-CALC-019):
x = 252,8 mm, z = 635,7 mm, M_R = 2 · 203 · 0,6357 = 258,11 kNm (vorher
238,19 kNm), Φ = 29,07 mrad, u_M = 88,1 mm, F = 85,20 kN (a = 3,0293 m).

**Excel (noch umzustellen):** Sheet "Rahmenecke GL24h SD" C80 = I96/3 (I96 =
400 mm) → C80 = I179/3; damit C82 = 720 − x/3 = I183. I96 bleibt, weil I98
(Querdruckfläche 160 × 400 mm für die Tragfähigkeit I101) ebenfalls darauf
verweist; ob diese Druckflächennachweise ebenfalls x verwenden sollen, ist
nicht entschieden. Analog GL75 ("Rahmenecke GL75 SD" C85 = H106/3), sobald
dort eine Nulllinie gerechnet ist.

Hinweis (Claude): Die Nulllinie stammt aus dem elastischen Zustand; unter
Bruchlast kann sich die Druckzone durch Plastifizieren vergrößern und z
verkleinern. Für die Ausarbeitung erwähnen.
