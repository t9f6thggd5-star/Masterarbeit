---
calculation_id: R2-GL24h-CALC-004
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions:
method: >
  Serienschaltung der vier parallel wirkenden Gewindestangen
  (R2-GL24h-CALC-002) mit dem gemeinsamen verstärkten Schubfeld
  (R2-GL24h-CALC-003).
equations: Serienfeder (1/c_1 + 1/c_2)^-1.
result:
  quantity: Gesamt-Zugseitensteifigkeit c_T, GL24h
  value: 38.392
  unit: kN/mm
  original_value: 38391.996
  original_unit: N/mm
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen C169-C170 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-3 (STATE.md Abschnitt 5, CURRENT_MODEL_PARAMETERS.md
Abschnitt B) und unabhängig gegen die reale Excel-Datei verifiziert:
`c_T = (1/116.000 + 1/57.384,18)^-1 = 38.391,996 N/mm ≈ 38,39 kN/mm`
(Zelle C169, in kN/mm auch direkt in C170 = 38,392).

Dies ist laut chat-3 die vorläufig abgeschlossene lineare
Zugseiten-Steifigkeit für die erste Phase-2-Abschätzung. Die
Druckseitensteifigkeit `c_C` und die Kombination zu einer
Rotationssteifigkeit der gesamten Rahmenecke stehen noch aus (siehe
R2-COMMON-OPQ-001/006). Kein entsprechender Wert liegt bisher für GL75
vor — siehe R2-GL75-OPQ-001.
