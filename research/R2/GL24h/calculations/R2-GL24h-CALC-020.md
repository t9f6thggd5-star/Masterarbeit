---
calculation_id: R2-GL24h-CALC-020
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources:
  literature: FragiacomoBatchelar2012a
  experimental_data:
  assumptions:
method: >
  Gesamt-Druckseitensteifigkeit `c_C` als Serienschaltung der beiden
  Holzfedern `c_c,90` (Querdruck) und `c_c,0` (Druck parallel zur
  Faser), gemäß der in R2-COMMON-DEC-004 bestätigten Federmodell-
  Topologie (Fig. 7, FragiacomoBatchelar2012a, siehe
  R2-COMMON-CLAIM-031): `1/c_C = 1/c_c,90 + 1/c_c,0`. Kein
  Stangen-/Schub-Anteil auf der Druckseite (anders als bei c_T).

  Für `c_c,90` wird — gemäß Nutzerentscheidung vom 2026-09-17 ("wir
  verwenden in der Folge nur den verstärkten [Wert]") — der ASSY-
  verstärkte Bejtka-Wert der Druckseite (A=2, beidseitige
  Lastausbreitung) angesetzt, nicht der unverstärkte FprEN-Wert.
equations: >
  Serienfeder: `(1/c_1+1/c_2)^-1`. `c_c,90`: Bejtka (2005) Gl. 67,
  siehe R2-COMMON-CALC-001. `c_c,0`: Hookesches Gesetz, siehe
  R2-GL24h-CALC-019.
result:
  quantity: Gesamt-Druckseitensteifigkeit c_C, GL24h (ASSY-verstärkt)
  value: 160.137
  unit: kN/mm
  original_value: 160136.628
  original_unit: N/mm
source_file:
certainty: CALCULATED
superseded_by:
---

**Eingangswerte:** `c_c,90 = 175,402 kN/mm` (Bejtka-verstärkt,
Druckseite, `A=2`, aus R2-COMMON-CALC-001 nachgerechnet — dort bisher
nur die Zugseiten-Beispielrechnung dokumentiert, Druckseiten-Wert im
Chat vom 2026-09-17 ergänzend durchgerechnet), `c_c,0 = 1.840 kN/mm`
(R2-GL24h-CALC-019).

**Rechnung:**

```
c_C = (1/c_c,90 + 1/c_c,0)^-1
    = (1/175,402 + 1/1.840)^-1
    = (0,0057013 + 0,00054348)^-1
    = 160,137 kN/mm
```

**Plausibilitäts-Hinweis:** Das Verhältnis `c_c,90/c_c,0` (verstärkt)
beträgt hier `≈9,5 %`. FragiacomoBatchelar2012b (R2-COMMON-CLAIM-003)
berichtet für eine vergleichbare, aber UNVERSTÄRKTE ("tensioned")
Konfiguration experimentell ein Verhältnis von `≈5 %`
(Querdrucksteifigkeit ≈5% der Steifigkeit parallel zur Faser) — ein
direkter Vergleich mit dem unverstärkten Zugseiten-Wert dieser Arbeit
(`c_c,90=100,866 kN/mm`, R2-GL24h-CALC-001) ergibt `100,866/1.840 ≈
5,5 %`, bemerkenswert nah am Literaturwert trotz abweichender
Geometrie/Material — ein unabhängiges Plausibilitätsindiz für den
gewählten Ansatz `l=240mm` bei `c_c,0` (R2-GL24h-CALC-019), auch wenn
dieser weiterhin über R2-COMMON-OPQ-011 offen zur Absprache mit der
Betreuerin steht.

**Status:** Erste vollständige Druckseiten-Gesamtsteifigkeit. Beruht
auf der noch offenen Modellierungsannahme zu `c_c,0` (l=240mm,
R2-COMMON-OPQ-011) — bei Änderung dieser Annahme ist dieser Wert zu
revidieren. Die Kombination mit `c_T` (Zugseite) zu einer
Rotationssteifigkeit der gesamten Rahmenecke über den Hebelarm `z`
steht noch aus (R2-COMMON-OPQ-006).

**Update (2026-09-17): Bestätigung direkt aus dem R2-Excel.** Der
Nutzer hat dieselbe Kette jetzt auch im Excel abgebildet (Sheet
"Rahmenecke GL24h SD", Zellen H97-H112) und geprüft. Ergebnis
deckungsgleich mit obiger Handrechnung: `H105 (c_c,90,verstärkt,
Druckseite, A=2) = 175,4015 kN/mm`, `H108 (c_c,0) = 1.840 kN/mm`,
`H112 (c_C) = 160,13623 kN/mm` — Rundungsdifferenz zu `160,137` oben
vernachlässigbar (<0,001%).

**Zwei Abweichungen gegenüber diesem Eintrag, geprüft und als
unkritisch eingestuft:**

1. Die Excel-Formel in `H112` (`=(1/H105+1/H108+1/H94)^-1`) hat einen
   DRITTEN Term `H94` ("c_t,ep", Steifigkeit der Ankerplatte auf
   Biegung, Druckseite) — abweichend von der in R2-COMMON-DEC-004
   festgelegten reinen Zwei-Feder-Topologie (`c_c,90`+`c_c,0`). `H94`
   ist aber auf `1e99` gesetzt ("Annahme wird vernachlässigt", analog
   zum Zugseiten-Pendant `c_t,ep`) — numerisch identisch zu `1/∞≈0`,
   ändert das Ergebnis nicht. Strukturell bleibt aber festzuhalten,
   dass der Nutzer hier bewusst einen Platzhalter für eine mögliche
   künftige Ankerplatten-Biegesteifigkeit auf der Druckseite
   vorgesehen hat, den die DEC-004-Topologie (aus einer andere
   Geometrie/Konstruktion betreffenden Literaturquelle) nicht
   vorsieht — sollte bei Bedarf mit der Betreuerin abgeglichen werden,
   ob die R2-eigene Ankerplatte auf der Druckseite tatsächlich lokal
   biegeweich sein könnte.
2. Der Excel-Kommentar zu `H108` (`c_c,0`) lautet "Annahme
   Druckzonenhöhe =240mm" — bezeichnet die hier verwendete Länge
   `l=240mm` also als "Druckzonenhöhe" (`h_d`). Das ist eine engere
   Lesart als die in R2-GL24h-CALC-019 dokumentierte Saint-Venant-
   Analogie (dort als reine Plattentiefe begründet, nicht explizit als
   `h_d` identifiziert) — inhaltlich aber kompatibel: `l=240mm` kann
   als erster konkreter Zahlenwert für die in R2-COMMON-OPQ-006 noch
   offene Druckzonenhöhe gelesen werden. Ergänzender Querverweis in
   R2-COMMON-OPQ-011 empfohlen.
