---
result_id: R2-GL24h-II-PO-S-SD-34-RES-002
scope:
  connection: R2
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "II-PO-S-SD-34-*"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Push-Out-Versuch derselben Prüfkörper
  wie R2-GL24h-II-PO-S-SD-34-RES-001, nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit)
  und K_e (Wiederbelastungssteifigkeit) werden je Prüfkörper zweimal
  unabhängig ausgewertet: einmal aus den Wegaufnehmern VL+HL ("LINKS"),
  einmal aus VR+HR ("RECHTS") — zwei getrennte Messstellenpaare am
  selben Prüfkörper, nicht zwei unterschiedliche Prüfkörper. Ergänzung zum bereits bestehenden F_max-Eintrag R2-GL24h-II-PO-S-SD-34-RES-001 (dieselben Prüfkörper) — Quelle diesmal die separate Steifigkeitsauswertung 'Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx' (common/general/), nicht die R2-Berechnungs-Excel.
result:
  quantity: Anfangssteifigkeit K_ser, LINKS, Mittelwert aus 3 Prüfkörpern
  value: 44.617
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"), alle in kN/mm:

| Prüfkörper | K_ser LINKS | K_ser RECHTS | K_e LINKS | K_e RECHTS |
|---|---|---|---|---|
| II-PO-S-SD-34-1 | 38.89 | 42.15 | 93.84 | 98.62 |
| II-PO-S-SD-34-2 | 34.08 | 56.54 | 93.21 | 115.78 |
| II-PO-S-SD-34-3 | 60.88 | 59.19 | 122.29 | 116.91 |
| **Mittelwert** | **44.617** | **52.629** | **103.114** | **110.436** |

Nicht weiter interpretiert.
