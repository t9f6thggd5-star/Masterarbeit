---
result_id: R2-GL24h-II-T-S-BR-22-RES-002
scope:
  connection: R2
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers übernommen: `R2/COMMON/
  calculations/2026-06_05_Auswertung_Steifigkeiten_Bonded-inRods.xlsx`,
  Blatt "Überblick" (Zeilen "II-T-S-BR-22-1/2/3"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Zugversuch derselben Prüfkörper wie
  R2-GL24h-II-T-S-BR-22-RES-001 (2×2-Anordnung, eingeklebte
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
  value: 840.871
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"):

| Prüfkörper | K_ser oben | K_ser unten | K_e oben | K_e unten | K_e/K_ser oben [%] | K_e/K_ser unten [%] |
|---|---|---|---|---|---|---|
| II-T-S-BR-22-1 | 418,71 | 1133,87 | 455,13 | 910,26 | 108,70 | 80,28 |
| II-T-S-BR-22-2 | 663,91 | 609,23 | 715,89 | 585,23 | 107,83 | 96,06 |
| II-T-S-BR-22-3 | 1440,00 | 909,47 | 3032,51 | 854,46 | 210,59 | 93,95 |
| **Mittelwert** | **840,871** | **884,191** | **1401,176** | **783,318** | — | — |

Alle Werte in kN/mm.

**Deutlich größere Streuung als bei der 11er-Serie**
(R2-GL24h-II-T-S-BR-11-RES-002): K_ser oben schwankt zwischen 418,71
und 1440,00 kN/mm (Faktor ~3,4), K_e oben zwischen 455,13 und
3032,51 kN/mm (Faktor ~6,7). Das "Verhältnis oben/unten" ist für
Prüfkörper 1 und 3 deutlich von 100 % entfernt (37 % bzw. 158 % für
K_ser, 50 % bzw. 355 % für K_e). Bei n=3 wird dieser Mittelwert deshalb
ausdrücklich nicht als charakteristischer/typischer Wert dargestellt
(CLAUDE.md Abschnitt 15) — die Einzelwerte streuen zu stark, um sie ohne
Weiteres als eine homogene Stichprobe zu behandeln.

Nicht weiter interpretiert (kein eigener INTERPRETATION- oder
OPEN_QUESTION-Eintrag) — die Ursache der großen Streuung (Prüfkörper-
Varianz, Messmethodik, Auswertungsfenster o. ä.) ist ungeklärt und wird
hier bewusst nicht geraten (CLAUDE.md Abschnitt 4). Siehe
R2-GL24h-II-T-S-BR-22-RES-001 für die zugehörige Höchstzugkraft F_max
derselben Prüfkörperserie.
