---
calculation_id: R3-GL24h-CALC-003
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: ETA-11-0190-2026
  literature:
  experimental_data:
  assumptions:
method: >
  Summe der axialen Einzelschrauben-Steifigkeiten der ASSY-Schraubengruppe
  (32 Schrauben, Layout 8 Reihen in Lastrichtung × 4 nebeneinander).
  Herleitung der Einzelschrauben-Steifigkeit selbst (z. B. nach
  ETA-11/0190) ist im Ursprungsmaterial nicht im Detail nachvollzogen —
  siehe Hinweis unten.
equations: "c_ax = Σ c_ax,Einzelschraube (32 Schrauben)"
result:
  quantity: Axiale Steifigkeit der ASSY-Schraubengruppe
  value: 199.1466
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl.
  Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" Zelle H30 bzw. Sheet
  "Rahmenecke GL24h HD" Zelle I29 (beide 199,14614238271503 ≈ 199,1466,
  Zellwert per openpyxl verifiziert); Stand August 2026 trotz Dateiname
  vom 08.02.2026
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-1, KNOWLEDGE.md ("ASSY: 32 screws/group, 8×4 layout,
updated c_ax=199.1466 kN/mm, derived as sum of single-screw axial
stiffnesses").

**Wichtiger Hinweis zur Versionsgeschichte:** chat-1 nennt explizit einen
früheren Wert `c_ax = 191,11 kN/mm`, der durch diesen aktualisierten Wert
(199,1466 kN/mm) ersetzt wurde. Der frühere Wert wurde im Ursprungsmaterial
nie als eigener `research/`-Eintrag geführt, daher existiert kein
Ziel-Eintrag für ein `superseded_by`-Feld — die Korrektur wird hier nur
dokumentiert (analog zu R3-GL24h-DEC-006 für die Plattenlängen-Korrektur).

**Nachvollziehbarkeit:** die genaue Herleitung der Einzelschrauben-
Axialsteifigkeit (vermutlich nach ETA-11/0190, Gleichungen 4.38–4.43 laut
chat-1/SOURCES.md) ist in den übernommenen Chat-Dateien nicht im Detail
enthalten — nur das Endergebnis und die Methode ("Summe der
Einzelschrauben-Steifigkeiten") sind überliefert. Diese Berechnung wurde
deshalb als Endergebnis übernommen, nicht eigenständig nachgerechnet.
