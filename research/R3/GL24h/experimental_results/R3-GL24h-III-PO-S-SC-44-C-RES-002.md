---
result_id: R3-GL24h-III-PO-S-SC-44-C-RES-002
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "III-PO-S-SC-44-C-*"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Push-Out-Versuch derselben Prüfkörper
  wie R3-GL24h-III-PO-S-SC-44-C-RES-001, nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit)
  und K_e (Wiederbelastungssteifigkeit) werden je Prüfkörper zweimal
  unabhängig ausgewertet: einmal aus den Wegaufnehmern VL+HL ("LINKS"),
  einmal aus VR+HR ("RECHTS") — zwei getrennte Messstellenpaare am
  selben Prüfkörper, nicht zwei unterschiedliche Prüfkörper.
result:
  quantity: Anfangssteifigkeit K_ser, LINKS, Mittelwert aus 3 Prüfkörpern
  value: 193.768
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"), alle in kN/mm:

| Prüfkörper | K_ser LINKS | K_ser RECHTS | K_e LINKS | K_e RECHTS |
|---|---|---|---|---|
| III-PO-S-SC-44-C-1 | 225.85 | 273.18 | 458.86 | 563.49 |
| III-PO-S-SC-44-C-2 | 156.57 | 161.87 | 428.93 | 431.07 |
| III-PO-S-SC-44-C-3 | 198.89 | 243.31 | 415.00 | 483.96 |
| **Mittelwert** | **193.768** | **226.121** | **434.595** | **492.841** |

Deutliche Streuung zwischen den Prüfkörpern (K_ser LINKS: 156,6–225,9 kN/mm) — nicht weiter interpretiert.

**Update (2026-09-22, R3-GL24h-DEC-012):** Die obige Beschreibung
("zwei getrennte Messstellenpaare am selben Prüfkörper") ist überholt —
LINKS und RECHTS sind laut Nutzerbestätigung zwei unabhängige
Verbindungen. Gepoolter Mittelwert (n=6): siehe
R3-GL24h-III-PO-S-SC-44-C-RES-003 (209,945 kN/mm).

**Update (2026-09-22, R3-GL24h-DEC-013):** RES-003 ist seinerseits um
Faktor 2 zu hoch (ungeteilte statt scherfugenbezogener Kraft, siehe
DEC-013) und wurde durch R3-GL24h-III-PO-S-SC-44-C-RES-004
(104,973 kN/mm) ersetzt. Die K_ser-Rohwerte in der Tabelle oben sind
ebenfalls als ungeteilt (Gesamtkraft) zu lesen.
