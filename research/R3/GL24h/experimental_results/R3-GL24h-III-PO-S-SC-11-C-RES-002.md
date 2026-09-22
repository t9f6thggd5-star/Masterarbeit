---
result_id: R3-GL24h-III-PO-S-SC-11-C-RES-002
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "III-PO-S-SC-11-C-*"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Push-Out-Versuch derselben Prüfkörper
  wie R3-GL24h-III-PO-S-SC-11-C-RES-001, nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit)
  und K_e (Wiederbelastungssteifigkeit) werden je Prüfkörper zweimal
  unabhängig ausgewertet: einmal aus den Wegaufnehmern VL+HL ("LINKS"),
  einmal aus VR+HR ("RECHTS") — zwei getrennte Messstellenpaare am
  selben Prüfkörper, nicht zwei unterschiedliche Prüfkörper.
result:
  quantity: Anfangssteifigkeit K_ser, LINKS, Mittelwert aus 3 Prüfkörpern
  value: 18.228
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"), alle in kN/mm:

| Prüfkörper | K_ser LINKS | K_ser RECHTS | K_e LINKS | K_e RECHTS |
|---|---|---|---|---|
| III-PO-S-SC-11-C-1 | 20.71 | 19.42 | 50.28 | 49.21 |
| III-PO-S-SC-11-C-2 | 16.21 | 13.57 | 38.05 | 35.52 |
| III-PO-S-SC-11-C-3 | 17.76 | 15.18 | 41.11 | 37.84 |
| **Mittelwert** | **18.228** | **16.059** | **43.143** | **40.859** |

Nicht weiter interpretiert.

**Update (2026-09-22, R3-GL24h-DEC-012):** Die obige Beschreibung
("zwei getrennte Messstellenpaare am selben Prüfkörper") ist überholt —
LINKS und RECHTS sind laut Nutzerbestätigung zwei unabhängige
Verbindungen. Gepoolter Mittelwert (n=6): siehe
R3-GL24h-III-PO-S-SC-11-C-RES-003 (17,142 kN/mm).

**Update (2026-09-22, R3-GL24h-DEC-013):** RES-003 ist seinerseits um
Faktor 2 zu hoch (ungeteilte statt scherfugenbezogener Kraft, siehe
DEC-013) und wurde durch R3-GL24h-III-PO-S-SC-11-C-RES-004
(8,571 kN/mm) ersetzt. Die K_ser-Rohwerte in der Tabelle oben sind
ebenfalls als ungeteilt (Gesamtkraft) zu lesen.
