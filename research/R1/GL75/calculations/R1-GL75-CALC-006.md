---
calculation_id: R1-GL75-CALC-006
scope:
  connection: R1
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature: Buchholz2025
  experimental_data:
  assumptions: R1-COMMON-ASS-001, R1-COMMON-ASS-002
method: >
  Wie R1-GL24h-CALC-009 (Federmodell Buchholz2025 Gl. 1–5,
  R1-COMMON-DEC-004; c_br,par und Druckseite vorläufig starr,
  Schlitzblech starr), mit den GL75-Werten: c_v,f = 2 · 727,74 kN/mm
  (R1-GL75-CALC-005), K_ser nach FprEN Tab. 11.12 mit ρ_mean = 800 kg/m³
  (R1-GL75-DEC-001), z = 550 mm.
equations: >
  Wie R1-GL24h-CALC-009: C_rot,tot = z²/(1/c_t,tot + 1/c_c,tot) +
  4 · I_p · K_ser.
result:
  quantity: Anfangsrotationssteifigkeit C_rot,tot der Rahmenecke R1 (GL75)
  value: 442124.6
  unit: kNm/rad
  original_value:
  original_unit:
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet "Rahmenecke GL75 SD", Stand 2026-09-26 (Datei-mtime
  1790430993271): I15 c_br,par = 1E+99, I18 c_v,f = 1.455,48 kN/mm,
  I21 c_t = 1.455,48 kN/mm, I24 c_t,tot = 727,74 kN/mm, N21 c_c,tot =
  2,5E+98, I27 K_ser = 47,222 kN/mm, I40 C_rot,v,f = 55.495,8 kNm/rad,
  N27 C_rot,t+c = 220.141,4 kNm/rad (=C91^2/(1/I24+1/N21)*10^-3, C91 = z =
  550 mm), N29 C_rot,tot = 442.124,6 kNm/rad (=N27+4*I40).
certainty: CALCULATED
superseded_by:
---

**Rechnung:**

```
c_t,tot   = 1/(1/1.455,48 + 1/1.455,48)        = 727,74 kN/mm
C_rot,t+c = 550² · 727,74 · 10⁻³                = 220.141,4 kNm/rad
C_rot,v,f = 1.175.200 · 47,222 · 10⁻³           = 55.495,8 kNm/rad
C_rot,tot = 220.141,4 + 4 · 55.495,8             = 442.124,6 kNm/rad
```

Vorbehalte wie R1-GL24h-CALC-009 (K_ser Versuchswert c_v,f/32 =
45,48 kN/mm statt 47,22 kN/mm: Σ C_rot,v,f −3,7 %).
