---
scope:
  connection: R1
  material: GL75
last_updated: 2026-09-21
---

# Bearbeitungsstand: R1 / GL75

Kurze, laufend aktualisierte Zusammenfassung — kein Ersatz für die
strukturierten Einträge in `research/R1/GL75/`, sondern ein
schneller Überblick darüber, was dort schon existiert. Diese Datei selbst
trägt keine eigene ID (sie ist kein Claim/Ergebnis, siehe `schema.yaml`
Abschnitt "ID naming convention") und wird nicht von
`scripts/build_index.py` katalogisiert.

## Zusammenfassung

R1 = Schlitzblech + Stabdübel-Anschluss, hier die BauBuche/GL75-Variante.
Vorliegend sind die effektive Anzahl n_ef sowie die Steifigkeitsgrößen
des Federmodells (Drehfeder der Dübelgruppen, Zugpfad): n_ef = 7,31 nach
FprEN Tab. 11.10 (7) mit t = 144mm (vom Nutzer bestätigt, Grundlage von
F_est = 1254,16 kN für 4×8, 627,08 kN je 2×8-Gruppe) und der DIN-Vergleichswert
5,50. Die übrige Bearbeitung von R1 konzentriert sich bislang auf GL24h
(siehe research/R1/GL24h/current_state.md). Zugversuche I-T-B-SD-28-1 bis -3
(2×8, GL75) liegen in der Excel "Auswertung Steifigkeiten_0703_..."
(R1/COMMON/calculations) vor, sind aber noch nicht als Versuchsergebnisse
im Wiki abgelegt.

## Wichtigste Einträge

- Berechnungen: R1-GL75-CALC-003 (n_ef = 7,308 nach FprEN Tab. 11.10 (7),
  t = 144mm, bestätigt; ersetzt R1-GL75-CALC-001 mit 3,93), R1-GL75-CALC-002
  (n_ef = 5,50 nach DIN EN 1995-1-1 Gl. 8.34, nur Vergleichswert).
  R1-GL75-CALC-004 (Drehfeder C_rot,v,f = 55.496 kNm/rad je Gruppe),
  R1-GL75-CALC-005 (Zugpfad c_t,tot = 727,74 kN/mm).
- Entscheidungen: R1-GL75-DEC-001 (K_ser,Dübel = 47,22 kN/mm nach FprEN
  Tab. 11.12 mit ρ_mean = 800 kg/m³; C_rot,v,f = 55.496 kNm/rad je 4×8-Gruppe).
- Annahmen: R1-COMMON-ASS-001 (Geometrie der vier Dübelgruppen, identisch mit
  GL24h).
- Versuchsergebnisse: —
- Interpretationen/Schlussfolgerungen: —

## Offene Fragen / bekannte Widersprüche

- R1-GL75-OPQ-001 (Rohdichte 730 vs. 800 kg/m³ in den Versuchsblättern).
- R1-GL75-OPQ-003 (K_ser stammt aus der Formel FprEN Tab. 11.12 mit
  ρ_mean = 800 kg/m³; offen ist, ob Versuche an Einzeldübeln den Normwert
  belegen).
- R1-GL75-OPQ-002 (t in Tab. 11.10 (9) bei Stahl-Innenteil): am 2026-09-21
  RESOLVED, t = 144mm, n_ef = 7,31. Offen bleiben Beschriftungen im Blatt
  (D47, D72, A96, A97) und das R2-Blatt (Zeile (6) für GL75).
- Auch für GL75 relevant: R1-COMMON-OPQ-003 (LVDT-Bezugspunkte),
  R1-COMMON-OPQ-004 (F_est-Basis für K_ser, für GL75 jetzt 627,08 kN je 2×8); R1-COMMON-OPQ-002 (Mittelwerte
  K_ser, gelöst); siehe außerdem `research/R1/GL24h/open_questions/`.

## Nächste Schritte

Johansen-Tragfähigkeit und Verformungsabschätzung analog zu R1/GL24h auch
für GL75 auswerten (Sheet "Rahmenecke GL75 SD" der externen Excel-Datei).

**Update (2026-09-25), Rückmeldung der Betreuung:**
- Zugversuche I-T-B-SD-28 (GL75): Versagen des Nettoquerschnitts im
  Schlitzblech; F_max ist nur eine Untergrenze der Dübelgruppe
  (R1-GL75-CALC-003).
- R1-GL75-OPQ-001 RESOLVED: ρ_mean = 800 kg/m³; 730 kg/m³ war ein Fehler
  der Auswertungsdatei (nur Vergleichswerte betroffen).
- R1-COMMON-OPQ-003/004 RESOLVED: Messwert = c_v,f; Lastfenster mit
  F_est = 800 kN bleibt, c_t,tot = 727,74 kN/mm unverändert. Offen:
  R1-COMMON-OPQ-005.

**Update (2026-09-26), Modellfestlegungen:**
- Federmodell nach Buchholz2025 Gl. (1)–(5), Drehfedern nach Gl. (5)
  summiert (R1-COMMON-DEC-004); Abb. 3 schematisch gelesen, kein
  Widerspruch zu Gl. (5).
- Schlitzblech starr (R1-COMMON-DEC-003, löst R1-GL24h-OPQ-009).
- c_br,par vorläufig starr, offener Diskussionspunkt (R1-COMMON-OPQ-005).
- Druckseite vorläufig starr wegen Kontaktpressung (R1-COMMON-ASS-002),
  z = 550 mm vorerst beibehalten, Klärung in R1-COMMON-OPQ-006.
- Noch offen: Druckversuche auswerten (ersetzt ASS-002), Zugverformung
  des Holzes, F_est-Basis für die Übersichtstabelle, K_ser für die
  Drehfeder (Norm oder Versuch).

**Update (2026-09-26), Anfangsrotationssteifigkeit:** C_rot,tot = 442.125 kNm/rad (R1-GL75-CALC-006).
Zugseite im Excel in c_v,f und c_br,par getrennt; Kräftepaar mit
Druckseite starr plus vier Drehfedern nach Buchholz2025 Gl. (5).
Nächste Schritte: F_est/M_R festlegen, K_ser für die Drehfeder (Norm oder
Versuch) entscheiden, dann Φ = M_R/C_rot,tot und u_M für die Übersicht.
