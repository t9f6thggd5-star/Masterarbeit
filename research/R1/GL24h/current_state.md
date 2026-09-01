---
scope:
  connection: R1
  material: GL24h
last_updated: 2026-09-01
---

# Bearbeitungsstand: R1 / GL24h

Kurze, laufend aktualisierte Zusammenfassung — kein Ersatz für die
strukturierten Einträge in `research/R1/GL24h/`, sondern ein
schneller Überblick darüber, was dort schon existiert. Diese Datei selbst
trägt keine eigene ID (sie ist kein Claim/Ergebnis, siehe `schema.yaml`
Abschnitt "ID naming convention") und wird nicht von
`scripts/build_index.py` katalogisiert.

## Zusammenfassung

R1 = Schlitzblech + Stabdübel-Anschluss. Bearbeitung befindet sich in
Phase 2 (Vorbemessung/Tragfähigkeits- und Verformungsabschätzung, siehe
COMMON-COMMON-DEC-003). Tragfähigkeit nach Johansen ist für die GL24h-
Variante rechnerisch abgeschätzt und gegen die reale Berechnungs-Excel
verifiziert; eine erste Verformungsabschätzung (Dübelgruppen-Schlupf,
Lochspiel) liegt vor, die kinematische Umrechnung auf die
Rahmeneckenrotation steht noch aus (R1-GL24h-HYP-001). Für GL75 liegt
bisher nur die effektive Anzahl n_ef vor.

## Wichtigste Einträge

- Entscheidungen: R1-GL24h-DEC-001–009 (u. a. Johansen-Modi/
  Bauteilnummerierung, Faktor-2-Vorsicht, Trennung Lochspiel/elastischer
  Schlupf, keine skalare Schlupf-Addition); siehe auch R1-COMMON-DEC-001/002
  und COMMON-COMMON-DEC-003 für projektweite/materialunabhängige Punkte.
- Berechnungen: R1-GL24h-CALC-001–006 (Johansen-Tragfähigkeit je
  Scherfuge und Gruppe, Verschiebungsmodul K_SLS,v, Schlupfkette,
  vektorielle 108°-Relativverschiebung).
- Annahmen: —
- Versuchsergebnisse: —
- Interpretationen/Schlussfolgerungen: —
- Hypothesen: R1-GL24h-HYP-001 (`CLAUDE_DRAFT`, `reviewed: false` — noch
  vom Forschenden zu prüfen, siehe CLAUDE.md Abschnitt 14).

## Offene Fragen / bekannte Widersprüche

12 offene Fragen unter `research/R1/GL24h/open_questions/`
(R1-GL24h-OPQ-001–012), u. a. zur Kinematik der Rahmeneckenrotation,
zum Faktor-2 bei der Gesamttragfähigkeit und zu zwei fehlenden externen
Quellen (DIN EN 14080, EN 1995-3:202y §6.4).

## Nächste Schritte

Kinematische Herleitung gemäß R1-GL24h-HYP-001 (Schritte 1–5); danach
Umrechnung von Rahmeneckenrotation auf Aktuatorweg für die
Versuchsplanung.
