---
result_id: COMMON-GL24h-PO-S-SD-11-RES-001
scope:
  connection: COMMON
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "PO-S-SD-11-1/2/3", Spalte "Fmax,SF [kN]").
n: 3
method: >
  Push-Out-Versuch, Prüfkörperserie "PO-S-SD-11". Höchstlast pro Scherfuge
  (Fmax,SF = Fmax,ges / 2 — Prüfkörper mit zwei Scherfugen, Wert direkt
  aus der Auswertungsdatei übernommen, nicht selbst nachgerechnet). Einzelverbindungsmittel-Basisversuch (1×1 Stabdübel), scope COMMON: dient als Referenz für die Gruppeneffekt-Auswertung von R2 (II-PO-S-SD-34) und R3 (III-PO-S-SD-36), nicht einer einzelnen Rahmenecke zugeordnet (Zuordnung vom Nutzer am 2026-09-16 bestätigt).
result:
  quantity: Höchstlast F_max pro Scherfuge (Mittelwert aus 3 Prüfkörpern)
  value: 9.093
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Fmax,SF, Blatt "Überblick"):

| Prüfkörper | Fmax,SF [kN] |
|---|---|
| PO-S-SD-11-1 | 10.120 |
| PO-S-SD-11-2 | 8.740 |
| PO-S-SD-11-3 | 8.420 |
| **Mittelwert** | **9.093** |

Nicht weiter interpretiert. Vergleich Gruppen-/Einzelwert (nicht normiert) siehe R2-GL24h-II-PO-S-SD-34-RES-001 (F_max/Scherfuge 68,061 kN) und R3-GL24h-III-PO-S-SD-36-RES-001 — eine formale Gruppeneffizienz-Auswertung (n_ef) ist bewusst noch nicht angelegt (siehe Hinweis in den current_state.md-Dateien).
