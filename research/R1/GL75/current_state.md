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
Bisher liegen nur Werte zur effektiven Anzahl n_ef vor (DIN EN 1995-1-1
gegen FprEN Tab. 11.10 (7)); die übrige Bearbeitung von R1 konzentriert
sich bislang auf GL24h (siehe research/R1/GL24h/current_state.md).
Zugversuche I-T-B-SD-28-1 bis -3 (2×8, GL75) liegen in der Excel
"Auswertung Steifigkeiten_0703_..." (R1/COMMON/calculations) vor, sind
aber noch nicht als Versuchsergebnisse im Wiki abgelegt.

## Wichtigste Einträge

- Berechnungen: R1-GL75-CALC-001 (n_ef ≈ 3.93 nach FprEN Tab. 11.10 (7)
  mit t = t_ms = 12mm, siehe R1-GL24h-DEC-005 zur Materialunterscheidung),
  R1-GL75-CALC-002 (n_ef ≈ 5.50 nach DIN EN 1995-1-1 Gl. 8.34, Formel
  gegen die Norm geprüft), R1-GL75-CALC-003 (n_ef nach (7) in Abhängigkeit
  von t, Variante t = 144mm: 7.31).
- Annahmen: —
- Versuchsergebnisse: —
- Interpretationen/Schlussfolgerungen: —

## Offene Fragen / bekannte Widersprüche

- R1-GL75-OPQ-001 (Rohdichte 730 vs. 800 kg/m³ in den Versuchsblättern).
- R1-GL75-OPQ-002 (Auslegung von t in FprEN Tab. 11.10 (9) bei
  Stahl-Innenteil: 12mm oder 144mm, n_ef 3.93 gegen 7.31; DIN-Wert 5.50).
- Auch für GL75 relevant: R1-COMMON-OPQ-003 (LVDT-Bezugspunkte),
  R1-COMMON-OPQ-004 (F_est-Basis für K_ser); R1-COMMON-OPQ-002 (Mittelwerte
  K_ser, gelöst); siehe außerdem `research/R1/GL24h/open_questions/`.

## Nächste Schritte

Johansen-Tragfähigkeit und Verformungsabschätzung analog zu R1/GL24h auch
für GL75 auswerten (Sheet "Rahmenecke GL75 SD" der externen Excel-Datei).
