---
calculation_id: R3-GL24h-CALC-001
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions: R3-GL24h-ASS-002
method: >
  Reiner Stab (Zug/Druck), c_H = E·A/L, mit der wirksamen Länge L_eff aus
  der Equal-row-load-Vereinfachung (R3-GL24h-ASS-002) statt der vollen
  Laschenlänge, um die verteilte ASSY-Abstützung der Holzlasche zu
  berücksichtigen (siehe R3-GL24h-DEC-005).
equations: "c_H,eff = E_0,mean · A_netto / L_eff"
result:
  quantity: Effektive axiale Steifigkeit der Holzseitenlasche (mit ASSY-Abstützung)
  value: 299.0
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl.
  Holzlaschen.xlsx (Sheet "VSP GL24h ohne Druckkontakt", Eingangswerte
  E_0,mean und A_netto aus Sheet "Holzkennwerte"; Stand August 2026 trotz
  Dateiname vom 08.02.2026 — bestätigt durch übereinstimmenden Wert
  c_ax=199,1466 kN/mm)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-1, KNOWLEDGE.md ("Side-plate stiffness" →
"Equal-row-row-simplification") und `artifacts/effective-sideplate-stiffness.md`.
Mit E_0,mean = 11.500 N/mm², A_netto = 11.700 mm² und L_eff = 450 mm
(aus R3-GL24h-ASS-002, hergeleitet aus Geometrie 170 mm + 7×80 mm + 70 mm
= 800 mm Gesamtlänge, siehe R3-GL24h-DEC-006):

c_H,eff = 11.500 · 11.700 / 450 = 299,0 kN/mm.

Zum Vergleich mit der vollen Laschenlänge ohne ASSY-Abstützung siehe
R3-GL24h-CALC-002 (c_H,800 = 168,19 kN/mm).

**Hinweis:** der Wert 299,0 kN/mm konnte in der aktuellen Exceltabelle
nicht als eigenständige, eindeutig benannte Zelle wiedergefunden werden
(nur die Eingangswerte E, A, L sind dort direkt nachvollziehbar) — er
stammt als fertiges Zwischenergebnis aus dem Chatverlauf. Die Rechnung
selbst wurde unabhängig nachgerechnet: 11.500 · 11.700 / 450 = 299.000
N/mm = 299,0 kN/mm — exakt bestätigt, nicht blind übernommen.
