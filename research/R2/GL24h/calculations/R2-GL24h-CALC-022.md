---
calculation_id: R2-GL24h-CALC-022
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: FragiacomoBatchelar2012a
  experimental_data:
  assumptions:
method: >
  Anwendung der in R2-COMMON-HYP-001 (noch `CLAUDE_DRAFT`,
  `reviewed: false`) hergeleiteten Kombinationsformel
  `S_j,ini = z²/(1/c_T+1/c_C)` auf die bereits vorliegende
  Zugseiten-Gesamtsteifigkeit `c_T` (R2-GL24h-CALC-021) und
  Druckseiten-Gesamtsteifigkeit `c_C` (R2-GL24h-CALC-020), mit dem
  inneren Hebelarm `z=560mm`, der im R2-Excel identisch in allen drei
  Blättern ("Rahmenecke GL24h SD" C90/C92, "Rahmenecke GL24h HD"
  I92/I94, "Rahmenecke GL75 SD" I54/I56) als Eingabewert für den
  Momenten-Tragfähigkeitsnachweis `M_max=F·z` (R2-GL24h-CALC-012)
  verwendet wird. Direkt in der Exceldatei per openpyxl geprüft: `z`
  ist dort ein reiner Zahlen-Input ohne Formelherleitung — unabhängig
  von der `h_d=240mm`-Modellierungsannahme in `c_c,0` (R2-GL24h-CALC-019).
  Die Wiederverwendung desselben `z` für Tragfähigkeit UND Steifigkeit
  entspricht der üblichen Bauteilmethode-Praxis, ist hier aber
  ebenfalls noch nicht mit der Betreuerin abgestimmt.
equations: >
  S_j,ini = z²/(1/c_T + 1/c_C), siehe R2-COMMON-HYP-001 für die
  Herleitung.
result:
  quantity: Anfangsrotationssteifigkeit S_j,ini der Rahmenecke, GL24h
  value: 12540.8
  unit: kNm/rad
  original_value: 12540820306
  original_unit: N*mm/rad
source_file: >
  Abgeleitet aus R2-GL24h-CALC-020 (c_C), R2-GL24h-CALC-021 (c_T) und
  dem Excel-Zellwert z=560mm (R2/COMMON/calculations/20260109_Berechnung_
  Rahmenecke_eingeklebte Gewindestangen.xlsx, Sheet "Rahmenecke GL24h
  SD", Zellen C90/C92, per openpyxl mit data_only=True und
  data_only=False geprüft, Stand 2026-09-17)
certainty: CALCULATED
superseded_by:
---

**Eingangswerte:** `c_T = 53,300 kN/mm` (R2-GL24h-CALC-021),
`c_C = 160,137 kN/mm` (R2-GL24h-CALC-020), `z = 560 mm` (Excel, s. o.).

**Rechnung:**

```
c_eq = (1/c_T + 1/c_C)^-1 = (1/53,300 + 1/160,137)^-1 = 39,990 kN/mm
S_j,ini = z² · c_eq = 560² mm² · 39,990 kN/mm = 12.540.820 kN·mm
        = 12.540,8 kNm/rad
```

**Status:** Erste vollständige Anfangsrotationssteifigkeit der
Rahmenecke R2/GL24h. Beruht auf zwei noch offenen/unbestätigten
Punkten: (1) der Kombinationsformel selbst (R2-COMMON-HYP-001,
`CLAUDE_DRAFT`), (2) der Übernahme des bestehenden, in seiner Herkunft
weiterhin ungeklärten Hebelarms `z=560mm` (siehe R2-COMMON-OPQ-008) für
die Steifigkeits- statt nur die Tragfähigkeitskette. Zusätzlich erbt
dieser Wert alle bereits in R2-GL24h-CALC-020/021 dokumentierten
Vorbehalte (ASSY-verstärktes `c_c,90` nicht offiziell mit der
Betreuerin abgestimmt, `c_c,0`-Modellierungsannahme `l=240mm` gemäß
R2-COMMON-OPQ-011 offen). Als laufende Arbeitsthese zu behandeln, nicht
als bestätigtes Endergebnis — siehe R2-COMMON-OPQ-006 (Status bleibt
`OPEN`).
