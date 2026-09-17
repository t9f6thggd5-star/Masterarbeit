---
calculation_id: R2-GL24h-CALC-019
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
  Axiale Druck-Steifigkeit des Holzes PARALLEL zur Faser (0°) in der
  Druckzone des Rahmenecken-Innenknotens ("c_c,0"), als homogener
  Ersatzstab nach Hookeschem Gesetz: `c_c,0 = E_0,mean·A/l`. Fläche
  `A` = Fläche der Ankerplatte (160×240mm = 38.400mm², identisch zu
  `A_H`/`A_Stahlplatte` bei `c_c,90`). Länge `l` = 240mm (Plattentiefe
  in Kraftrichtung), in Analogie zu `h_ef` bei `c_c,90` (FprEN Gl.
  9.31) als Saint-Venant-artige Abklinglänge angesetzt: die
  konzentrierte Pressung unter der Platte klingt über eine Strecke in
  der Größenordnung der Plattenabmessung ab, bevor sie sich
  gleichmäßig über den vollen (deutlich größeren) Trägerquerschnitt
  verteilt hat.

  FprEN 1995-1-1:2024 enthält für diesen Fall KEINE Formel — Kapitel 9
  (Serviceability limit states) kennt nur 9.1 General, 9.2
  Deformations (allgemeine Bauteilverformung nach Balkentheorie), 9.3
  Vibrations und 9.4 "Compressive deformation perpendicular to grain"
  (Gl. 9.31, = Grundlage von c_c,90). Es folgt kein "9.5" oder
  Äquivalent für die Parallelrichtung (geprüft am 2026-09-17,
  vollständige Durchsicht Kapitel 9). Das ist inhaltlich konsistent:
  Druck parallel zur Faser zeigt kein Eindrück-/Lastausbreitungs-
  verhalten wie Querdruck und wird daher als gewöhnliche Stab-Mechanik
  behandelt, für die die Norm keine Sonderklausel vorsieht.

  Fläche und Länge sind damit eine eigene Modellierungsannahme ohne
  Normbezug — siehe R2-COMMON-OPQ-011 (offen, zur Absprache mit der
  Betreuerin).
equations: >
  Hookesches Gesetz für den homogenen Stab: `c=E·A/l`. Keine
  FprEN-Fundstelle (siehe method).
result:
  quantity: Axiale Druck-Steifigkeit parallel zur Faser, c_c,0, GL24h
  value: 1840
  unit: kN/mm
  original_value: 1840000
  original_unit: N/mm
source_file:
certainty: ASSUMED
superseded_by:
---

**Eingangswerte:** `E_0,mean=11.500 N/mm²` (GL24h, Holzkennwerte!D34),
`A=38.400 mm²` (=160×240mm, Ankerplattenfläche, identisch zu
`A_Stahlplatte`/`A_H` bei c_c,90), `l=240mm` (Plattentiefe in
Kraftrichtung).

**Rechnung:**

```
c_c,0 = E_0,mean · A / l
      = 11.500 N/mm² · 38.400 mm² / 240 mm
      = 1.840.000 N/mm
      = 1.840 kN/mm
```

Zum Vergleich deutlich steifer als `c_c,90` (111,339–175,402 kN/mm,
je nach Zug-/Druckseite und Verstärkung, R2-COMMON-CALC-001): Holz ist
parallel zur Faser um den Faktor `E_0/E_90 = 11.500/300 ≈ 38,3`
steifer als quer zur Faser, hier zusätzlich mit einer kürzeren
Bezugslänge (240mm statt 580mm bzw. 140mm) gerechnet.

**Status:** Fläche `A` und Länge `l` sind vom Nutzer im Chat vom
2026-09-17 vorläufig festgelegt (`A`=Plattenfläche, `l`=240mm nach
Saint-Venant-Analogie zu `h_ef`), da FprEN keine Normvorgabe für
diesen Fall liefert. Die Modellierungsannahme ist noch **nicht** mit
der Betreuerin abgestimmt — daher `certainty: ASSUMED` statt
`CALCULATED`, und als offene Frage in R2-COMMON-OPQ-011 vermerkt
(vorzulegen in der nächsten Besprechung). Bei Bedarf ist diese
Berechnung entsprechend zu revidieren (`superseded_by`).

Weiterverwendung: `c_c,0` ist eine der Federn der noch aufzubauenden
Druckseiten-Gesamtsteifigkeitskette `c_C` (analog zu `c_T` auf der
Zugseite, siehe R2-GL24h-INT-001) — die konkrete Verschaltung mit
`c_c,90` (Serie? Parallel? welche Hebelarme?) ist noch nicht
festgelegt, siehe R2-COMMON-OPQ-006.
