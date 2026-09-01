---
calculation_id: R1-GL75-CALC-001
scope:
  connection: R1
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Effektive Anzahl n_ef für die BauBuche/GL75-Variante des R1-Anschlusses
  nach der materialspezifischen LVL/GLVL-FprEN-Formel (siehe
  R1-GL24h-DEC-005 zur Materialunterscheidung), mit n_0=8, d=12mm,
  a_1=80mm, a_3,t=183mm und t_ms=12mm (voller innerer
  Stahlblech-Querschnitt, nicht halbiert).
equations: >
  n_ef = min{n_0, n_0^0.9 · (t·a / (50·d²))^(1/4)}, mit
  t = min{2t_1, 2t_2, t_ms} und a = min(a_1, a_3,t) für n_0≥2
  (FprEN 1995-1-1:2024, Tab. 11.10)
result:
  quantity: Effektive Anzahl n_ef (BauBuche/GL75, LVL/GLVL-Formel)
  value: 3.927
  unit: "-"
  original_value: 3.9265910508716924
  original_unit: "-"
source_file: >
  R1/COMMON/calculations/20260208_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL75 SD", Zellen C23-C26, C45/C50 (per openpyxl mit
  data_only=True ausgelesen, Stand der abgelegten Datei am 2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-2, KNOWLEDGE.md §5 ("BauBuche/GL75 example: n_0=8,
d=12, a_1=80, a_3,t=183, t_ms=12 → n_ef≈3.93") und unabhängig gegen die
reale Excel-Datei verifiziert (chat nannte ≈3.93, Excel-Zellwert
3.9266).

Dies ist der erste eigenständige Eintrag für R1/GL75 in diesem Wiki. Im
Unterschied zu GL24h (R1-GL24h-CALC-001, softwood-artige Abstandsregel,
n_ef≈5.50) wird hier die LVL/GLVL-spezifische Formel verwendet, siehe
R1-GL24h-DEC-005.
