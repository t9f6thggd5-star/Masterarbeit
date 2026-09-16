---
result_id: R2-GL75-II-T-B-BR-11-RES-002
scope:
  connection: R2
  material: GL75
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers übernommen: `R2/COMMON/
  calculations/2026-06_05_Auswertung_Steifigkeiten_Bonded-inRods.xlsx`,
  Blatt "Überblick" (Zeilen "II-T-B-BR-11-1/2/3"), gegengeprüft gegen die
  gleichnamigen Einzelblätter je Prüfkörper in derselben Datei.
n: 3
method: >
  Steifigkeitsauswertung aus dem Zugversuch derselben Prüfkörper wie
  R2-GL75-II-T-B-BR-11-RES-001 (1×1-Anordnung, eingeklebte
  Gewindestange), nach DIN EN 26891 (Erstbelastung bis 0,4·F_est,
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
  value: 225.442
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Blatt "Überblick"):

| Prüfkörper | K_ser oben | K_ser unten | K_e oben | K_e unten | K_e/K_ser oben [%] | K_e/K_ser unten [%] |
|---|---|---|---|---|---|---|
| II-T-B-BR-11-1 | 236,81 | 228,96 | 247,51 | 222,48 | 104,52 | 97,17 |
| II-T-B-BR-11-2 | 216,88 | 240,84 | 236,60 | 256,32 | 109,09 | 106,43 |
| II-T-B-BR-11-3 | 222,63 | 213,45 | 225,24 | 213,13 | 101,17 | 99,85 |
| **Mittelwert** | **225,442** | **227,751** | **236,452** | **230,644** | — | — |

Alle Werte in kN/mm. Verhältnis oben/unten liegt für diese Serie relativ
nah an 100 % (K_ser: 90–111 %, K_e: 92–111 % je Prüfkörper) — im
Unterschied zur 22er-Serie (siehe R2-GL75-II-T-B-BR-22-RES-002), wo diese
Streuung deutlich größer ist.

Nahezu identisch zum GL24h-Wert derselben Serie (K_ser oben:
205,360 kN/mm, R2-GL24h-II-T-S-BR-11-RES-002) — analog zur bereits für
F_max dokumentierten Beobachtung, dass diese Kenngröße primär vom
Stahl/der Verklebung, nicht vom umgebenden Holzwerkstoff abhängt.

Nicht weiter interpretiert (kein eigener INTERPRETATION-Eintrag). Siehe
R2-GL75-II-T-B-BR-11-RES-001 für die zugehörige Höchstzugkraft F_max
derselben Prüfkörperserie.
