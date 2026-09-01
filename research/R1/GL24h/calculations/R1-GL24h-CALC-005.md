---
calculation_id: R1-GL24h-CALC-005
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
  Kombination aus Lochspiel u_0 (FprEN Gl. 11.25) und elastischem Schlupf
  u_el,S = F/K_SLS,v zu einer kombinierten Schlupfgröße der Dübelgruppe,
  gemäß R1-GL24h-DEC-007 mit getrennt ausgewiesenen Anteilen.
equations: >
  u_0 = (d_Bohrung,Stahl - d) / 2 (FprEN Gl. 11.25); u_el,S = F_est / K_SLS,v;
  u_Gruppe = u_0 + u_el,S
result:
  quantity: Kombinierter Schlupf der Dübelgruppe (u_0 + u_el,S)
  value: 3.409
  unit: mm
  original_value: 3.409443196354402
  original_unit: mm
source_file: >
  R1/COMMON/calculations/20260208_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Zellen C89, C90, C91 (per openpyxl mit
  data_only=True ausgelesen, Stand der abgelegten Datei am 2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-2, KNOWLEDGE.md §8 / artifacts/VERFORMUNGSKONZEPT_GL24H.md
("Step B", "Step C") und unabhängig gegen die reale Excel-Datei
verifiziert.

**Anteile:**
- u_0 = 0.5 mm (Zelle C89) — Lochspiel im Stahlblech: (Ø13 - Ø12)/2. Für
  das Holz selbst ergibt sich u_0,Holz = (Ø12 - Ø12)/2 = 0 mm (kein
  Lochspiel, da Holzbohrung und Dübeldurchmesser identisch sind).
- u_el,S ≈ 2.909 mm (Zelle C90) = F_est / K_SLS,v = 627.16 kN / 215.56
  kN/mm — F_est aus R1-GL24h-CALC-003, K_SLS,v aus R1-GL24h-CALC-004.
- u_Gruppe = u_0 + u_el,S ≈ 3.409 mm (Zelle C91).

Gemäß R1-GL24h-DEC-007 werden u_0 und u_el,S hier zwar zu u_Gruppe addiert,
aber weiterhin explizit als getrennte Anteile ausgewiesen — die Summe
selbst ersetzt nicht die Notwendigkeit, beide Anteile bei Bedarf getrennt
zu betrachten.
