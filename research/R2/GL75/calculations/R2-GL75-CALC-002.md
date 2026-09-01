---
calculation_id: R2-GL75-CALC-002
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Unverstärkte FprEN-Querdruckfestigkeitsverifikation unter der
  Ankerplatte, rechnerisch identisch zum GL24h-Verfahren (Gl. 8.5/8.7,
  gleiche Geometrie `A=38.400 mm²`, `A_ef=60.800 mm²`,
  `k_c,90=1,2583`, `k_mat=1,4`), aber mit der wesentlich höheren
  mittleren Querdruckfestigkeit von GL75/BauBuche
  (`f_c,90,mean≈15,2505 N/mm²` statt `≈3,3156 N/mm²` bei GL24h).
equations: FprEN 1995-1-1:2024, Gl. 8.5 (σ_c,90); Gl. 8.7 (k_c,90); Tab. 8.1 (k_mat).
result:
  quantity: Unverstärkte Querdrucktragfähigkeit F_v,R, GL75
  value: 1031.646
  unit: kN
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD", Zellen G55-I71 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Eigenständig aus der R2-Excel-Datei erschlossen und rechnerisch
nachvollzogen (nicht in chat-3 besprochen, dort existiert für GL75 keine
Querdruck-Festigkeitsdiskussion).

**Eingangswerte** (Zelle → Wert): `A=38.400 mm²` (I65),
`A_ef=60.800 mm²` (I66), `k_c,90=1,2583` (I67, Gl. 8.7 — identisch zu
GL24h, da gleiche Plattengeometrie), `k_mat=1,4` (I68, Tab. 8.1 —
identisch zu GL24h), `σ_c,90=26,866 N/mm²` (I69, Gl. 8.5) →
`F_v,R = 26,866×38.400/1.000 = 1.031,646 kN` (I71).

**Rechnerische Plausibilitätsprüfung (Claude, 2026-09-01):** Das
Verhältnis `F_v,R(GL75)/F_v,R(GL24h) = 1.031,65/224,29 ≈ 4,600` entspricht
exakt dem Verhältnis der mittleren Querdruckfestigkeiten
`f_c,90,mean(GL75)/f_c,90,mean(GL24h) = 15,2505/3,3156 ≈ 4,600`
(Holzkennwerte-Blatt, Zellen D20/F20) — der Wert ist also intern
rechnerisch konsistent und **kein** Excel-Formelfehler im engeren Sinne.

**Verbleibende offene Frage:** Ob dieselben `k_mat`/`k_c,90`-Werte
(hergeleitet für die SWB-Klassifikation, siehe R2-GL24h-DEC-003) ohne
Anpassung auf GL75/BauBuche (klassifiziert als hardwood GLVL, siehe
COMMON-COMMON-DEC-004) übertragen werden dürfen, ist damit noch nicht
beantwortet — siehe R2-GL75-OPQ-003. Der Dowel-Johansen-Nachweis auf
demselben Excel-Blatt (R2-GL75-CALC-001) verwendet für GL75 explizit
einen eigenen, GLVL-spezifischen Tabellenwert (`k_4`), während dieser
Querdrucknachweis keine erkennbare materialspezifische Anpassung
vornimmt.
