---
scope:
  connection: R2
  material: GL24h
last_updated: "2026-09-16"
---

# Bearbeitungsstand: R2 / GL24h

Kurze, laufend aktualisierte Zusammenfassung — kein Ersatz für die
strukturierten Einträge in `research/R2/GL24h/`, sondern ein
schneller Überblick darüber, was dort schon existiert. Diese Datei selbst
trägt keine eigene ID (sie ist kein Claim/Ergebnis, siehe `schema.yaml`
Abschnitt "ID naming convention") und wird nicht von
`scripts/build_index.py` katalogisiert.

## Zusammenfassung

R2 = Rahmenecke mit eingeklebten Gewindestangen (4× M16). Bearbeitung
befindet sich in Phase 2 (Verformungs-/Steifigkeitsabschätzung, siehe
COMMON-COMMON-DEC-003). Für GL24h liegt die Zugseiten-Steifigkeitskette
vollständig vor und wurde inzwischen teilweise durch Versuchsdaten
ersetzt: der rein rechnerische Anteil "vier Stangen ohne Querdruck"
(133,12 kN/mm nach FprEN) wurde durch den gepoolten Messwert der
BR-22-Zugversuche (K_ser, n=6, 862,531 kN/mm,
R2-GL24h-II-T-S-BR-22-RES-003) ersetzt — der Messwert liegt um den
Faktor ≈6,48 über der FprEN-Vorhersage für denselben Teilanteil
(R2-GL24h-CALC-014, `CLAUDE_DRAFT`-Beobachtung, noch nicht als eigene
Interpretation dokumentiert/geprüft). Der Querdruckanteil `c_c,90`
selbst bleibt rein rechnerisch (R2-GL24h-CALC-001, nicht Teil des
Versuchsaufbaus). Damit ergibt sich `c_T≈50,78 kN/mm`
(R2-GL24h-CALC-015, +32,3 % gegenüber dem bisherigen rein rechnerischen
Wert `38,39 kN/mm`, R2-GL24h-CALC-004 — jetzt superseded). Die
1×1-Versuchsserie (BR-11) wird für die Kette vorerst nicht verwendet, da
der Nutzer entschieden hat, ausschließlich auf BR-22 (deckt bereits alle
vier Stangen ab) zurückzugreifen. Die dortige `c_c,90`-Herleitung selbst
setzt weiterhin bewusst einseitige Lastausbreitung an; der Nutzer hat am
2026-09-01 entschieden, diese Zugseiten-Kette **nicht** auf beidseitig
umzustellen — Begründung: die Stahlplatte liegt hier direkt am
Trägerrand, sodass geometrisch nur eine einseitige Ausbreitung möglich
ist, siehe R2-GL24h-DEC-008). Die FprEN-Querdruckfestigkeit wurde am
2026-09-01 korrigiert: unverstärkt jetzt `≈262,38 kN`
(R2-GL24h-CALC-010, zuvor `≈224,29 kN` in R2-GL24h-CALC-005 — Fehler:
nur einseitige statt beidseitige Lastausbreitung; identisch bestätigt
auf Blatt "GL24h HD", R2-GL24h-CALC-013) und ASSY-verstärkt jetzt
`≈384,12 kN` (R2-GL24h-CALC-011, zuvor `≈248,85 kN` in R2-GL24h-CALC-006
— Fehler: `k_mat=1,0` aus dem Ausziehwiderstands-Kontext fälschlich für
den Holzanteil-Term übernommen statt `k_mat=1,75` nach 8.1.6.2(6)). Die
Rangfolge unverstärkt < verstärkt ist damit wieder plausibel. Die
Momenten-Abschätzung wurde entsprechend nachgezogen
(R2-GL24h-CALC-012, `M_max≈160,03 kNm`, zuvor `≈139,35 kNm` in
R2-GL24h-CALC-008): die maßgebende Komponente ist dabei tatsächlich vom
verstärkten Querdruck auf das Gewindestangen-Zugversuchsmittel
(`285,77 kN`) gewechselt — GL24h und GL75 werden rechnerisch jetzt durch
denselben Mechanismus begrenzt. Die Frage, ob `l_1,ef` nach Gl. 8.13
oder 8.14 anzusetzen ist, wurde geklärt (R2-GL24h-OPQ-003, RESOLVED —
bewusst als Zwischenauflager, Gl. 8.14, `l_1,ef=300 mm` unverändert
korrekt). Die Druckseiten-Steifigkeit (`c_c,90`, `c_c,0`) und damit das
vollständige Rotationsmodell der Rahmenecke stehen noch aus. Der
bisherige Blocker dafür ist inzwischen aufgelöst: die Betreuerin hat am
2026-09-04 festgelegt, die Druckzone als RECHTECKIG anzusetzen, mit dem
Hebelarm mittig in der Druckzone (R2-COMMON-DEC-002, löst
R2-COMMON-OPQ-001). Offen bleibt damit noch die konkrete Bestimmung der
Druckzonenhöhe selbst sowie die Kombination von Zug- und
Druckseiten-Steifigkeit zu einer vollständigen Rotationssteifigkeit
(R2-COMMON-OPQ-006). Reale Komponentenversuche (Stabdübel-Push-Out,
Gewindestangen-Zug 2×2 und 1×1) liegen als eigene Versuchsergebnis-
Einträge vor, ihre genaue Rolle im R2-Gesamtkonzept ist größtenteils
weiter ungeklärt (Stabdübel-Nachweis, VSP-Blätter, R2-COMMON-OPQ-008) —
die Rolle des "Tragfähigkeit Stütze auf Zug"-Blocks ist dagegen
inzwischen ausreichend geklärt: er liefert einen der drei
Kandidatenwerte für die `M_max`-maßgebende Komponente (siehe
R2-GL24h-CALC-012), verwendet bewusst Mittelwerte der Holzfestigkeit
(wie alle Tragfähigkeiten dieser Tabelle), und seine unklare
Normzitat-Beschriftung wird vom Nutzer nicht weiterverfolgt
(R2-COMMON-OPQ-008).

## Wichtigste Einträge

- Entscheidungen: R2-GL24h-DEC-001–008 (u. a. freie Stangenlänge,
  Federmodell-Topologie, SWB-Klassifikation, ASSY-Geometrie,
  Schrauben-Knicken maßgebend, DEC-008: einseitige Lastausbreitung bei
  `c_c,90` bleibt bestehen); siehe auch R2-COMMON-DEC-001–003 (DEC-002:
  rechteckige Druckzone, Hebelarm mittig, löst R2-COMMON-OPQ-001;
  DEC-003: Anfangssteifigkeit je Gruppe wird durchgängig aus Blatt
  "Überblick", Zellen B94:B97 der Steifigkeiten-Auswertungsdatei
  angesetzt) und COMMON-COMMON-DEC-001–004 für projektweite/
  materialunabhängige Punkte.
- Berechnungen: R2-GL24h-CALC-001–015 (Zugseiten-Steifigkeitskette,
  unverstärkte/verstärkte Querdruckfestigkeit, Schrauben-Knick-
  tragfähigkeit, Momenten-Abschätzung, Stabdübel-Johansen-Nachweis mit
  ungeklärter Rolle; CALC-010/011 korrigieren CALC-005/006, CALC-012
  korrigiert CALC-008, CALC-013 ist ein Cross-Check-Eintrag ohne
  Vorgänger, CALC-014 korrigiert/ersetzt CALC-002 durch den BR-22-
  Messwert, CALC-015 korrigiert/ersetzt CALC-004 entsprechend — siehe
  jeweils `superseded_by`-Feld der alten Einträge).
- Annahmen: — (materialunabhängige Annahmen siehe R2-COMMON-ASS-001–005).
- Versuchsergebnisse: R2-GL24h-II-PO-S-SD-34-RES-001,
  R2-GL24h-II-PO-S-WD-34-RES-001, R2-GL24h-II-T-S-BR-22-RES-001,
  R2-GL24h-II-T-S-BR-11-RES-001, R2-GL24h-II-T-S-BR-11-RES-002
  (Steifigkeiten K_ser/K_e), R2-GL24h-II-T-S-BR-22-RES-002
  (Steifigkeiten, deutlich größere Streuung als bei der 11er-Serie),
  R2-GL24h-II-T-S-BR-22-RES-003 (gepoolter K_ser-Mittelwert oben+unten,
  n=6, 862,531 kN/mm — jetzt Eingangswert von R2-GL24h-CALC-014),
  R2-GL24h-II-T-S-BR-11-RES-003 (analog gepoolt, 203,303 kN/mm, bisher
  nicht in einer Kette verwendet, siehe R2-COMMON-DEC-003).
- Interpretationen/Schlussfolgerungen: — (frühere Beobachtung zum
  materialabhängigen Versagensmodus in R2-GL24h-CALC-008 durch die
  Korrektur in R2-GL24h-CALC-012 überholt — GL24h und GL75 werden jetzt
  rechnerisch durch denselben Mechanismus [Gewindestangenzug] begrenzt;
  weiterhin nur als Freitext vermerkt, nicht als eigene INT-Einträge,
  `CLAUDE_DRAFT` — noch vom Forschenden zu prüfen. Neu: der Faktor
  ≈6,48 zwischen gemessener und FprEN-rechnerischer Stangengruppen-
  Steifigkeit in R2-GL24h-CALC-014, ebenfalls nur als Freitext-
  Beobachtung, `CLAUDE_DRAFT`, noch nicht gedeutet).

## Offene Fragen / bekannte Widersprüche

R2-GL24h-OPQ-001–002 offen; R2-GL24h-OPQ-003 (Gl. 8.13 vs. 8.14 bei
`l_1,ef`) am 2026-09-01 RESOLVED (Zwischenauflager, Gl. 8.14). Dazu 10
materialunabhängige offene Fragen unter
`research/R2/COMMON/open_questions/` (R2-COMMON-OPQ-001–010), davon
OPQ-001 (Druckzonen-Geometrie) am 2026-09-04 RESOLVED durch
Betreuerin-Entscheidung (rechteckige Druckzone, Hebelarm mittig,
R2-COMMON-DEC-002) und OPQ-009 bereits gelöst durch COMMON-COMMON-DEC-004.

## Nächste Schritte

Konkrete Druckzonenhöhe bestimmen und darauf aufbauend `c_c,90`/`c_c,0`
sowie vollständiges Rotationsmodell aufstellen (R2-COMMON-OPQ-006, jetzt
durch R2-COMMON-DEC-002 freigegeben); Klärung der Rolle des
Stabdübel-Nachweises und der VSP-Excel-Blätter mit dem Nutzer
(R2-COMMON-OPQ-008, Punkte 1/3/4 weiterhin offen — Punkt 2,
"Stütze auf Zug"-Block, ist inzwischen ausreichend geklärt: Rolle im
Rechenschema als MIN-Kandidat für `M_max` sowie die bewusste
Mittelwertbasis sind bestätigt, die genaue Normzuordnung der
Zellbeschriftung "Gl. 11.14" wird vom Nutzer nicht weiterverfolgt).
Perspektivisch: den auffälligen Faktor ≈6,48 zwischen BR-22-Messwert
und FprEN-Vorhersage (R2-GL24h-CALC-014) fachlich einordnen (eigene
INTERPRETATION, noch nicht angelegt).
