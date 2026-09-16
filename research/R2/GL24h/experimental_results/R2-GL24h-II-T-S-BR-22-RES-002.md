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
  ("unten"). Quelle: gleichnamiges Einzelblatt je Prüfkörper derselben
  Excel-Datei, Spaltenbeschriftung "Auswertung Steifigkeit nach DIN EN
  26891". **Korrektur (siehe Update unten, 2026-09-16): "oben"/"unten"
  sind zwei separat eingeklebte, geometrisch identische 2×2-M16-
  Stangengruppen an den beiden Enden desselben Prüfkörpers — nicht zwei
  Messstellenpaare derselben Stangengruppe.**
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

**Update (2026-09-16, Korrektur des Versuchsaufbaus, vom Nutzer im Chat
mitgeteilt):** "Oben" und "unten" sind entgegen der ursprünglichen
Formulierung oben NICHT zwei Messstellenpaare an derselben Klebefuge/
Stangengruppe, sondern zwei separate, geometrisch identische
2×2-M16-Stangengruppen an den beiden Enden desselben Prüfkörpers (je 4
Gewindestangen oben und 4 unten in denselben Holzquerschnitt
160×240 mm eingeklebt), die durch gleichmäßiges Ziehen an beiden Enden
gleichzeitig, aber unabhängig geprüft wurden. "Oben" (Wegaufnehmer
03+04) und "unten" (Wegaufnehmer 01+02) sind damit zwei unabhängige
Realisierungen derselben Verbindungsart (2×2-Gruppe), nicht zwei
Messungen derselben physischen Stangengruppe. Da beide Positionen mit
gleicher Prüfkörperzahl (n=3 je Position) vorliegen und dieselbe
Verbindungsart abbilden, werden sie in R2-GL24h-II-T-S-BR-22-RES-003 zu
einem gepoolten n=6-Mittelwert zusammengeführt (arithmetisches Mittel
der beiden Teilmittelwerte ist bei gleicher Gruppengröße identisch zum
Mittelwert aller 6 Einzelwerte). Die oben dokumentierte große Streuung
zwischen den Prüfkörpern bleibt davon unberührt und wird in
RES-003 nicht kleingerechnet.
