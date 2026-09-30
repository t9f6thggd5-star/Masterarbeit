---
calculation_id: R3-GL75-CALC-003
scope:
  connection: R3
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature: Buchholz2025
  experimental_data:
  assumptions: >
    Wie R3-GL24h-CALC-012, jedoch G_mean = 850 N/mm² (Holzkennwerte F36);
    b = 160 mm (Excel "Rahmenecke GL75 SD" H93).
method: >
  Schubfeld im Riegel wie R3-GL24h-CALC-012 (R3-COMMON-DEC-007).
equations: >
  c_v,H = 850 · 160 · 800 / 800 = 136,00 kN/mm;
  c_v,P = 500 · 30 · 800 / 460 = 26,09 kN/mm je Seite;
  c_v = 136,00 + 2 · 26,09 = 188,17 kN/mm
result:
  quantity: Schubsteifigkeit des Schubfelds im Riegel (Holz + 2 Verstärkungsplatten)
  value: 188.17
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  Gerechnet im Chat 2026-09-28.
certainty: CALCULATED
superseded_by: R3-GL75-CALC-004
---

c_t,sleeve und c_t,tot für GL75 folgen, sobald c_ax,v,f,α für GL75 vorliegt
(R3-GL75-OPQ-002).

**Update (2026-09-30):** ersetzt, siehe superseded_by.
