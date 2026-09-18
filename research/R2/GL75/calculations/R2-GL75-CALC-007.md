---
calculation_id: R2-GL75-CALC-007
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions: R2-COMMON-OPQ-011
method: >
  Axiale Druck-Steifigkeit des Holzes PARALLEL zur Faser (0°) in der
  Druckzone des Rahmenecken-Innenknotens ("c_c,0"), als homogener
  Ersatzstab nach Hookeschem Gesetz: `c_c,0 = E_0,mean·A/l`. Fläche
  `A` = Fläche der Ankerplatte (160×240mm = 38.400mm², identisch zu
  `A_Stahlplatte` bei `c_c,90`). Länge `l` = 240mm (Plattentiefe in
  Kraftrichtung), dieselbe Saint-Venant-artige Modellierungsannahme wie
  bei GL24h (R2-GL24h-CALC-019, R2-COMMON-OPQ-011) — materialunabhängige
  Annahme, hier direkt auf GL75 übertragen. FprEN 1995-1-1:2024 enthält
  auch für GL75 keine Formel für diesen Fall (Kapitel 9 kennt nur 9.4,
  Querdruck, siehe R2-GL24h-CALC-019).
equations: >
  Hookesches Gesetz für den homogenen Stab: `c=E·A/l`. Keine
  FprEN-Fundstelle (siehe method).
result:
  quantity: Axiale Druck-Steifigkeit parallel zur Faser, c_c,0, GL75
  value: 2688
  unit: kN/mm
  original_value: 2688000
  original_unit: N/mm
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD", Zelle I66 (Formel
  `=Holzkennwerte!F34*I42/I35*10^-3`, per openpyxl mit data_only=True
  ausgelesen, Stand 2026-09-18). Vom Nutzer im Chat unabhängig mit
  demselben Ergebnis (2688) nachgerechnet.
certainty: ASSUMED
superseded_by:
---

Analog zu R2-GL24h-CALC-019, mit GL75-Kennwerten.

**Eingangswerte:** `E_0,mean=16.800 N/mm²` (GL75, Holzkennwerte!F34),
`A=38.400 mm²` (=160×240mm, Ankerplattenfläche), `l=240mm`
(Plattentiefe in Kraftrichtung, Excel-Zelle I35 "b_Stahlplatte" — im
GL75-Sheet mit demselben Zahlenwert wie bei GL24h verwendet).

**Rechnung:**

```
c_c,0 = E_0,mean · A / l
      = 16.800 N/mm² · 38.400 mm² / 240 mm
      = 2.688.000 N/mm
      = 2.688 kN/mm
```

**Status:** Wie bei GL24h (`certainty: ASSUMED` statt `CALCULATED`) —
die Bezugslänge `l=240mm` ist eine Modellierungsannahme ohne
Normvorgabe, bisher nicht mit der Betreuerin abgestimmt
(R2-COMMON-OPQ-011, materialunabhängig geführt, gilt also auch hier).
Bei Revision dieser Annahme ist dieser Wert entsprechend zu revidieren
(`superseded_by`).

Weiterverwendung: die zweite Feder der Druckseiten-Gesamtsteifigkeits-
kette `c_C`, siehe R2-GL75-CALC-008.
