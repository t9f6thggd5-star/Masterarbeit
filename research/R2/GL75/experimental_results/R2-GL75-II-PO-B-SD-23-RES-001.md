---
result_id: R2-GL75-II-PO-B-SD-23-RES-001
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
  Push-Out-Versuch an einem Stabdübelanschluss (Versuchsreihe
  "II-PO-B-SD-23", GL75/BauBuche, Sheet "Rahmenecke GL75 SD").
result:
  quantity: Höchstlast F_max (Mittelwert aus 3 Prüfkörpern)
  value: 103.915
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Zellen B70-C72, Sheet "Rahmenecke GL75 SD" der Datei
`R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
Gewindestangen.xlsx`, per openpyxl mit data_only=True ausgelesen, Stand
der abgelegten Datei am 2026-09-01): `II-PO-B-SD-23-1 = 105,46 kN`
(C70), `II-PO-B-SD-23-2 = 100,73 kN` (C71), `II-PO-B-SD-23-3 =
102,37 kN` (C72). Mittelwert `103,915 kN` (C73).

Deutlich höher als die vergleichbaren GL24h-Versuchsreihen
(`II-PO-S-SD-34`: 68,715 kN; `II-PO-S-WD-34`: 69,605 kN) — konsistent mit
der wesentlich höheren Querdruckfestigkeit von BauBuche/GL75.

Nicht im Chat (chat-3) besprochen — Rolle dieser Versuchsreihe im
R2-Gesamtkonzept unklar, siehe R2-COMMON-OPQ-008.
