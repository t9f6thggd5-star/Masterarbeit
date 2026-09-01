---
claim_id: R2-COMMON-CLAIM-024
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Anhang A.2 kompiliert drei Bemessungsvorschläge für QUER (rechtwinklig
    zur Stangenachse) beanspruchte eingeklebte Gewindestangen: (1) Möhler/
    Hemmer (1981), Gl. A.27: zul.F = A·d² [N], mit A=10 N/mm² (d≤16mm)
    bzw. 8 N/mm² (d=30mm) für faserparallel eingeklebte Stangen, A=14
    N/mm² (d≤30mm) für rechtwinklig zur Faser eingeklebte Stangen; bei
    Ausmitte der Kraft zur Holzoberfläche e>10mm sind die Werte um 20%
    abzumindern. (2) Riberholt (1988), Gl. A.28: Johansen-artige
    Fließgelenk-Formel F=[√(e²+k_s)−e−t]·f_e+t·f_e,s·d, berücksichtigt
    optional eine Verstärkung der Holzoberfläche durch aufgeklebtes
    Baufurniersperrholz (Parameter t, f_e,s). (3) EC5/DIN 1052 (nach
    Johansen 1949, wie in DIN V ENV 1995-2 (1997) und E DIN 1052 (1999)):
    bei rechtwinklig zur Faser eingeklebten Gewindestangen darf die
    Lochleibungsfestigkeit um 25% gegenüber einer Stabdübelverbindung
    erhöht werden; bei faserparallel eingeklebten Gewindestangen beträgt
    die Lochleibungsfestigkeit nur 10% des Werts für rechtwinklig zur
    Faser eingeklebte Stangen (Bemessungsgleichungen selbst werden im
    Original nicht wiederholt, sondern auf die Normen verwiesen).
  source: Lippert2002
  pages: "190-191"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Relevant, falls für R2 die Querbeanspruchung der Gewindestangen (z. B.
aus der Umlenkkraft, siehe R2-COMMON-CLAIM-010/011/017 zum Faktor v)
gegen einen dieser Vorschläge nachzuweisen wäre — bislang wird in den
bekannten R2-Berechnungen (research/R2/*/calculations/) nach
Kenntnisstand dieser Auswertung mit E-DIN-1052-artigen Nachweiswerten
gearbeitet (nicht verifiziert, keine explizite Quellenangabe in den
research/-Einträgen bekannt). Auffällig: der Faktor 10 zwischen
faserparalleler und rechtwinkliger Lochleibungsfestigkeit (Punkt 3)
ist eine erhebliche Differenzierung, die bei der Bewertung von R2s
Querstangen (falls vorhanden und faserparallel eingeklebt) relevant
sein könnte — dies wurde nicht geprüft.
