---
result_id: R3-GL24h-III-PO-S-WD-36-RES-002
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "III-PO-S-WD-36-*"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Push-Out-Versuch derselben Prüfkörper
  wie R3-GL24h-III-PO-S-WD-36-RES-001, nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit)
  und K_e (Wiederbelastungssteifigkeit) werden je Prüfkörper zweimal
  unabhängig ausgewertet: einmal aus den Wegaufnehmern VL+HL ("LINKS"),
  einmal aus VR+HR ("RECHTS") — zwei getrennte Messstellenpaare am
  selben Prüfkörper, nicht zwei unterschiedliche Prüfkörper.
result:
  quantity: Anfangssteifigkeit K_ser, LINKS, Mittelwert aus 3 Prüfkörpern
  value: 75.803
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"), alle in kN/mm:

| Prüfkörper | K_ser LINKS | K_ser RECHTS | K_e LINKS | K_e RECHTS |
|---|---|---|---|---|
| III-PO-S-WD-36-1 | 67.87 | 65.90 | 130.27 | 124.36 |
| III-PO-S-WD-36-2 | 74.56 | 75.63 | 132.98 | 132.09 |
| III-PO-S-WD-36-3 | 84.97 | 76.44 | 139.40 | 137.83 |
| **Mittelwert** | **75.803** | **72.656** | **134.215** | **131.428** |

Nicht weiter interpretiert.

**Update (2026-09-22, R3-GL24h-DEC-012):** Die obige Beschreibung
("zwei getrennte Messstellenpaare am selben Prüfkörper") ist überholt —
LINKS und RECHTS sind laut Nutzerbestätigung zwei unabhängige
Verbindungen. Gepoolter Mittelwert (n=6): siehe
R3-GL24h-III-PO-S-WD-36-RES-003 (74,228 kN/mm).

**Update (2026-09-22, R3-GL24h-DEC-013):** RES-003 ist seinerseits um
Faktor 2 zu hoch (ungeteilte statt scherfugenbezogener Kraft, siehe
DEC-013) und wurde durch R3-GL24h-III-PO-S-WD-36-RES-004
(37,114 kN/mm) ersetzt. Die K_ser-Rohwerte in der Tabelle oben sind
ebenfalls als ungeteilt (Gesamtkraft) zu lesen.
