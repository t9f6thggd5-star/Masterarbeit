---
calculation_id: R1-GL24h-CALC-006
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions:
method: >
  Geometrische Kombination der Schlupfwege beider geneigter
  Anschlussbereiche (Innenwinkel 108°) über den Kosinussatz, als
  Vektor-Relativverschiebung. Ausdrücklich NICHT als Rahmeneckenrotation
  zu interpretieren — siehe R1-GL24h-DEC-009.
equations: >
  Δu_ges = √(u_Gruppe² + u_Gruppe² - 2·u_Gruppe²·cos(108°)) — Excel-Formeln
  "=2*C90^2*COS(BOGENMASS(108))" bzw.
  "=WURZEL(C90^2+C90^2-2*C90^2*COS(BOGENMASS(108)))"
result:
  quantity: Vektorielle Relativverschiebung bei 108°-Öffnungswinkel (Δu_ges) — NICHT die Rahmeneckenrotation
  value: 5.517
  unit: mm
  original_value: 5.516594974413504
  original_unit: mm
source_file: >
  R1/COMMON/calculations/20260208_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Zelle C92 ("delta u_ges", Norm-Vermerk "Umrechnung
  mit 108° Öffnungswinkel"; per openpyxl mit data_only=True ausgelesen,
  Stand der abgelegten Datei am 2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-2, artifacts/FORMULAS_EXCEL.md ("Full law-of-cosines
expression", dort explizit als "[Superseded for direct frame-rotation
calculation]" gekennzeichnet) und unabhängig gegen die reale Excel-Datei
verifiziert (Zelle C92 verwendet als Eingangswert u = u_Gruppe aus
R1-GL24h-CALC-005, nicht die Einzelanteile u_0/u_el,S getrennt).

**Wichtiger Status-Hinweis:** Dieser Wert ist mathematisch eine gültige
Vektor-Distanz zwischen den relativen Endpunkten der beiden geneigten
Schlupfrichtungen, aber laut R1-GL24h-DEC-009 nicht automatisch mit der
Rahmeneckenrotation φ gleichzusetzen. Die tatsächliche kinematische
Herleitung von φ steht noch aus — siehe R1-GL24h-HYP-001 und
R1-GL24h-OPQ-002/003. Kein Nachfolge-Eintrag (`superseded_by`) existiert
bislang, da die korrekte Rotationsberechnung noch nicht hergeleitet wurde.
