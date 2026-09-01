---
calculation_id: R2-GL24h-CALC-002
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions: R2-COMMON-ASS-002
method: >
  Serienschaltung der Federn je Gewindestange (freie Stangendehnung
  `c_t`, Verbundsteifigkeit `c_ax,f,par`, anteilige Querdrucksteifigkeit
  `c_c,90/4`, starre Ankerplatte `c_t,ep`); Parallelschaltung von 2
  Stangen je Zugpfad, dann Parallelschaltung von 2 Zugpfaden (4 Stangen
  gesamt), noch vor dem gemeinsamen Schubfeld.
equations: >
  Serienfeder `(Σ 1/c_i)^-1`; Parallelfeder `Σc_i`; FprEN
  1995-1-1:2024, 11.3.8.3 (2)/Tab. 11.13 (3) für die
  Verbund-Einklebesteifigkeit.
result:
  quantity: Vier Gewindestangen parallel, vor dem gemeinsamen Schubfeld
  value: 57.384
  unit: kN/mm
  original_value: 57384.178
  original_unit: N/mm
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen C120-C147 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-3 (STATE.md Abschnitt 3, KNOWLEDGE.md Abschnitt 4)
und unabhängig gegen die reale Excel-Datei verifiziert.

**Zwischenwerte je Zelle:**
- `c_t,1 = 40.950 N/mm` (C120, freie Stangendehnung, R2-GL24h-DEC-001)
- `l_w = 320 mm` ansetzbare Einklebelänge (C123, FprEN 11.3.8.3 (2))
- `K_SLS,w = c_ax,f,par = 177.646,15 N/mm` (C124/C126, FprEN Tab. 11.13
  (3))
- `c_t,ep = 1E+99 N/mm` (C129, R2-COMMON-ASS-001)
- `c_c,90 = 100.866,36 N/mm` (C141, R2-GL24h-CALC-001)
- **Gesamtsteifigkeit je Stange** `c_Stange = (1/c_t + 1/c_t,ep +
  1/(4·c_c,90/... nach Excel-Formelnotation) + 1/c_ax,f,par)^-1 =
  14.346,04 N/mm ≈ 14,35 kN/mm` (C145)
- **Ein Zugpfad (2 Stangen parallel)** `c_Zugpfad = 28.692,09 N/mm ≈
  28,69 kN/mm` (C146)
- **Vier Stangen gesamt (2 Zugpfade parallel)** `c_Zugpfade,ges =
  57.384,18 N/mm ≈ 57,38 kN/mm` (C147) — dies ist das hier dokumentierte
  Endergebnis.

Eingang in R2-GL24h-CALC-004 (Gesamt-Zugseitensteifigkeit `c_T`, in Serie
mit dem Schubfeld R2-GL24h-CALC-003).
