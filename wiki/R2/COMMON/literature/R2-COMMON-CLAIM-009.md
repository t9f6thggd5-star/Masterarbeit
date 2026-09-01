---
claim_id: R2-COMMON-CLAIM-009
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Lipperts eigener Berechnungsvorschlag für den Lastausbreitungswinkel
    φ am Ende axial beanspruchter, eingeklebter Gewindestangen (Gl. 3.41,
    Abschnitt 3.3.1), hergeleitet aus einer FE-Parameterstudie (verifiziert
    an Versuchskörper D0, Modellvariante "1-4": Gewindestange als Volumen,
    mit Abreißen der Klebefuge bei Zugbeanspruchung berücksichtigt):
    φ = φ₀,c/t · k_α(α) · k_ρ(ρ) · k_u(u), mit Basiswinkel φ₀,t = 5°
    (Zugbeanspruchung, keine Normalkraftübertragung am Stangenende) bzw.
    φ₀,c = 7.5° (Druckbeanspruchung); k_α = 1.25 + 0.25·sin(2α−90°)
    (Kraft-Faserwinkel, Gl. 3.24); k_ρ = 0.0007·ρ + 0.7 (Rohdichte
    [kg/m³], Gl. 3.32); k_u = 1.1 − u·0.01 (Holzfeuchte [%], Gl. 3.39).
    Die mittragende Breite ergibt sich aus b_m = 2·l_g·tan(φ). Aus der
    Parameterstudie (Tabelle 3.11, Standardfall fett): Körperbreite und
    -dicke beeinflussen die Lastausbreitung nur bis zu einer Grenze
    (Breite: bis ca. 36cm ≈ 30·d_g; Dicke: bis 10·d_g), danach kein
    weiterer Effekt; Körperhöhe hat keinen Einfluss; größerer
    Stangendurchmesser verringert die Dehnung am Stangenende (größere
    Mantelfläche überwiegt höhere Steifigkeit); die Einklebelänge wird
    bereits automatisch korrekt über die Berechnung der mittragenden
    Breite erfasst (k_lg=1.0); der E-Modul allein (bei konstantem
    Verhältnis E/G) hat keinen Einfluss auf den Lastausbreitungswinkel,
    der Schubmodul dagegen wurde für den Berechnungsvorschlag NICHT
    verwendet ("Hierfür sind weitergehende Untersuchungen erforderlich").
    Gültigkeitseinschränkung (Abschnitt 3.3.2): der Vorschlag wurde
    bewusst konservativ (abgemindert) kalibriert; beim Vergleich mit 5
    Kontroll-Varianten wichen die FE-Ergebnisse teils erheblich vom
    Berechnungsvorschlag ab (Tabelle 3.14: σ/σ_FE-Verhältnis 117–342%);
    zudem konnte NICHT geklärt werden, ob die am Stangenende berechnete
    Spannungsspitze tatsächlich das versagensmaßgebende Kriterium ist, da
    in den Versuchen kein Versagen im Holzquerschnitt erzielt wurde. Der
    Vorschlag gilt nur für den untersuchten Parameterbereich
    (Tabelle 3.11).
  source: Lippert2002
  pages: "65-88"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Dies ist der zentrale, konkret anwendbare Berechnungsvorschlag aus
Kapitel 3 und thematisch eng mit R2-COMMON-CLAIM-007 (Stand der Technik/
Motivation) verknüpft — Lippert liefert hier erstmals ein Modell, das
Einklebelänge UND Kraft-Faserwinkel gleichzeitig erfasst, was die in
CLAIM-007 dokumentierten älteren Ansätze (Kangas, Riberholt, DIN V ENV
1995-2) nicht leisten. Für R2 selbst nicht direkt übertragbar, da es sich
um die Lastausbreitung am Stangenende selbst handelt (Bemessung des
Holzquerschnitts gegen die dort auftretende Spannungsspitze), nicht um
die bereits im Projekt behandelte Querdruck-Lastausbreitung unter der
Ankerplatte (FprEN 8.1.6.x, siehe Normstellen-Index). Bemerkenswert und
unbedingt bei künftiger Nutzung zu beachten: Lippert selbst warnt
ausdrücklich, dass ungeklärt ist, ob diese Stangenend-Spannungsspitze
überhaupt das bemessungsrelevante Versagenskriterium darstellt — der
Vorschlag ist somit eine konservative Rechenhilfe, kein validiertes
Bemessungsverfahren, und die Abweichungen zur FE-Berechnung erreichen im
ungünstigsten Fall Faktor 3.4. Sollte dieser Ansatz für R2 in Betracht
gezogen werden (z. B. zur Abschätzung einer wirksamen Verbundfläche),
wäre dies eine eigenständige methodische Entscheidung, die explizit vom
Nutzer zu treffen ist (nicht eigenmächtig übernehmen).
