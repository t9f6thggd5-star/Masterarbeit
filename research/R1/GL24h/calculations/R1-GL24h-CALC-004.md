---
calculation_id: R1-GL24h-CALC-004
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
  Verschiebungsmodul der Stabdübelgruppe, ausgehend vom
  Verschiebungsmodul eines Einzeldübels/einer Scherfuge (FprEN
  Tab. 11.12(1)) und hochgerechnet auf die Gruppe (FprEN Gl. 11.26) mit
  n_90=4 Reihen, min(n_0,6)=6 wirksamen Dübeln je Reihe (n_0=8, gekappt
  auf 6) und m=2 Scherfugen.
equations: >
  K_SLS,v,i = ρ_mean^1.5 · d / 23 (FprEN Tab. 11.12(1));
  K_SLS,v = n_90 · min(n_0;6) · m · K_SLS,v,i (FprEN Gl. 11.26; Excel-Formel
  "=C22*MIN(C23;6)*C6*C87")
result:
  quantity: Verschiebungsmodul der Stabdübelgruppe K_SLS,v
  value: 215.560
  unit: kN/mm
  original_value: 215560.2025479084
  original_unit: N/mm
source_file: >
  R1/COMMON/calculations/20260208_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Zellen C6, C22, C23, C87, C88; Sheet
  "Holzkennwerte", Zelle D21 (per openpyxl mit data_only=True ausgelesen,
  Stand der abgelegten Datei am 2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-2, KNOWLEDGE.md §8 / artifacts/VERFORMUNGSKONZEPT_GL24H.md
("Step A") und unabhängig gegen die reale Excel-Datei verifiziert.

**Zwischenschritt Einzeldübel:** K_SLS,v,i ≈ 4.4908 kN/mm (Zelle C87),
mit ρ_mean = 420 kg/m³ (Sheet "Holzkennwerte", Zelle D21 — unabhängig
bestätigter Mittelwert für GL24h, nicht nur aus dem Chat übernommen) und
d = 12 mm.

Diese Größe ist gemäß R1-GL24h-DEC-006 die erste Verformungseingangsgröße
für die Phase-2-Verformungsabschätzung — siehe R1-GL24h-CALC-005 für die
daraus abgeleitete elastische Schlupfgröße.
