---
result_id: R3-GL24h-III-PO-S-SD-36-RES-002
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "III-PO-S-SD-36-*"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 2
method: >
  Steifigkeitsauswertung aus dem Push-Out-Versuch derselben Prüfkörper
  wie R3-GL24h-III-PO-S-SD-36-RES-001, nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit)
  und K_e (Wiederbelastungssteifigkeit) werden je Prüfkörper zweimal
  unabhängig ausgewertet: einmal aus den Wegaufnehmern VL+HL ("LINKS"),
  einmal aus VR+HR ("RECHTS") — zwei getrennte Messstellenpaare am
  selben Prüfkörper, nicht zwei unterschiedliche Prüfkörper. **Nur n=2** — Prüfkörper 1 ist in der Auswertungsdatei als 'nv' (nicht verwertbar) markiert und wird hier ausgeschlossen (siehe R3-GL24h-III-PO-S-SD-36-RES-001 zum zugehörigen, dort dokumentierten Fmax-Wert von PK1 und zur ungeklärten Ursache).
result:
  quantity: Anfangssteifigkeit K_ser, LINKS, Mittelwert aus 2 Prüfkörpern
  value: 66.381
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"), alle in kN/mm:

| Prüfkörper | K_ser LINKS | K_ser RECHTS | K_e LINKS | K_e RECHTS |
|---|---|---|---|---|
| III-PO-S-SD-36-2 | 63.14 | 47.51 | 155.25 | 135.65 |
| III-PO-S-SD-36-3 | 69.62 | 62.51 | 159.40 | 151.18 |
| **Mittelwert** | **66.381** | **55.009** | **157.325** | **143.418** |

n=2 ist eine sehr kleine Stichprobe; der Mittelwert wird deshalb ausdrücklich nicht als charakteristischer Wert dargestellt (CLAUDE.md Abschnitt 15, sinngemäß auch für n=2 angewendet).
