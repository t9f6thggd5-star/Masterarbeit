---
calculation_id: R2-GL75-CALC-005
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024, ETA-14-0354-2026
  literature:
  experimental_data:
  assumptions: R2-GL75-DEC-001, R2-GL24h-DEC-008
method: >
  Korrektur von R2-GL75-CALC-004: `k_mat` wird jetzt gemäß R2-GL75-DEC-001
  mit `1,0` (Hardwood LVL/GLVL, Case A, edgewise) statt `1,4` (SWB)
  angesetzt. Zugleich hat der Nutzer die R2-Excel-Datei so erweitert,
  dass die unverstärkte Querdrucktragfähigkeit — analog zu GL24h,
  R2-GL24h-CALC-010/018 — jetzt getrennt nach Zug- und Druckseite
  berechnet wird (einseitige Lastausbreitung auf der Zugseite,
  beidseitige auf der Druckseite, R2-GL24h-DEC-008, für GL75 mit
  identischer Ankerplattengeometrie übernommen).
equations: FprEN 1995-1-1:2024, Gl. 8.5 (σ_c,90); Gl. 8.7 (k_c,90); Gl. 8.9 (A_ef); Tab. 8.1 (k_mat, jetzt Hardwood LVL/GLVL-Zeile).
result:
  quantity: Unverstärkte Querdrucktragfähigkeit F_v,R, GL75, getrennt nach Druck- und Zugseite (k_mat korrigiert)
  value: 862.011 (Druckseite) / 736.890 (Zugseite)
  unit: kN
  original_value: 862010.647 / 736890.158
  original_unit: N
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL75 SD", Zellen G32-M48 (per
  openpyxl mit data_only=True und als Formeltext ausgelesen, Stand der
  abgelegten Datei am 2026-09-17, Datei-mtime 1789638113424).
certainty: CALCULATED
superseded_by:
---

Korrektur/Erweiterung von R2-GL75-CALC-004, ausgelöst durch zwei
unabhängige Änderungen, die der Nutzer gleichzeitig in der R2-Excel-Datei
vorgenommen hat: (1) `k_mat=1,4→1,0` gemäß R2-GL75-DEC-001, (2) Trennung
der Berechnung nach Zug-/Druckseite gemäß demselben Prinzip wie bei
GL24h (R2-GL24h-DEC-008).

**Zellenkette Druckseite** (Spalte I): `l_ef=520 mm` (I40, beidseitig),
`A_ef=83.200 mm²` (I43), `k_c,90=1,4720` (I44), `k_mat=1,0` (I45, neu,
vorher `1,4`), `σ_c,90=22,448 N/mm²` (I46, Gl. 8.5, mit
`f_c,90,mean(GL75)=15,2505 N/mm²`) → `F_v,R=22,448×38.400/1.000=862,011
kN` (I48).

**Zellenkette Zugseite** (Spalte M): `l_ef=380 mm` (M40, einseitig),
`A_ef=60.800 mm²` (M43), `k_c,90=1,2583` (M44), `k_mat=1,0` (M45),
`σ_c,90=19,190 N/mm²` (M46) → `F_v,R=19,190×38.400/1.000=736,890 kN`
(M48).

**Konsistenzprüfung:** Verhältnis neu/alt (Druckseite, altes
undifferenziertes `k_mat=1,4`-Ergebnis aus R2-GL75-CALC-004,
`1.206,815 kN`): `862,011/1.206,815≈0,7143=1,0/1,4` — exakt der
erwartete Faktor aus der reinen `k_mat`-Korrektur, keine weitere
Änderung eingeflossen. Analog Zugseite gegenüber dem (undokumentierten,
weil bisher nicht seitengetrennt berechneten) alten Wert.

**Keine Auswirkung auf `M_max`:** Wie schon bei der vorherigen Korrektur
(R2-GL75-CALC-004) bleibt die maßgebende Komponente für GL75 auch nach
dieser weiteren Reduktion das Gewindestangen-Zugversuchsmittel
(`291,003 kN`, R2-GL75-CALC-003) — beide neuen Querdruckwerte
(`862,011 kN` Druckseite, `736,890 kN` Zugseite) liegen weiterhin weit
darüber. `R2-GL75-CALC-003` (`M_max=162,962 kNm`) bleibt damit
unverändert gültig; siehe dortige Ergänzung.

**Löst R2-GL75-OPQ-003** (Anwendbarkeit der SWB-Beiwerte auf
GL75/BauBuche) — die Frage war ursprünglich, ob `k_mat=1,4` überhaupt für
dieses Material einschlägig ist; mit R2-GL75-DEC-001 ist das jetzt
verneint und durch `k_mat=1,0` ersetzt.
