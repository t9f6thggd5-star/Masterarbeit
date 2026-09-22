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
  aus CALC-006 übernommen); R3-GL24h-DEC-012 (LINKS/RECHTS = zwei
  unabhängige Verbindungen, Poolung n=6/n=4); R3-GL24h-DEC-013
  (K_ser/K_e-Rohwerte aus der Auswertungsdatei sind um Faktor 2 zu hoch,
  analog Fmax,SF=Fmax,ges/2 zu halbieren — RES-003→RES-004-Korrektur);
  siehe auch COMMON-COMMON-DEC-001–006
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
  Gewindestange, kombinierter Arbeitswert; CALC-004 seit 2026-09-22
  vollständig nachvollziehbar, DIN EN 1993-1-8 Tab. 6.11); R3-GL24h-CALC-006
  (grobe 4×8-Tragfähigkeits-Vorhersage ASSY-Schraubengruppe aus
  Push-Out-Daten, `≈329,1 kN` je Laschenseite, CALCULATED, nicht
  bemessungsreif); R3-GL24h-CALC-007 (Hochrechnung
  ASSY-Schraubengruppen-Anfangssteifigkeit Column-Seite 16→32 Schrauben,
  `c_32,Column ≈ 183,68 kN/mm`, Potenzgesetz-Modell mit α=0,807);
  R3-GL24h-CALC-008 (Hochrechnung Beam-Seite 16→32 Schrauben über
  konstantes Beam/Column-Verhältnis, `c_32,Beam ≈ 147,47 kN/mm`,
  ausdrücklich als vorläufige Vereinfachung gekennzeichnet).
- Annahmen: R3-GL24h-ASS-001–002 (starre Kopf-/Endplatten,
  Equal-row-load ASSY-Schrauben); R3-GL24h-ASS-003 (Gruppenineffizienz
  ASSY-Schraubengruppe nur über Reihen, Spalten linear — Grundlage für
  CALC-007, ausdrücklich nur Column-Seite geltend); R3-GL24h-ASS-004
  (Beam/Column-Steifigkeitsverhältnis als schraubenzahl-unabhängig
  angenommen — Grundlage für CALC-008, bewusste Vereinfachung mangels
  belastbarer Beam-Gruppendaten).
- Versuchsergebnisse: R3-GL24h-III-PO-S-SD-36-RES-001/002/003/004,
  R3-GL24h-III-PO-S-WD-36-RES-001/002/003/004,
  R3-GL24h-III-PO-S-SC-11-B-RES-001/002/003/004,
  R3-GL24h-III-PO-S-SC-11-C-RES-001/002/003/004,
  R3-GL24h-III-PO-S-SC-44-B-RES-001 (n=1, Einzelbefund),
  R3-GL24h-III-PO-S-SC-44-C-RES-001/002/003/004. RES-003 jeweils
  `superseded_by` RES-004 (siehe DEC-013); RES-004 ist der aktuell
  gültige, je-Scherfuge korrigierte K_ser-Wert.
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
`III-PO-S-SC-44-B` fehlen komplett; Ursache für PK1's "nv"-Steifigkeit
mittlerweile geklärt — Querzugversagen, s. u. — Ursache für die
komplett fehlenden PK2/PK3 aber weiterhin unklar).

**Neu (2026-09-22):** R3-GL24h-OPQ-022 — die Beam-seitige ASSY-
Schraubengruppen-Steifigkeit für 4×4/4×8 ist nicht empirisch belegt;
der aktuell verwendete Wert (R3-GL24h-CALC-008, c32,Beam≈147,47 kN/mm)
beruht vollständig auf der unbelegten Vereinfachungsannahme
R3-GL24h-ASS-004 (konstantes Beam/Column-Verhältnis). Offen bis eine
verwertbare Beam-Gruppenmessung oder eine faserwinkelabhängige
normative/wissenschaftliche Methode verfügbar wird.

**Update (2026-09-22):** Arbeit an der Anfangsrotationssteifigkeit S_j,ini
begonnen (Variante priorisiert: No-Contact + zugseitige Vorspannung).
Dabei R3-GL24h-DEC-012 getroffen: LINKS/RECHTS bei den Push-Out-Serien
sind zwei unabhängige Verbindungen (nicht Messstellenpaare derselben
Verbindung, wie die bisherige RES-002-Beschreibung fälschlich nahelegte)
— analog zur BR-22-Poolung bei R2. Zunächst gepoolte RES-003-Einträge
(n=6, bzw. n=4 bei SD-36) angelegt, dann aber als um Faktor 2 zu hoch
erkannt und durch RES-004 ersetzt (siehe folgender Absatz) — Geltungs-
bereich der Poolung selbst vorerst nur R3/GL24h, nicht rückwirkend auf
R1/R2 angewendet (Nutzerentscheidung).

**Update (2026-09-22, Korrektur):** Nutzerhinweis zum Prüfaufbau
(symmetrischer Doppelscher-Prüfkörper: Träger/Stütze mittig, je eine
Holzlasche mit Schrauben links und rechts) führte zur Prüfung, ob K_ser
analog zu Fmax,SF = Fmax,ges/2 ebenfalls halbiert werden muss. Eigene
Prüfung der Formelzellen in der Auswertungsdatei bestätigte: ja — K_ser
wird dort mit der *ungeteilten* Gesamtkraft des Prüfstands berechnet,
während Fmax bereits als eigene "Fmax,SF"-Spalte (= Fmax,ges/2) geführt
wird; für K_ser fehlt die entsprechende Halbierung. Mit R3-GL24h-DEC-013
festgehalten und korrigiert: die RES-003-Werte wurden durch neue
RES-004-Einträge (halbiert) ersetzt: SC-11-B 6,881 kN/mm, SC-11-C
8,571 kN/mm, SC-44-C 104,973 kN/mm, SD-36 30,348 kN/mm, WD-36
37,114 kN/mm (je Scherfuge/Einzelverbindung). Die Gruppeneffizienz-
Beobachtung bleibt unverändert: 16× die gepoolte Einzelschrauben-
Steifigkeit je Scherfuge (SC-11-C, 8,571 kN/mm) ergäbe rechnerisch
137,13 kN/mm, gemessen sind nur 104,973 kN/mm (Gruppeneffizienz
≈76,5 %) — relevant für die noch offene Hochrechnung der ASSY-Gruppe
von 16 auf die reale 32-Schrauben-Gruppe (siehe Nächste Schritte). K_e
unterliegt derselben Problematik, wurde aber bislang nicht gepoolt
(DEC-013).

Außerdem: HYP-001 soll um eine eigene Rotationsfeder `C_v,f,rot` der
ASSY-Schraubengruppe erweitert werden (Vorschlag, CLAUDE_DRAFT, basierend
auf einem vom Nutzer geteilten generischen Komponentenmethode-Federmodell,
vgl. Buchholz et al. WCTE2025-Systematik) — Kombination vorgeschlagen als
`1/S_j,ini = 1/(z²·c_eq) + 1/C_v,f,rot`, noch nicht mit dem Forschenden
abgestimmt.

**Update (2026-09-22, Hochrechnung ASSY-Schraubengruppe 16→32):**
Zugpfad-Zusammenfassung der Spring-Chain (`c_t,sleeve`) geklärt:
Reihenfolge Gewindestange (`c_t`, DIN EN 1993-1-8 Tab. 6.11, `c_t=49,59
kN/mm`, CALC-004 vollständig nachvollziehbar gemacht) — Stahlplatte
(`c_c,ep=∞`, je Anschlussende) — Holzstauchung unter der Platte (`c_c,0`,
je Anschlussende, gleicher Wert beidseitig da konstante Laschenfaser,
noch offen) — ASSY-Schraubengruppe (lumped `c_ax+br,par` Column-Seite
bzw. `c_ax+br,perp` Beam-Seite, jeweils axial+queraxial in einem
Push-Out-Wert enthalten, keine weitere Aufschlüsselung).

Für die Column-Seite (`c_ax+br,par`) liegt jetzt eine Hochrechnung von
16 auf 32 Schrauben vor: mit R3-GL24h-ASS-003 (Spalten linear, Reihen
mit Potenzgesetz-Abminderung n_Reihen^α) aus den 1×1-/4×4-Push-Out-
Steifigkeiten (RES-004) kalibriert α=0,807, damit `c_32,Column ≈
183,68 kN/mm` (R3-GL24h-CALC-007). Plausibilitätsprüfung mit den
Tragfähigkeitsdaten derselben Serien (eigener Exponent α_F=0,968)
weicht nur ≈2,2 % vom unabhängig ermittelten CALC-006-Wert (329,054 kN)
ab.

Für die Beam-Seite (`c_ax+br,perp`) liegt jetzt ebenfalls eine
(als vorläufige Vereinfachung gekennzeichnete) Hochrechnung vor:
keine verwertbaren 4×4-Steifigkeitsdaten (`III-PO-S-SC-44-B`,
OPQ-021 — Ursache jetzt geklärt, Nutzerhinweis 2026-09-22:
Querzugversagen im Holz, "nv"-Flag in der Auswertungsdatei ist eine
bewusste manuelle Markierung, kein Formelfehler), und der einzige
dortige Fmax-Wert (n=1, 47,3 kN) gilt aus demselben Grund ebenfalls
nicht als belastbare Datenbasis für eine indirekte Ableitung. Geprüfte
und verworfene Ansätze: (a) gleiches α wie Column-Seite, (b) Kreuz-
verhältnis-Schätzung aus dem Beam/Column-Tragfähigkeitsverhältnis
(hängt vollständig vom nicht belastbaren 44-B-Fmax-Wert ab), (c) eine
im Push-Out-Workbook für die Column-Seite hinterlegte normative
n_ef-Formel (FprEN 1995-1-1 Tab. 11.10(6), n_ef≈12,48 für 4×4) — diese
ist zwar unabhängig von Column-Testdaten, aber faserrichtungsunabhängig
und liefert daher zwangsläufig dasselbe Verhältnis wie (a)/(b)
(mathematisch äquivalent, siehe Diskussion 2026-09-22). Literatur-
recherche (Stamatopoulos & Malo 2017 u. a.) bestätigt, dass der
Gruppeneffekt bei axial beanspruchten Schrauben/Gewindestangen real
vom Faserwinkel abhängt, liefert aber keine direkt anwendbare Formel.

**Nutzerentscheidung 2026-09-22:** pragmatische Vereinfachung gewählt
(R3-GL24h-ASS-004) — das Verhältnis c1,Beam/c1,Column = 0,8028 wird als
bei jeder Schraubenanzahl konstant angenommen (rechnerisch identisch
zu "gleiches α", jetzt aber bewusst als vorläufige Näherung markiert).
Ergebnis (R3-GL24h-CALC-008): c16,Beam ≈ 84,275 kN/mm,
c32,Beam ≈ 147,466 kN/mm. Damit liegen für beide Seiten Hochrechnungen
auf die reale 4×8-Gruppe vor: c32,Column = 183,684 kN/mm (CALC-007,
empirisch kalibriertes α), c32,Beam = 147,466 kN/mm (CALC-008, über
Beam/Column-Verhältnis). Beide noch nicht in die Zugpfad-
Gesamtsteifigkeitskette eingebunden (c_c,0 weiterhin offen).

## Nächste Schritte

Klärung von R3-GL24h-OPQ-020/021 mit dem Nutzer. Schritt-für-Schritt-
Neuherleitung der Zugpfad-Teilsteifigkeiten (c_t, c_H,eff, c_ax) statt der
bisherigen, teils undokumentierten Altwerte (CALC-001–005) — dabei c_ax
jetzt mit echten SC-11/SC-44-Versuchsdaten statt Theoriewert möglich,
Hochrechnung 16→32 Schrauben aber noch offen (kein normativer
Gruppensteifigkeits-Ansatz in ETA-11/0190 gefunden, nur ein
Tragfähigkeits-n_ef in Anhang A.8.2). Druckseiten-Steifigkeitskette
(c_c,90/c_c,0) existiert für R3 noch gar nicht und muss neu aufgebaut
werden. C_v,f,rot-Integration ins Kinematikmodell mit dem Forschenden
abstimmen. R3-GL24h-HYP-001 durch den Forschenden reviewen lassen.
