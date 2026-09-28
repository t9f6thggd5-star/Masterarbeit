---
calculation_id: R1-GL75-CALC-007
scope:
  connection: R1
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature: Buchholz2025
  experimental_data:
  assumptions: R1-COMMON-ASS-002, R1-COMMON-ASS-003
method: >
  Werte der Übersichtstabelle nach COMMON-COMMON-DEC-008 (linear), wie
  R1-GL24h-CALC-011, jedoch mit M_R aus der rechnerischen Tragfähigkeit der
  Dübelgruppe (n_ef = 7,31, R1-GL75-CALC-003) nach R1-GL75-DEC-002;
  C_rot,tot nach R1-GL75-CALC-006.
equations: >
  φ_el = M_R / C_rot,tot; φ_S = 2·v0,mittel / z; Φ_ges = φ_el + φ_S;
  F = M_R / a; u_M = Φ · a; v0 = v01 − F01 / K_ser je Kurve (EN 26891).
result:
  quantity: Übersichtswerte R1/GL75 – F = 293,8 kN; φ_el = 1,560 mrad; φ_S = 1,196 mrad; Φ_ges = 2,757 mrad; u_M = 3,66 mm ohne / 6,47 mm mit Anfangsschlupf
  value: 1.560 / 2.757
  unit: mrad
  original_value:
  original_unit:
source_file: >
  R1/COMMON/calculations/20260109_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL75 SD", Stand 2026-09-28: C100 M_R = 689,79 kNm
  (=C96*C91*10^-3, C96 = C30 = C72 = 1254,16 kN), N40 C_rot,tot =
  442.124,6 kNm/rad, C91 z = 550 mm, C108 a = 2,3476 m, C111 F = 293,83 kN,
  I46–I55 v0 je Kurve, I57 v0,mittel = 0,3290 mm, I59 φ_S, I64 φ_el
  (=C100/N40*1000), I66 Φ_ges, I68/I69 u_M.
certainty: CALCULATED
superseded_by:
---

**Rechnung:**

```
φ_el  = 689,79 / 442.124,6 · 1000         = 1,560 mrad
v0    = (0,422 + 0,238 + 0,336 + 0,306 + 0,444 + 0,228) / 6 = 0,329 mm
φ_S   = 2 · 0,329 / 550 · 1000             = 1,196 mrad
Φ_ges = 1,560 + 1,196                      = 2,757 mrad
F     = 689,79 / 2,3476                    = 293,8 kN
u_M   = 1,560 · 2,3476 = 3,66 mm (ohne) ; 2,757 · 2,3476 = 6,47 mm (mit Schlupf)
```

v0 je Kurve aus den Versuchsblättern I-T-B-SD-28-1 bis -3 (M11, S11, P11,
M21, S21), vom Nutzer eingetragen, von Claude geprüft (2026-09-28); das
Mittel der sechs K_ser ist 727,74 kN/mm (= J7).

**Vergleich:** Mit M_R aus den Versuchen (C102 = 684,50 kNm) wären es
F = 291,6 kN, φ_el = 1,548 mrad, u_M = 3,63 / 6,44 mm.

**Vorbehalte:** wie R1-GL24h-CALC-011 (Druckseite starr → Untergrenze,
Schlupf R1-COMMON-OPQ-008, u_M nur Anschlussanteil). Zusätzlich:
Nettoquerschnittsversagen des Schlitzblechs in der Rahmenecke
(R1-GL75-OPQ-004). Im Blatt verweist C109 (V_ed) noch auf C102, C111 auf
C100.
