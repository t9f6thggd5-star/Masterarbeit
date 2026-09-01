---
calculation_id: R2-GL24h-CALC-007
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Knicktragfähigkeit je ASSY-Verstärkungsschraube nach FprEN 11.2.2.5:
  Bettungsmodul `c_h`, Biegesteifigkeit `E_sI_s`, ideal-elastische
  Knicklast `N_ki`, plastische Normalkraft `N_pl`, bezogene Schlankheit
  `λ`, Knickbeiwert `φ_c` nach Ayrton-Perry-Ansatz.
equations: >
  FprEN 1995-1-1:2024, Gl. 11.5 (F_c), Gl. 11.6 (φ_c), Gl. 11.7 (φ),
  Gl. 11.8 (λ), Gl. 11.9 (N_pl), Gl. 11.10 (N_ki), Gl. 11.11 (c_h), Gl.
  11.12 (E_sI_s).
result:
  quantity: Knicktragfähigkeit je ASSY-Schraube, GL24h (maßgebend gegenüber Ausziehen)
  value: 11.734
  unit: kN
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen H93-H103 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-3 (FORMULAS.md Abschnitt 17, EXCEL_FORMULAS.md
Abschnitt 11) und unabhängig gegen die reale Excel-Datei verifiziert.

**Kette** (Zelle → Wert): `c_h=120,12 N/mm²` (H96, Gl. 11.11),
`E_sI_s=6.442.719,31 Nmm²` (H97, Gl. 11.12), `N_ki=27,819 kN` (H98, Gl.
11.10), `N_pl=17,671 kN` (H99, Gl. 11.9, mit `f_y,k=900 N/mm²`, ETA
11/0190, siehe R2-GL24h-DEC-006), `λ=0,797` (H100, Gl. 11.8),
`φ=0,964` (H101, Gl. 11.7), `φ_c=0,664` (H102, Gl. 11.6),
`F_c=φ_c·N_pl=11,734 kN` (H103, Gl. 11.5).

Zum Vergleich: FprEN-Ausziehwiderstand `F_w,k≈73,55 kN` (Zelle H94, Gl.
11.3, generisches Modell mit `k_screw=8,2`, siehe R2-COMMON-OPQ-003 zur
Frage einer produktspezifischen Alternative) — deutlich höher, daher
governiert das Knicken (`min(F_w,k;F_c)=11,734 kN`).
