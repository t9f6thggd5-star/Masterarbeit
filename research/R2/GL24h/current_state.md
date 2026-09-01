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
vollständig vor (`c_T≈38,39 kN/mm`), ebenso die FprEN-Querdruck-
festigkeit unverstärkt (`≈224,29 kN`) und ASSY-verstärkt
(`≈248,85 kN`, maßgebender Widerstandsmechanismus für GL24h) sowie eine
Momenten-Abschätzung (`M_max≈139,35 kNm`). Die Druckseiten-Steifigkeit
(`c_c,90`, `c_c,0`) und damit das vollständige Rotationsmodell der
Rahmenecke stehen noch aus — blockiert durch die ungeklärte
Druckzonen-Geometrie (R2-COMMON-OPQ-001). Reale Komponentenversuche
(Stabdübel-Push-Out, Gewindestangen-Zug) liegen als eigene
Versuchsergebnis-Einträge vor, ihre genaue Rolle im R2-Gesamtkonzept
(insbesondere der Stabdübel-Block) ist aber ungeklärt (R2-COMMON-OPQ-008).

## Wichtigste Einträge

- Entscheidungen: R2-GL24h-DEC-001–007 (u. a. freie Stangenlänge,
  Federmodell-Topologie, SWB-Klassifikation, ASSY-Geometrie,
  Schrauben-Knicken maßgebend); siehe auch R2-COMMON-DEC-001 und
  COMMON-COMMON-DEC-001–004 für projektweite/materialunabhängige Punkte.
- Berechnungen: R2-GL24h-CALC-001–009 (Zugseiten-Steifigkeitskette,
  unverstärkte/verstärkte Querdruckfestigkeit, Schrauben-Knick-
  tragfähigkeit, Momenten-Abschätzung, Stabdübel-Johansen-Nachweis mit
  ungeklärter Rolle).
- Annahmen: — (materialunabhängige Annahmen siehe R2-COMMON-ASS-001–005).
- Versuchsergebnisse: R2-GL24h-II-PO-S-SD-34-RES-001,
  R2-GL24h-II-PO-S-WD-34-RES-001, R2-GL24h-II-T-S-BR-22-RES-001.
- Interpretationen/Schlussfolgerungen: — (Beobachtungen zum
  materialabhängigen Versagensmodus bisher nur als Freitext in
  R2-GL24h-CALC-008 vermerkt, nicht als eigene INT-Einträge, `CLAUDE_DRAFT`
  — noch vom Forschenden zu prüfen).

## Offene Fragen / bekannte Widersprüche

R2-GL24h-OPQ-001–002 (materialspezifisch); dazu 8 materialunabhängige
offene Fragen unter `research/R2/COMMON/open_questions/`
(R2-COMMON-OPQ-001–008, davon OPQ-009 bereits gelöst durch
COMMON-COMMON-DEC-004).

## Nächste Schritte

Druckzonen-Geometrie klären (R2-COMMON-OPQ-001), dann `c_c,90`/`c_c,0`
und vollständiges Rotationsmodell (R2-COMMON-OPQ-006); Klärung der Rolle
des Stabdübel-/Stütze-auf-Zug-/VSP-Excel-Inhalts mit dem Nutzer
(R2-COMMON-OPQ-008).
