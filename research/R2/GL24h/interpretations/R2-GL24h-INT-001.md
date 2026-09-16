---
interpretation_id: R2-GL24h-INT-001
scope:
  connection: R2
  material: GL24h
type: INTERPRETATION
based_on:
  experimental_results: R2-GL24h-II-T-S-BR-22-RES-003
  observations: R2-GL24h-CALC-001, R2-GL24h-CALC-003, R2-GL24h-CALC-004, R2-GL24h-CALC-014, R2-GL24h-CALC-015
interpretation: >
  Der Anstieg von c_T durch Einsetzen des BR-22-Messwerts (38,39 →
  50,78 kN/mm, +32,3 %) fällt trotz einer um Faktor ≈6,48 gestiegenen
  Einzelkomponente (Stangengruppe) moderat aus, weil c_T eine reine
  Serienschaltung dreier Federn ist und von der jeweils weichsten
  Komponente dominiert wird. Schon rein rechnerisch war nicht die
  Stangengruppe, sondern c_c,90 die weichste Komponente; durch den
  Messwert wird die Stangengruppe nahezu "unendlich steif" relativ zu
  den beiden übrigen Gliedern und fällt damit als limitierender Faktor
  praktisch aus der Kette heraus. c_T nähert sich dadurch der
  theoretischen Obergrenze (Stangengruppe → unendlich steif) von
  53,95 kN/mm bereits auf 94,1 % an. Ihr Einfluss auf die
  Gesamt-Nachgiebigkeit 1/c_T sinkt dabei von 28,8 % auf nur noch
  5,9 %, während c_c,90 (38,1 % → 50,3 %) und c_v,ges (33,1 % → 43,8 %)
  jetzt zusammen ca. 94 % der Gesamt-Nachgiebigkeit bestimmen — beide
  nach wie vor rein rechnerisch (FprEN), nicht experimentell validiert.
certainty: INTERPRETED
superseded_by:
authored_by: CLAUDE_DRAFT
reviewed: false
---

## Ausgangslage

R2-GL24h-CALC-015 ersetzt den bis dahin rein rechnerischen Wert für die
Gesamt-Zugseitensteifigkeit `c_T` (R2-GL24h-CALC-004, jetzt
`superseded_by`) durch eine teilweise messwertbasierte Fassung: der
Teilanteil "vier Gewindestangen parallel, ohne Querdruck" wurde in
R2-GL24h-CALC-014 vom rein rechnerischen FprEN-Wert (133,115 kN/mm) auf
den gepoolten Versuchswert R2-GL24h-II-T-S-BR-22-RES-003 (862,531 kN/mm,
K_ser, n=6) angehoben — ein Faktor von ≈6,48. Alle übrigen Glieder der
Kette (`c_c,90`, `c_v,ges`) blieben unverändert rechnerisch. Diese
Interpretation ordnet ein, warum sich dieser große Sprung in einer
Einzelkomponente nur in einem vergleichsweise moderaten Sprung des
Gesamtergebnisses niederschlägt, und was das für die weitere
Bearbeitung bedeutet.

## Serienfeder-Mechanik als Ursache

`c_T` ergibt sich als flache Serienschaltung dreier unabhängiger
Federn (Assoziativität der harmonischen Summe — Gruppierung über
`c_Zugpfade,ges` als Zwischenschritt ändert das Ergebnis nicht):

```
1/c_T = 1/c_Stangen,4x + 1/c_c,90 + 1/c_v,ges
```

| Komponente | alt (rein rechnerisch, CALC-004) | neu (teilw. messwertbasiert, CALC-015) | Quelle |
|---|---|---|---|
| c_Stangen,4x | 133,115 kN/mm | 862,531 kN/mm (Versuch) | CALC-002 (alt) / CALC-014 + RES-003 (neu) |
| c_c,90 | 100,866 kN/mm | 100,866 kN/mm (unverändert) | CALC-001 |
| c_v,ges | 116,0 kN/mm | 116,0 kN/mm (unverändert) | CALC-003 |
| **c_T** | **38,39 kN/mm** | **50,78 kN/mm** | CALC-004 / CALC-015 |

Bei einer Serienschaltung dominiert stets die weichste Feder das
Ergebnis, nicht die steifste. Bereits im rein rechnerischen Modell war
`c_Stangen,4x` (133,1 kN/mm) nicht die weichste Komponente — das war
schon dort `c_c,90` (100,9 kN/mm). Wird die Stangengruppe durch den
Messwert deutlich steifer, nähert sie sich dem Verhalten einer
"unendlich steifen" Feder an (vgl. den Platzhalterwert `c_t,ep=1e99`
im Excel-Modell) und trägt kaum noch zur Gesamt-Nachgiebigkeit bei —
sie fällt damit praktisch als limitierender Faktor aus der Kette
heraus.

## Theoretische Obergrenze

Lässt man `c_Stangen,4x → unendlich` (Grenzfall: die Stangengruppe
würde keine Nachgiebigkeit mehr beisteuern), ergibt sich als
Obergrenze für `c_T` bei sonst unveränderten `c_c,90` und `c_v,ges`:

`c_T,max = (1/c_c,90 + 1/c_v,ges)^-1 = (1/100,866 + 1/116,0)^-1 = 53,952 kN/mm`

Der aktuelle Wert (50,776 kN/mm) liegt bereits bei **94,1 %** dieser
Obergrenze. Eine weitere, auch deutlich höhere Stangengruppen-Steifigkeit
könnte `c_T` also kaum noch nennenswert weiter steigern — der Grenznutzen
ist bereits weitgehend ausgeschöpft (Sättigungseffekt).

## Verschiebung der Einflussanteile

Anteil der jeweiligen Komponente an der Gesamt-Nachgiebigkeit `1/c_T`:

| Komponente | Anteil alt | Anteil neu |
|---|---|---|
| c_Stangen,4x | 28,8 % | 5,9 % |
| c_c,90 (Querdruck) | 38,1 % | 50,3 % |
| c_v,ges (Verankerung) | 33,1 % | 43,8 % |

Vor dem Einsetzen des Messwerts waren alle drei Komponenten mit
vergleichbarem Gewicht beteiligt (grob 29/38/33 %). Danach bestimmen
`c_c,90` und `c_v,ges` zusammen bereits ca. 94 % der
Gesamt-Nachgiebigkeit, während die (jetzt versuchsgestützte)
Stangengruppe nur noch mit knapp 6 % beiträgt.

## Konsequenz für die weitere Bearbeitung

`c_c,90` und `c_v,ges` sind nach wie vor ausschließlich rechnerisch
(FprEN-basiert) hergeleitet, keine der beiden Größen ist bislang durch
einen eigenen Komponentenversuch abgesichert. Da sie jetzt den weit
überwiegenden Teil der Gesamt-Nachgiebigkeit bestimmen, hängt die
Verlässlichkeit von `c_T=50,78 kN/mm` in erster Linie an der Richtigkeit
dieser beiden rechnerischen Größen — nicht mehr wesentlich an der
Stangengruppen-Steifigkeit, die durch RES-003 bereits vergleichsweise
gut abgesichert ist (wenn auch mit den in RES-002/RES-003 dokumentierten
Vorbehalten zur Streuung). Ein experimenteller Abgleich von `c_c,90`
(Querdruck) und/oder `c_v,ges` (Verankerung) würde für die
Gesamtsteifigkeit aktuell einen größeren Erkenntnisgewinn liefern als
weitere Zugversuche an der Stangengruppe selbst.

## Einordnung / Vorbehalt

Diese Interpretation ist eine reine Konsequenz der bereits dokumentierten
Werte (CALC-001, CALC-003, CALC-004, CALC-014, CALC-015) und führt keine
neuen Eingangsgrößen ein. `CLAUDE_DRAFT` — vom Forschenden noch zu
prüfen und ggf. auf `reviewed: true` zu setzen (CLAUDE.md Abschnitt 14).
Der in R2-GL24h-CALC-014 offen gelassene, unabhängige Punkt — warum die
Stangengruppe selbst um Faktor ≈6,48 über der FprEN-Vorhersage liegt —
wird hier nicht behandelt und bleibt eine gesonderte, noch offene Frage.
