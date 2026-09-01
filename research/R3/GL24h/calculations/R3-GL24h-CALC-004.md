---
calculation_id: R3-GL24h-CALC-004
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
  Axiale Dehnsteifigkeit der Gewindestange (Zug). Herleitungsdetails
  (Querschnitt, Länge, E-Modul Stahl) sind im Ursprungsmaterial nicht
  überliefert — siehe Hinweis unten.
equations:
result:
  quantity: Axiale Steifigkeit der Gewindestange
  value: 49.59
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl.
  Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" Zelle H71 bzw. Sheet
  "Rahmenecke GL24h HD" Zelle I69 (beide 49,59036144578313 ≈ 49,59,
  Zellwert per openpyxl verifiziert); Stand August 2026 trotz Dateiname
  vom 08.02.2026
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-1, KNOWLEDGE.md ("c_t=49.59 kN/mm").

**Nachvollziehbarkeit:** die konkrete Herleitung (Gewindestangen-
Querschnitt, freie Länge, Stahl-E-Modul) ist in den übernommenen
Chat-Dateien nicht enthalten — nur das Endergebnis ist überliefert.
Als Endergebnis übernommen, nicht eigenständig nachgerechnet.
