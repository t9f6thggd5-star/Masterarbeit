---
calculation_id: R2-GL75-CALC-006
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions: R2-COMMON-DEC-002, R2-GL24h-DEC-008
method: >
  FprEN-Querdruckverformungsmodell unter der 160×240 mm-Ankerplatte,
  Druckseite (rechteckige Druckzone, R2-COMMON-DEC-002), beidseitige
  Lastausbreitung (analog GL24h-DEC-008, für GL75 mit identischer
  Ankerplattengeometrie übernommen, siehe R2-GL75-CALC-005): `c_c,90 =
  2·E_90,mean / (h_ef·(1/A + 1/A_ef))`. Anders als bei GL24h OHNE
  ASSY-Querdruckverstärkung (R2-GL75-OPQ-002, RESOLVED — keine ASSY bei
  GL75), also der unverstärkte FprEN-Ansatz, keine Bejtka-Formel
  (R2-COMMON-CALC-001) nötig.
equations: >
  FprEN 1995-1-1:2024, §9.4(5), Gl. 9.31, S. 152; Lastausbreitung nach
  Tab. 8.2/Gl. 8.11 (h_ef), Gl. 8.9 (A_ef).
result:
  quantity: Querdrucksteifigkeit unter der Ankerplatte, Druckseite, GL75 (unverstärkt)
  value: 176.409
  unit: kN/mm
  original_value: 176409.023
  original_unit: N/mm
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD", Zelle I55 (Formel
  `=2*Holzkennwerte!F35/(I37*(1/I42+1/I43))*10^-3`, per openpyxl mit
  data_only=True ausgelesen, Stand 2026-09-18). Vom Nutzer im Chat
  unabhängig mit demselben Ergebnis (176,41) nachgerechnet.
certainty: CALCULATED
superseded_by:
---

Analog zu R2-GL24h-CALC-001 (dieselbe Formel, dort für GL24h), aber mit
GL75-Kennwerten und der für die Druckseite bereits in R2-GL75-CALC-005
verwendeten (beidseitigen) Lastausbreitungsgeometrie.

**Eingangswerte** (Zelle → Wert, Sheet "Rahmenecke GL75 SD"):
`E_90,mean=470 N/mm²` (Holzkennwerte!F35), `h_ef=140mm` (I37,
`=MIN(0,4·h_Träger;140)`, `h_Träger=800mm`, I36), `l_ef=520mm` (I40,
beidseitig: `b_Stahlplatte+2·Δl`), `b_90,c=160mm` (I41),
`A_Stahlplatte=38.400mm²` (I42, `=160·240`), `A_ef=83.200mm²` (I43,
`=I40·I41`).

**Rechnung:**

```
c_c,90 = 2·E_90,mean / (h_ef·(1/A + 1/A_ef))
       = 2·470 / (140·(1/38.400 + 1/83.200))
       ≈ 176,409 kN/mm
```

**Plausibilitätshinweis:** Der Wert liegt sogar leicht über dem
ASSY-**verstärkten** GL24h-Wert der Druckseite (`c_c,90=175,402 kN/mm`,
Bejtka-Formel, siehe R2-GL24h-CALC-020) — obwohl GL75 unverstärkt ist.
Das ist konsistent mit dem bereits für die Tragfähigkeit dokumentierten
Befund (BauBuche braucht keine ASSY-Verstärkung, R2-GL75-OPQ-002): das
deutlich höhere `E_90,mean` von GL75 (470 vs. 300 N/mm² bei GL24h)
kompensiert den fehlenden Verstärkungseffekt.

Weiterverwendung: eine der beiden Federn der Druckseiten-Gesamt-
steifigkeitskette `c_C`, siehe R2-GL75-CALC-008.
