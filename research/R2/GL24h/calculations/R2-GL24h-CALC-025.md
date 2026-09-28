---
calculation_id: R2-GL24h-CALC-025
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: FragiacomoBatchelar2012a
  experimental_data: 
  assumptions: R2-COMMON-ASS-006
method: >
  Wie R2-GL24h-CALC-022 (Kombinationsformel nach R2-COMMON-HYP-001,
  CLAUDE_DRAFT, reviewed: false), mit c_T,ges nach R2-GL24h-CALC-024 und
  c_C = 160,14 kN/mm (R2-GL24h-CALC-020), z = 560 mm.
equations: >
  S_j,ini = z²/(1/c_T,ges + 1/c_C).
result:
  quantity: Anfangsrotationssteifigkeit S_j,ini der Rahmenecke, GL24h (mit freier Stangendehnung)
  value: 10154.6
  unit: kNm/rad
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD": H128 (=C92^2/(1/L136+1/H109)*10^-3) = 10.154,63 kNm/rad; Sheet "GL24h HD": I128 identisch, Stand 2026-09-28 (vom Nutzer ergänzt, von Claude per openpyxl geprüft)
certainty: CALCULATED
superseded_by:
---

Ersetzt R2-GL24h-CALC-022 (12.540,8 kNm/rad, −19 %). Die Kombinationsformel
(R2-COMMON-HYP-001) ist weiterhin `CLAUDE_DRAFT`, `reviewed: false`, und nicht
mit der Betreuung abgestimmt (R2-COMMON-OPQ-006).
