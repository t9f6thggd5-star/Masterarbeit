---
calculation_id: R2-GL24h-CALC-017
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024, ETA-11-0190-2026
  literature:
  experimental_data:
  assumptions: R2-GL24h-DEC-008
method: >
  Verstärkte Querdrucktragfähigkeit nach Gl. 8.12, jetzt für die Zugseite
  separat berechnet: `l_1,ef` wird dort nicht mehr nach Gl. 8.14
  (Zwischenauflager, wie in R2-GL24h-CALC-011 für die Druckseite/
  Ankerplatte) angesetzt, sondern nach Gl. 8.13 (Endauflager) mit
  `l_e=0 mm`, da die Stahlplatte auf der Zugseite direkt am Trägerrand
  liegt und dort nur einseitige Lastausbreitung möglich ist
  (R2-GL24h-DEC-008). Übrige Eingangswerte (Schraubengeometrie,
  `k_mat Holz=1,75`, `k_mat Schraube=1`, Schraubenanteil) unverändert
  gegenüber R2-GL24h-CALC-011.
equations: >
  FprEN 1995-1-1:2024, Gl. 8.12; Gl. 8.13 (l_1,ef, Endauflager, mit
  l_e-Term); Gl. 8.15 (l_2,ef).
result:
  quantity: Verstärkte Querdrucktragfähigkeit F_c,90, GL24h, Zugseite (Endauflager, l_e=0)
  value: 356.273
  unit: kN
  original_value: 356272.752
  original_unit: N
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen J32-L87 (per
  openpyxl mit data_only=True und als Formeltext ausgelesen, Stand der
  abgelegten Datei am 2026-09-17, Datei-mtime 1789638113424). Identisch
  auf Blatt "Rahmenecke GL24h HD", Zellen K32-M87 (dort mit
  `M84=M87=356,273 kN`, exakt übereinstimmend).
certainty: CALCULATED
superseded_by:
---

Ergänzung zu R2-GL24h-CALC-011: der Nutzer hat die R2-Excel-Datei am
2026-09-17 so erweitert, dass die Querdrucktragfähigkeit (unverstärkt
und verstärkt) jetzt durchgängig getrennt nach Zug- und Druckseite
berechnet wird (bisher nur eine gemeinsame Spalte). Dieser Eintrag
dokumentiert den dabei neu entstandenen Zugseiten-Wert.

**Hintergrund der Unterscheidung:** In einer vorangegangenen Diskussion
(2026-09-17) wurde geklärt, dass FprEN Gl. 8.13 (Endauflager) und Gl.
8.14 (Zwischenauflager) sich nur im Term `min{l_e;30;l_s/2}` (Endauflager)
gegenüber `min{30;l_s/2}` (Zwischenauflager) unterscheiden — bei
`l_s=560 mm` (also `l_s/2=280 mm`, stets oberhalb des 30 mm-Deckels)
ergibt das:
- Zwischenauflager (Druckseite, ausreichender Randabstand):
  `min{30;280}+min{30;280}=30+30=60 mm`
- Endauflager (Zugseite, `l_e≈0`, Stahlplatte direkt am Trägerrand):
  `min{0;30;280}+min{30;280}=0+30=30 mm`

**Zellenkette Zugseite** (Sheet "Rahmenecke GL24h SD", Spalte L):
`l_e=0 mm` (L66, neu als eigene Zelle eingeführt), `l_1,ef=270 mm` (L69,
`=L35+(MIN(L66,30,L68/2)+MIN(30,L68/2))`, Gl. 8.13), Holzanteil
`L82=1,75×160×270×3,3156/1.000=250,663 kN` (10 % kleiner als der
Druckseiten-Holzanteil `278,515 kN`, proportional zu `l_1,ef`),
Schraubenanteil `L83=105,610 kN` (unverändert, kein `l_1,ef`-Bezug), 1.
Versagensmodus `L84=250,663+105,610=356,273 kN`, 2. Versagensmodus
(Ebene Schraubenspitze) `L85=413,793 kN` (unverändert) — maßgebend der
kleinere Wert: `F_c,90=356,273 kN` (L87).

**Vergleich mit der Druckseite** (R2-GL24h-CALC-011, 384,124 kN):
Zugseite liegt um `27,851 kN` (−7,25 %) niedriger — ausschließlich durch
den kleineren `l_1,ef`-Wert (270 mm statt 300 mm) bedingt, da der
Schraubenanteil auf beiden Seiten identisch ist (identische
Schraubengeometrie, Nutzerangabe). Beide Werte bleiben oberhalb des
gemessenen Gewindestangen-Zugversuchsmittels (`285,77 kN`,
R2-GL24h-II-T-S-BR-22-RES-001) — an der bisherigen `M_max`-Kette
(R2-GL24h-CALC-012, maßgebend weiterhin das Gewindestangen-
Zugversuchsmittel) ändert sich dadurch numerisch nichts, siehe aber
R2-GL24h-OPQ-004 zu einer Formel-Lücke, die dabei auffiel.

**R2-GL24h-CALC-011 gilt ab sofort explizit nur für die Druckseite** —
siehe dortige Ergänzung.
