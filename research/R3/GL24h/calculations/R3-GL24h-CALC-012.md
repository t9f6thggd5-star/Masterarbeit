---
calculation_id: R3-GL24h-CALC-012
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: Buchholz2025
  experimental_data:
  assumptions: >
    Reiner Schub, gleichmäßige Schubspannung, G_mean über den vollen
    Querschnitt; Holzfeld 800 × 800 mm, b = 160 mm, G_mean = 650 N/mm²;
    Verstärkung je Seite t_P = 30 mm, h_P = 800 mm, l_v,P = 460 mm,
    G_P = 500 N/mm² (wie R2, "KLH ETA Scheibenbeanspruchung");
    Holz und Platten parallel (R3-COMMON-DEC-007).
method: >
  Steifigkeit des Schubfelds im Riegel (Katalog Nr. 5): Schubspannung
  τ = V/(b·h_v), Gleitung γ = τ/G, Verschiebung δ = γ·l_v, daraus
  c = V/δ = G·b·h_v/l_v. Rechenweg wie R2.
equations: >
  c_v,H = 650 · 160 · 800 / 800 = 104,00 kN/mm;
  c_v,P = 500 · 30 · 800 / 460 = 26,09 kN/mm je Seite;
  c_v = 104,00 + 2 · 26,09 = 156,17 kN/mm
result:
  quantity: Schubsteifigkeit des Schubfelds im Riegel (Holz + 2 Verstärkungsplatten)
  value: 156.17
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  Gerechnet im Chat 2026-09-28; Umsetzung im Nutzer-Excel R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl. Holzlaschen.xlsx,
  Sheet "Rahmenecke GL24h SD" (Zelle I136 laut Nutzerformel).
certainty: CALCULATED
superseded_by: R3-GL24h-CALC-017
---

Anteil an der Nachgiebigkeit der Zugseite etwa 20 %. Modellgrenzen siehe
R3-COMMON-OPQ-005.

**Update (2026-09-30):** ersetzt, siehe superseded_by.
