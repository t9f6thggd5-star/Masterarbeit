---
calculation_id: R2-GL24h-CALC-016
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature:
  experimental_data: R2-GL24h-II-T-S-BR-11-RES-002, R2-GL24h-II-T-S-BR-22-RES-003
  assumptions:
method: >
  Vergleich der gemessenen Stangengruppen-Steifigkeit (BR-11, BR-22) mit
  der reinen elastischen Dehnsteifigkeit der freien (nicht eingeklebten)
  Stangenlänge nach dem Hooke'schen Gesetz `k=E·A/L`, als zusätzlicher
  Erklärungsansatz zur in R2-GL24h-CALC-014 dokumentierten Diskrepanz
  zwischen Messwert und FprEN-Verbundmodell. Methodische Grundidee
  übernommen aus `R2/COMMON/calculations/2026-06_05_Auswertung_
  Steifigkeiten_Bonded-inRods.xlsx`, Blatt "Überblick", Zeilen 101-117
  ("Versuch der Auswertung: Vergleich experimentelle Steifigkeit mit
  Hooke'sche Gesetz", Hinweis dort: "Da das Versagen stets in der
  Stahlstange ist, kann man die Steifigkeit der Stahlstange mittels dem
  Hooke'sches Gesetz ermitteln.") — jedoch mit KORRIGIERTER
  Querschnittsfläche, siehe Freitext. Die Quelldatei selbst wurde nicht
  verändert (CLAUDE.md Abschnitt 1); diese Neuberechnung ist ein eigener
  Eintrag.
equations: k = E·A/L (Hooke'sches Gesetz).
result:
  quantity: Elastische Dehnsteifigkeit der freien Stangenlänge (Stahl allein), BR-11 (1 Stange, L=400mm) und BR-22 (4 Stangen, L=100mm), GL24h, mit Spannungsquerschnitt A_s
  value: 81.9 / 1310.4
  unit: kN/mm
  original_value: 81900.0 / 1310400.0
  original_unit: N/mm
source_file: >
  Längen L (400 mm BR-11, 100 mm BR-22, jeweils "Länge außerhalb Holz")
  aus R2/COMMON/calculations/2026-06_05_Auswertung_Steifigkeiten_
  Bonded-inRods.xlsx, Blatt "Überblick", Zellen B110/B111. E-Modul und
  Spannungsquerschnitt A_s aus R2/COMMON/calculations/20260109_
  Berechnung_Rahmenecke_eingeklebte Gewindestangen.xlsx, Sheet
  "Rahmenecke GL24h SD", Zellen H16 (E_s=210.000 N/mm²) und H17
  (Spannungsquerschnitt A_s=156 mm²) — dieselbe Flächenquelle, die
  bereits für `c_t` in R2-GL24h-CALC-002 (Zelle C120) verwendet wird.
certainty: CALCULATED
superseded_by:
---

**Korrektur gegenüber der Quelldatei:** Die "Auswertung
Steifigkeiten"-Datei berechnet an dieser Stelle (Zeile 109,
"Querschnittsfläche" = 201,062 mm²) mit der NOMINELLEN Bruttofläche
`π·d²/4` (d=16 mm). Das ist für eine über die volle Länge mit Gewinde
versehene Gewindestange nicht die technisch passende Fläche für die
elastische Längung — maßgebend ist der Spannungsquerschnitt (reduzierte
Fläche am Gewindekern), der in der anderen Excel-Datei (Berechnung der
eigentlichen R2-Verbindung) bereits korrekt mit `A_s=156 mm²` geführt
wird (Zelle H17, dort auch für `c_t,1` in R2-GL24h-CALC-002 verwendet).
Diese Neuberechnung verwendet konsequent `A_s=156 mm²` statt der in der
Quelldatei stehenden 201,06 mm². Die Quelldatei selbst bleibt unverändert
(CLAUDE.md Abschnitt 1) — dieser Fehler ist dort nicht korrigiert,
sondern nur hier dokumentiert.

**Rechnung** (`k=E·A_s/L`, `E=210.000 N/mm²`, `A_s=156 mm²`):
- BR-11 (L=400 mm, 1 Stange): `k=210.000·156/400=81.900 N/mm=81,9 kN/mm`
- BR-22 (L=100 mm, 1 Stange): `k=210.000·156/100=327.600 N/mm=327,6 kN/mm`;
  4 Stangen parallel: `4·327,6=1.310,4 kN/mm`

**Vergleich mit den gepoolten Messwerten:**
- BR-11: gemessen 203,303 kN/mm (R2-GL24h-II-T-S-BR-11-RES-002,
  Mittelwert oben+unten) — Faktor **≈2,48** über der reinen
  Stahl-Freilängen-Steifigkeit.
- BR-22: gemessen 862,531 kN/mm (R2-GL24h-II-T-S-BR-22-RES-003) —
  liegt UNTER der reinen Stahl-Freilängen-Steifigkeit der Gruppe
  (1.310,4 kN/mm), Verhältnis ≈0,66. Das ist physikalisch plausibel:
  die freie Stahllänge ist nur eine von mehreren in Serie wirkenden
  Nachgiebigkeiten (dazu kommen die beiden Klebefugen an den Enden), die
  Gesamtsteifigkeit eines Serienmodells kann nicht höher liegen als die
  steifste Einzelkomponente allein.

**Einordnung (weiterhin nur Beobachtung, `CLAUDE_DRAFT`, nicht
gedeutet):** Mit der korrigierten Fläche liegt der Messwert für BR-11
deutlicher über der reinen Stahl-Freilängen-Steifigkeit als zunächst
(mit der fehlerhaften Nominalfläche) angenommen — die ursprünglich in
der Diskussion genannte Näherung "Messwert nur rund doppelt so hoch wie
Stahl-Freilänge" war zu optimistisch und ist hiermit korrigiert
(≈2,48-fach statt ≈1,93-fach). Für BR-22 bestätigt sich dagegen die
plausible Größenordnung (Messwert unterhalb der Stahl-Freilängen-
Steifigkeit allein). Eine schlüssige Erklärung für den in
R2-GL24h-CALC-014 dokumentierten Faktor ≈6,48 zwischen Messwert und
FprEN-Verbundmodell liefert dieser Vergleich weiterhin nicht — er zeigt
nur, dass die freie Stahllänge einen relevanten, aber für sich allein
nicht ausreichenden Beitrag zur Gesamtnachgiebigkeit liefert.
