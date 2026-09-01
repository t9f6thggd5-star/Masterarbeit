---
claim_id: R2-COMMON-CLAIM-023
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Anhang A.1 kompiliert acht historische Bemessungsvorschläge zur
    charakteristischen/zulässigen Haftspannung f_v achsial beanspruchter
    eingeklebter Gewindestangen (Übersicht, jeweils mit Originalformel):
    (1) Möhler/Hemmer (1981): pauschale zul. Schubspannung
    zul.f_v=1.2 N/mm² (d≤24mm) bzw. 0.8 N/mm² (d=30mm), bei Zug
    rechtwinklig zur Faser zu halbieren. (2) Gerold (1992/1993):
    f_v,m = f_v,m,b·(1−k_s·l_g/d_g) − τ_Δu·γ, berücksichtigt
    Holzfeuchteänderung. (3) DIN V ENV 1995-2 (1997), Gl. A.9:
    f_v,k = 1.2·10⁻³·d_equ^(-0.2)·ρ_k^1.5 — UNABHÄNGIG von Einklebelänge/
    Schlankheit (bereits in R2-COMMON-CLAIM-007 als Kritikpunkt
    dokumentiert). (4) Kangas (1994), Gl. A.12:
    f_v,k = 6.5·(1−l_g,ef/(100·d_g)), l_g,ef=l_g−1.5·d_g. (5) Riberholt
    (1986/1988), Gl. A.13/A.16: nichtdimensionsreine Kraftformel
    F=f_ws·ρ_k·d·√l_g (l_g≥200mm) bzw. F=f_wl·ρ_k·d·l_g (l_g<200mm),
    Festigkeitsparameter je nach Klebstoff (spröde/nichtspröde) nach
    Tabelle A.1. (6) Blaß u. a. (1996), Gl. A.19: an Riberholt angepasst,
    Umschlagpunkt bei l_g≥250mm (statt 200mm), keine Klebstoff-
    Unterscheidung mehr (Tabelle A.2). (7) E DIN 1052 (1999), Gl. A.22
    (Geradenzug-Näherung an Blaß u. a., ρ_k=380kg/m³ angenommen):
    f_v,k=4.0 N/mm² (l<250mm); (5.25−0.005·l) N/mm² (250≤l<500mm);
    (3.5−0.0015·l) N/mm² (500≤l<1000mm). (8) Aicher (2001a), Gl.
    A.25/A.26 — bruchmechanisch basiert (Johansson u. a. 1995,
    Aicher u. a. 1999), UNTERSCHEIDET explizit nach Klebstofftyp:
    Phenol-Resorcinharz (nachgiebig) f_v,k=min{5.42;
    12·d_h^(-0.25)·(l_g/d_h)^(-0.12)}; Epoxydharz (spröde) f_v,k=min{7.55;
    60·d_h^(-0.49)·(l_g/d_h)^(-0.46)} — die Resorcin-Formel ist identisch
    mit der bereits in R2-COMMON-CLAIM-012 (Gl. 5.10) dokumentierten
    Formel.
  source: Lippert2002
  pages: "185-189"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Konsolidierte Referenztabelle aller im Werk behandelten historischen
Bemessungsansätze für die axiale Haftspannung eingeklebter
Gewindestangen — nützlich als Nachschlagewerk, falls für R2 ein
Vergleich verschiedener Bemessungsansätze für c_ax,f (Zugstangen-
Grundwert der Steifigkeitskette, Bezug: R2-COMMON-CLAIM-006) gewünscht
wird. WICHTIGSTE Erkenntnis für R2: nur der Ansatz nach Aicher (2001a,
Punkt 8) berücksichtigt explizit den Klebstofftyp (spröde vs.
nachgiebig) UND ist der einzige der acht Ansätze, der bereits in der
R2-Berechnung über Gl. 5.10/CLAIM-012 aufgetaucht ist — die anderen
sieben Formeln wurden bislang NICHT mit R2 abgeglichen. Keine dieser
Formeln wurde in diesem Durchgang nachgerechnet oder bewertet; eine
Auswahl/Anwendung auf R2 wäre eine eigenständige, vom Nutzer zu
treffende methodische Entscheidung.
