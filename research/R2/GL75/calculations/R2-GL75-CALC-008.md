---
calculation_id: R2-GL75-CALC-008
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature: FragiacomoBatchelar2012a
  experimental_data:
  assumptions: R2-COMMON-DEC-004
method: >
  Gesamt-Druckseitensteifigkeit `c_C` als Serienschaltung der beiden
  Holzfedern `c_c,90` (Querdruck) und `c_c,0` (Druck parallel zur
  Faser), gemäß der materialunabhängigen Federmodell-Topologie aus
  R2-COMMON-DEC-004 (Fig. 7, FragiacomoBatchelar2012a): `1/c_C = 1/c_c,90
  + 1/c_c,0`. Kein Stangen-/Schub-Anteil auf der Druckseite. Anders als
  bei GL24h wird hier der UNVERSTÄRKTE `c_c,90`-Wert angesetzt, da GL75
  keine ASSY-Querdruckverstärkung hat (R2-GL75-OPQ-002, RESOLVED).
equations: >
  Serienfeder: `(1/c_1+1/c_2)^-1`. `c_c,90`: FprEN Gl. 9.31, siehe
  R2-GL75-CALC-006. `c_c,0`: Hookesches Gesetz, siehe R2-GL75-CALC-007.
result:
  quantity: Gesamt-Druckseitensteifigkeit c_C, GL75 (unverstärkt)
  value: 165.545
  unit: kN/mm
  original_value: 165544.602
  original_unit: N/mm
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD", Zelle I70 (Formel
  `=(1/I55+1/I66)^-1`, per openpyxl mit data_only=True ausgelesen, Stand
  2026-09-18). Vom Nutzer im Chat unabhängig mit demselben Ergebnis
  (165,54) nachgerechnet.
certainty: CALCULATED
superseded_by:
---

Analog zu R2-GL24h-CALC-020, aber mit dem unverstärkten `c_c,90`
(GL75 hat keine ASSY-Verstärkung, R2-GL75-OPQ-002).

**Eingangswerte:** `c_c,90 = 176,409 kN/mm` (unverstärkt, R2-GL75-CALC-006),
`c_c,0 = 2.688 kN/mm` (R2-GL75-CALC-007).

**Rechnung:**

```
c_C = (1/c_c,90 + 1/c_c,0)^-1
    = (1/176,409 + 1/2.688)^-1
    = 165,545 kN/mm
```

**Plausibilitäts-Hinweis:** `c_C(GL75)≈165,5 kN/mm` liegt über dem
ASSY-**verstärkten** GL24h-Wert (`c_C=160,137 kN/mm`, R2-GL24h-CALC-020)
— obwohl GL75 keine Verstärkung hat. Konsistent mit dem höheren
`E_90,mean` von BauBuche, siehe Plausibilitätshinweis in
R2-GL75-CALC-006.

**Status:** Beruht auf der bei `c_c,0` weiterhin offenen
Modellierungsannahme (`l=240mm`, R2-COMMON-OPQ-011) — bei Änderung
dieser Annahme ist dieser Wert zu revidieren. Die Kombination mit der
(für GL75 noch nicht aufgestellten) Zugseitensteifigkeit `c_T` zu einer
Rotationssteifigkeit steht noch aus (R2-GL75-OPQ-001, R2-COMMON-OPQ-006).
