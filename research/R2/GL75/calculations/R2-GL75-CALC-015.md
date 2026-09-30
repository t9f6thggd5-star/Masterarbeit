---
calculation_id: R2-GL75-CALC-015
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature: FragiacomoBatchelar2012a
  experimental_data: 
  assumptions: R2-COMMON-ASS-007, R2-COMMON-DEC-005
method: >
  Wie R2-GL24h-CALC-026 mit den GL75-Werten.
equations: >
  F = M/a; Φ = M/S_j,ini; u_M = Φ·a; V = F·sin 45°; N = F·cos 45°.
result:
  quantity: Übersichtswerte R2/GL75 – F = 53,79 kN; V = N = 38,04 kN; Φ = 13,53 mrad; u_M = 40,98 mm
  value: 13.53
  unit: mrad
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD": C94 M_max = 162,96 kNm, C101 a = 3,0293 m, C103 F = 53,79 kN, C102 V = 38,04 kN, M98 φ_el = 13,529 mrad, M99 φ_S, M100 Φ_ges, M102 u_M = 40,98 mm, Stand 2026-09-28 (vom Nutzer ergänzt, von Claude per openpyxl geprüft)
certainty: CALCULATED
superseded_by:
---

**Rechnung:**

```
F   = 162,96 / 3,0293              = 53,79 kN
V=N = 53,79 · 0,7071               = 38,04 kN
Φ   = 162,96 / 12.045,5 · 1000     = 13,53 mrad
u_M = 13,53 · 3,0293               = 40,98 mm
```

Hinweis zum Blatt: M99 (φ_S) verweist auf M109 (leer) statt auf M96 (= 0);
Ergebnis derzeit gleich, Bezug sollte korrigiert werden. N ist im Excel noch
nicht angelegt. Vorbehalte wie R2-GL24h-CALC-026.
