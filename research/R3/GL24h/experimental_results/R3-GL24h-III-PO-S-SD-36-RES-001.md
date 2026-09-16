---
result_id: R3-GL24h-III-PO-S-SD-36-RES-001
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "III-PO-S-SD-36-1/2/3", Spalte "Fmax,SF [kN]").
n: 3
method: >
  Push-Out-Versuch, Prüfkörperserie "III-PO-S-SD-36". Höchstlast pro Scherfuge
  (Fmax,SF = Fmax,ges / 2 — Prüfkörper mit zwei Scherfugen, Wert direkt
  aus der Auswertungsdatei übernommen, nicht selbst nachgerechnet). Erster Eintrag für R3 in dieser Kategorie (vorher keine Versuchsergebnisse dokumentiert).
result:
  quantity: Höchstlast F_max pro Scherfuge (Mittelwert aus 3 Prüfkörpern)
  value: 56.547
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Fmax,SF, Blatt "Überblick"):

| Prüfkörper | Fmax,SF [kN] |
|---|---|
| III-PO-S-SD-36-1 | 35.525 |
| III-PO-S-SD-36-2 | 65.420 |
| III-PO-S-SD-36-3 | 68.695 |
| **Mittelwert** | **56.547** |

**Prüfkörper 1 weicht stark ab** (35,525 kN vs. 65,42/68,695 kN bei PK2/3 — weniger als halb so groß) und ist in der Auswertungsdatei als 'entfällt' markiert (Stand der Versuchsdurchführung), die zugehörige Steifigkeit ist dort als 'nv' (nicht verwertbar) vermerkt (siehe R3-GL24h-III-PO-S-SD-36-RES-002). Der Nutzer hat am 2026-09-16 bestätigt, dass der Fmax-Wert trotzdem dokumentiert werden soll. **Nicht geklärt, warum PK1 'entfällt' markiert ist** (Prüfabbruch, Fehlmessung o.ä.) — bewusst nicht geraten (CLAUDE.md Abschnitt 4). Der Mittelwert (56,547 kN) schließt PK1 mit ein; ob das sachlich richtig ist, ist ungeklärt, da PK1 möglicherweise einen anderen (ungültigen) Versagensmechanismus zeigt.
