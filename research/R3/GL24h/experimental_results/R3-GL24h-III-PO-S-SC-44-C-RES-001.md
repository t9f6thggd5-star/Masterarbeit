---
result_id: R3-GL24h-III-PO-S-SC-44-C-RES-001
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "III-PO-S-SC-44-C-1/2/3", Spalte "Fmax,SF [kN]").
n: 3
method: >
  Push-Out-Versuch, Prüfkörperserie "III-PO-S-SC-44-C". Höchstlast pro Scherfuge
  (Fmax,SF = Fmax,ges / 2 — Prüfkörper mit zwei Scherfugen, Wert direkt
  aus der Auswertungsdatei übernommen, nicht selbst nachgerechnet). Schraubenverbindung, Lasche an der Stütze (Column), 4×4. Zum Vergleich: die Beam-Variante derselben Anordnung (III-PO-S-SC-44-B) hat nur einen einzigen verwertbaren Prüfkörper (R3-GL24h-III-PO-S-SC-44-B-RES-001, 47,3 kN) — ein Vergleich Beam/Column ist für die 44er-Anordnung deshalb nicht sinnvoll möglich (Scope Isolation, CLAUDE.md Abschnitt 4).
result:
  quantity: Höchstlast F_max pro Scherfuge (Mittelwert aus 3 Prüfkörpern)
  value: 164.527
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Fmax,SF, Blatt "Überblick"):

| Prüfkörper | Fmax,SF [kN] |
|---|---|
| III-PO-S-SC-44-C-1 | 166.455 |
| III-PO-S-SC-44-C-2 | 170.050 |
| III-PO-S-SC-44-C-3 | 157.075 |
| **Mittelwert** | **164.527** |

Nicht weiter interpretiert.
