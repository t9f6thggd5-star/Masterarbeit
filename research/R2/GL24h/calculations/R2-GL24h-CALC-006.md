---
calculation_id: R2-GL24h-CALC-006
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024, ETA-11-0190-2026
  literature:
  experimental_data:
  assumptions:
method: >
  Querdruckverstärkte Tragfähigkeit nach FprEN Gl. 8.12 (dedizierte
  Verstärkungsgleichung, siehe R2-GL24h-DEC-004): Holzanteil
  (`k_mat=1,0` im verstärkten Fall) plus 9× Schraubenanteil
  (`min(F_w,k;F_c)` je Schraube, R2-GL24h-CALC-007), gegen zweiten
  Versagensmodus (Ebene der Schraubenspitze) geprüft.
equations: FprEN 1995-1-1:2024, Gl. 8.12; Gl. 8.13 (l_1,ef); Gl. 8.15 (l_2,ef).
result:
  quantity: Verstärkte Querdrucktragfähigkeit F_c,90, GL24h (maßgebender Modus)
  value: 248.846
  unit: kN
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen F73-F109 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-3 (FORMULAS.md Abschnitt 13, CURRENT_MODEL_PARAMETERS.md
Abschnitt G) und unabhängig gegen die reale Excel-Datei verifiziert.

**Ergebniskette:** Holzanteil `143,236 kN` (H104), Schraubenanteil
`9×11,734 kN = 105,610 kN` (H105, siehe R2-GL24h-CALC-007 für die
Herleitung von `F_c=11,734 kN` je Schraube), 1. Versagensmodus
`F_R1 = 248,846 kN` (H106), 2. Versagensmodus (Ebene Schraubenspitze)
`F_R2 = 413,793 kN` (H107) — maßgebend ist der kleinere Wert,
`F_c,90 = 248,846 kN` (H109, Gl. 8.12). Effektive Längen:
`l_1,ef=270 mm` (H91), `l_2,ef=780 mm` (H92).

Dieser Wert liegt knapp unter dem gemessenen Gewindestangen-
Zugversuchsmittel (`285,77 kN`, R2-GL24h-II-T-S-BR-22-RES-001) — die
verstärkte Querdruckresistenz ist damit (nach diesem Modell) der
rechnerisch maßgebende Widerstandsmechanismus für GL24h. Siehe
R2-GL24h-CALC-008 für die daraus abgeleitete Momententragfähigkeit.
