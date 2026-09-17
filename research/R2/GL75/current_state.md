---
scope:
  connection: R2
  material: GL75
last_updated: "2026-09-17"
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
(R2-GL75-CALC-003 bleibt unverändert gültig). **Update (2026-09-17):**
Die zuvor offene Frage nach der richtigen `k_mat`-Tabellenzeile für
GL75/BauBuche (R2-GL75-OPQ-003) ist geklärt: BauBuche GL75 ist laut
eigener EAD/ETA-Klassifikation (ETA-14/0354, EAD 130010) als Hardwood
GLVL einzuordnen, nicht als SWB — `k_mat=1,0` statt bisher `1,4`
(R2-GL75-DEC-001). Zugleich hat der Nutzer die Querdrucktragfähigkeit
auch für GL75 nach Zug-/Druckseite getrennt berechnet (analog zu
GL24h). Ergebnis: unverstärkte Querdrucktragfähigkeit jetzt
`862,011 kN` (Druckseite) bzw. `736,890 kN` (Zugseite), beide deutlich
unter dem alten, undifferenzierten Wert `1.206,82 kN`
(R2-GL75-CALC-005, ersetzt R2-GL75-CALC-004). An der maßgebenden
Komponente ändert sich dadurch nichts: das Gewindestangen-
Zugversuchsmittel (`291,00 kN`) bleibt weit unter beiden neuen Werten
maßgebend, `M_max` bleibt bei `≈162,96 kNm` (R2-GL75-CALC-003,
bestätigt). Für GL75 ist weiterhin keine ASSY-Verstärkung im Excel
modelliert, daher existiert kein verstärkter Querdruckwert. Neu
(2026-09-16): die
1×1-Zugserie `II-T-B-BR-11` (Mittelwert 73,367 kN,
R2-GL75-II-T-B-BR-11-RES-001) liegt, umgerechnet auf eine Einzelstange,
nahe am 2×2-Wert (291,003/4 ≈ 72,75 kN) und nahezu identisch zum
GL24h-Wert derselben 1×1-Serie (72,337 kN) — Plausibilitätshinweis,
nicht weiter interpretiert. Ebenfalls neu (2026-09-04): der
materialunabhängige Druckzonen-Blocker R2-COMMON-OPQ-001 wurde durch
Betreuerin-Entscheidung aufgelöst (Druckzone RECHTECKIG, Hebelarm
mittig, R2-COMMON-DEC-002) — für GL75 relevant, sobald eine
Druckseiten-Steifigkeitskette aufgestellt wird, was aber erst nach
Klärung von R2-GL75-OPQ-001 (fehlende Zugseiten-Steifigkeitskette)
ansteht.

## Wichtigste Einträge

- Entscheidungen: R2-GL75-DEC-001 (neu, 2026-09-17: `k_mat=1,0` für
  GL75/BauBuche als Hardwood GLVL, löst R2-GL75-OPQ-003); dazu
  materialübergreifende Klassifikationsentscheidung siehe
  COMMON-COMMON-DEC-004; materialunabhängige R2-Entscheidungen siehe
  R2-COMMON-DEC-002 [Druckzonengeometrie] und R2-COMMON-DEC-003
  [Anfangssteifigkeit je Gruppe aus Blatt "Überblick", Zellen B94:B97];
  GL24h-spezifische Entscheidungen unter R2-GL24h-DEC-001–008, nicht
  ungeprüft auf GL75 übertragbar.
- Berechnungen: R2-GL75-CALC-001–005 (Stabdübel-Johansen-Nachweis,
  unverstärkte Querdruckfestigkeit, Momenten-Abschätzung; CALC-004
  korrigiert CALC-002, CALC-005 korrigiert/erweitert CALC-004 um die
  `k_mat`-Korrektur und die Zug-/Druckseiten-Trennung [2026-09-17] —
  siehe jeweils `superseded_by`-Feld).
- Annahmen: — (materialunabhängige Annahmen siehe R2-COMMON-ASS-001–005,
  bisher jedoch nur für GL24h konkret angewendet).
- Versuchsergebnisse: R2-GL75-II-PO-B-SD-23-RES-001,
  R2-GL75-II-T-B-BR-22-RES-001, R2-GL75-II-T-B-BR-11-RES-001,
  R2-GL75-II-T-B-BR-11-RES-002 (Steifigkeiten K_ser/K_e),
  R2-GL75-II-T-B-BR-22-RES-002 (Steifigkeiten, mit deutlichem Ausreißer
  bei Prüfkörper 2 — Verhältnis oben/unten nur ~23 %),
  R2-GL75-II-T-B-BR-11-RES-003 (gepoolter K_ser-Mittelwert, n=6,
  226,596 kN/mm) und R2-GL75-II-T-B-BR-22-RES-003 (gepoolter
  K_ser-Mittelwert, n=6, 1.119,496 kN/mm, aber mit Vorsicht zu
  verwenden — siehe dortiger Vorbehalt zur Streuung) — beide gemäß
  R2-COMMON-DEC-003 direkt aus Blatt "Überblick" übernommen, bisher
  aber in keiner GL75-Steifigkeitskette verwendet, da eine solche noch
  nicht existiert (R2-GL75-OPQ-001).
- Interpretationen/Schlussfolgerungen: — (Beobachtung zum materialabhängig
  verschobenen Versagensmodus bisher nur als Freitext in
  R2-GL75-CALC-003 vermerkt, `CLAUDE_DRAFT` — noch vom Forschenden zu
  prüfen).

## Offene Fragen / bekannte Widersprüche

R2-GL75-OPQ-001–002 offen (fehlende Steifigkeitskette, fehlender
ASSY-Verstärkungsblock); R2-GL75-OPQ-003 (Anwendbarkeit der
SWB-Querdruckbeiwerte auf BauBuche) am 2026-09-17 RESOLVED
(R2-GL75-DEC-001: Hardwood GLVL, `k_mat=1,0`). Dazu die
materialunabhängigen offenen Fragen unter
`research/R2/COMMON/open_questions/`, von denen R2-COMMON-OPQ-001
(Druckzonen-Geometrie) am 2026-09-04 RESOLVED wurde (rechteckige
Druckzone, Hebelarm mittig, R2-COMMON-DEC-002).

## Nächste Schritte

Klärung, ob/wie eine Zugseiten-Steifigkeitskette für GL75 aufgestellt
werden soll (R2-GL75-OPQ-001). Die "edgewise"-Annahme hinter
`k_mat=1,0` (R2-GL75-DEC-001) ist noch nicht anhand der konkreten
BauBuche-Einbaugeometrie in R2 verifiziert — falls "flatwise" zutrifft,
wäre `k_mat=1,3` (Case A) statt `1,0` anzusetzen. Für eine spätere
Druckseiten-Steifigkeitskette steht die Modellierungsgrundlage bereits
fest (rechteckige Druckzone, R2-COMMON-DEC-002).
