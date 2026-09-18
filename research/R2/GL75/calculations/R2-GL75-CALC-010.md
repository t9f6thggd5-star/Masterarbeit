---
calculation_id: R2-GL75-CALC-010
scope:
  connection: R2
  material: GL75
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions: R2-COMMON-ASS-003
method: >
  Elastisches Schubfeld `c_v = G·A_v/l_v` für das 800×800×160 mm
  Holzschubfeld (`G_mean=850 N/mm²` GL75, Holzkennwerte!F36), parallel
  dazu zwei Furniersperrholzplatten (BFU-BU F50/25, `t=9mm` je Platte,
  `G_r,mean=500 N/mm²` angenommen — dieselbe materialunabhängige
  Annahme wie bei GL24h, R2-COMMON-ASS-003), auf der linken und rechten
  Seitenfläche des Trägers. Anders als bei GL24h (`t=12mm`) hier mit
  `t=9mm` gemäß R2-Prüfkörperkonstruktion für GL75.
equations: c_v = G·A_v/l_v; Parallelschaltung c_v,ges = c_v,H + Σc_v,P.
result:
  quantity: Gesamt-Schubfeldsteifigkeit, GL75 (Holz + 2 Sperrholzplatten)
  value: 145
  unit: kN/mm
  original_value: 145000
  original_unit: N/mm
source_file: >
  Vom Nutzer im Chat berechnet (c_v,H=136, Platte je 4,5) und hier
  formelbasiert nachvollzogen/bestätigt; `G_mean=850 N/mm²` gegen
  Holzkennwerte!F36 verifiziert. **Update (2026-09-18):** Der Nutzer hat
  den Zugseiten-Rechenweg jetzt auch im R2-Excel ergänzt — Sheet
  "Rahmenecke GL75 SD", Block K63:M80: `M67` (A_v=128.000, `=M66*M64`),
  `M69` (c_v,H=136, `=(Holzkennwerte!F36*M67)/M65*10^-3`), `M75`
  (A_v,P=7.200, `=M72*M73`), `M77` (c_v,P=4,5 je Platte,
  `=(Holzkennwerte!L23*M75)/M74*10^-3`), `M80` (c_v,ges=145,
  `=M69+2*M77`) — alle Werte exakt deckungsgleich mit den hier
  dokumentierten. **Neuer Fund:** die Notiz in N77 lautet "Annahme
  Schubmodul 500 N/mm^2 KLH ETA Scheibenbeanspruchung" — liefert damit
  erstmals eine konkrete technische Quellenangabe für die
  `G_r,mean=500 N/mm²`-Annahme (Bezug auf eine ETA für KLH-Brettsperrholz,
  Scheibenbeanspruchung), bisher in R2-COMMON-ASS-003 nur als
  Nutzerangabe ohne Dokumentquelle vermerkt — sollte dort nachgetragen
  werden.
certainty: CALCULATED
superseded_by:
---

Analog zu R2-GL24h-CALC-003, mit GL75-Kennwerten und `t=9mm` statt
`12mm` bei den Sperrholzplatten.

**Zwischenwerte:**
- Holzschubfeld: `A_v=128.000 mm²` (=160×800, identisch zu GL24h,
  materialunabhängige Geometrie), `l_v=800mm` →
  `c_v,H = G_mean·A_v/l_v = 850·128.000/800 = 136.000 N/mm = 136 kN/mm`.
- Je Sperrholzplatte (`t=9mm`): `c_v,P = G_r,mean·t = 500·9 = 4.500
  N/mm = 4,5 kN/mm` (da `A_v,P/l_v = t`, siehe Herleitung analog
  R2-GL24h-CALC-003). Zwei Platten parallel: `2·4,5=9 kN/mm`.
- Gesamt (Holz + 2 Platten parallel, gleiche Schubverformung):
  `c_v,ges = 136 + 9 = 145 kN/mm`.

**Plausibilitätshinweis:** Verhältnis der Plattenwerte
`c_v,P(GL75)/c_v,P(GL24h) = 4,5/6 = 0,75 = 9mm/12mm` — exakt die
erwartete lineare Skalierung mit der Plattendicke bei sonst gleichem
`G_r,mean`. `G_mean(GL75)/G_mean(GL24h) = 850/650 ≈ 1,308`, passend zum
Verhältnis `c_v,H(GL75)/c_v,H(GL24h) = 136/104 ≈ 1,308`.

Weiterverwendung: eine der Federn der Zugseiten-Gesamt-
steifigkeitskette `c_T`, siehe R2-GL75-CALC-011.
