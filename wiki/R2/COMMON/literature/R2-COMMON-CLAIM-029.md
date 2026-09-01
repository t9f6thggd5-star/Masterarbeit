---
claim_id: R2-COMMON-CLAIM-029
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Rotationskapazität φ_Cd (Abschnitt 2.6, Gl. 27-31): wird primär
    durch die Verformungskapazität der SCHWÄCHSTEN Komponente bestimmt
    — hier: Stahlkastenprofil auf Biegung unter Zug (F_T,1,Rd, Modus-1-
    T-Stub-Versagen). Verformungsgrenzwert nach Beg u. a. (2004), Gl.
    27: δ_u,T,1 = 2·ε_u·m²/e (ε_u = Grenzdehnung an der T-Stub-
    Außenfaser, hier experimentell zu 0.30 ermittelt). Gesamtverformung
    der Zugseite (Gl. 28): δ_t = δ_cc,t + δ_bt + 2·δ_u,T,1 + δ_grt;
    Gesamtverformung der Druckseite (Gl. 29): δ_c = δ_cc,c + δ_cs +
    δ_srtc + δ_bc. Rotationskapazität φ_Cd = (δ_t,max+δ_c,max)/h_1
    (Gl. 30). Für die Kraft-Verformungsbeziehungen der Einzelkomponenten
    werden vereinfachte Kurven nach Beg u. a. (2004) angesetzt: für
    Stahlkomponenten elastisch-ideal-plastisch (Fig. 8a), für
    Holzkomponenten auf Druck NICHTLINEAR elastisch-plastisch (Fig. 8b,
    nach [35]=Eurocode 5 Hintergrunddokument), für Holzkomponenten auf
    Zug/Schub linear-elastisch angenommen.
  source: YangLiuRen2016
  pages: "47-48"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Ergänzt die bereits dokumentierten Steifigkeits-/Tragfähigkeitsmodelle
(CLAIM-026 bis -028) um den dritten Kernbestandteil der EN-1993-1-8-
Komponentenmethode: die Rotationskapazität. Für R2 methodisch relevant,
FALLS für R2 ebenfalls eine explizite Rotationskapazität (nicht nur
Momententragfähigkeit und Anfangssteifigkeit) ermittelt werden soll —
bislang in den bekannten R2-Berechnungen (research/R2/*/calculations/)
nach Kenntnisstand dieser Auswertung nicht Gegenstand. Die Annahme
unterschiedlicher Kraft-Verformungs-Charakteristiken je Werkstoff
(Stahl: ideal-plastisch; Holz-Druck: nichtlinear; Holz-Zug/Schub:
linear) ist ein allgemein übertragbares Modellierungsprinzip, keine
R2-spezifische Aussage.
