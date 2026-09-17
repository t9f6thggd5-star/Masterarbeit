---
calculation_id: R2-GL24h-CALC-015
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data: R2-GL24h-II-T-S-BR-22-RES-003
  assumptions: R2-COMMON-ASS-003, R2-COMMON-ASS-004
method: >
  Serienschaltung der (teilweise messwertbasierten) Vier-Stangen-Gruppe
  inkl. Querdruckanteil (R2-GL24h-CALC-014) mit dem unveränderten,
  weiterhin rein rechnerischen Schubfeld (R2-GL24h-CALC-003).
equations: Serienfeder (1/c_1 + 1/c_2)^-1.
result:
  quantity: Gesamt-Zugseitensteifigkeit c_T, GL24h (teilweise messwertbasiert)
  value: 50.776
  unit: kN/mm
  original_value: 50776.431
  original_unit: N/mm
source_file: >
  Keine Excel-Datei zugrunde liegend — eigene Nachrechnung auf Basis von
  R2-GL24h-CALC-014 und R2-GL24h-CALC-003.
certainty: CALCULATED
superseded_by: R2-GL24h-CALC-021
---

Ersetzt R2-GL24h-CALC-004 als aktuellen Wert für dieselbe Größe
(Gesamt-Zugseitensteifigkeit `c_T`); CALC-004 bleibt dokumentiert und
ist über dessen `superseded_by`-Feld auf diesen Eintrag verwiesen
(CLAUDE.md Abschnitt 13).

**Rechnung:** `c_T,neu = (1/90,306 + 1/116,0)^-1 = 50,776 kN/mm`
(50.776,431 N/mm), gegenüber dem bisherigen rein rechnerischen Wert
`38,392 kN/mm` (R2-GL24h-CALC-004) eine Erhöhung um ≈32,3 %.

Diese Erhöhung geht ausschließlich auf den Ersatz des Stangengruppen-
Teilwerts durch den BR-22-Messwert zurück (R2-GL24h-CALC-014); das
Schubfeld (CALC-003, 116,0 kN/mm, weiterhin nur auf der Annahme
`G_r,mean=500 N/mm²` basierend, R2-COMMON-ASS-003) ist unverändert und
bleibt vollständig rechnerisch/angenommen — für eine weitere Erhöhung
der Belastbarkeit dieses Werts wäre eine entsprechende Versuchsreihe für
das Schubfeld selbst nötig, die aktuell nicht vorliegt.

Weiterhin offen: Druckseitensteifigkeit `c_C` und vollständiges
Rotationsmodell der Rahmenecke (R2-COMMON-OPQ-006, durch R2-COMMON-DEC-002
freigegeben, aber noch nicht bearbeitet). Kein entsprechender Wert liegt
bisher für GL75 vor (R2-GL75-OPQ-001 — dort existiert noch keine
Zugseiten-Steifigkeitskette, die man mit den analogen GL75-Versuchen
`II-T-B-BR-11/22` speisen könnte).

**Update (2026-09-17):** Durch R2-GL24h-CALC-021 überholt, das denselben
`c_T` mit dem inzwischen verfügbaren ASSY-verstärkten `c_c,90`
(R2-COMMON-CALC-001) statt des hier verwendeten unverstärkten Werts
neu berechnet (`53,300 kN/mm`, `+5,0%` gegenüber diesem Eintrag).
Dieser Eintrag bleibt als der zuletzt gültige Wert MIT unverstärktem
`c_c,90` dokumentiert.
