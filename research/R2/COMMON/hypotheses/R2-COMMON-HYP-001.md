---
hypothesis_id: R2-COMMON-HYP-001
scope:
  connection: R2
  material: COMMON
type: HYPOTHESIS
statement: >
  Die Zugseiten- und Druckseiten-Gesamtsteifigkeit (`c_T`, `c_C`) lassen
  sich über den inneren Hebelarm `z` (Abstand Zugkraft-Druckkraft-
  Resultierende) zur Anfangsrotationssteifigkeit der Rahmenecke
  kombinieren gemäß:

    S_j,ini = z² / (1/c_T + 1/c_C) = z² · c_T·c_C / (c_T+c_C)

  Herleitung: Zug- und Druckfeder sitzen im Abstand `z` auf einer
  gemeinsamen Linie und sind über einen als starr angenommenen Balken
  verbunden, der um ein (durch das Kräftegleichgewicht bestimmtes)
  Rotationszentrum `x₀` um den Winkel `φ` rotiert (T/C/z/φ-Topologie
  nach Fig. 7, siehe R2-COMMON-CLAIM-031). Zugfeder `T` bei `x=0`,
  Druckfeder `C` bei `x=z`. Aus der Starrkörperkinematik folgt für die
  Federverschiebungen `δ_T=φ·x₀` bzw. `δ_C=φ·(z-x₀)` (bei vertauschter
  Anordnung symmetrisch `δ_T=φ·(z-x₀)`, `δ_C=φ·x₀` — das Ergebnis ist
  in beiden Fällen identisch, siehe unten). Aus dem Momentengleichgewicht
  (reines Kräftepaar, `c_T·δ_T = c_C·δ_C`) folgt
  `x₀ = c_C·z/(c_T+c_C)` und damit `M = φ·z²·c_T·c_C/(c_T+c_C)`, also
  obige Formel für `S_j,ini = M/φ`.
  Strukturell analog zur Bauteilmethode für Stahlanschlüsse (EN
  1993-1-8, 6.3.1) und konsistent mit der Fig.-7-Topologie, aber eine
  eigene mechanische Herleitung — keine wörtliche Formel aus
  FragiacomoBatchelar2012a (die Quelle liefert laut R2-COMMON-CLAIM-001/
  031 nur die Topologie, keine Kombinationsformel).
motivated_by: >
  R2-COMMON-OPQ-006 (wie werden c_T und c_C zur Rotationssteifigkeit
  kombiniert?), R2-COMMON-CLAIM-031 (T/C/z/φ-Topologie, Fig. 7
  FragiacomoBatchelar2012a), R2-COMMON-DEC-004 (Druckpfad-Topologie).
tested_by: >
  Noch nicht getestet/bestätigt. Mögliche künftige Prüfung: Vergleich
  der daraus berechneten Momenten-Rotationskurve mit den in Phase 4
  vorgesehenen realen Rahmenecken-Vollverbindungsversuchen (siehe
  COMMON-COMMON-DEC-003); fachliche Rücksprache mit der Betreuerin zur
  grundsätzlichen Eignung des Zwei-Feder-Rotationsmodells steht noch
  aus.
certainty: HYPOTHESIZED
superseded_by:
authored_by: CLAUDE_DRAFT
reviewed: false
---

## Herleitung im Detail

Koordinate `x` entlang des Hebelarms, Zugfeder `T` bei `x=0`,
Druckfeder `C` bei `x=z`, Rotationszentrum bei `x=x₀` (zunächst
unbekannt):

```
x=0 (T)                      x=x₀                          x=z (C)
  |---------------------------|------------------------------|
  |<---------- x₀ ----------->|<---------- z-x₀ ------------>|
```

Starrkörperrotation um `φ`: Verschiebung eines Punkts = `φ · Abstand
von x₀`. Damit `δ_T = φ·x₀`, `δ_C = φ·(z-x₀)`.

Gleichgewicht (reines Moment, keine Normalkraft, also Zug- und
Druckkraft betragsgleich): `c_T·δ_T = c_C·δ_C`, eingesetzt
`c_T·x₀ = c_C·(z-x₀)`, aufgelöst `x₀ = c_C·z/(c_T+c_C)`.

Moment über die Zugfeder: `M = F·z = c_T·δ_T·z = c_T·φ·x₀·z`.
Einsetzen von `x₀` ergibt nach Umformen:

```
M = φ · z² · c_T·c_C/(c_T+c_C)
S_j,ini = M/φ = z²/(1/c_T + 1/c_C)
```

**Zahlenbeispiel (GL24h, siehe R2-GL24h-CALC-022):** mit
`c_T=53,300 kN/mm`, `c_C=160,137 kN/mm`, `z=560mm`:
`x₀ = c_C·z/(c_T+c_C) = 160,137·560/213,437 ≈ 420,2mm` (Abstand von
`T`), `z-x₀ ≈ 139,8mm` (Abstand von `C`) — das Rotationszentrum liegt
näher an der steiferen Feder `C`, wie erwartet.

**Vertauschungsprobe:** Tauscht man die Positionen (Druckfeder bei
`x=0`, Zugfeder bei `x=z`), ergibt dieselbe Herleitung
`x₀=c_T·z/(c_T+c_C)` und wieder `S_j,ini=z²/(1/c_T+1/c_C)` — die
Formel ist symmetrisch in `c_T`/`c_C`, nur die Lage von `x₀` selbst
"wandert" mit der Vertauschung an die jeweils andere Seite (das
Rotationszentrum liegt stets näher an der steiferen der beiden
Federn).

**Hinweis zur Orientierung (2026-09-18):** Diese Fassung führt `T` bei
`x=0` und `C` bei `x=z` als Hauptdarstellung, auf Wunsch des Nutzers
(entspricht dessen eigener Skizzenkonvention); zuvor war es umgekehrt
(`C` bei `x=0`, `T` bei `x=z`, jetzt die Vertauschungsprobe oben).
Reine Darstellungsfrage, keine inhaltliche Änderung — Endformel und
Zahlenwert (R2-GL24h-CALC-022) sind unverändert.

## Einordnung / Vorbehalt

Diese Formel ist eine eigene, in sich schlüssige mechanische
Herleitung (Starrkörperkinematik + Kräftegleichgewicht), keine
wörtlich aus der Literatur übernommene Gleichung. Sie ist strukturell
konsistent mit der Fig.-7-Topologie (T/C/z/φ, R2-COMMON-CLAIM-031) und
mathematisch analog zur klassischen Bauteilmethode für Stahlanschlüsse
(EN 1993-1-8, 6.3.1, dort `S_j,ini = E·z²/Σ(1/k_i)`), aber weder von
FragiacomoBatchelar2012a noch von einer anderen hier verwendeten
Quelle wörtlich bestätigt. `CLAUDE_DRAFT`, `reviewed: false` — vom
Forschenden und nach Möglichkeit mit der Betreuerin zu prüfen, bevor
sie als methodische Grundlage der vollständigen Rotationssteifigkeit
gilt. Löst R2-COMMON-OPQ-006 noch nicht endgültig (Status dort bleibt
`OPEN`), liefert aber die erste konkrete Kombinationsmethodik und ein
erstes Zahlenergebnis (siehe R2-GL24h-CALC-022).
