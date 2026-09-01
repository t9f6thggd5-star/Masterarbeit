---
calculation_id: R1-GL24h-CALC-002
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Wie R1-GL24h-CALC-001, jedoch mit dem experimentell ermittelten
  Fließmoment M_y,k aus dem Stabdübel-Biegeversuch (Mittelwert) anstelle
  des normativen FprEN-Tabellenwerts.
equations: >
  FprEN 1995-1-1:2024, Gl. 11.14 (Modi a,b,d,f); Modi (a) und (b) sind vom
  Fließmoment unabhängig und identisch zu R1-GL24h-CALC-001.
result:
  quantity: Governierende Johansen-Tragfähigkeit je Scherfuge (Modus d, experimentelles M_y,k)
  value: 14.257
  unit: kN
  original_value:
  original_unit:
source_file: >
  R1/COMMON/calculations/20260208_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Zellen C58-C65 und C71-C73 (per openpyxl mit
  data_only=True ausgelesen, Stand der abgelegten Datei am 2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-2, KNOWLEDGE.md §4 ("With experimental
M_y,k=156989 Nmm") und unabhängig gegen die reale Excel-Datei verifiziert.

**Eingangswert:** M_y,k = 156989 Nmm ("Biegeversuche Stabdübel Mittel",
C73/C18) — Excel weist zusätzlich einen 5%-Fraktilwert
M_y,k = 139652 Nmm aus (C72, "Biegeversuche Stabdübel 5%"), der hier nicht
weiter ausgewertet wird.

**Ergebnisse je Modus** (kN): a = 26.185 (C59, unverändert), b = 43.2
(C60, unverändert), d = 14.257 (C61/C64, governierend, "Versagensmodus"
C65), f = 16.956 (C62).

**Bezug zur Höchstlastannahme:** Die in der Excel-Datei als "Höchstlast
F_est" (C27, mit Vermerk "Es liegen keine Versuchsergebnisse vor")
geführte Last F ≈ 627.16 kN entspricht der auf dieser experimentellen
Basis hochgerechneten Gesamttragfähigkeit der Dübelgruppe — siehe
R1-GL24h-CALC-003.
