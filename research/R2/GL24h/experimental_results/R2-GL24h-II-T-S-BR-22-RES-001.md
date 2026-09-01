---
result_id: R2-GL24h-II-T-S-BR-22-RES-001
scope:
  connection: R2
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; die drei
  Einzelprüfwerte sind unten im Freitext dokumentiert (Provenienz:
  R2-Excel, siehe source-Hinweis).
n: 3
method: >
  Zugversuch an einer eingeklebten M16-Gewindestangenverbindung
  (Versuchsreihe "II-T-S-BR-22", GL24h). Identisch referenziert auf den
  Sheets "Rahmenecke GL24h SD" und "Rahmenecke GL24h HD" — dieselbe
  Versuchsreihe wird in beiden Berechnungsblättern als Eingangswert
  verwendet.
result:
  quantity: Höchstzugkraft F_max (Mittelwert aus 3 Prüfkörpern)
  value: 285.77
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Zellen G35-H38, Sheet "Rahmenecke GL24h SD" der Datei
`R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
Gewindestangen.xlsx`, per openpyxl mit data_only=True ausgelesen, Stand
der abgelegten Datei am 2026-09-01; identisch auf Sheet "Rahmenecke
GL24h HD"): `II-T-S-BR-22-1 = 289,92 kN` (H35), `II-T-S-BR-22-2 =
285,08 kN` (H36), `II-T-S-BR-22-3 = 282,31 kN` (H37). Mittelwert
`285,77 kN` (H38), auch als `F_ax,d Versuche` referenziert (H40).

Dieser Mittelwert entspricht der in chat-3 unter "one M16 rod path
component" diskutierten Versuchsgröße (SUMMARY.md/STATE.md nennen jedoch
keinen Zahlenwert für diese konkrete Versuchsreihe — die 285,77 kN
stammen ausschließlich aus der Excel-Datei, nicht aus dem Chattext
selbst).

Vergleich mit rechnerischen Widerständen: liegt oberhalb der unverstärkten
Querdrucktragfähigkeit (`224,29 kN`, R2-GL24h-CALC-005) und knapp
oberhalb der verstärkten Querdrucktragfähigkeit (`248,85 kN`,
R2-GL24h-CALC-006) — die Gewindestangen-Zugtragfähigkeit selbst scheint
für GL24h nicht der bemessungskritische Mechanismus zu sein (siehe
R2-GL24h-CALC-008 zur Wahl der "maßgebenden Komponente").
