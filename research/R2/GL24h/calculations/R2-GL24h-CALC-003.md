---
calculation_id: R2-GL24h-CALC-003
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions: R2-COMMON-ASS-003, R2-COMMON-ASS-004
method: >
  Elastisches Schubfeld `c_v = G·A_v/l_v` für das 800×800×160 mm
  Holzschubfeld (`G_mean=650 N/mm²` GL24h), parallel dazu zwei
  beidseitige, vollflächig verklebte BFU-BU-F50/25-Sperrholzplatten
  (`t=12 mm` je Seite, `G_r,mean=500 N/mm²` angenommen), Schub-
  Korrekturbeiwert `κ=1`.
equations: c_v = G·A_v/l_v; Parallelschaltung c_v,ges = c_v,H + Σc_v,P.
result:
  quantity: Verstärkte Gesamt-Schubfeldsteifigkeit
  value: 116.0
  unit: kN/mm
  original_value: 116000
  original_unit: N/mm
source_file: >
  R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen C150-C166 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-3 (STATE.md Abschnitt 5, KNOWLEDGE.md Abschnitt 6)
und unabhängig gegen die reale Excel-Datei verifiziert.

**Zwischenwerte:** Holzschubfeld `A_v=128.000 mm²` (C153), `c_v,H=
104.000 N/mm = 104 kN/mm` (C155). Je Sperrholzplatte `A_v,P=9.600 mm²`
(C161), `c_v,P=6.000 N/mm = 6 kN/mm` (C163, Annahme
`G_r,mean=500 N/mm²`, Anmerkung Zelle D163). Zwei Platten parallel:
`2×6=12 kN/mm`. Gesamt (Kehrwerte werden hier NICHT gebildet — Timber und
Platten wirken parallel bei gleicher Schubverformung, siehe Anmerkung
Zelle D166 "Kehrwerte addieren da Federn in Reihe" bezieht sich auf den
nachfolgenden Schritt, nicht auf diese Parallelschaltung):
`c_v,ges = 104 + 12 = 116 kN/mm` (C166).

Eingang in R2-GL24h-CALC-004 (Serienschaltung mit den vier Stangen aus
R2-GL24h-CALC-002).
