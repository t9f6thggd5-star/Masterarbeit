---
decision_id: R2-COMMON-DEC-003
scope:
  connection: R2
  material: COMMON
type: DECISION
question: >
  Welcher Wert wird künftig als Anfangssteifigkeit (K_ser) je
  Stangengruppe (BR-11/BR-22, beide Materialien GL24h/GL75) für die
  Weiterverwendung in den Steifigkeitsketten angesetzt — ein
  eigenständig (je nach Bedarfsfall neu) hergeleiteter gepoolter
  oben+unten-Mittelwert, oder der in der Auswertungsdatei bereits
  vorliegende Mittelwert?
decision: >
  Es werden durchgängig die in `R2/COMMON/calculations/2026-06_05_
  Auswertung_Steifigkeiten_Bonded-inRods.xlsx`, Blatt "Überblick",
  Zellen B94:B97 ("Mean Anfangssteifigkeit") bereits vorliegenden Werte
  als Anfangssteifigkeit je Gruppe angesetzt: `II-T-B-BR-11 =
  226,596 kN/mm` (B94), `II-T-B-BR-22 = 1.119,496 kN/mm` (B95),
  `II-T-S-BR-11 = 203,303 kN/mm` (B96), `II-T-S-BR-22 = 862,531 kN/mm`
  (B97).
reason: >
  Nutzerentscheidung (Chat, 2026-09-16). Die B94:B97-Werte sind
  rechnerisch identisch zur unabhängig hergeleiteten Poolung
  (arithmetisches Mittel der "oben"- und "unten"-Teilmittelwerte, bei
  gleicher Stichprobengröße n=3 je Position rechnerisch deckungsgleich
  mit dem Mittelwert aller 6 Einzelwerte — verifiziert für
  II-T-S-BR-22 in R2-GL24h-II-T-S-BR-22-RES-003). Direkte Übernahme aus
  der Datei vermeidet Doppelarbeit und hält die Wertkette näher an der
  Primärquelle.
alternatives_considered: >
  Eigenständige Poolung je Bedarfsfall neu berechnen (wie zunächst für
  II-T-S-BR-22 gemacht, siehe RES-003 dort) — verworfen zugunsten der
  direkten Übernahme aus B94:B97.
date: "2026-09-16"
---

Gilt materialunabhängig (R2/COMMON) und für beide Stangengruppen-
Konfigurationen (1×1 und 2×2), da die Zellen B94:B97 alle vier
Kombinationen (GL24h/GL75 × BR-11/BR-22) einheitlich abdecken. Betrifft
die folgenden Einträge:

- `R2-GL24h-II-T-S-BR-11-RES-003` (203,303 kN/mm, = B96)
- `R2-GL24h-II-T-S-BR-22-RES-003` (862,531 kN/mm, = B97, bereits vor
  dieser Entscheidung unabhängig hergeleitet und jetzt zusätzlich direkt
  auf B97 rückgeführt)
- `R2-GL75-II-T-B-BR-11-RES-003` (226,596 kN/mm, = B94)
- `R2-GL75-II-T-B-BR-22-RES-003` (1.119,496 kN/mm, = B95)

Für GL75 existiert aktuell noch keine Zugseiten-Steifigkeitskette im
Excel (R2-GL75-OPQ-001), diese Entscheidung legt aber bereits fest,
welcher Wert dafür anzusetzen wäre, sobald eine solche Kette aufgestellt
wird.
