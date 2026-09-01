---
claim_id: R2-COMMON-CLAIM-027
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Momententragfähigkeit M_j,Rd nach Komponentenmethode (Abschnitt
    2.4, Gl. 4-13): M_j,Rd = Σ F_tr,Rd·h_r, wobei die dritte
    Schraubenreihe konservativ vernachlässigt wird — nur die beiden
    äußeren Reihen tragen (Gl. 5). F_tr,Rd ist jeweils der kleinste Wert
    aus sieben Einzelnachweisen: (a) Stütze auf Schub F_t,cs,Rd=f_v·b_c·
    l_v,eff (Gl. 6); (b) Stütze auf Querdruck F_t,cc,Rd=f_cu,90,l·b_c·
    (2c+a+d_n) (Gl. 8) — mit Lastausbreitung nach Van der Put (2008),
    Ausbreitungswinkel θ=45° im elastischen Bereich, UND zusätzlicher
    Bearing-width-Erweiterung c nach EN 1993-1-8 Gl. (7) (Analogie zu
    Stahl-Stützenflansch-Bemessung, hier auf Holz-Querdruck übertragen);
    (c) Schraube auf Zug F_t,bt,Rd=f_y·A_b (Gl. 9); (d) Stahlkastenprofil
    auf Biegung unter Zug F_T,1,Rd (T-Stub, drei Versagensmodi nach EN
    1993-1-8/EN1993-1-1, Gl. 10-11, mit Überfestigkeitsfaktor der
    Zugfestigkeit statt Fließspannung wegen Kaltverfestigung); (e)
    Stahlkastenprofil auf Druck M_T,c,Rd=f_u·b_f·t_f²/6 (Gl. 12); (f)
    eingeklebte Gewindestangen auf Zug F_t,grt,Rd — es wird ANGENOMMEN,
    dass hier KEIN Versagen auftritt (Überfestigkeitsfaktor γ_Rd=1.70
    zwischen duktilem T-Stub und sprödem Gewindestangen-Versagen nach
    Jorissen/Fragiacomo 2011); (g) Riegel auf Druck F_t,bc,Rd=f_cu,0·b_b·
    l_eff,bc=0.5·f_cu,0·b_b·h_srt (Gl. 13). Von den drei T-Stub-
    Versagensmodi wird Modus 1 (vollständiges Fließen des Flansches,
    duktil) explizit als BEVORZUGTER Bemessungs-Versagensmodus
    empfohlen, da inspizierbar/austauschbar nach Erdbeben und gute
    Duktilität/Festigkeit; Modus 3 (reines Schraubenversagen) wird als
    NICHT empfohlen bezeichnet (schwer reparierbar, geringe plastische
    Rotation).
  source: YangLiuRen2016
  pages: "45-46"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Ergänzt R2-COMMON-CLAIM-019 (Lipperts Kraftaufteilungsoptionen bei
verstärkter Druckzone) um einen alternativen, EN-1993-1-8-konformen
Ansatz zur Querdruck-Tragfähigkeit von Holzstützen unter konzentrierter
Lasteinleitung (Van-der-Put-Lastausbreitung + Bearing-width-Erweiterung
c) — methodisch unabhängig von Lipperts Ansatz und potenziell
interessant als Vergleich für R2-COMMON-OPQ-001/OPQ-008. Die explizite
Duktilitäts-Bemessungsphilosophie (Modus-1-T-Stub-Versagen bevorzugt,
mit Überfestigkeitsfaktor γ_Rd=1.70 zum Schutz der spröden
Gewindestangen-Verbindung) ist ein Bemessungskonzept, das in den
bisher ausgewerteten R2-Quellen (Lippert2002) nicht in dieser
expliziten Form vorkam — ob und wie R2 eine vergleichbare Kapazitäts-
Bemessungsphilosophie verfolgt, wurde nicht geprüft. Keine der
Formeln wurde nachgerechnet oder auf R2 angewendet.
