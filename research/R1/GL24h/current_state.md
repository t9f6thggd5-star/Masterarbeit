---
scope:
  connection: R1
  material: GL24h
last_updated: 2026-09-21
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
Rahmeneckenrotation steht noch aus (R1-GL24h-HYP-001). Für das Federmodell liegen die Drehfeder der Dübelgruppen (CALC-007) und
die Zugpfad-Steifigkeit (CALC-008) vor, die Druckseite fehlt noch. Für GL75
liegen n_ef, Drehfeder und Zugpfad-Steifigkeit vor.

## Wichtigste Einträge

- Entscheidungen: R1-GL24h-DEC-001–009 (u. a. Johansen-Modi/
  Bauteilnummerierung, Faktor-2-Vorsicht, Trennung Lochspiel/elastischer
  Schlupf, keine skalare Schlupf-Addition); siehe auch R1-COMMON-DEC-001/002
  und COMMON-COMMON-DEC-003 für projektweite/materialunabhängige Punkte.
- Berechnungen: R1-GL24h-CALC-001–008 (Johansen-Tragfähigkeit je
  Scherfuge und Gruppe, Verschiebungsmodul K_SLS,v, Schlupfkette,
  vektorielle 108°-Relativverschiebung; neu: CALC-007 Drehfeder C_rot,v,f =
  21.111 kNm/rad je Gruppe, CALC-008 Zugpfad c_t,tot = 279,52 kN/mm).
- Annahmen: R1-COMMON-ASS-001 (Geometrie der vier Dübelgruppen, 4×8, a_1 = 80,
  a_2 = 50 mm; gilt auch für GL75).
- Versuchsergebnisse: —
- Interpretationen/Schlussfolgerungen: —
- Hypothesen: R1-GL24h-HYP-001 (`CLAUDE_DRAFT`, `reviewed: false` — noch
  vom Forschenden zu prüfen, siehe CLAUDE.md Abschnitt 14).

## Offene Fragen / bekannte Widersprüche

12 Fragedateien unter `research/R1/GL24h/open_questions/`
(R1-GL24h-OPQ-001–012), u. a. zur Kinematik der Rahmeneckenrotation,
zum Faktor-2 bei der Gesamttragfähigkeit und zu zwei fehlenden externen
Quellen (DIN EN 14080, EN 1995-3:202y §6.4). **Korrigiert 2026-09-22:**
OPQ-003 (Bedeutung z=550mm) und OPQ-006 (Faktor "m=2") sind bereits
RESOLVED — tatsächlich offen sind nur OPQ-001–002, 004–005, 007–012
(10 von 12).
Neu seit 2026-09-21: R1-GL24h-OPQ-013 (K_ser je Dübel für die Drehfeder
c_v,f,rot, entschieden) und R1-GL24h-DEC-010 (K_ser,Dübel = 17,96 kN/mm nach
FprEN Tab. 11.12; C_rot,v,f = 21.111 kNm/rad je 4×8-Gruppe). Offen dazu: R1-GL24h-OPQ-014
(Herkunft und Versuchsbelege des Normwerts K_ser, Eingang ρ_mean = 420 kg/m³). Projektweit offen bleiben R1-COMMON-OPQ-003
(Messbasis der Wegaufnehmer) und R1-COMMON-OPQ-004 (F_est-Basis).

## Nächste Schritte

Kinematische Herleitung gemäß R1-GL24h-HYP-001 (Schritte 1–5); danach
Umrechnung von Rahmeneckenrotation auf Aktuatorweg für die
Versuchsplanung.

**Update (2026-09-25), Rückmeldung der Betreuung:**
- Zugversuche I-T-S-SD-28 (GL24h): Versagen durch kombiniertes
  Blockscheren und Nettoquerschnittsversagen im Holz; die tatsächliche
  Höchstlast wurde erreicht. Maßgebend ist damit ein Sprödversagen des
  Holzes (Komponente br,par, FprEN 11.5), nicht die Johansen-Tragfähigkeit
  (R1-GL24h-CALC-003). Rechnerischer Nachweis offen (R1-GL24h-OPQ-015).
- R1-COMMON-OPQ-003 RESOLVED: Messwert = c_v,f, Holzverformung nicht
  enthalten; Folgefrage R1-COMMON-OPQ-005.
- R1-COMMON-OPQ-004 RESOLVED: Lastfenster mit F_est = 480 kN bleibt,
  c_T = 559,04 kN/mm und c_t,tot = 279,52 kN/mm unverändert.
