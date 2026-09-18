---
scope:
  connection: R2
  material: GL75
last_updated: "2026-09-18"
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
COMMON-COMMON-DEC-004). Im R2-Excel liegt für GL75 bisher nur der
Festigkeitsnachweis vor (Stabdübel-Johansen mit ungeklärter Rolle,
Momenten-Abschätzung `M_max≈162,96 kNm`); die vollständige
Druck- und Zugseiten-Steifigkeitskette sowie `S_j,ini(GL75)` wurden
seit 2026-09-18 im Chat mit dem Nutzer aufgestellt und im Wiki
dokumentiert (R2-GL75-CALC-006–012), bisher aber noch nicht als
eigener Block im R2-Excel nachgebildet (ein ASSY-Verstärkungsblock
entfällt für GL75 ohnehin, R2-GL75-OPQ-002 RESOLVED).
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
  siehe jeweils `superseded_by`-Feld). Neu [2026-09-18]: vollständige
  Druckseiten-Kette R2-GL75-CALC-006 (`c_c,90`, unverstärkt,
  176,409 kN/mm), R2-GL75-CALC-007 (`c_c,0`, 2.688 kN/mm, `certainty:
  ASSUMED` wie das GL24h-Pendant), R2-GL75-CALC-008 (`c_C`,
  Serienschaltung, 165,545 kN/mm); vollständige Zugseiten-Kette
  R2-GL75-CALC-009 (`c_c,90`, unverstärkt, 158,021 kN/mm),
  R2-GL75-CALC-010 (`c_v,ges`, Schubfeld Holz + 2×BFU-BU 9mm,
  145 kN/mm), R2-GL75-CALC-011 (`c_T`, Serienschaltung mit gepooltem
  Stangenmesswert, 70,831 kN/mm, löst R2-GL75-OPQ-001); und —
  aufbauend auf beiden Ketten — R2-GL75-CALC-012 (`S_j,ini`,
  Kombination über `z=560mm` nach R2-COMMON-HYP-001, 15.556,5 kNm/rad,
  vom Nutzer unabhängig bestätigt: 15.556,61) — erste vollständige
  Anfangsrotationssteifigkeit für GL75, analog zu
  R2-GL24h-CALC-020/021/022.
- Annahmen: R2-COMMON-ASS-003 [Schubfeldverstärkung, Sperrholzplatten
  links/rechts auf den Seitenflächen des Trägers flankierend um die
  Gewindestangen, `G_r,mean=500 N/mm²`] und R2-COMMON-ASS-006 [Herkunft
  `z=560mm`] neu für GL75 angewendet (2026-09-18); übrige
  materialunabhängige Annahmen siehe R2-COMMON-ASS-001–005.
- Versuchsergebnisse: R2-GL75-II-PO-B-SD-23-RES-001,
  R2-GL75-II-T-B-BR-22-RES-001, R2-GL75-II-T-B-BR-11-RES-001,
  R2-GL75-II-T-B-BR-11-RES-002 (Steifigkeiten K_ser/K_e),
  R2-GL75-II-T-B-BR-22-RES-002 (Steifigkeiten, mit deutlichem Ausreißer
  bei Prüfkörper 2 — Verhältnis oben/unten nur ~23 %),
  R2-GL75-II-T-B-BR-11-RES-003 (gepoolter K_ser-Mittelwert, n=6,
  226,596 kN/mm) und R2-GL75-II-T-B-BR-22-RES-003 (gepoolter
  K_ser-Mittelwert, n=6, 1.119,496 kN/mm, mit Vorsicht zu verwenden —
  siehe dortiger Vorbehalt zur Streuung) — beide gemäß
  R2-COMMON-DEC-003 direkt aus Blatt "Überblick" übernommen; der
  Zugseiten-Messwert (`II-T-B-BR-22`) ist seit 2026-09-18 in
  R2-GL75-CALC-011 (`c_T`) verwendet.
- Interpretationen/Schlussfolgerungen: — (Beobachtung zum materialabhängig
  verschobenen Versagensmodus bisher nur als Freitext in
  R2-GL75-CALC-003 vermerkt, `CLAUDE_DRAFT` — noch vom Forschenden zu
  prüfen).

## Offene Fragen / bekannte Widersprüche

R2-GL75-OPQ-001 (fehlende Zugseiten-Steifigkeitskette) am 2026-09-18
RESOLVED — vollständige Kette R2-GL75-CALC-009/010/011 aufgestellt.
R2-GL75-OPQ-002 (ASSY-Verstärkungsblock) am 2026-09-18 RESOLVED — vom
Nutzer bestätigt: keine ASSY-Querdruckverstärkung bei GL75.
R2-GL75-OPQ-003 (Anwendbarkeit der SWB-Querdruckbeiwerte auf BauBuche)
am 2026-09-17 RESOLVED (R2-GL75-DEC-001: Hardwood GLVL, `k_mat=1,0`).
Dazu die materialunabhängigen offenen Fragen unter
`research/R2/COMMON/open_questions/`, von denen R2-COMMON-OPQ-001
(Druckzonen-Geometrie) am 2026-09-04 RESOLVED wurde (rechteckige
Druckzone, Hebelarm mittig, R2-COMMON-DEC-002). Weiterhin OPEN:
R2-COMMON-OPQ-006 (Kombinationsformel `S_j,ini`, `CLAUDE_DRAFT`
R2-COMMON-HYP-001 noch nicht Betreuerin-geprüft) und
R2-COMMON-OPQ-011 (`c_c,0`-Modellierungsannahme `l=240mm`, betrifft
auch `z=560mm` gemäß R2-COMMON-ASS-006).

## Nächste Schritte

Die "edgewise"-Annahme hinter `k_mat=1,0` (R2-GL75-DEC-001) ist noch
nicht anhand der konkreten BauBuche-Einbaugeometrie in R2 verifiziert —
falls "flatwise" zutrifft, wäre `k_mat=1,3` (Case A) statt `1,0`
anzusetzen. Größere Blocker vor einem formalen Abschluss von Phase 2:
alle unter "Offene Fragen" genannten `OPEN`-Punkte sind noch nicht mit
der Betreuerin abgestimmt (Kombinationsformel, `l=240mm`-Annahme für
`c_c,0`/`z`, `G_r,mean=500 N/mm²`-Annahme für die
Sperrholzverstärkung, Streuung des Stangengruppen-Messwerts).

**Update (2026-09-18): Druckseiten-Steifigkeitskette für GL75 erstmals
vollständig.** Da R2-GL75-OPQ-002 jetzt RESOLVED ist (keine
ASSY-Verstärkung bei GL75), kommt durchgängig der unverstärkte
FprEN-Ansatz (Gl. 9.31) zum Einsatz, mit der bereits für GL75 im Excel
hinterlegten Druckseiten-Geometrie (`A_ef=83.200mm²`, beidseitige
Lastausbreitung, aus R2-GL75-CALC-005) und `E_90,mean=470 N/mm²`:
`c_c,90=176,409 kN/mm` (R2-GL75-CALC-006). Mit `c_c,0` (gleiche
`l=240mm`-Annahme wie GL24h, R2-COMMON-OPQ-011, `E_0,mean=16.800 N/mm²`)
`=2.688 kN/mm` (R2-GL75-CALC-007) ergibt die Serienschaltung
`c_C=165,545 kN/mm` (R2-GL75-CALC-008) — direkt aus dem R2-Excel
verifiziert (Sheet "Rahmenecke GL75 SD", Zellen I55/I66/I70) und vom
Nutzer unabhängig nachgerechnet. Bemerkenswert: liegt über dem
ASSY-verstärkten GL24h-Wert (`160,137 kN/mm`, R2-GL24h-CALC-020), da
BauBuche auch unverstärkt ein deutlich höheres `E_90,mean` hat.

**Update (2026-09-18): Zugseiten-Steifigkeitskette für GL75 erstmals
vollständig, `S_j,ini(GL75)` berechnet.** Analog zur Druckseite:
`c_c,90=158,021 kN/mm` (Zugseite, unverstärkt, einseitige
Lastausbreitung, R2-GL75-CALC-009), Schubfeld `c_v,ges=145 kN/mm`
(Holz + 2× BFU-BU-Sperrholzplatten `t=9mm` auf den Seitenflächen des
Trägers flankierend um die Gewindestangen, R2-GL75-CALC-010, korrigierte
Geometrie gemäß R2-COMMON-ASS-003). Zusammen mit dem gepoolten
Stangengruppen-Messwert (`1.119,496 kN/mm`, mit Vorsicht zu verwenden,
R2-GL75-II-T-B-BR-22-RES-003) ergibt die Serienschaltung
`c_T=70,831 kN/mm` (R2-GL75-CALC-011, löst R2-GL75-OPQ-001). Mit `c_T`
und `c_C` (R2-GL75-CALC-008) sowie dem materialunabhängigen Hebelarm
`z=560mm` (R2-COMMON-ASS-006) liefert die Kombinationsformel
R2-COMMON-HYP-001: `S_j,ini(GL75)=15.556,5 kNm/rad`
(R2-GL75-CALC-012, vom Nutzer unabhängig bestätigt: 15.556,61) — rund
24 % über dem GL24h-Pendant (`12.540,8 kNm/rad`, R2-GL24h-CALC-022),
obwohl GL75 unverstärkt bleibt. Damit liegt für GL75 erstmals ein
vollständiges Anfangssteifigkeits-Ergebnis vor, analog zu GL24h — beide
noch als `CLAUDE_DRAFT`/`OPEN` markierte Kombinationsformel
(R2-COMMON-HYP-001, R2-COMMON-OPQ-006) und mit den jeweils
materialspezifisch dokumentierten Vorbehalten zu behandeln, nicht als
mit der Betreuerin abgestimmtes Endergebnis.
