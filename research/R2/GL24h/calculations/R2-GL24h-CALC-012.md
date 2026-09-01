---
calculation_id: R2-GL24h-CALC-012
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data:
  assumptions:
method: >
  Aufnehmbares Moment am Rahmeneck-Innenknoten aus dem inneren Hebelarm
  `z` (Abstand Zug- zu Druckkraftresultierende) und der maßgebenden
  Zug-/Druckkomponente der Verbindung: `M_max = F_maßgebend · z`. Die
  maßgebende Komponente wird im Excel als Minimum dreier Kandidatenwerte
  gebildet: (1) Gewindestangen-Zugversuchsmittel `H40`, (2)
  "Tragfähigkeit Stütze auf Zug" (FprEN Fig. 11.38-Block) `H52`, (3)
  verstärkte Querdrucktragfähigkeit `H109` (= R2-GL24h-CALC-011).
equations: >
  M = F·z (Kräftepaar-Modell, kein FprEN-Gleichungsverweis im Excel
  angegeben); H123 = MIN(H40;H52;H109).
result:
  quantity: Aufnehmbares Moment M_max, GL24h (maßgebende Komponente Gewindestangen-Zugversuchsmittel)
  value: 160.031
  unit: kNm
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen H34-H52 und
  H116-H125 (per openpyxl mit data_only=True ausgelesen, Stand der
  abgelegten Datei am 2026-09-01, Datei-mtime 1788273961000)
certainty: CALCULATED
superseded_by:
---

Korrektur von R2-GL24h-CALC-008, veranlasst durch die Korrektur der
verstärkten Querdrucktragfähigkeit in R2-GL24h-CALC-011 (`k_mat`-Fehler,
248,846 kN → 384,124 kN). Da sich `H109` dadurch erhöht hat, ändert sich
auch das `MIN(H40;H52;H109)`, mit dem das Excel die für `M_max`
maßgebende Komponente bestimmt — und damit auch, welche Komponente
überhaupt maßgebend wird.

**Kette:** innerer Hebelarm `z=560 mm` (H116/H118, unverändert zu
CALC-008). Die drei Kandidatenwerte für die maßgebende Zug-/
Druckkomponente:

- `H40=285,77 kN` — Gewindestangen-Zugversuchsmittel (`H38=AVERAGE(H35:H37)`,
  identisch zum in R2-GL24h-CALC-002/CALC-007 verwendeten Versuchsmittel).
- `H52=717,072 kN` — "Tragfähigkeit Stütze auf Zug"-Block (Zellen
  H43-H52, FprEN Fig. 11.38-Modell, Eingaben `a=88 mm`, `b=80 mm`,
  `A_ef=7.040 mm²`; `H50` je Stange, `H52=H50·4` für alle vier
  Gewindestangen). Dieser Block war bisher nur als ungeklärter
  Excel-Inhalt unter R2-COMMON-OPQ-008 (Punkt 2) vermerkt — mit dieser
  Dokumentation ist seine Funktion im Rechenschema erstmals konkret
  belegt: er liefert einen der drei MIN-Kandidaten für die maßgebende
  Komponente. Seine normative Herleitung/Bedeutung (vermutlich eine
  Block-/Sprödbruchprüfung der Gewindestangengruppe) bleibt aber
  weiterhin ungeklärt, siehe R2-COMMON-OPQ-008.
- `H109=384,124 kN` — verstärkte Querdrucktragfähigkeit, korrigiert
  gemäß R2-GL24h-CALC-011 (vorher `248,846 kN`, siehe R2-GL24h-CALC-008
  alt).

`H123 = MIN(285,77; 717,072; 384,124) = 285,77 kN` (H40 = Gewindestangen-
Zugversuchsmittel ist jetzt maßgebend, nicht mehr die Querdrucktragfähigkeit).
`M_max = 285,77 × 0,560 = 160,031 kNm` (H125).

**Wechsel der maßgebenden Komponente:** Mit der Korrektur von CALC-011
ist die Querdrucktragfähigkeit (384,12 kN) nicht mehr der kleinste der
drei Kandidatenwerte — maßgebend ist jetzt das Gewindestangen-
Zugversuchsmittel (285,77 kN), analog zu GL75 (siehe
R2-GL75-CALC-003, wo dort ebenfalls der Gewindestangenzug maßgebend
ist). Die in R2-GL24h-CALC-008 formulierte "Bemerkenswert"-Beobachtung
(materialabhängiger Wechsel des Versagensmechanismus zwischen GL24h und
GL75) ist damit hinfällig: beide Materialien werden nach dieser
Korrektur rechnerisch durch dieselbe Komponente (Gewindestangenzug)
begrenzt. Dies war bereits als erwartete Konsequenz im
"Konsequenzen"-Abschnitt von R2-GL24h-CALC-011 angekündigt.

Nachgelagert im selben Excel-Block: "Zylinderkraft"-Abschnitt (Hebelarm
3,03 m, Zellen H131-H133) — unverändert zu CALC-008, weiterhin nicht
erläutert (siehe R2-COMMON-OPQ-008).
