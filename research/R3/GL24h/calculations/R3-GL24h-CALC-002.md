---
calculation_id: R3-GL24h-CALC-002
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions:
method: >
  Reiner Stab (Zug/Druck), c_H = E·A/L, über die volle Laschenlänge ohne
  Berücksichtigung der verteilten ASSY-Abstützung. Dient als Vergleichswert
  zu R3-GL24h-CALC-001, um die Wirkung der ASSY-Abstützung sichtbar zu
  machen (siehe R3-GL24h-DEC-005).
equations: "c_H,800 = E_0,mean · A_netto / L"
result:
  quantity: Axiale Steifigkeit der Holzseitenlasche über volle Länge (ohne ASSY-Abstützung)
  value: 168.19
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl.
  Holzlaschen.xlsx (Eingangswerte E_0,mean, A_netto, Laschenlänge 800 mm
  aus Sheet "Holzkennwerte"; Stand August 2026 trotz Dateiname vom
  08.02.2026, siehe R3-GL24h-CALC-001)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-1, KNOWLEDGE.md ("Side-plate stiffness" → "Pure bar").
Mit E_0,mean = 11.500 N/mm², A_netto = 11.700 mm² und L = 800 mm
(Laschenlänge, siehe R3-GL24h-DEC-006):

c_H,800 = 11.500 · 11.700 / 800 = 168.187,5 N/mm ≈ 168,19 kN/mm.

Unabhängig nachgerechnet und bestätigt. Zeigt gegenüber R3-GL24h-CALC-001
(299,0 kN/mm) den Effekt der ASSY-Abstützung: die reine
Vollquerschnittsannahme unterschätzt die tatsächliche wirksame Steifigkeit
deutlich (siehe R3-GL24h-DEC-005 — "volle 800-mm-Länge zu weich für
verteilte ASSY-Abstützung").
