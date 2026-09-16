---
result_id: R2-GL24h-II-T-S-BR-11-RES-002
scope:
  connection: R2
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers übernommen: `R2/COMMON/
  calculations/2026-06_05_Auswertung_Steifigkeiten_Bonded-inRods.xlsx`,
  Blatt "Überblick" (Zeilen "II-T-S-BR-11-1/2/3"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Zugversuch derselben Prüfkörper wie
  R2-GL24h-II-T-S-BR-11-RES-001 (1×1-Anordnung, eingeklebte
  Gewindestange), nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
  Entlastung auf 0,1·F_est, Wiederbelastung). K_ser (Anfangssteifigkeit,
  aus der Erstbelastung zwischen 0,1·F_est und 0,4·F_est) und K_e
  (Wiederbelastungssteifigkeit, aus dem Wiederbelastungsast) werden je
  Prüfkörper zweimal unabhängig ausgewertet: einmal aus den
  Wegaufnehmern 03+04 ("oben"), einmal aus den Wegaufnehmern 01+02
  ("unten"). Quelle: Einzelblatt "II-T-S-BR-11-1" (u. a.) derselben
  Excel-Datei, Spaltenbeschriftung "Auswertung Steifigkeit nach DIN EN
  26891". **Korrektur (siehe Update unten, 2026-09-16): "oben"/"unten"
  sind zwei separat eingeklebte, geometrisch identische Klebefugen an
  den beiden Enden desselben Prüfkörpers — nicht zwei Messstellenpaare
  derselben Klebefuge.**
result:
  quantity: Anfangssteifigkeit K_ser, oben, Mittelwert aus 3 Prüfkörpern
  value: 205.360
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"):

| Prüfkörper | K_ser oben | K_ser unten | K_e oben | K_e unten | K_e/K_ser oben [%] | K_e/K_ser unten [%] |
|---|---|---|---|---|---|---|
| II-T-S-BR-11-1 | 229,36 | 200,69 | 247,52 | 204,58 | 107,92 | 101,94 |
| II-T-S-BR-11-2 | 178,96 | 202,42 | 187,64 | 218,74 | 104,85 | 108,06 |
| II-T-S-BR-11-3 | 207,76 | 200,63 | 242,17 | 203,47 | 116,57 | 101,42 |
| **Mittelwert** | **205,360** | **201,246** | **225,777** | **208,932** | — | — |

Alle Werte in kN/mm. Verhältnis oben/unten liegt für diese Serie relativ
nah an 100 % (K_ser: 88–120 %, K_e: 86–121 % je Prüfkörper) — im
Unterschied zur 22er-Serie (siehe R2-GL24h-II-T-S-BR-22-RES-002), wo
diese Streuung deutlich größer ist.

Nicht weiter interpretiert (kein eigener INTERPRETATION-Eintrag). Siehe
R2-GL24h-II-T-S-BR-11-RES-001 für die zugehörige Höchstzugkraft F_max
derselben Prüfkörperserie.

**Update (2026-09-16, Korrektur des Versuchsaufbaus, vom Nutzer im Chat
mitgeteilt):** "Oben" und "unten" sind entgegen der ursprünglichen
Formulierung oben NICHT zwei Messstellenpaare an derselben Klebefuge,
sondern zwei separate, geometrisch identische Klebefugen an den beiden
Enden desselben Prüfkörpers (je 1 Gewindestange oben und 1 unten
eingeklebt), die durch gleichmäßiges Ziehen an beiden Enden
gleichzeitig, aber unabhängig geprüft wurden. "Oben" (Wegaufnehmer
03+04) und "unten" (Wegaufnehmer 01+02) sind damit zwei unabhängige
Realisierungen derselben Verbindungsart (Einzelstange), nicht zwei
Messungen derselben physischen Klebefuge. Für BR-11 wird diese Poolung
(anders als für BR-22, siehe R2-GL24h-II-T-S-BR-22-RES-003) aktuell
nicht weiterverfolgt — der Nutzer hat entschieden, für die
Zugseiten-Steifigkeitskette vorerst ausschließlich auf die
BR-22-Ergebnisse zurückzugreifen, da diese bereits alle vier Stangen der
Verbindung abdecken.

**Korrektur (2026-09-16, vom Nutzer im Chat mitgeteilt):** Der obige
Update-Absatz nannte fälschlich denselben Holzquerschnitt (160×240 mm)
wie bei BR-22 (R2-GL24h-II-T-S-BR-22-RES-002). Tatsächlich ist die
BR-11-Einzelstange mittig in einen deutlich kleineren Querschnitt
80×80 mm eingeklebt — ein eigener, kleinerer Prüfkörperquerschnitt, nicht
derselbe wie bei der 2×2-Gruppe BR-22 (160×240 mm). Diese Korrektur
betrifft nur die Geometriebeschreibung, nicht die gemessenen
Steifigkeitswerte selbst.
