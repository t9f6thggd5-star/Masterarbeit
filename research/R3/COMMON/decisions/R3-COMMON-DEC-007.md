---
decision_id: R3-COMMON-DEC-007
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Wird das Schubfeld im Riegel (Katalog Nr. 5, c_v, Buchholz2025 Gl. 12) bei
  R3 angesetzt, und wie wird es berechnet?
decision: >
  Ja, in Reihe zu den parallel geschalteten Laschen. Berechnung wie bei R2
  (R2-Excel "Rahmenecke GL24h SD" J115–L132): c_v = c_v,H + 2·c_v,P mit
  c_v,H = G_mean·b·h_v/l_v (Holz Riegel, Feld 800 × 800 mm, b = 160 mm) und
  c_v,P = G_P·t_P·h_P/l_v,P je Seite (Verstärkungsplatte, t_P = 2 × 15 = 30 mm,
  h_P = 800 mm, l_v,P = 460 mm, G_P = 500 N/mm², gleiches Material wie bei R2).
reason: >
  Buchholz2025 schaltet c_v bei Typ II und III in Reihe zur Zugzone, weil die
  Kraftumlenkung im Eck ein Schubfeld im Riegel erzeugt. Nutzerentscheidung
  und Geometrieangaben im Chat 2026-09-28.
alternatives_considered: >
  c_v weglassen bzw. als offene Frage führen — verworfen.
date: "2026-09-28"
superseded_by: R3-COMMON-DEC-010
---

Ergebnisse: R3-GL24h-CALC-012 (156,17 kN/mm), R3-GL75-CALC-003
(188,17 kN/mm). Modellgrenzen (Platte kürzer als das Holzfeld, reiner
Schub, G_P als Annahme) in R3-COMMON-OPQ-005.

**Korrektur (2026-09-30):** Laut Nutzer eine 15-mm-Platte je Seite (nicht
2 × 15 mm); G neu nach COMMON-COMMON-DEC-010. Ersetzt durch R3-COMMON-DEC-010.
