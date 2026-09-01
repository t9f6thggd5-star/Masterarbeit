---
calculation_id: R2-GL75-CALC-004
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
  Ankerplatte, korrigiert auf beidseitige Lastausbreitung `l_ef =
  b_Stahlplatte + 2·Δl` (Gl. 8.5/8.7/8.9) — analog zur Korrektur für
  GL24h, siehe R2-GL24h-CALC-010.
equations: FprEN 1995-1-1:2024, Gl. 8.5 (σ_c,90); Gl. 8.7 (k_c,90); Gl. 8.9 (A_ef); Tab. 8.1 (k_mat).
result:
  quantity: Unverstärkte Querdrucktragfähigkeit F_v,R, GL75
  value: 1206.815
  unit: kN
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD", Zellen I55-I71 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01, Datei-mtime 1788273961000)
certainty: CALCULATED
superseded_by:
---

Korrektur von R2-GL75-CALC-002. Der Nutzer hat mitgeteilt, dieselbe
Korrektur der Lastausbreitung (einseitig → beidseitig), die zuerst für
GL24h identifiziert und behoben wurde (siehe R2-GL24h-CALC-010), auch
auf Blatt "Rahmenecke GL75 SD" angewendet zu haben.

**Kette:** Struktur identisch zu R2-GL75-CALC-002 (`A=38.400 mm²`,
`k_mat=1,4`, `f_c,90,mean≈15,2505 N/mm²`), aber mit größerer effektiver
Fläche durch die korrigierte, beidseitige Lastausbreitung: `k_c,90`
erhöht sich entsprechend gegenüber dem alten, einseitigen Wert
(`1,2583`). `F_v,R = 1.206,815 kN` (I71) — ein Anstieg um den Faktor
`1.206,815/1.031,646 ≈ 1,170` gegenüber dem alten Wert, konsistent mit
dem für GL24h beobachteten Anstiegsfaktor
(`262,376/224,292 ≈ 1,170`, siehe R2-GL24h-CALC-010), da beide
Korrekturen auf derselben Geometrieänderung beruhen und `f_c,90,mean`
linear in `F_v,R` eingeht.

**Keine Auswirkung auf die maßgebende Komponente/`M_max`:** Anders als
bei GL24h (siehe R2-GL24h-CALC-012) ändert diese Korrektur für GL75
nichts an der maßgebenden Komponente oder an `M_max`. Nach
R2-GL75-CALC-003 ist für GL75 ohnehin das Gewindestangen-
Zugversuchsmittel (`291,003 kN`) maßgebend, nicht die unverstärkte
Querdrucktragfähigkeit — und der hier korrigierte Wert (`1.206,815 kN`)
liegt weiterhin weit darüber (wie schon der alte Wert `1.031,646 kN`).
`R2-GL75-CALC-003` bleibt daher unverändert gültig (`M_max=162,962
kNm`).

Die in R2-GL75-CALC-002 offen gelassene Frage, ob dieselben `k_mat`/
`k_c,90`-Werte (hergeleitet für die SWB-Klassifikation) ohne Anpassung
auf GL75/BauBuche übertragen werden dürfen, bleibt von dieser Korrektur
unberührt — siehe weiterhin R2-GL75-OPQ-003.
