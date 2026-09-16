---
calculation_id: R3-GL75-CALC-001
scope:
  connection: R3
  material: GL75
type: CALCULATION
inputs:
  normative_sources: ETA-11/0190 (Fassung 22.01.2026), Tabelle A.8.1, Formel (8.1d) —
    vereinfachend als n_ef = 0,9·n angewendet (Holz-Holz-Verbindung, axial
    beanspruchte, 45° geneigte ASSY-Schrauben)
  literature:
  experimental_data: R3-GL75-III-PO-B-SC-44-B-RES-001, R3-GL75-III-PO-B-SC-44-C-RES-001,
    R3-GL75-III-PO-B-SC-11-B-RES-001, R3-GL75-III-PO-B-SC-11-C-RES-001
  assumptions: Faserrichtung der Holzlasche wird für diese grobe Vorhersage vereinfachend
    als durchgehend maßgebend für die n_ef-Reihenrichtung angenommen (Diskussion
    Trägerseite/Stützenseite und Hauptbauteil- vs. Laschenfaser bewusst nicht
    aufgelöst, siehe Hinweis unten); "governing"-Wert je Prüfserie = MIN(Mittelwert
    Lasche-an-Beam; Mittelwert Lasche-an-Column), analog zur Konvention des Nutzers
    für die Push-Out-Auswertungstabelle.
method: >
  Grobe Vorhersage der Tragfähigkeit EINER 4×8-ASSY-Schraubengruppe (eine Laschenseite,
  nicht die beidseitige Summe) aus den vorliegenden 1×1- und 4×4-Push-Out-Versuchen
  derselben 45°-geneigten, axial beanspruchten Schrauben. Identische Methode wie
  R3-GL24h-CALC-006 (siehe dort für die vollständige Herleitung von
  F_pred(4×8) = n_perp·(0,9·n_par)·F₁ = 4·(0,9·8)·F₁ und die Vereinfachung auf
  Faktor 2 gegenüber dem gemessenen 4×4-Wert).

  Governing-Basis: im Unterschied zu GL24h liegen für GL75 sowohl Lasche-an-Beam
  (44-B) als auch Lasche-an-Column (44-C) vollständige Daten (je n=3) vor. Governing
  = MIN(Mittelwert 44-B=209,043 kN; Mittelwert 44-C=276,213 kN) = 44-B.

  Plausibilitätsprüfung mit 1×1-Wert (SC-11-B, F₁=16,757 kN, konsistent zur
  44-B-Basis): Modellvorhersage 14,4·16,757 = 241,30 kN vs. gemessen (44-B)
  209,043 kN → Test liegt ca. 13,4 % UNTER der einfachen 0,9n-Modellvorhersage —
  Gegenrichtung zu GL24h (dort Test +6,3 % über Vorhersage). Das 0,9n-Modell
  über- bzw. unterschätzt je nach Material/Seite in unterschiedliche Richtungen;
  keine durchgängig konservative Vorhersage.
equations: "F_pred(4×8) = n_perp · (0,9·n_par) · F₁, mit n_perp=4 (konstant), n_par ∈ {4,8}"
result:
  quantity: Grob abgeschätzte Tragfähigkeit EINER 4×8-ASSY-Schraubengruppe (eine
    Laschenseite; Scherkraft parallel zur Scherfuge, Fmax,SF-Konvention wie bei den
    Push-Out-Versuchen), basierend auf Verdopplung des gemessenen 4×4-Werts (Lasche
    an Beam)
  value: 418.086
  unit: kN
  original_value:
  original_unit:
certainty: CALCULATED
superseded_by:
---

**Ausdrücklich eine grobe Vorhersage, keine Bemessungsgrundlage** — dieselben
Einschränkungen wie in R3-GL24h-CALC-006 gelten hier unverändert (ungeklärte
maßgebende Faserrichtung Lasche vs. Hauptbauteil, ungeprüfter Blockscher-/
Netto-Querschnittsnachweis quer zur Faser, bewusst konservative 0,9n-Vereinfachung
statt n_ef=n für n≤10, 45°-Schrägschrauben als axial statt lateral beansprucht
klassifiziert).

Ergebnis bezieht sich auf EINE Laschenseite (eine 4×8-Schraubengruppe); die reale
Verbindung hat laut Nutzer je Zugpfad zwei solcher Gruppen (Lasche an Beam UND
Lasche an Column) sowie eine Verdopplung durch beidseitige Laschen — eine
Zusammenführung zu einem Gesamtwert für den Zugpfad ist hier nicht vorgenommen.

Dies ist der erste CALC-Eintrag für R3/GL75 (zuvor keine R3-GL75-spezifischen
Berechnungen vorhanden, siehe vormaliger current_state.md-Stand).

**Nachtrag (2026-09-16):** Dieser Wert (418,086 kN) wurde per
R3-GL75-DEC-001 (erste R3/GL75-spezifische Entscheidung) als "gewählte
Last" für die weitere Bemessung des Zugpfads festgelegt. Die oben
genannten Einschränkungen (grobe Vorhersage, keine Bemessungsgrundlage)
gelten dafür unverändert fort.
