---
scope:
  connection: R3
  material: GL75
last_updated: "2026-09-16"
---

# Bearbeitungsstand: R3 / GL75

Kurze, laufend aktualisierte Zusammenfassung — kein Ersatz für die
strukturierten Einträge in `research/R3/GL75/`, sondern ein
schneller Überblick darüber, was dort schon existiert. Diese Datei selbst
trägt keine eigene ID (sie ist kein Claim/Ergebnis, siehe `schema.yaml`
Abschnitt "ID naming convention") und wird nicht von
`scripts/build_index.py` katalogisiert.

## Zusammenfassung

R3 = Rahmenecke mit seitlichen Holzlaschen (Anschlusstyp `III`), hier
die GL75/Buche-Variante. Erste Push-Out-Komponentenversuche liegen jetzt
vor (Quelle: `common/general/Auswertung_Steifigkeiten_Push-Out-
Versuche_FINAL.xlsx`, Blatt "Überblick", eingepflegt 2026-09-16):
Stabdübel 2×5 (`III-PO-B-SD-25`, vollständig) und Schraube 1×1 mit
Lasche an Beam bzw. Column (`III-PO-B-SC-11-B`/`-C`, je vollständig).
**Nachtrag (2026-09-16):** Schraube 4×4 (`III-PO-B-SC-44-B`/`-C`) war
zunächst als komplett fehlend/"offen" vermerkt (R3-GL75-OPQ-001); der
Nutzer hat die Werte für alle 6 Prüfkörper noch am selben Tag in zwei
Schritten nachgereicht — zunächst Fmax,ges (Gesamtlast), dann explizit
auch Fmax,SF (Höchstlast pro Scherfuge, = Fmax,ges/2, vom Nutzer
bestätigt und rechnerisch übereinstimmend) — Frage damit RESOLVED
(R3-GL75-III-PO-B-SC-44-C-RES-001, R3-GL75-III-PO-B-SC-44-B-RES-001).
Beide Einträge führen jetzt Fmax,SF als primären Ergebniswert, konsistent
mit den übrigen 44er-Serien dieser Wiki, und sind damit direkt
vergleichbar (z. B. mit R3-GL24h-III-PO-S-SC-44-C-RES-001). Auffällig: anders als bei
GL24h (`III-PO-S-WD-36`) gibt es für GL75 keine Holzdübel-Serie in der
Quelldatei — dieselbe Lücke besteht durchgängig auch bei R2 und der
COMMON-Basisserie (kein `*-B-WD-*` in der gesamten Auswertungsdatei),
spricht eher für eine bewusste Auslassung (Holzdübel nicht mit
GL75/Buche getestet) als für einen Einzelfehler — nicht weiter geklärt.

**Neu (2026-09-16):** grobe Tragfähigkeits-Vorhersage für die reale
4×8-ASSY-Schraubengruppe (eine Laschenseite) aus den 1×1-/4×4-Push-Out-
Versuchen abgeleitet, R3-GL75-CALC-001 (erster CALC-Eintrag für
R3/GL75), `≈418,1 kN` — Governing-Basis ist die Lasche-an-Beam-Serie
(kleinerer der beiden vollständigen 4×4-Mittelwerte). Explizit als
grobe, nicht bemessungsreife Vorhersage gekennzeichnet (mehrere
ungeklärte Annahmen, siehe CALC-001 selbst); dieselbe Methode wie
R3-GL24h-CALC-006.

**Neu (2026-09-16):** R3-GL75-DEC-001 (erste R3/GL75-spezifische
Entscheidung) legt den CALC-001-Wert (418,086 kN) als "gewählte Last"
für die weitere Bemessung des Zugpfads fest (Wert bezieht sich auf eine
Laschenseite). Die in CALC-001 dokumentierten Einschränkungen (grobe,
nicht bemessungsreife Vorhersage) gelten dafür unverändert fort.

## Wichtigste Einträge

- Entscheidungen: R3-GL75-DEC-001 (gewählte Last 4×8-ASSY-Schraubengruppe
  = 418,086 kN, aus CALC-001 übernommen).
- Berechnungen: R3-GL75-CALC-001 (grobe 4×8-Tragfähigkeits-Vorhersage
  ASSY-Schraubengruppe aus Push-Out-Daten, `≈418,1 kN` je Laschenseite,
  CALCULATED, nicht bemessungsreif).
- Annahmen: — (noch keine).
- Versuchsergebnisse: R3-GL75-III-PO-B-SD-25-RES-001/002,
  R3-GL75-III-PO-B-SC-11-B-RES-001/002,
  R3-GL75-III-PO-B-SC-11-C-RES-001/002,
  R3-GL75-III-PO-B-SC-44-C-RES-001 (Fmax,SF, Mittelwert 276,213 kN;
  Fmax,ges-Mittelwert 552,423 kN ebenfalls dokumentiert),
  R3-GL75-III-PO-B-SC-44-B-RES-001 (Fmax,SF, Mittelwert 209,043 kN;
  Fmax,ges-Mittelwert 418,083 kN ebenfalls dokumentiert).
- Interpretationen/Schlussfolgerungen: — (noch keine).

## Offene Fragen / bekannte Widersprüche

R3-GL75-OPQ-001 (zunächst: alle 6 Prüfkörper der 4×4-Schraubenserien
`III-PO-B-SC-44-B`/`-C` als "offen" markiert) wurde am 2026-09-16 noch
am selben Tag RESOLVED — die Versuche waren durchgeführt, nur die
Auswertung fehlte, Werte vom Nutzer nachgereicht.

## Nächste Schritte

Keine offenen Schritte mehr zu `III-PO-B-SC-44-B`/`-C` — Fmax,SF liegt
jetzt vor und ist mit den übrigen 44er-Serien vergleichbar.
