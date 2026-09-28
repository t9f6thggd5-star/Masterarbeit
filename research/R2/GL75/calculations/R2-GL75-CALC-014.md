---
calculation_id: R2-GL75-CALC-014
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature: FragiacomoBatchelar2012a
  experimental_data: 
  assumptions: R2-COMMON-ASS-006
method: >
  Wie R2-GL75-CALC-012 (R2-COMMON-HYP-001, CLAUDE_DRAFT, reviewed: false),
  mit c_T,ges nach R2-GL75-CALC-013 und c_C = 165,54 kN/mm
  (R2-GL75-CALC-008), z = 560 mm.
equations: >
  S_j,ini = z²/(1/c_T,ges + 1/c_C).
result:
  quantity: Anfangsrotationssteifigkeit S_j,ini der Rahmenecke, GL75 (mit freier Stangendehnung)
  value: 12045.5
  unit: kNm/rad
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD": I89 (=C86^2/(1/M91+1/I70)*10^-3) = 12.045,46 kNm/rad, Stand 2026-09-28 (vom Nutzer ergänzt, von Claude per openpyxl geprüft)
certainty: CALCULATED
superseded_by:
---

Ersetzt R2-GL75-CALC-012 (15.556,6 kNm/rad, −23 %). Vorbehalt wie
R2-GL24h-CALC-025.
