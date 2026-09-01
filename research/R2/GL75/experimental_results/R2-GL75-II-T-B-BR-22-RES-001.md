---
result_id: R2-GL75-II-T-B-BR-22-RES-001
scope:
  connection: R2
  material: GL75
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; die drei
  Einzelprüfwerte sind unten im Freitext dokumentiert (Provenienz:
  R2-Excel, siehe source-Hinweis).
n: 3
method: >
  Zugversuch an einer eingeklebten M16-Gewindestangenverbindung
  (Versuchsreihe "II-T-B-BR-22", GL75/BauBuche, Sheet "Rahmenecke GL75
  SD").
result:
  quantity: Höchstzugkraft F_max (Mittelwert aus 3 Prüfkörpern)
  value: 291.003
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Zellen G35-I38, Sheet "Rahmenecke GL75 SD" der Datei
`R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
Gewindestangen.xlsx`, per openpyxl mit data_only=True ausgelesen, Stand
der abgelegten Datei am 2026-09-01): `II-T-B-BR-22-1 = 291,07 kN` (I35),
`II-T-B-BR-22-2 = 291,39 kN` (I36), `II-T-B-BR-22-3 = 290,55 kN` (I37).
Mittelwert `291,003 kN` (I38), auch als `F_ax,d Versuche` referenziert
(I40).

Nahezu identisch zum GL24h-Wert (`II-T-S-BR-22`: 285,77 kN,
R2-GL24h-II-T-S-BR-22-RES-001) — plausibel, da die
Gewindestangen-Zugtragfähigkeit primär vom Stahl (Stange) und der
Verklebung abhängt, nicht vom umgebenden Holzwerkstoff. Ist für GL75 laut
R2-GL75-CALC-003 die "maßgebende Komponente" für die Momenten-
tragfähigkeit (anders als bei GL24h, wo die Querdrucktragfähigkeit
maßgebend ist).
