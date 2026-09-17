---
calculation_id: R2-GL24h-CALC-018
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions: R2-GL24h-DEC-008
method: >
  Unverstärkte Querdrucktragfähigkeit nach Gl. 8.5/8.7/8.9, jetzt für die
  Zugseite separat berechnet: einseitige Lastausbreitung
  (`l_ef=b_Stahlplatte+Δl`, `A_ef=60.800 mm²`), da die Stahlplatte auf der
  Zugseite direkt am Trägerrand liegt (R2-GL24h-DEC-008) — im Unterschied
  zur beidseitigen Ausbreitung auf der Druckseite/Ankerplatte
  (R2-GL24h-CALC-010).
equations: FprEN 1995-1-1:2024, Gl. 8.5 (σ_c,90); Gl. 8.7 (k_c,90); Gl. 8.9 (A_ef); Tab. 8.1 (k_mat).
result:
  quantity: Unverstärkte Querdrucktragfähigkeit F_v,R, GL24h, Zugseite (einseitige Lastausbreitung)
  value: 224.292
  unit: kN
  original_value: 224292.164
  original_unit: N
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen J32-L48 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-17, Datei-mtime 1789638113424). Identisch auf Blatt "Rahmenecke
  GL24h HD", Zellen K32-M48 (dort `M48=224,292 kN`, exakt
  übereinstimmend).
certainty: CALCULATED
superseded_by:
---

Ergänzung zu R2-GL24h-CALC-010, entstanden aus derselben Excel-
Erweiterung wie R2-GL24h-CALC-017 (Zug-/Druckseite jetzt getrennt
berechnet, Stand 2026-09-17).

**Zellenkette Zugseite** (Sheet "Rahmenecke GL24h SD", Spalte L):
`h_ef=140 mm` (L37, Gl. 8.11, unverändert — hängt nur von `h_Träger` ab,
nicht von der Seite), `Δl=140 mm` (L39), `l_ef=380 mm` (L40,
`=L35+L39`, einseitig — nur ein `Δl`-Term, im Gegensatz zur Druckseite
`H40=520 mm=H35+2·H39`), `A_ef=60.800 mm²` (L43), `k_c,90=1,2583` (L44,
Gl. 8.7), `k_mat=1,4` (L45, Tab. 8.1, Case A, SWB, unverändert), `σ_c,90
=5,8409 N/mm²` (L46, Gl. 8.5) → `F_v,R=5,8409×38.400/1.000=224,292 kN`
(L48).

**Bemerkenswert:** Dieser Wert entspricht exakt dem alten, vor der
Lastausbreitungs-Korrektur dokumentierten Zwischenstand
(`≈224,29 kN`, ursprünglich in R2-GL24h-CALC-005 als vermeintlich
allgemeingültiger Wert festgehalten, dann durch R2-GL24h-CALC-010 auf
`262,376 kN` "korrigiert"). Mit der jetzt vorliegenden Zug-/Druck-
Trennung zeigt sich: beide Werte waren korrekt — nur für
unterschiedliche Seiten. CALC-005 traf (unbeabsichtigt) die Zugseite,
CALC-010 die Druckseite. Diese Koinzidenz wird hier nur als Beobachtung
festgehalten; an der Gültigkeit von CALC-010 (Druckseite) und diesem
Eintrag (Zugseite) ändert sie nichts.

**R2-GL24h-CALC-010 gilt ab sofort explizit nur für die Druckseite** —
siehe dortige Ergänzung.
