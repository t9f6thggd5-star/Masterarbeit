---
interpretation_id: COMMON-COMMON-INT-001
scope:
  connection: COMMON
  material: COMMON
type: INTERPRETATION
based_on:
  sources:
    - MA-Aufgabenstellung-Maucher-2026
  decisions:
    - COMMON-COMMON-DEC-003
  experimental_results:
  observations:
interpretation: >
  Auslegung der Zielsetzung der Arbeit: Gefordert ist ein analytisches
  Federmodell je Rahmenecke (geschlossene Formeln, in Excel rechenbar),
  dessen Federwerte möglichst aus den Komponentenversuchen stammen.
  Komponentenversuche sind Eingangsgröße, Rahmeneckversuche dienen
  ausschließlich der Validierung. Nicht gefordert ist eine Rechenformel,
  die die Komponenten-Versuchssteifigkeiten aus Geometrie/Material
  reproduziert. Die über den Einzelfall hinaus übertragbaren Ergebnisse
  der Arbeit liegen auf Ebene der Methode (Gültigkeit des Zusammensetzens,
  Übertragungsregeln Versuch → realer Anschluss, Abgrenzung der
  Komponenten, dominierende Federn, Anforderungen an
  Komponentenversuche), nicht auf Ebene der anschlussspezifischen
  Zahlenwerte.
certainty: INTERPRETED
superseded_by:
authored_by: CLAUDE_DRAFT
reviewed: false
date: "2026-09-23"
---

# Zielsetzung und Einordnung der Arbeit (Auslegung der Aufgabenstellung)

Entstanden aus der Diskussion vom 2026-09-23 nach vollständiger Sichtung
der Aufgabenstellung (`MA-Aufgabenstellung-Maucher-2026`, 4 Seiten).
Die Phasenstruktur selbst ist in COMMON-COMMON-DEC-003 festgehalten;
dieser Eintrag ergänzt die **inhaltliche Auslegung** des Ziels.
Kapitelzuordnung: Einleitung/Zielsetzung (`research/thesis/introduction/`),
mit direktem Bezug zu `methodology/`, `limitations/` und `outlook/`.

**Status:** `CLAUDE_DRAFT`, `reviewed: false` — Auslegung von Claude,
vom Forschenden im Chat grundsätzlich mitgetragen, aber noch nicht
formal geprüft (CLAUDE.md Abschnitt 14). Nicht als bestätigte Aussage
zitieren, bevor `reviewed: true` gesetzt ist.

## 1. Wortlaut der Aufgabenstellung (Bezugsstellen)

Quelle: `MA-Aufgabenstellung-Maucher-2026`

- S. 2, Problemstellung: „Ziel der Arbeit ist es, die Vorgehensweise zur
  Anwendung der Komponentenmethode auf die drei unterschiedlichen
  Anschlusskonfigurationen aufzuzeigen und wesentliche Einflussparameter
  der entwickelten Federmodelle für die Beschreibung des
  Anschlussverhaltens zu bewerten."
- S. 2, Einleitung: Der vorliegende Komponentenkatalog soll hinsichtlich
  seiner allgemeinen Anwendbarkeit „durch experimentelle Untersuchungen
  validiert werden".
- S. 3, Phase 3: Eingangsgrößen „möglichst reale, aus den Versuchen
  bestimmte Kennwerte anstelle rein normativer oder theoretischer
  Annahmen"; Federmodelle so aufbauen, dass das
  Momenten-Rotationsverhalten „analytisch (bspw. mithilfe eines
  Excel-Tools)" bestimmt werden kann.
- S. 4, Phase 4: Einfluss der Grundkomponenten auf Gesamtsteifigkeit und
  Tragverhalten; Auswirkungen der Streuung der Eingangsgrößen; Vergleich
  mit Rahmeneckversuchen, soweit vorhanden; Grenzen der Modellierung und
  Ansätze zur Weiterentwicklung der Komponentenmethode.

## 2. „Analytisch" + „Versuchswerte als Eingang"

- **Modell = analytisch:** Federmodell mit geschlossenen Formeln —
  Reihenschaltung `1/c = Σ 1/c_i`, Parallelschaltung `c = Σ c_i`,
  Hebelarm z, `M = F·z`, `φ = (Δ_Zug + Δ_Druck)/z`,
  `S_j,ini = z²·c_eq` (ggf. zusätzliche Drehfeder); Tragfähigkeit über
  die maßgebende Komponente. Kein FE, kein Kurvenfit an die ganze Ecke.
- **Eingangswerte = aus Komponentenversuchen:** Steifigkeit/F_max je Feder
  aus Push-Out-/Zugversuchen statt Normformel. Beispiel im Repo:
  R3-GL24h-CALC-003 (normativer Wert nach FprEN 1995-1-1 Gl. 11.29,
  superseded) → R3-GL24h-CALC-007/-008 (aus Push-Out-Versuchen).
- **Komponentenversuche = Input, Rahmeneckversuche = Validierung.**
  Rahmeneckversuche dürfen nicht in Federwerte einfließen, sonst wird das
  Modell in Phase 4 mit sich selbst verglichen.
- **„Möglichst":** Wo kein Komponentenversuch vorliegt (z. B.
  Gewindestange nach DIN EN 1993-1-8, Stahlplatte als starr,
  Holzpressung c_c,90/c_c,0), sind Norm-/Theoriewerte zulässig — im Modell
  kenntlich machen; gehört zur Diskussion der Modellgrenzen.
- **Übertragungsregeln Versuch → realer Anschluss** sind Teil des
  analytischen Modells und als Annahmen zu dokumentieren, z. B.
  Gruppenhochrechnung 16→32 Schrauben (R3-GL24h-ASS-003/-004),
  K_ser je Scherfuge beim Doppelscher-Prüfkörper (R3-GL24h-DEC-013).
- **Streuung → Parameterstudie:** Modell mit Mittelwert ± s bzw.
  Min/Max der Versuchswerte rechnen → Bandbreite von S_j,ini bzw. der
  M-φ-Kurve und dominierende Federn (deckt die Phase-4-Forderung ab).
- **Nichtlinearität** bleibt analytisch möglich: Federn als bi-/trilineare
  Kennlinien aus den Versuchs-Last-Verschiebungskurven, laststufenweise
  kombiniert.

## 3. Was nicht das Hauptziel ist

- Nicht gefordert: eine Formel, die die Komponentensteifigkeit aus
  Geometrie/Material so vorhersagt, dass die Versuchswerte herauskommen
  („bessere K_ser-Formel"). Die Komponentensteifigkeit ist gemessener
  Input, kein Rechenergebnis.
- Gefordert ist die Ebene darüber: aus gemessenen Komponenten das
  Verhalten der gesamten Rahmenecke vorhersagen und bewerten, ob
  Zerlegen + Zusammensetzen für drei konstruktiv sehr unterschiedliche
  Anschlüsse funktioniert.
- Übertragbarkeit auf andere Anschlüsse entsteht in der
  Komponentenmethode über den **Baukasten**: allgemeine
  Kombinationslogik + Komponenten im Katalog, die in anderen Anschlüssen
  wiederverwendet werden; neue Komponenten erfordern Versuch oder Formel.
  Die Arbeit ist ein Validierungsbeitrag hierzu.
- Mögliche Ergänzung (Phase 3/4): Gegenüberstellung Versuchswert vs.
  Normwert (z. B. Push-Out-K_ser vs. FprEN 1995-1-1 Gl. 11.29). Eine
  daraus kalibrierte Bemessungsformel wäre eher Ausblick (geringe
  Prüfkörperanzahl je Serie). Umfang mit Betreuung (L. Buchholz)
  abstimmen — noch offen.

## 4. Was an der Arbeit übertragbar ist, obwohl die Zahlen fallspezifisch sind

Anschlussspezifische Zahlenwerte (z. B. S_j,ini einer bestimmten
Rahmenecke/Materialkombination) gelten nur für diese Geometrie.
Übertragbar sind Erkenntnisse über die Methode:

1. **Gültigkeit des Zusammensetzens im Holzbau:** Passt die
   komponentenbasierte M-φ-Kurve zum Rahmeneckversuch → Beleg für das
   Prinzip. Passt sie nicht → zeigen, welche Annahme versagt (fehlende
   Komponenteninteraktion, Kontakt, Vorspannung, Hebelarm). Auch ein
   begründetes „passt nicht" ist ein übertragbares Ergebnis.
2. **Übertragung Versuch → realer Anschluss** (größte Lücke im Katalog):
   Gruppeneffekt 16→32 (R3-GL24h-ASS-003/-004), Beam- vs. Column-Seite
   bzw. Faserwinkel ohne verfügbare Formel (R3-GL24h-OPQ-022), K_ser je
   Scherfuge (R3-GL24h-DEC-013).
3. **Abgrenzung der Komponenten:** z. B. c_c,0 vs. c_H,Lasche (mögliche
   Doppelerfassung, R3/GL24h, noch offen), c_t vs. c_ax (R2) — zeigt, wo
   der Katalog Komponenten nicht eindeutig voneinander trennt.
4. **Dominierende Federn:** Muster, die bei allen drei Anschlüssen
   auftreten, sind übertragbare Aussagen. Ein solcher Vergleich ist nach
   CLAUDE.md Abschnitt 12 unter `wiki/cross_connection/` zu führen.
5. **Anforderungen an Komponentenversuche:** z. B. Querzugversagen bei
   III-PO-S-SC-44-B, fehlende Kraftaufteilung je Scherfuge in der
   Auswertungsdatei, fehlende Beam-Gruppenversuche → Empfehlungen für
   künftige Versuchsprogramme.

Einordnung: Die Arbeit ist ein Baustein im Forschungsprojekt HIP_2685085;
die allgemeine Methode entsteht dort aus mehreren solchen Fallstudien.

## 5. Konsequenz für das Schreiben

In jedem Kapitel bewusst trennen zwischen „gilt nur für diesen Anschluss"
und „gilt für die Methode". Die Punkte 4.2 und 4.3 liefern die Grundlage
für die Phase-4-Kapitel „Grenzen der Modellierung" (`limitations/`) und
„Weiterentwicklung der Komponentenmethode" (`outlook/`).
