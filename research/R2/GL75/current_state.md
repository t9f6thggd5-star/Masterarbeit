---
scope:
  connection: R2
  material: GL75
last_updated: 2026-09-01
---

# Bearbeitungsstand: R2 / GL75

Kurze, laufend aktualisierte Zusammenfassung — kein Ersatz für die
strukturierten Einträge in `research/R2/GL75/`, sondern ein
schneller Überblick darüber, was dort schon existiert. Diese Datei selbst
trägt keine eigene ID (sie ist kein Claim/Ergebnis, siehe `schema.yaml`
Abschnitt "ID naming convention") und wird nicht von
`scripts/build_index.py` katalogisiert.

## Zusammenfassung

R2 = Rahmenecke mit eingeklebten Gewindestangen, Materialvariante
GL75 (= BauBuche/Pollmeier-Furnierschichtholz, siehe
COMMON-COMMON-DEC-004). Für GL75 liegt im R2-Excel nur der
Festigkeitsnachweis vor (Stabdübel-Johansen mit ungeklärter Rolle,
Momenten-Abschätzung `M_max≈162,96 kNm`); eine Zugseiten-
Steifigkeitskette und ein ASSY-Verstärkungsblock existieren für GL75 —
anders als für GL24h — bisher gar nicht im Excel (R2-GL75-OPQ-001/002).
Anders als bei GL24h ist für GL75 rechnerisch die Gewindestangen-
Zugtragfähigkeit (`291,00 kN`), nicht die Querdruckfestigkeit, der
maßgebende Widerstandsmechanismus. Die unverstärkte
Querdrucktragfähigkeit wurde am 2026-09-01 korrigiert: jetzt
`≈1.206,82 kN` (R2-GL75-CALC-004, zuvor `≈1.031,65 kN` in
R2-GL75-CALC-002 — dieselbe einseitig-statt-beidseitig-Lastausbreitungs-
Korrektur wie bei GL24h, siehe R2-GL24h-CALC-010). Da bereits der alte
Wert weit über der Gewindestangen-Zugtragfähigkeit lag, ändert diese
Korrektur weder die maßgebende Komponente noch `M_max`
(R2-GL75-CALC-003 bleibt unverändert gültig).

## Wichtigste Einträge

- Entscheidungen: — (materialübergreifende Klassifikationsentscheidung
  siehe COMMON-COMMON-DEC-004; GL24h-spezifische Entscheidungen unter
  R2-GL24h-DEC-001–007, nicht ungeprüft auf GL75 übertragbar).
- Berechnungen: R2-GL75-CALC-001–004 (Stabdübel-Johansen-Nachweis,
  unverstärkte Querdruckfestigkeit, Momenten-Abschätzung; CALC-004
  korrigiert CALC-002, siehe dessen `superseded_by`-Feld).
- Annahmen: — (materialunabhängige Annahmen siehe R2-COMMON-ASS-001–005,
  bisher jedoch nur für GL24h konkret angewendet).
- Versuchsergebnisse: R2-GL75-II-PO-B-SD-23-RES-001,
  R2-GL75-II-T-B-BR-22-RES-001.
- Interpretationen/Schlussfolgerungen: — (Beobachtung zum materialabhängig
  verschobenen Versagensmodus bisher nur als Freitext in
  R2-GL75-CALC-003 vermerkt, `CLAUDE_DRAFT` — noch vom Forschenden zu
  prüfen).

## Offene Fragen / bekannte Widersprüche

R2-GL75-OPQ-001–003 (fehlende Steifigkeitskette, fehlender
ASSY-Verstärkungsblock, Anwendbarkeit der SWB-Querdruckbeiwerte auf
BauBuche); dazu die materialunabhängigen offenen Fragen unter
`research/R2/COMMON/open_questions/`.

## Nächste Schritte

Klärung, ob/wie eine Zugseiten-Steifigkeitskette für GL75 aufgestellt
werden soll (R2-GL75-OPQ-001); Klärung der korrekten
FprEN-Querdruckbeiwerte für die LVL/GLVL-Klassifikation
(R2-GL75-OPQ-003).
