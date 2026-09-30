---
calculation_id: R2-GL24h-CALC-024
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: Bejtka-2005
  experimental_data: R2-GL24h-II-T-S-BR-22-RES-003
  assumptions: R2-COMMON-ASS-001, R2-COMMON-ASS-009
method: >
  Wie R2-GL24h-CALC-021 (Serienschaltung nach R2-COMMON-DEC-004), ergänzt um
  die freie Stangendehnung c_t der vier Gewindestangen (R2-COMMON-ASS-009):
  c_t,1 = E_s·A_s/l_frei mit l_frei = 800 − 30 = 770 mm, vier Stangen parallel.
equations: >
  c_t = 4·E_s·A_s/l_frei; 1/c_T,ges = 1/c_Stange,4x + 1/c_t + 1/c_t,ep +
  1/c_c,90 + 1/c_v.
result:
  quantity: Gesamt-Zugseitensteifigkeit c_T,ges, GL24h (messwertbasiert, mit freier Stangendehnung)
  value: 40.588
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD": L97 l_frei = 770 mm, L98 c_t,1 = 42,545 kN/mm (=H16*H17/L97*10^-3), L99 c_t = 170,18 kN/mm, L136 c_T,ges = 40,588 kN/mm (=(1/L94+1/L99+1/L102+1/L113+1/L132)^-1); identisch im Sheet "Rahmenecke GL24h HD" (M97–M99, M136), Stand 2026-09-28 (vom Nutzer ergänzt, von Claude per openpyxl geprüft)
certainty: CALCULATED
superseded_by:
---

**Rechnung:**

```
c_t     = 4 · 210.000 · 156 / 770 · 10⁻³        = 170,18 kN/mm
c_T,ges = (1/862,53 + 1/170,18 + 0 + 1/111,34 + 1/116,0)⁻¹ = 40,59 kN/mm
```

Ersetzt R2-GL24h-CALC-021 (53,30 kN/mm ohne c_t). Anteile an der
Nachgiebigkeit: c_c,90 ≈ 36 %, c_v ≈ 35 %, c_t ≈ 24 %, Stangenverbund ≈ 5 %.
A_s = 156 mm² im Blatt (nach DIN EN ISO 898-1 für M16: 157 mm², Einfluss
< 1 %). Vorbehalt c_c,90 (Bejtka, verstärkt) wie in CALC-021.
