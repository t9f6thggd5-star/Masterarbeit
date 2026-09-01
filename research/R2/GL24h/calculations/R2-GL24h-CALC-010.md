---
calculation_id: R2-GL24h-CALC-010
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Korrektur von R2-GL24h-CALC-005: Lastausbreitung unter der Ankerplatte
  wird jetzt beidseitig angesetzt (`l_ef = b_Stahlplatte + 2·Δl` statt
  zuvor nur `b_Stahlplatte + Δl`), entsprechend FprEN 1995-1-1:2024 Fig.
  8.2/8.3 (Regelfall bei beidseitig ausreichend vorhandenem Material).
  Übrige Eingangswerte (`h_ef`, `α`, `k_mat`, `f_c,90,mean`) unverändert
  gegenüber CALC-005.
equations: >
  FprEN 1995-1-1:2024, Gl. 8.5 (σ_c,90); Gl. 8.7 (k_c,90); Gl. 8.8/8.9
  (A_ef = b_ef·l_ef); Tab. 8.1 (k_mat); Tab. 8.2 (Lastausbreitungsgradient
  α=45° parallel zur Faser); Fig. 8.2/8.3 (beidseitige Ausbreitung).
result:
  quantity: Unverstärkte Querdrucktragfähigkeit F_v,R, GL24h (korrigiert, beidseitige Lastausbreitung)
  value: 262.376
  unit: kN
  original_value: 262375.920
  original_unit: N
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen H58-H71 (per
  openpyxl mit data_only=True und als Formeltext ausgelesen, Stand der
  abgelegten Datei am 2026-09-01. Die Datei wurde vom Nutzer während der
  Korrektur von "20260208_Berechnung_..." auf
  "20260109_Berechnung_..." umbenannt — derselbe Kalkulationsstand,
  nur neuer Dateiname.)
certainty: CALCULATED
superseded_by:
---

Korrektur zu R2-GL24h-CALC-005, entstanden aus einer Rückfrage zur
Lastausbreitung nach FprEN 1995-1-1:2024, 8.1.6.1 (Fig. 8.2/8.3): das
Grundmodell zeigt dort durchgängig beidseitige Ausbreitung der
Kontaktfläche zu einem Trapez; CALC-005 hatte nur einseitig
`Δl=h_ef·tan(45°)=140 mm` addiert.

**Aktuelle Zellenkette** (Sheet "Rahmenecke GL24h SD"): `b_Stahlplatte
=240 mm` (H58, Formel `H58+2·H62`), `h_ef=140 mm` (H60, Gl. 8.11),
`Δl=140 mm` (H62, `=H60·tan(45°)`), `l_ef=520 mm` (H63,
`=H58+2·H62`, jetzt beidseitig), `b_90,c=160 mm` (H64), `A=38.400 mm²`
(H65), `A_ef=83.200 mm²` (H66, `=H63·H64`), `k_c,90=1,4720` (H67, Gl.
8.7), `k_mat=1,4` (H68, Tab. 8.1, unverändert, siehe R2-GL24h-DEC-003),
`σ_c,90=6,8327 N/mm²` (H69, Gl. 8.5) → `F_v,R = 6,8327×38.400/1.000 =
262,376 kN` (H71).

**Bezug zur Zugseiten-Steifigkeitskette:** Die Ankerplattengeometrie
(`b_Stahlplatte`, `h_ef`, `α`) ist identisch zu der in R2-GL24h-CALC-001
für die Querdrucksteifigkeit `c_c,90` verwendeten — ob die dortige
Steifigkeitsberechnung (`A_ef=60.800 mm²`, einseitige Ausbreitung)
ebenfalls auf beidseitige Ausbreitung umgestellt werden soll, ist damit
eine offene Folgefrage (noch nicht geklärt, nicht Teil dieser Korrektur).

**Vergleich mit anderen Werten:** `262,376 kN` liegt jetzt — anders als
im ursprünglich dokumentierten (und als Widerspruch aufgefallenen)
Zwischenstand — plausibel **unterhalb** der korrigierten verstärkten
Querdrucktragfähigkeit (`384,124 kN`, R2-GL24h-CALC-011) und weiterhin
unterhalb des gemessenen Gewindestangen-Zugversuchsmittels (`285,77 kN`,
R2-GL24h-II-T-S-BR-22-RES-001). Die Rangfolge unverstärkt < verstärkt
ist damit wieder konsistent mit der physikalischen Erwartung, dass eine
Verstärkung die Tragfähigkeit nicht verringern darf.
