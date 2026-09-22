---
hypothesis_id: R2-GL24h-HYP-001
scope:
  connection: R2
  material: GL24h
type: HYPOTHESIS
statement: >
  Der in R2-GL24h-CALC-014 festgehaltene Faktor ≈6,48 zwischen dem
  gepoolten Versuchsmittelwert der 2×2-M16-Stangengruppe
  (R2-GL24h-II-T-S-BR-22-RES-003, K_ser=862,531 kN/mm) und dem rein
  rechnerischen FprEN-Wert für denselben Teilanteil ("vier Stangen ohne
  c_c,90", 133,115 kN/mm) sowie die in R2-GL24h-II-T-S-BR-22-RES-002
  dokumentierte erhebliche Streuung zwischen den einzelnen Prüfkörpern
  (Faktor ~3,4 bei K_ser, ~6,7 bei K_e) sind bislang beide unbewertet
  ("wird hier nur als Beobachtung festgehalten"/"wird hier bewusst nicht
  geraten"). Mögliche, nicht bestätigte Einflussfaktoren für beide
  Beobachtungen (einzeln oder in Kombination):

  (1) Bezugslängen-Diskrepanz: die rechnerische Größe `c_t=40.950 N/mm`
  (freie Stangendehnung, dominiert das rein rechnerische "4 Stangen
  ohne c_c,90"-Ergebnis stärker als der Verbundanteil `c_ax,f,par`, da
  `c_t < c_ax,f,par` in der Serienschaltung) setzt eine bestimmte freie
  Stangenlänge voraus. Die im Versuch mit Wegaufnehmern gemessene K_ser
  könnte über eine davon abweichende Messbasis (kürzerer/anderer
  Messweg als die im Modell angesetzte freie Länge) ermittelt worden
  sein, was einen systematischen Steifigkeitsunterschied erklären
  könnte, unabhängig vom eigentlichen Verbundverhalten.

  (2) Konservativer Ansatz der FprEN-Verbundsteifigkeit: der normative
  Wert `K_SLS,w` (FprEN 1995-1-1:2024, 11.3.8.3 (2)/Tab. 11.13 (3),
  l_w=320mm) könnte, wie in CALC-014 bereits spekuliert, konservativ
  kalibriert sein und die tatsächliche Verbundsteifigkeit systematisch
  unterschätzen.

  (3) Gruppenwirkung: FprEN 11.3.8.3 behandelt eine einzelne
  eingeklebte Stange; mögliche Interaktionseffekte zwischen den vier in
  einem gemeinsamen, eng benachbarten Holzquerschnitt eingeklebten
  Stangen (z. B. durch überlagerte Spannungsfelder im Holz) sind darin
  nicht erfasst und könnten die Gruppensteifigkeit gegenüber der
  Einzelstangen-Rechnung erhöhen.

  (4) Prüfkörper-/Werkstoffstreuung: lokale Unterschiede in
  Holzfeuchte, Rohdichte oder tatsächlicher Einklebequalität
  (Klebstoffmenge, Bohrlochtoleranz) zwischen den drei Prüfkörpern
  könnten sowohl zur Streuung zwischen den Prüfkörpern als auch —falls
  die Prüfkörper im Mittel günstiger ausfielen als die normativen
  Bemessungsannahmen— zum systematischen Überschreiten der
  FprEN-Vorhersage beitragen.

  Diese vier Mechanismen schließen sich nicht gegenseitig aus und sind
  hier bewusst als gleichrangige, ungeprüfte Kandidaten aufgeführt, nicht
  als abgestufte Wahrscheinlichkeiten.
motivated_by: >
  R2-GL24h-CALC-014 (Faktor ≈6,48, dort ausdrücklich "nur als Beobachtung
  festgehalten und nicht weiter gedeutet"); R2-GL24h-II-T-S-BR-22-RES-002
  (Streuung zwischen den drei Prüfkörpern, dort ausdrücklich "nicht
  weiter interpretiert ... wird hier bewusst nicht geraten");
  R2-GL24h-CALC-002 (Herkunft von `c_t` und `c_ax,f,par`); Aufgabenstellung
  Phase 3, Punkt "Einflussfaktoren statistisch untersuchen" — bislang der
  einzige noch unbearbeitete Teilpunkt dieser Phase für R2/GL24h.
tested_by: >
  Noch nicht getestet oder bestätigt. Mögliche künftige Prüfschritte,
  keiner davon bisher unternommen: (a) Prüfprotokoll/Messaufbau der
  BR-22-Versuche (Excel-Quelldatei, Wegaufnehmerpositionen) daraufhin
  prüfen, welche Bezugslänge die Wegaufnehmer 01-04 tatsächlich
  überspannen, und diese mit der im FprEN-Modell angesetzten freien
  Stangenlänge vergleichen (zu Hypothese 1); (b) Abgleich der
  FprEN-Verbundsteifigkeit mit unabhängiger Literatur zu eingeklebten
  Gewindestangen (zu Hypothese 2); (c) weitere Komponentenversuche mit
  variierter Stangenzahl/Anordnung, falls im Rahmen der Arbeit noch
  möglich (zu Hypothese 3); (d) Rücksprache mit der Betreuerin, ob eine
  vertiefte Klärung im Rahmen dieser Masterarbeit überhaupt noch
  vorgesehen ist, oder ob der gemessene Wert (gemäß COMMON-COMMON-DEC-006
  ohnehin als K_ser vorrangig vor der rein rechnerischen FprEN-Vorhersage
  verwendet wird) für die weitere Bearbeitung ausreicht und die Ursache
  als Grenze der Arbeit (Limitations) benannt wird, statt sie hier
  aufzulösen.
certainty: HYPOTHESIZED
superseded_by:
authored_by: CLAUDE_DRAFT
reviewed: false
---

## Ausgangslage

Zwei bislang unbewertete Beobachtungen zur selben Prüfkörperserie
(II-T-S-BR-22, 2×2-M16-Gewindestangengruppe, GL24h):

1. **Systematischer Faktor ≈6,48** zwischen gepooltem Versuchsmittelwert
   (K_ser=862,531 kN/mm, n=6, R2-GL24h-II-T-S-BR-22-RES-003) und rein
   rechnerischer FprEN-Vorhersage für denselben Teilanteil (133,115
   kN/mm, R2-GL24h-CALC-014).
2. **Erhebliche Streuung zwischen den drei Prüfkörpern** innerhalb der
   Messreihe selbst (K_ser oben: 418,71 bis 1440,00 kN/mm, Faktor ~3,4;
   K_e oben bis Faktor ~6,7), dokumentiert in
   R2-GL24h-II-T-S-BR-22-RES-002.

Beide Punkte wurden an ihrer jeweiligen Fundstelle bewusst nicht gedeutet
(CLAUDE.md Abschnitt 4 — keine Spekulation ohne Kennzeichnung). Dieser
Eintrag liefert erstmals eine gekennzeichnete, unbestätigte
Kandidatenliste möglicher Ursachen, wie von der Aufgabenstellung
(Phase 3, "Einflussfaktoren statistisch untersuchen") gefordert.

## Woher der Faktor 133,115 kN/mm rechnerisch kommt

Aus R2-GL24h-CALC-002 (Zwischenwerte je Zelle): der rein rechnerische
Anteil "4 Stangen ohne c_c,90" ergibt sich aus einer Serienschaltung von
`c_t=40.950 N/mm` (freie Stangendehnung) und `c_ax,f,par=177.646,15 N/mm`
(Verbund-Einklebesteifigkeit `K_SLS,w`, FprEN 11.3.8.3 (2)/Tab. 11.13 (3),
`l_w=320mm`) je Stange, danach 4 Stangen parallel:

```
c_Stange,ohne c_c,90 = (1/40.950 + 1/177.646,15)^-1 = 33.279 N/mm
4 Stangen parallel: 4 · 33.279 ≈ 133.115 N/mm
```

Bemerkenswert: `c_t` (40.950 N/mm) ist die weichere der beiden Federn und
dominiert das Ergebnis stärker als die eigentliche Verbund-/Klebefugen-
steifigkeit `c_ax,f,par`. Das rein rechnerische Ergebnis ist damit primär
eine Aussage über die angesetzte freie Stangendehnung, nicht in erster
Linie über das Verbundverhalten selbst — ein Grund, weshalb Hypothese (1)
oben (Bezugslängen-Diskrepanz) als eigenständiger, von der eigentlichen
Klebefugen-Frage unabhängiger Kandidat aufgeführt ist.

## Verhältnis zur Streuung

Ob die systematische Abweichung (Faktor ≈6,48, Mittelwertebene) und die
Streuung zwischen den Prüfkörpern (Faktor ~3,4, Einzelwertebene)
dieselbe Ursache haben, ist selbst eine offene Frage und wird hier nicht
unterstellt (CLAUDE.md Abschnitt 4 — keine Verknüpfung ohne Beleg).
Hypothese (4) (Prüfkörper-/Werkstoffstreuung) ist der einzige der vier
Kandidaten, der beide Beobachtungen gemeinsam erklären könnte; die
Hypothesen (1)-(3) beträfen in erster Linie die systematische Abweichung
und wären mit der beobachteten Streuung allein nicht unmittelbar
erklärbar — es sei denn, die zugrundeliegende Größe (z. B. die effektive
Bezugslänge) selbst schwankt zwischen den Prüfkörpern.

## Einordnung / Vorbehalt

`CLAUDE_DRAFT`, `reviewed: false` — vom Forschenden zu prüfen. Keiner der
vier Kandidaten ist bestätigt oder als wahrscheinlicher gekennzeichnet;
diese Liste ersetzt keine Prüfung der Rohdaten/Messprotokolle. Ändert
nichts an der bereits getroffenen Entscheidung (COMMON-COMMON-DEC-006),
für die Steifigkeitskette weiterhin den Versuchsmittelwert (K_ser) statt
der rein rechnerischen FprEN-Vorhersage zu verwenden — diese Hypothese
befasst sich ausschließlich mit der noch offenen Frage, *warum* beide
so weit auseinanderliegen, nicht damit, welcher Wert für die weitere
Bearbeitung maßgebend ist. Da eine vertiefte Klärung (Prüfschritte a-c
oben) über den Rahmen der laufenden Bearbeitung hinausgehen könnte, wird
empfohlen, mit der Betreuerin zu klären, ob dies im Rahmen der Arbeit
weiterverfolgt oder als offene Limitation benannt werden soll (siehe
`tested_by`, Punkt d) — ggf. als zusätzlicher Punkt für die ohnehin
anstehende Besprechung (neben R2-COMMON-OPQ-006/008/011).

## Update (2026-09-22, R2-GL24h-DEC-009): Kandidaten (1)-(3) gegenstandslos

Der Nutzer hat klargestellt, dass die Excel-Zeilen 124-178 (Sheet
"Rahmenecke GL24h SD"), aus denen der Vergleichswert 133,115 kN/mm
(R2-GL24h-CALC-014) sowie der unverstärkte `c_c,90` (R2-GL24h-CALC-001)
stammen, eine händische, vorerst ungültige Berechnung sind — weder als
Eingangsgröße noch als Vergleichsbasis zu verwenden (R2-GL24h-DEC-009).

**Konsequenz:** Der "Faktor ≈6,48" (Beobachtung 1 oben) ist damit keine
reale fachliche Diskrepanz, die einer Erklärung bedarf — er vergleicht
lediglich gegen eine unvollständige Handrechnung. Die Kandidaten
**(1) Bezugslängen-Diskrepanz**, **(2) konservative
FprEN-Verbundsteifigkeit** und **(3) Gruppenwirkung** waren ausschließlich
zur Erklärung dieses Faktors formuliert und sind damit **gegenstandslos**
— sie werden hier nicht gelöscht (CLAUDE.md Abschnitt 13), gelten aber
nicht mehr als zu prüfende Hypothesen.

**Weiterhin gültig und offen:** Kandidat **(4) Prüfkörper-/
Werkstoffstreuung** bleibt als Erklärungsansatz für Beobachtung 2 (die
reale, versuchsbasierte Streuung zwischen den drei BR-22-Prüfkörpern,
R2-GL24h-II-T-S-BR-22-RES-002, Faktor ~3,4 bei K_ser) unverändert
bestehen — diese Streuung selbst ist von R2-GL24h-DEC-009 nicht betroffen
und weiterhin ungeklärt. Der Abschnitt "Verhältnis zur Streuung" oben
bleibt entsprechend nur noch für Kandidat (4) relevant.

Die Aufgabenstellungs-Phase-3-Anforderung ("Einflussfaktoren statistisch
untersuchen") ist damit für R2/GL24h nur noch teilweise offen: nicht mehr
für einen (nicht existenten) Versuch-vs-FprEN-Vergleich, sondern
weiterhin für die Ursache der Prüfkörperstreuung selbst.
