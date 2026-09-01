---
calculation_id: R2-GL24h-CALC-005
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
  Unverstärkte FprEN-Querdruckfestigkeitsverifikation unter der
  Ankerplatte: `σ_c,90 = k_mat·k_c,90·f_c,90,mean`,
  `F_v,R = σ_c,90·A`, mit mittlerer Querdruckfestigkeit GL24h
  (`f_c,90,mean ≈ 3,3156 N/mm²`) und experimentnaher `γ=1`-Betrachtung
  (COMMON-COMMON-DEC-001).
equations: FprEN 1995-1-1:2024, Gl. 8.5 (σ_c,90); Gl. 8.7 (k_c,90); Tab. 8.1 (k_mat).
result:
  quantity: Unverstärkte Querdrucktragfähigkeit F_v,R, GL24h
  value: 224.292
  unit: kN
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen F55-F71 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-3 (FORMULAS.md Abschnitt 12, KNOWLEDGE.md Abschnitt
8) und unabhängig gegen die reale Excel-Datei verifiziert.

**Eingangswerte** (Zelle → Wert, Spalte "Norm"): `A=38.400 mm²` (H65),
`A_ef=60.800 mm²` (H66), `k_c,90=1,2583` (H67, Gl. 8.7), `k_mat=1,4`
(H68, Tab. 8.1, siehe R2-GL24h-DEC-003), `σ_c,90=5,8409 N/mm²` (H69, Gl.
8.5) → `F_v,R = 5,8409×38.400/1.000 = 224,292 kN` (H71).

Dieser Wert liegt deutlich unter dem gemessenen Gewindestangen-
Zugversuchsmittel (`285,77 kN`, siehe
R2-GL24h-II-T-S-BR-22-RES-001) und unter dem verstärkten Wert
(`≈248,85 kN`, R2-GL24h-CALC-006) — die unverstärkte Querdruckfestigkeit
allein wäre für diese Verbindung nicht ausreichend, weshalb die
ASSY-Verstärkung erforderlich ist.
