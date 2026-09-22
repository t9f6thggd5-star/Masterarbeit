---
scope:
  connection: R3
  material: GL24h
last_updated: "2026-09-16"
---

# Bearbeitungsstand: R3 / GL24h

Kurze, laufend aktualisierte Zusammenfassung — kein Ersatz für die
strukturierten Einträge in `research/R3/GL24h/`, sondern ein
schneller Überblick darüber, was dort schon existiert. Diese Datei selbst
trägt keine eigene ID (sie ist kein Claim/Ergebnis, siehe `schema.yaml`
Abschnitt "ID naming convention") und wird nicht von
`scripts/build_index.py` katalogisiert.

**Hinweis (2026-09-16):** Diese Datei war zuvor fälschlich als
Platzhalter ("noch keine Einträge") formuliert, obwohl bereits
Entscheidungen, Berechnungen, Annahmen, eine Hypothese und 19 offene
Fragen vorlagen — sie wurde beim Einpflegen der Push-Out-Versuche jetzt
korrigiert und erstmals vollständig befüllt.

## Zusammenfassung

R3 = Rahmenecke mit seitlichen Holzlaschen und Vorspannung
(Anschlusstyp `III`, vom Nutzer am 2026-09-16 bestätigt). Zugpfad besteht
aus Holzlasche (mit/ohne ASSY-Schrauben-Abstützung), einer
ASSY-Schraubengruppe (32 Schrauben, 8 Reihen in Lastrichtung × 4
nebeneinander, "Equal-row-load"-Annahme R3-GL24h-ASS-002) und
Gewindestange; ein vom Forschenden angegebener Arbeitswert für den
kombinierten "sleeve"-Zugpfad liegt bei `27,09 kN/mm`
(R3-GL24h-CALC-005). Vorspannung nur auf der Zugseite (R3-COMMON-DEC-001, ehemals R3-GL24h-DEC-002),
Kriechen/Schwinden werden experimentell erfasst statt rechnerisch
angesetzt (R3-COMMON-DEC-002, ehemals R3-GL24h-DEC-003); beide Vorspannungsvarianten ("Contact" und
"No-Contact") werden als getrennte, aktive Modellvarianten geführt
(R3-GL24h-DEC-004/010). Wirksame Laschenlänge 800 mm (R3-GL24h-DEC-005/
006, nicht die volle Länge als Verformungslänge wirksam), Hebelarm
vorläufig `z=640 mm` (R3-GL24h-DEC-007). Die Tragfähigkeits-Vorbemessung
gilt als abgeschlossen (R3-GL24h-DEC-009); Prüfstandkonfiguration:
zentraler Zylinder, 45°-Anordnung (R3-GL24h-DEC-008). Eine kinematische
Hypothese zur Rotationssteifigkeit (Δ=Δ_Zug+Δ_Druck, φ≈Δ/z,
C_rot=M/φ) liegt als `CLAUDE_DRAFT` vor (R3-GL24h-HYP-001, noch nicht
vom Forschenden geprüft).

**Neu (2026-09-16):** Erste Push-Out-Komponentenversuche eingepflegt
(Quelle: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_
FINAL.xlsx`, Blatt "Überblick"): Stabdübel 3×6 (`III-PO-S-SD-36`, n=3
Fmax / n=2 Steifigkeit — PK1 mit unklarem Status, R3-GL24h-OPQ-020),
Holzdübel 3×6 (`III-PO-S-WD-36`, vollständig), Schraube 1×1 mit Lasche
an Beam bzw. Column (`III-PO-S-SC-11-B`/`-C`, je vollständig) und
Schraube 4×4 (`III-PO-S-SC-44-C` vollständig, `III-PO-S-SC-44-B` nur 1
von 3 Prüfkörpern, R3-GL24h-OPQ-021). Diese Push-Out-Ergebnisse sind
noch nicht mit der obigen Zugpfad-Steifigkeitskette verknüpft.

**Neu (2026-09-16):** grobe Tragfähigkeits-Vorhersage für die reale
4×8-ASSY-Schraubengruppe (eine Laschenseite) aus den 1×1-/4×4-Push-Out-
Versuchen abgeleitet, R3-GL24h-CALC-006, `≈329,1 kN` — Governing-Basis
ist die Lasche-an-Column-Serie (44-B nicht verwertbar, s. o.). Explizit
als grobe, nicht bemessungsreife Vorhersage gekennzeichnet (mehrere
ungeklärte Annahmen, siehe CALC-006 selbst). Beruht auf denselben
axial-45°-geneigten ASSY-Schrauben wie R3-GL24h-CALC-001–005, aber
bewusst nicht mit der dortigen Steifigkeitskette verknüpft (reine
Tragfähigkeits-, keine Steifigkeitsbetrachtung).

**Neu (2026-09-16):** R3-GL24h-DEC-011 legt den CALC-006-Wert (329,054 kN)
als "gewählte Last" für die weitere Bemessung des Zugpfads fest (Wert
bezieht sich auf eine Laschenseite). Die in CALC-006 dokumentierten
Einschränkungen (grobe, nicht bemessungsreife Vorhersage) gelten dafür
unverändert fort.

## Wichtigste Einträge

- Entscheidungen: R3-GL24h-DEC-002–003 (historisch, siehe unten),
  R3-GL24h-DEC-004–010 (No-Contact-Variante, Laschenlänge, Hebelarm,
  Prüfstandkonfiguration, Status Vorbemessung, Modellvarianten);
  R3-GL24h-DEC-011 (gewählte Last 4×8-ASSY-Schraubengruppe = 329,054 kN,
  aus CALC-006 übernommen); siehe auch COMMON-COMMON-DEC-001–006
  (korrigiert 2026-09-22, zuvor stand hier "–004"; tatsächlich 6
  Einträge, siehe DEC-005 FprEN als primäre Normquelle und DEC-006
  K_ser statt K_e projektweit) für projektweite/materialunabhängige
  Punkte. **Nummerierung:** Die Entscheidungsdateien beginnen bei
  DEC-002, nicht DEC-001 — keine Spur eines DEC-001 im Projekt
  gefunden; Ursache laut Nutzer nicht mehr rekonstruierbar und ohne
  Bedeutung, Nummerierung bleibt bewusst bei 002 beginnend stehen
  (2026-09-22). **Gelöst 2026-09-22 (Nutzerentscheidung):** Der zuvor
  dangling Verweis "R3-COMMON-DEC-001/002" ist aufgelöst — es gibt
  jetzt einen `research/R3/COMMON/decisions/`-Zweig mit
  `R3-COMMON-DEC-001` (Vorspannung nur Zugseite) und
  `R3-COMMON-DEC-002` (Kriechen/Schwinden experimentell bestimmt) —
  beide inhaltlich übernommen aus den zuvor als GL24h-spezifisch
  geführten, tatsächlich aber materialunabhängigen R3-GL24h-DEC-002/003
  (jetzt `superseded_by` auf die neuen COMMON-IDs verweisend, Einträge
  selbst bleiben als Historie erhalten).
- Berechnungen: R3-GL24h-CALC-001–005 (Zugpfad-Steifigkeitskette:
  Holzlasche mit/ohne ASSY-Abstützung, ASSY-Schraubengruppe,
  Gewindestange, kombinierter Arbeitswert); R3-GL24h-CALC-006 (grobe
  4×8-Tragfähigkeits-Vorhersage ASSY-Schraubengruppe aus Push-Out-Daten,
  `≈329,1 kN` je Laschenseite, CALCULATED, nicht bemessungsreif).
- Annahmen: R3-GL24h-ASS-001–002 (starre Kopf-/Endplatten,
  Equal-row-load ASSY-Schrauben).
- Versuchsergebnisse: R3-GL24h-III-PO-S-SD-36-RES-001/002,
  R3-GL24h-III-PO-S-WD-36-RES-001/002,
  R3-GL24h-III-PO-S-SC-11-B-RES-001/002,
  R3-GL24h-III-PO-S-SC-11-C-RES-001/002,
  R3-GL24h-III-PO-S-SC-44-B-RES-001 (n=1, Einzelbefund),
  R3-GL24h-III-PO-S-SC-44-C-RES-001/002.
- Interpretationen/Schlussfolgerungen: — (noch keine).
- Hypothesen: R3-GL24h-HYP-001 (`CLAUDE_DRAFT`, `reviewed: false` —
  noch vom Forschenden zu prüfen).

## Offene Fragen / bekannte Widersprüche

R3-GL24h-OPQ-001–019 (bereits vorhanden, Inhalt im Rahmen dieser
Aktualisierung nicht im Detail neu geprüft) — **korrigiert 2026-09-22:**
davon sind OPQ-016 und OPQ-017 bereits RESOLVED, tatsächlich offen aus
diesem Block sind nur OPQ-001–015, 018–019; neu am 2026-09-16:
R3-GL24h-OPQ-020 (Prüfkörper 1 von `III-PO-S-SD-36` als "entfällt"
markiert, Ursache unklar) und R3-GL24h-OPQ-021 (Prüfkörper 2/3 von
`III-PO-S-SC-44-B` fehlen komplett, Ursache unklar).

## Nächste Schritte

Klärung von R3-GL24h-OPQ-020/021 mit dem Nutzer; Verknüpfung der neuen
Push-Out-Ergebnisse mit der bestehenden Zugpfad-Steifigkeitskette
(R3-GL24h-CALC-001–005) prüfen; R3-GL24h-HYP-001 durch den Forschenden
reviewen lassen.
