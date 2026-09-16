---
result_id: R3-GL75-III-PO-B-SC-11-B-RES-002
scope:
  connection: R3
  material: GL75
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "III-PO-B-SC-11-B-*"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Push-Out-Versuch derselben Prüfkörper
  wie R3-GL75-III-PO-B-SC-11-B-RES-001, nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit)
  und K_e (Wiederbelastungssteifigkeit) werden je Prüfkörper zweimal
  unabhängig ausgewertet: einmal aus den Wegaufnehmern VL+HL ("LINKS"),
  einmal aus VR+HR ("RECHTS") — zwei getrennte Messstellenpaare am
  selben Prüfkörper, nicht zwei unterschiedliche Prüfkörper.
result:
  quantity: Anfangssteifigkeit K_ser, LINKS, Mittelwert aus 3 Prüfkörpern
  value: 23.969
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"), alle in kN/mm:

| Prüfkörper | K_ser LINKS | K_ser RECHTS | K_e LINKS | K_e RECHTS |
|---|---|---|---|---|
| III-PO-B-SC-11-B-1 | 26.25 | 21.03 | 66.60 | 39.07 |
| III-PO-B-SC-11-B-2 | 23.31 | 23.10 | 46.83 | 53.69 |
| III-PO-B-SC-11-B-3 | 22.35 | 24.51 | 40.48 | 45.50 |
| **Mittelwert** | **23.969** | **22.880** | **51.304** | **46.086** |

K_e LINKS von PK1 (66,60 kN/mm) deutlich höher als PK2/3 (46,83 / 40,48 kN/mm) — nicht weiter interpretiert.
