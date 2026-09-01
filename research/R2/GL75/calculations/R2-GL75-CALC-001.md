---
calculation_id: R2-GL75-CALC-001
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
  Johansen-Tragfähigkeit eines zweischnittigen Stabdübelanschlusses
  (d=12mm, S235, 2 Reihen × 3 Stabdübel = 6 Stück, a_1=85mm) für GL75, auf
  demselben Excel-Blatt wie die eigentliche R2-Gewindestangen-Berechnung,
  Rolle im R2-Gesamtkonzept unklar (siehe R2-COMMON-OPQ-008). Für GL75
  wird — anders als bei GL24h — der Beiwert `k_4` explizit aus einer
  "hardwood GLVL-P"-Tabelle entnommen, nicht aus der GL/softwood-Tabelle
  (siehe COMMON-COMMON-DEC-004).
equations: >
  FprEN 1995-1-1:2024, Gl. 11.14 (a-f); Gl. 11.15 (β); Tab. 11.6
  (28)-(31) (f_h,1,k/f_h,2,k/k_90/k_4/k_mat, mit expliziter
  hardwood-GLVL-P-Spalte für GL75); Tab. 11.10 (6) (n_ef).
result:
  quantity: Gruppen-Tragfähigkeit F_D,k,ges (Basis Stabdübel-Biegeversuch)
  value: 47.511
  unit: kN
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD", Zellen A34-A78 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Eigenständig aus der R2-Excel-Datei erschlossen — nicht in chat-3
besprochen (siehe R2-COMMON-OPQ-008 zur Rolle dieses Blocks).

**Geometrie-Unterschied zu GL24h:** 2×3-Anordnung (6 Stabdübel) statt
3×4 (12 Stabdübel) bei GL24h (R2-GL24h-CALC-009), `a_1=85 mm` statt
70 mm.

**Normative Basis** (`M_y,k=69.070,88 Nmm`, C36, identisch zu GL24h,
Tab. 11.7(2)): Modi a-f, C50-C55 (44,621 / 48,190 / 19,218 / 16,725 /
17,524 / 10,287 kN), governierend Modus f `F_D,k=10,287 kN` (C55/C56),
`n_ef=2,309` (C46/C48, Tab. 11.10(6), aus der GLVL-Zeile von Tab.
11.10(6)), `F_D,k,ges=47,511 kN` (C58).

**Basis aus Stabdübel-Biegeversuch** (`M_y,mean=156.989 Nmm`, C78, aus
demselben Biegeversuch wie bei GL24h — Versuchsdaten sind
materialunabhängig, da der Stabdübel selbst aus Stahl ist): Modi a-f
C60-C65, governierend Modus f `F_D,k=15,508 kN` (C65/C66),
`F_D,k,ges=71,627 kN` (C68).

**Vergleich mit realer Versuchsreihe** `II-PO-B-SD-23` (n=3, Mittelwert
`103,915 kN`, siehe R2-GL75-II-PO-B-SD-23-RES-001): deutlich höher als
beide rechnerischen Werte — passt zur insgesamt höheren
Querdruckfestigkeit von BauBuche/GL75 gegenüber GL24h.
