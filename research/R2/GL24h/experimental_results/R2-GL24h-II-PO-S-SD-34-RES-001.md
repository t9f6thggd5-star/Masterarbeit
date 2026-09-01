---
result_id: R2-GL24h-II-PO-S-SD-34-RES-001
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
  Push-Out-Versuch an einem Stabdübelanschluss (Versuchsreihe
  "II-PO-S-SD-34", GL24h, Sheet "Rahmenecke GL24h SD"). Laut
  Excel-Anmerkung war Querdruckversagen des Holzes maßgeblich
  ("Querdruckversagen war maßgeblich", nicht klassisches
  Stabdübel-/Johansen-Versagen).
result:
  quantity: Höchstlast F_max (Mittelwert aus 3 Prüfkörpern)
  value: 68.715
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Zellen B69-C71, Sheet "Rahmenecke GL24h SD" der Datei
`R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
Gewindestangen.xlsx`, per openpyxl mit data_only=True ausgelesen, Stand
der abgelegten Datei am 2026-09-01): `II-PO-S-SD-34-1 = 68,27 kN` (C69),
`II-PO-S-SD-34-2 = 66,75 kN` (C70), `II-PO-S-SD-34-3 = 69,16 kN` (C71).
Mittelwert `68,715 kN` (C72).

Rein rechnerisch (Johansen, siehe R2-GL24h-CALC-009) ergäbe sich für
diese Konfiguration `F_D,k,ges ≈ 78,72 kN` (Basis: Fließmoment aus
Stabdübel-Biegeversuch) bzw. `≈ 61,97 kN` (normative Basis) — der
gemessene Wert liegt zwischen beiden, was zur dokumentierten Anmerkung
"Querdruckversagen war maßgeblich" passt (ein anderer, nicht rein
Johansen-basierter Versagensmechanismus).

Nicht im Chat (chat-3) besprochen — Rolle dieser Versuchsreihe im
R2-Gesamtkonzept unklar, siehe R2-COMMON-OPQ-008.
