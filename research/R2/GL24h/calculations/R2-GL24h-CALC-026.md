---
calculation_id: R2-GL24h-CALC-026
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: FragiacomoBatchelar2012a
  experimental_data: 
  assumptions: R2-COMMON-ASS-007, R2-COMMON-DEC-005
method: >
  Übersichtstabelle nach COMMON-COMMON-DEC-008 (linear): Zylinderkraft
  F = M_max / a, Φ = M_max / S_j,ini (φ_S = 0 nach R2-COMMON-DEC-005),
  u_M = Φ · a, Schnittgrößen am Anschluss V = F·sin 45°, N = F·cos 45°
  (Druck), Hebelarm a nach R2-COMMON-ASS-007.
equations: >
  F = M/a; Φ = M/S_j,ini; u_M = Φ·a; V = F·sin 45°; N = F·cos 45°.
result:
  quantity: Übersichtswerte R2/GL24h – F = 52,83 kN; V = N = 37,35 kN; Φ = 15,76 mrad; u_M = 47,74 mm
  value: 15.76
  unit: mrad
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD": C99 M_max = 160,03 kNm, C105 a = 3,0293 m, C107 F = 52,83 kN, C106 V = 37,35 kN, L144 φ_el = 15,759 mrad, L145 φ_S = 0, L146 Φ_ges, L148 u_M = 47,74 mm, Stand 2026-09-28 (vom Nutzer ergänzt, von Claude per openpyxl geprüft)
certainty: CALCULATED
superseded_by:
---

**Rechnung:**

```
F   = 160,03 / 3,0293              = 52,83 kN
V=N = 52,83 · 0,7071               = 37,35 kN
Φ   = 160,03 / 10.154,6 · 1000     = 15,76 mrad
u_M = 15,76 · 3,0293               = 47,74 mm
```

Hinweis: R2-COMMON-ASS-007 ist die Geometrie-Annahme der Konfiguration 2/3
(a = 3029,3 mm). N ist im Excel noch nicht angelegt. Vorbehalte: S_j,ini
nach R2-COMMON-HYP-001 (nicht abgestimmt), c_c,0/z nach R2-COMMON-OPQ-011,
u_M nur Anschlussanteil (COMMON-COMMON-OPQ-004).
