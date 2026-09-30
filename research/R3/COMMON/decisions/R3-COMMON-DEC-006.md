---
decision_id: R3-COMMON-DEC-006
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Mit welcher Formel wird die Dehnsteifigkeit der Gewindestange c_t bei R3
  angesetzt?
decision: >
  c_t = E_s·A_s/L_b für eine Gewindestange je Lasche, ohne den Faktor 1,6.
  GL24h (M20): 210000·245/1660 = 30,99 kN/mm; GL75 (M24): 210000·353/1660
  = 44,66 kN/mm.
reason: >
  k_t = 1,6·A_s/L_b nach DIN EN 1993-1-8:2025-04, A.13.2, Gl. (A.40) gilt
  "für eine einzelne Schraubenreihe"; im T-Stummel-Modell sind das zwei
  Schrauben je Reihe (vgl. Symbolliste der Norm, "mit 2 Schrauben je Reihe"),
  der Faktor 1,6 entspricht 2 × 0,8 (Abminderung aus Abstützkräften). Bei R3
  gibt es eine Stange je Lasche (Excel "Rahmenecke GL24h SD" I76 "je
  Seite"), hinter einer starren Ankerplatte entstehen keine Abstützkräfte.
  Gleiche Behandlung wie bei R2 (dort ohne Faktor 1,6). Nutzer hat die
  Korrektur bestätigt und im Excel umgesetzt (Chat, 2026-09-28).
alternatives_considered: >
  k_t = 1,6·A_s/L_b (bisher, R3-GL24h-CALC-004) — um Faktor 1,6 zu steif.
date: "2026-09-28"
superseded_by:
---

Folge: c_t,sleeve GL24h sinkt von 25,28 auf 19,36 kN/mm je Seite. Neue
Werte: R3-GL24h-CALC-011, R3-GL75-CALC-002. Auswirkung auf die
Vorspannungsrechnung (Φ, F_sep im Sheet "VSP ... ohne Druckkontakt") wird
geprüft, wenn die Vorspannung behandelt wird.
