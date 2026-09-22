---
interpretation_id: R2-GL24h-INT-002
scope:
  connection: R2
  material: GL24h
type: INTERPRETATION
based_on:
  experimental_results: R2-GL24h-II-T-S-BR-22-RES-003
  observations: R2-COMMON-CALC-001, R2-GL24h-CALC-003, R2-GL24h-CALC-014, R2-GL24h-CALC-021
interpretation: >
  Neufassung von R2-GL24h-INT-001 mit dem aktuellen c_T
  (R2-GL24h-CALC-021, 53,300 kN/mm, mit ASSY-verstärktem statt
  unverstärktem c_c,90). Die qualitative Kernaussage von INT-001 bleibt
  unverändert gültig: c_T ist eine Serienschaltung, in der die
  Stangengruppe (jetzt versuchsgestützt, 862,531 kN/mm) praktisch als
  limitierender Faktor herausfällt (Anteil an der Gesamt-Nachgiebigkeit
  nur noch ≈6,2 %), während c_c,90 (≈47,9 %) und c_v,ges (≈46,0 %)
  zusammen weiterhin ≈93,8 % der Nachgiebigkeit bestimmen — beide nach
  wie vor rein rechnerisch (c_c,90: Bejtka-Modell, nicht mit der
  Betreuerin abgestimmt; c_v,ges: FprEN-Schubfeldansatz), keine der
  beiden durch einen eigenen Komponentenversuch abgesichert. c_T liegt
  bei 53,300 kN/mm bei ≈93,8 % der theoretischen Obergrenze (56,810
  kN/mm bei Stangengruppe → unendlich steif) — die Sättigung ist damit
  praktisch unverändert zu INT-001 (dort 94,1 %). Zusätzlich: die in
  R2-GL24h-CALC-021 getroffene Aussage, c_v,ges sei "jetzt die weichste
  Einzelkomponente", ist bei Nachrechnung nicht zutreffend — c_c,90
  (111,339 kN/mm) bleibt geringfügig weicher als c_v,ges (116,0 kN/mm);
  beide liegen mit ≈4 % Abstand aber praktisch gleichauf, sodass die
  übergeordnete Schlussfolgerung (beide zusammen dominieren die Kette)
  davon unberührt bleibt.
certainty: INTERPRETED
superseded_by:
authored_by: CLAUDE_DRAFT
reviewed: true
---

## Ausgangslage

R2-GL24h-CALC-021 ersetzt R2-GL24h-CALC-015 als aktuellen Wert für `c_T`
(50,776 → 53,300 kN/mm, +5,0 %), durch Einsetzen des ASSY-verstärkten
statt unverstärkten `c_c,90` (R2-COMMON-CALC-001 statt R2-GL24h-CALC-001).
R2-GL24h-INT-001 wurde bereits am 2026-09-17 als dadurch teilweise
veraltet markiert ("Neufassung steht noch aus"); dieser Eintrag löst das
ein.

## Aktuelle Zusammensetzung von c_T (CALC-021-Topologie, 4 Glieder)

```
1/c_T = 1/c_Stange,4x + 1/c_t,ep + 1/c_c,90 + 1/c_v,ges
```

| Komponente | Wert | Quelle | Anteil an 1/c_T |
|---|---|---|---|
| c_Stange,4x | 862,531 kN/mm (Versuch, K_ser, n=6) | RES-003 | 6,18 % |
| c_t,ep | 1e99 (vernachlässigt) | Excel-Annahme | ≈0 % |
| c_c,90 | 111,339 kN/mm (ASSY-verstärkt, A=1) | R2-COMMON-CALC-001 | 47,87 % |
| c_v,ges | 116,0 kN/mm | R2-GL24h-CALC-003 | 45,95 % |
| **c_T** | **53,300 kN/mm** | R2-GL24h-CALC-021 | 100 % |

Zum Vergleich die in INT-001 dokumentierte, jetzt überholte Aufteilung
(CALC-015-Topologie, unverstärktes `c_c,90=100,866 kN/mm`): Stange 5,9 %,
c_c,90 50,3 %, c_v,ges 43,8 %. Die Verschiebung gegenüber der Neufassung
ist gering — die ASSY-Verstärkung macht `c_c,90` steifer und verringert
dadurch dessen Anteil leicht zugunsten von `c_v,ges` und der
Stangengruppe, ändert aber nichts an der grundsätzlichen Aussage.

## Theoretische Obergrenze

```
c_T,max = (1/c_c,90 + 1/c_v,ges)^-1 = (1/111,339 + 1/116,0)^-1 = 56,810 kN/mm
```

`c_T=53,300 kN/mm` liegt bei `53,300/56,810 = 93,8 %` dieser Obergrenze
(INT-001, alte Rechnung: 94,1 %) — praktisch identischer Sättigungsgrad.
Weitere Verbesserungen der Stangengruppen-Steifigkeit (z. B. durch
weitere Versuche oder größere Stangendurchmesser) würden `c_T` kaum noch
nennenswert erhöhen.

## Korrektur zu R2-GL24h-CALC-021: welche Komponente ist "weichste"?

CALC-021 beschreibt `c_v,ges` (116,0 kN/mm) als "jetzt die weichste
Einzelkomponente der Kette", nachdem `c_c,90` durch die ASSY-Verstärkung
von 100,866 auf 111,339 kN/mm gestiegen ist. Bei genauer Nachrechnung
ist das nicht korrekt: `c_c,90=111,339 kN/mm` ist weiterhin (knapp)
kleiner als `c_v,ges=116,0 kN/mm` und bleibt damit die geringfügig
weichste Komponente — der Abstand hat sich durch die Verstärkung nur
von `100,866` auf `111,339 kN/mm` verringert (beide liegen jetzt
innerhalb von `≈4 %`, praktisch gleichauf). Für das Gesamtergebnis
(`c_T`, Sättigungsgrad, dominierende Rolle von `c_c,90`+`c_v,ges`
zusammen) ändert diese Korrektur nichts, da beide Komponenten ohnehin
gemeinsam betrachtet werden — sie betrifft nur die einzelne Aussage,
welche der beiden marginal weicher ist.

## Konsequenz für die weitere Bearbeitung

Unverändert gegenüber INT-001: Da `c_c,90` und `c_v,ges` zusammen fast
die gesamte Nachgiebigkeit von `c_T` bestimmen und beide ausschließlich
rechnerisch hergeleitet sind (keine eigenen Komponentenversuche), hängt
die Verlässlichkeit von `c_T` — und damit von `S_j,ini`
(R2-GL24h-CALC-022) — primär an der fachlichen Absicherung dieser beiden
Größen, nicht an weiteren Zugversuchen der Stangengruppe. Für `c_c,90`
kommt hinzu, dass der verwendete ASSY-verstärkte Wert selbst noch nicht
mit der Betreuerin abgestimmt ist (R2-COMMON-CALC-001, Status-Hinweis).

## Einordnung

`CLAUDE_DRAFT`, `reviewed: true` (2026-09-22, vom Forschenden bestätigt
im Chat: "die Neufassung stimmt"). Löst die in R2-GL24h-CALC-021
hinterlassene Anmerkung ("R2-GL24h-INT-001 … sollte bei Gelegenheit mit
den neuen Zahlen nachgezogen werden") ein. Der in
R2-GL24h-CALC-014 offen gelassene, gesonderte Punkt — warum die
Stangengruppe selbst um Faktor ≈6,48 über der FprEN-Vorhersage liegt —
wird auch hier nicht behandelt und bleibt weiterhin offen.
