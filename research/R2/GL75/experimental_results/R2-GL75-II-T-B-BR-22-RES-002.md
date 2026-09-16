---
result_id: R2-GL75-II-T-B-BR-22-RES-002
scope:
  connection: R2
  material: GL75
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers übernommen: `R2/COMMON/
  calculations/2026-06_05_Auswertung_Steifigkeiten_Bonded-inRods.xlsx`,
  Blatt "Überblick" (Zeilen "II-T-B-BR-22-1/2/3"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Zugversuch derselben Prüfkörper wie
  R2-GL75-II-T-B-BR-22-RES-001 (2×2-Anordnung, eingeklebte
  Gewindestangen), nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit,
  aus der Erstbelastung zwischen 0,1·F_est und 0,4·F_est) und K_e
  (Wiederbelastungssteifigkeit, aus dem Wiederbelastungsast) werden je
  Prüfkörper zweimal unabhängig ausgewertet: einmal aus den
  Wegaufnehmern 03+04 ("oben"), einmal aus den Wegaufnehmern 01+02
  ("unten") — zwei getrennte Messstellenpaare am selben Prüfkörper,
  nicht zwei unterschiedliche Prüfkörper. Quelle: gleichnamiges
  Einzelblatt je Prüfkörper derselben Excel-Datei, Spaltenbeschriftung
  "Auswertung Steifigkeit nach DIN EN 26891".
result:
  quantity: Anfangssteifigkeit K_ser, oben, Mittelwert aus 3 Prüfkörpern
  value: 742.347
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"):

| Prüfkörper | K_ser oben | K_ser unten | K_e oben | K_e unten | K_e/K_ser oben [%] | K_e/K_ser unten [%] |
|---|---|---|---|---|---|---|
| II-T-B-BR-22-1 | 1141,01 | 1020,91 | 1197,09 | 1110,96 | 104,91 | 108,82 |
| II-T-B-BR-22-2 | 601,59 | 2554,30 | 560,28 | 2454,54 | 93,13 | 96,09 |
| II-T-B-BR-22-3 | 484,44 | 914,73 | 557,86 | 997,71 | 115,16 | 109,07 |
| **Mittelwert** | **742,347** | **1496,644** | **771,739** | **1521,070** | — | — |

Alle Werte in kN/mm.

**Deutlich größere Streuung als bei der 11er-Serie**
(R2-GL75-II-T-B-BR-11-RES-002), insbesondere bei "unten": Prüfkörper 2
weist mit 2554,30 kN/mm (K_ser unten) einen mehr als 4-fach höheren Wert
auf als "oben" (601,59 kN/mm) — Verhältnis oben/unten nur 23,55 % (K_ser)
bzw. 22,83 % (K_e), der mit Abstand größte Ausreißer in der gesamten
Auswertung. Bei n=3 wird der Mittelwert deshalb ausdrücklich nicht als
charakteristischer/typischer Wert dargestellt (CLAUDE.md Abschnitt 15).

Nicht weiter interpretiert (kein eigener INTERPRETATION- oder
OPEN_QUESTION-Eintrag) — die Ursache der großen Streuung, insbesondere
des Ausreißers bei Prüfkörper 2, ist ungeklärt und wird hier bewusst
nicht geraten (CLAUDE.md Abschnitt 4). Siehe
R2-GL75-II-T-B-BR-22-RES-001 für die zugehörige Höchstzugkraft F_max
derselben Prüfkörperserie.
