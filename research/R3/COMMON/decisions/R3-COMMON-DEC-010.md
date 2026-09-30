---
decision_id: R3-COMMON-DEC-010
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Wird das Schubfeld im Riegel (Katalog Nr. 5, c_v) bei R3 angesetzt, und wie
  wird es berechnet? (Korrektur von R3-COMMON-DEC-007)
decision: >
  Ja, in Reihe zu den parallel geschalteten Laschen. c_v = c_v,H + 2·c_v,P mit
  c_v,H = G_mean·b·h_v/l_v (Holz Riegel, Feld 800 × 800 mm, b = 160 mm) und
  c_v,P = G_v·t_P·h_P/l_v,P je Seite mit **einer** BFU-BU-Platte je Seite,
  t_P = 15 mm (5-lagig), h_P = 800 mm, l_v,P = 460 mm, G_v = 520 N/mm²
  (COMMON-COMMON-DEC-010).
reason: >
  Nutzerangabe (Chat, 2026-09-30): 15 mm je Seite, nicht 2 × 15 mm wie in
  R3-COMMON-DEC-007 vermerkt; Faktor 2 im Excel (I143) vom Nutzer entfernt, da
  die Platten sonst doppelt gezählt wurden. G_v neu nach COMMON-COMMON-DEC-010.
alternatives_considered: >
  t_P = 2 × 15 mm je Seite und G_P = 500 N/mm² (R3-COMMON-DEC-007, fehlerhaft).
date: "2026-09-30"
superseded_by:
---

Ergebnisse: R3-GL24h-CALC-017 (131,13 kN/mm), R3-GL75-CALC-004 (163,13 kN/mm).
Modellgrenzen weiterhin R3-COMMON-OPQ-005; Länge im Nenner (l_v oder z)
R3-COMMON-OPQ-008.
