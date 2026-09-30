---
calculation_id: R2-GL75-CALC-013
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature: 
  experimental_data: R2-GL75-II-T-B-BR-22-RES-003
  assumptions: R2-COMMON-ASS-001, R2-COMMON-ASS-009
method: >
  Wie R2-GL75-CALC-011, ergänzt um die freie Stangendehnung c_t der vier
  Gewindestangen (R2-COMMON-ASS-009), l_frei = 770 mm.
equations: >
  c_t = 4·E_s·A_s/l_frei; 1/c_T,ges = 1/c_Stange,4x + 1/c_t + 1/c_t,ep +
  1/c_c,90 + 1/c_v.
result:
  quantity: Gesamt-Zugseitensteifigkeit c_T,ges, GL75 (messwertbasiert, mit freier Stangendehnung)
  value: 50.015
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD": M58 l_frei = 770 mm, M59 c_t,1 = 42,545 kN/mm, M60 c_t = 170,18 kN/mm, M91 c_t,ges = 50,015 kN/mm (=(1/M55+1/M60+1/M65+1/M68+1/M87)^-1), Stand 2026-09-28 (vom Nutzer ergänzt, von Claude per openpyxl geprüft)
certainty: CALCULATED
superseded_by:
---

**Rechnung:**

```
c_T,ges = (1/1.119,5 + 1/170,18 + 0 + 1/158,02 + 1/145,0)⁻¹ = 50,01 kN/mm
```

Ersetzt R2-GL75-CALC-011 (70,83 kN/mm ohne c_t). Die freie Länge wurde im
Blatt direkt als 800 − 30 mm eingetragen (keine eigene Zelle l_t im
GL75-Blatt); gilt bei Stützenbreite 800 mm wie GL24h.
