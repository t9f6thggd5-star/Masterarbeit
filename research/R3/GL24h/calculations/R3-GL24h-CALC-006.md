---
calculation_id: R3-GL24h-CALC-006
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: ETA-11/0190 (Fassung 22.01.2026), Tabelle A.8.1, Formel (8.1d) —
    vereinfachend als n_ef = 0,9·n angewendet (Holz-Holz-Verbindung, axial
    beanspruchte, 45° geneigte ASSY-Schrauben)
  literature:
  experimental_data: R3-GL24h-III-PO-S-SC-44-C-RES-001, R3-GL24h-III-PO-S-SC-11-B-RES-001,
    R3-GL24h-III-PO-S-SC-11-C-RES-001
  assumptions: Faserrichtung der Holzlasche wird für diese grobe Vorhersage vereinfachend
    als durchgehend maßgebend für die n_ef-Reihenrichtung angenommen (Diskussion
    Trägerseite/Stützenseite und Hauptbauteil- vs. Laschenfaser bewusst nicht
    aufgelöst, siehe Hinweis unten); "governing"-Wert je Prüfserie = MIN(Mittelwert
    Lasche-an-Beam; Mittelwert Lasche-an-Column), analog zur Konvention des Nutzers
    für die Push-Out-Auswertungstabelle.
method: >
  Grobe Vorhersage der Tragfähigkeit EINER 4×8-ASSY-Schraubengruppe (eine Laschenseite,
  nicht die beidseitige Summe) aus den vorliegenden 1×1- und 4×4-Push-Out-Versuchen
  derselben 45°-geneigten, axial beanspruchten Schrauben (R3-GL24h-ASS-002-Kontext).
  Vereinfachung (Nutzerentscheidung 2026-09-16): n_ef = 0,9·n, linear in n — dadurch
  ist n_perp (4, quer/nebeneinander, keine Abminderung) von n_par (4→8, längs/
  hintereinander in einer Reihe, mit 0,9-Abminderung) sauber trennbar:
  F_pred(4×4) = n_perp · (0,9·n_par) · F₁ = 4·(0,9·4)·F₁ = 14,4·F₁
  F_pred(4×8) = n_perp · (0,9·n_par) · F₁ = 4·(0,9·8)·F₁ = 28,8·F₁
  Da das Modell linear in n_par ist, kürzt sich F₁ beim Verhältnis F_pred(4×8)/F_pred(4×4)
  = 28,8/14,4 = 2 exakt heraus — die Hochrechnung reduziert sich rechnerisch auf eine
  Verdopplung des gemessenen 4×4-Werts, UNABHÄNGIG vom 1×1-Wert. Der 1×1-Wert dient
  trotzdem als Plausibilitätsprüfung des 0,9n-Modells (s. u.), auch wenn er im
  Endergebnis nicht mehr auftaucht.

  Governing-Basis: da für GL24h/Lasche-an-Beam (44-B) keine verwertbaren 4×4-Testdaten
  vorliegen (nur 1 von 3 Prüfkörpern, R3-GL24h-OPQ-021 — bewusst NICHT als
  Stellvertreter verwendet), ist die einzig verfügbare und damit automatisch
  "governing" (MIN-)Basis die Lasche-an-Column-Serie (44-C, n=3).

  Plausibilitätsprüfung mit 1×1-Wert (SC-11-C, F₁=10,745 kN): Modellvorhersage
  14,4·10,745 = 154,73 kN vs. gemessen (44-C) 164,527 kN → Test liegt ca. 6,3 % über
  der einfachen 0,9n-Modellvorhersage.
equations: "F_pred(4×8) = n_perp · (0,9·n_par) · F₁, mit n_perp=4 (konstant), n_par ∈ {4,8}"
result:
  quantity: Grob abgeschätzte Tragfähigkeit EINER 4×8-ASSY-Schraubengruppe (eine
    Laschenseite; Scherkraft parallel zur Scherfuge, Fmax,SF-Konvention wie bei den
    Push-Out-Versuchen), basierend auf Verdopplung des gemessenen 4×4-Werts (Lasche
    an Column)
  value: 329.054
  unit: kN
  original_value:
  original_unit:
certainty: CALCULATED
superseded_by:
---

**Ausdrücklich eine grobe Vorhersage, keine Bemessungsgrundlage:** mehrere
Vereinfachungen wurden explizit vom Nutzer am 2026-09-16 für eine erste
Abschätzung des Anschlussverhaltens gewählt, nicht als abgesicherte
Bemessungsmethode:

- Die genaue Frage, ob die für n_ef maßgebende Faserrichtung die der Holzlasche
  (bleibt bei Träger/Stütze-Montage konstant) oder die des tieferen Hauptbauteils
  (dreht sich um 90° zwischen Träger und Stütze) ist, wurde nicht abschließend
  geklärt — für diese grobe Vorhersage wird das nicht weiter unterschieden.
- Der ggf. maßgebende Blockscher-/Netto-Querschnittsnachweis der Lasche quer zur
  Faser (bei Verbreiterung der Gruppe) wurde NICHT geprüft — die reine
  n_ef-Betrachtung berücksichtigt nur die faserparallele Gruppenwirkung, nicht
  mögliche andere, quer wirkende Versagensmechanismen.
- Das 0,9n-Modell ist eine bewusste Vereinfachung (FprEN 1995-1-1:2024/
  ETA-11/0190 2026 bieten für n≤10 sogar n_ef=n, also gar keine Abminderung,
  Tabelle A.8.1 Formel 8.1c) — hier konservativer mit 0,9n angesetzt.
- 45°-Winkel der Schrauben und deren Klassifikation als überwiegend axial
  beanspruchte, geneigte Schrauben (nicht Scherbeanspruchung trotz
  "Push-Out"-Versuchsbezeichnung) siehe Diskussion vom 2026-09-16, ETA-11/0190
  Anhang A.2.4.5 und Tabelle A.8.1 Zeile (8.1g).

Ergebnis bezieht sich auf EINE Laschenseite (ein 4×8-Schraubengruppe); die reale
Verbindung hat laut Nutzer je Zugpfad zwei solcher Gruppen (Lasche an Beam UND
Lasche an Column) sowie eine Verdopplung durch beidseitige Laschen — eine
Zusammenführung zu einem Gesamtwert für den Zugpfad ist hier nicht vorgenommen.

Nicht verknüpft mit der bestehenden Zugpfad-Steifigkeitskette (R3-GL24h-CALC-001–005)
— das ist eine reine Tragfähigkeits-, keine Steifigkeitsbetrachtung.

**Nachtrag (2026-09-16):** Dieser Wert (329,054 kN) wurde per
R3-GL24h-DEC-011 als "gewählte Last" für die weitere Bemessung des
Zugpfads festgelegt. Die oben genannten Einschränkungen (grobe
Vorhersage, keine Bemessungsgrundlage) gelten dafür unverändert fort.
