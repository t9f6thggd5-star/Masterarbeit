---
result_id: R2-GL24h-II-PO-S-WD-34-RES-001
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
  "II-PO-S-WD-34", GL24h, Sheet "Rahmenecke GL24h HD" — Bezeichnungs-
  Diskrepanz "SD" vs. "WD"/"HD" zwischen Blattname und Versuchsreihen-ID
  nicht geklärt, siehe R2-COMMON-OPQ-008). Laut Excel-Anmerkung war auch
  hier Querdruckversagen des Holzes maßgeblich.
result:
  quantity: Höchstlast F_max (Mittelwert aus 3 Prüfkörpern)
  value: 69.605
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Zellen B81-C83, Sheet "Rahmenecke GL24h HD" der Datei
`R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
Gewindestangen.xlsx`, per openpyxl mit data_only=True ausgelesen, Stand
der abgelegten Datei am 2026-09-01): `II-PO-S-WD-34-1 = 69,29 kN` (C81),
`II-PO-S-WD-34-2 = 68,23 kN` (C82), `II-PO-S-WD-34-3 = 69,92 kN` (C83).
Mittelwert `69,605 kN` (C84), Anmerkung "Querdruckversagen war
maßgeblich" (D84).

Sehr ähnlicher Mittelwert wie die parallele Versuchsreihe
`II-PO-S-SD-34` (68,715 kN, R2-GL24h-II-PO-S-SD-34-RES-001) auf dem
"SD"-Blatt — beide Reihen könnten dieselbe physische Verbindungsdetail-
Variante mit geringfügig unterschiedlichem Prüfaufbau betreffen; nicht
bestätigt.

Nicht im Chat (chat-3) besprochen — Rolle dieser Versuchsreihe im
R2-Gesamtkonzept unklar, siehe R2-COMMON-OPQ-008.
