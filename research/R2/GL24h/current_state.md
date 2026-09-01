---
scope:
  connection: R2
  material: GL24h
last_updated: "2026-09-01"
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
vollständig vor (`c_T≈38,39 kN/mm`, R2-GL24h-CALC-001–004 — die dortige
`c_c,90`-Herleitung setzt weiterhin bewusst einseitige Lastausbreitung
an; der Nutzer hat am 2026-09-01 entschieden, diese Zugseiten-Kette
**nicht** auf beidseitig umzustellen — Begründung: die Stahlplatte
liegt hier direkt am Trägerrand, sodass geometrisch nur eine einseitige
Ausbreitung möglich ist, siehe R2-GL24h-DEC-008). Die
FprEN-Querdruckfestigkeit wurde am 2026-09-01 korrigiert: unverstärkt
jetzt `≈262,38 kN` (R2-GL24h-CALC-010, zuvor `≈224,29 kN` in
R2-GL24h-CALC-005 — Fehler: nur einseitige statt beidseitige
Lastausbreitung; identisch bestätigt auf Blatt "GL24h HD",
R2-GL24h-CALC-013) und ASSY-verstärkt jetzt `≈384,12 kN`
(R2-GL24h-CALC-011, zuvor `≈248,85 kN` in R2-GL24h-CALC-006 — Fehler:
`k_mat=1,0` aus dem Ausziehwiderstands-Kontext fälschlich für den
Holzanteil-Term übernommen statt `k_mat=1,75` nach 8.1.6.2(6)). Die
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
vollständige Rotationsmodell der Rahmenecke stehen noch aus — blockiert
durch die ungeklärte Druckzonen-Geometrie (R2-COMMON-OPQ-001). Reale
Komponentenversuche (Stabdübel-Push-Out, Gewindestangen-Zug) liegen als
eigene Versuchsergebnis-Einträge vor, ihre genaue Rolle im
R2-Gesamtkonzept ist größtenteils weiter ungeklärt (Stabdübel-Nachweis,
VSP-Blätter, R2-COMMON-OPQ-008) — die Rolle des
"Tragfähigkeit Stütze auf Zug"-Blocks ist dagegen inzwischen ausreichend
geklärt: er liefert einen der drei Kandidatenwerte für die
`M_max`-maßgebende Komponente (siehe R2-GL24h-CALC-012), verwendet
bewusst Mittelwerte der Holzfestigkeit (wie alle Tragfähigkeiten dieser
Tabelle), und seine unklare Normzitat-Beschriftung wird vom Nutzer nicht
weiterverfolgt (R2-COMMON-OPQ-008).

## Wichtigste Einträge

- Entscheidungen: R2-GL24h-DEC-001–008 (u. a. freie Stangenlänge,
  Federmodell-Topologie, SWB-Klassifikation, ASSY-Geometrie,
  Schrauben-Knicken maßgebend, DEC-008: einseitige Lastausbreitung bei
  `c_c,90` bleibt bestehen); siehe auch R2-COMMON-DEC-001 und
  COMMON-COMMON-DEC-001–004 für projektweite/materialunabhängige Punkte.
- Berechnungen: R2-GL24h-CALC-001–013 (Zugseiten-Steifigkeitskette,
  unverstärkte/verstärkte Querdruckfestigkeit, Schrauben-Knick-
  tragfähigkeit, Momenten-Abschätzung, Stabdübel-Johansen-Nachweis mit
  ungeklärter Rolle; CALC-010/011 korrigieren CALC-005/006, CALC-012
  korrigiert CALC-008, CALC-013 ist ein Cross-Check-Eintrag ohne
  Vorgänger, siehe jeweils `superseded_by`-Feld der alten Einträge).
- Annahmen: — (materialunabhängige Annahmen siehe R2-COMMON-ASS-001–005).
- Versuchsergebnisse: R2-GL24h-II-PO-S-SD-34-RES-001,
  R2-GL24h-II-PO-S-WD-34-RES-001, R2-GL24h-II-T-S-BR-22-RES-001.
- Interpretationen/Schlussfolgerungen: — (frühere Beobachtung zum
  materialabhängigen Versagensmodus in R2-GL24h-CALC-008 durch die
  Korrektur in R2-GL24h-CALC-012 überholt — GL24h und GL75 werden jetzt
  rechnerisch durch denselben Mechanismus [Gewindestangenzug] begrenzt;
  weiterhin nur als Freitext vermerkt, nicht als eigene INT-Einträge,
  `CLAUDE_DRAFT` — noch vom Forschenden zu prüfen).

## Offene Fragen / bekannte Widersprüche

R2-GL24h-OPQ-001–002 offen; R2-GL24h-OPQ-003 (Gl. 8.13 vs. 8.14 bei
`l_1,ef`) am 2026-09-01 RESOLVED (Zwischenauflager, Gl. 8.14). Dazu 8
materialunabhängige offene Fragen unter
`research/R2/COMMON/open_questions/` (R2-COMMON-OPQ-001–008, davon
OPQ-009 bereits gelöst durch COMMON-COMMON-DEC-004).

## Nächste Schritte

Druckzonen-Geometrie klären (R2-COMMON-OPQ-001), dann `c_c,90`/`c_c,0`
und vollständiges Rotationsmodell (R2-COMMON-OPQ-006); Klärung der Rolle
des Stabdübel-Nachweises und der VSP-Excel-Blätter mit dem Nutzer
(R2-COMMON-OPQ-008, Punkte 1/3/4 weiterhin offen — Punkt 2,
"Stütze auf Zug"-Block, ist inzwischen ausreichend geklärt: Rolle im
Rechenschema als MIN-Kandidat für `M_max` sowie die bewusste
Mittelwertbasis sind bestätigt, die genaue Normzuordnung der
Zellbeschriftung "Gl. 11.14" wird vom Nutzer nicht weiterverfolgt).
