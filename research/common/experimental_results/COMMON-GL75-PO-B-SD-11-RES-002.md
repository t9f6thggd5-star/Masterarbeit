---
result_id: COMMON-GL75-PO-B-SD-11-RES-002
scope:
  connection: COMMON
  material: GL75
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "PO-B-SD-11-*"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Push-Out-Versuch derselben Prüfkörper
  wie COMMON-GL75-PO-B-SD-11-RES-001, nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit)
  und K_e (Wiederbelastungssteifigkeit) werden je Prüfkörper zweimal
  unabhängig ausgewertet: einmal aus den Wegaufnehmern VL+HL ("LINKS"),
  einmal aus VR+HR ("RECHTS") — zwei getrennte Messstellenpaare am
  selben Prüfkörper, nicht zwei unterschiedliche Prüfkörper. Einzelverbindungsmittel-Basisversuch (1×1 Stabdübel), scope COMMON.
result:
  quantity: Anfangssteifigkeit K_ser, LINKS, Mittelwert aus 3 Prüfkörpern
  value: 13.010
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"), alle in kN/mm:

| Prüfkörper | K_ser LINKS | K_ser RECHTS | K_e LINKS | K_e RECHTS |
|---|---|---|---|---|
| PO-B-SD-11-1 | 11.61 | 11.36 | 19.82 | 22.36 |
| PO-B-SD-11-2 | 12.76 | 12.94 | 20.32 | 20.82 |
| PO-B-SD-11-3 | 14.66 | 12.63 | 22.09 | 24.26 |
| **Mittelwert** | **13.010** | **12.311** | **20.745** | **22.482** |

Nicht weiter interpretiert.
