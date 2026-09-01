---
claim_id: R2-COMMON-CLAIM-012
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Bemessung der Gewindestangen der Versuchskörper (Abschnitt 5.2.5):
    Mindestabstände nach E DIN 1052 (1999) untereinander 5·d, zum Rand
    2.5·d; bei Unterschreitung dieser Mindestabstände ist die
    charakteristische Haftfestigkeit mit einem Abminderungsfaktor
    χ = 0.128·(a/d) + 0.679 ≤ 1 zu verringern (Gl. 5.13, hier a = 2d
    vorhanden statt 2.5d gefordert → χ = 0.935). Haftfestigkeit der
    Klebefuge (Resorcinklebstoff) nach Aicher (2001a), Gl. 5.10:
    f_v,k = min{5.42; 12·d_h^(-0.25)·(l_g/d_h)^(-0.12)} [N/mm²]
    (d_h = Bohrlochdurchmesser [mm], l_g = Einklebelänge [mm]) —
    Zahlenbeispiel M20/800mm/⌀21mm-Bohrloch: f_v,k = 3.62 N/mm² ≤
    5.42 N/mm², daraus F_g,k = f_v,k·l_g·d_g·π = 191.2 kN (Gl. 5.12),
    nach Abminderung mit χ: F_g,k = 178.8 kN (Gl. 5.14). Einklebelänge
    wird über die Grenzschlankheit λ=40 (Ehlbeck/Siebert 1987 — ab dieser
    Schlankheit fällt die Haftspannung im mittleren Fugenbereich auf
    Null, weitere Verlängerung bringt keinen Tragfähigkeitszuwachs)
    festgelegt. Querzugbewehrung im Hirnholzbereich (Abschnitt 5.2.5.2,
    Verstärkung durch dünne, quer zu den Zugstangen eingeklebte
    Gewindestangen am Eintrittspunkt): nach Müller und Roth (1991)
    Steigerung der Tragfähigkeit um 19–32%; Wirksamkeit auch von Deng
    (1997) und Cenci/Pedraglio (1998, "L'Aquilone di Chicco") bestätigt.
    Maximale Querzugspannungen treten laut FE-Berechnungen von Müller
    und Roth (1991) am ENDE der Gewindestange auf, nicht am Anfang.
  source: Lippert2002
  pages: "106,115"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Die Aicher(2001a)-Haftfestigkeitsformel (Gl. 5.10) ist eine potenziell
wichtige ERGÄNZUNG zu den in R2-COMMON-CLAIM-006 dokumentierten älteren
DIN-V-ENV-1995-2-Werten: sie ist neueren Datums (2001, näher an
heutiger Bemessungspraxis) und berücksichtigt explizit sowohl
Bohrlochdurchmesser als auch Einklebelänge (im Gegensatz zur reinen
Verschiebungsmodul-Formel aus Kapitel 2). Sie wurde hier noch NICHT mit
den tatsächlichen R2-Parametern (M16, GL24h/GL75, konkrete
Einklebelänge) nachgerechnet — dies wäre ein sinnvoller nächster Schritt,
falls die Haftfestigkeit/Verankerungslänge der R2-Gewindestangen
explizit nachgewiesen werden soll (aktuell nicht Teil der bekannten
R2-Berechnungskette, siehe research/R2/*/calculations/). Der
Abminderungsfaktor χ für unterschrittene Mindestabstände (Gl. 5.13)
ist ebenfalls ein möglicher Prüfpunkt für R2, sofern dessen
Stangenabstände von den Normwerten abweichen — dies wurde nicht
geprüft. Die Querzugbewehrung-Beobachtung (19–32% Traglaststeigerung)
ist rein informativ, R2 verwendet nach bisherigem Kenntnisstand keine
solche Bewehrung (nicht verifiziert).
