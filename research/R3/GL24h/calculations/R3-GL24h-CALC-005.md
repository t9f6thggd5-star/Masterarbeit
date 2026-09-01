---
calculation_id: R3-GL24h-CALC-005
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions:
method: >
  Kombinierte/vollständige Zugpfad-Steifigkeit ("sleeve"-Pfad), als vom
  Forschenden angegebener Arbeitswert bezeichnet ("user-specified working
  value") — genaue Kombinationsformel aus den Einzelsteifigkeiten
  (Gewindestange, Holzlasche, ASSY) im Ursprungsmaterial nicht im Detail
  überliefert, siehe Hinweis unten.
equations:
result:
  quantity: Vollständige Zugpfad-Steifigkeit (sleeve)
  value: 27.09
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl.
  Holzlaschen.xlsx, Sheet "VSP GL24h ohne Druckkontakt" Zelle C17
  (27,093186160762205 ≈ 27,09, Zellwert per openpyxl verifiziert); Stand
  August 2026 trotz Dateiname vom 08.02.2026. Frühere Referenz laut
  chat-1/SOURCES.md: Zelle P160 in Sheet "Rahmenecke GL24h SD" bzw.
  "...SD G1-J30" — in der aktuellen Tabelle nicht mehr unter P160 zu
  finden (Sheet wurde vermutlich seither umstrukturiert/umbenannt).
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-1, KNOWLEDGE.md ("c_t,sleeve=27.09 kN/mm").

**Nachvollziehbarkeit:** die genaue Kombination aus c_t (R3-GL24h-CALC-004),
c_H,eff (R3-GL24h-CALC-001) und der ASSY-Steifigkeit (R3-GL24h-CALC-003)
zu diesem einen Wert ist in den übernommenen Chat-Dateien nicht im Detail
nachvollzogen — chat-1/OPEN_QUESTIONS.md hält selbst fest ("Correct
VDI-style load-fraction definition for this nonstandard timber/ASSY path"
ist unresolved, siehe R3-GL24h-OPQ zu diesem Themenkomplex, folgt in der
nächsten Charge). Als Endergebnis übernommen, nicht eigenständig
nachgerechnet.
