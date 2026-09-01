---
claim_id: R2-COMMON-CLAIM-026
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Yang, Liu und Ren (2016) entwickeln ein vollständiges Komponenten-
    methoden-Modell (nach EN 1993-1-8/Jaspart 2000, "UC model" nach
    Borges 2003/Girão Coelho 2004) für momententragfähige Brettschicht-
    holz-Stützen-Riegel-Anschlüsse mit eingeklebten Gewindestangen UND
    Stahlkastenprofilen. Der Anschluss wird in sieben "basic components"
    zerlegt, jede als Zugfeder/Starrkörper-Element (Fig. 2, Tab. 1): bc
    (Riegel auf Druck), bt (Schrauben auf Zug), cc (Stütze auf Druck),
    cs (Stütze auf Schub), grt (eingeklebte Gewindestangen auf Zug), gtt
    (eingeklebtes Stahlrohr auf Zug, für die Querkraftübertragung), srtb/
    srtb' (Stahlkastenprofil auf Biegung unter Zug). Kernmodellierungs-
    Idee: das Stahlkastenprofil wird — analog zur Anwendung bei Stahl-
    Endplattenverbindungen (Zoetemeijer 1974, EN 1993-1-8) — durch ein
    äquivalentes T-Stück ("equivalent T-stub") ersetzt, wobei Rohrwand
    und Quersteife als zwei parallel geschaltete T-Stücke (T-stub-1,
    T-stub-2) abgebildet werden (Fig. 3); deren Wechselwirkung wird
    vernachlässigt. Das Gesamtmodell (Fig. 4) wird nach EN 1993-1-8 zu
    einem vereinfachten Ersatzmodell mit äquivalentem Hebelarm z_eq,
    äquivalenter Zugsteifigkeit k_t (Gl. 1-3) und äquivalenter Druck-/
    Schubsteifigkeit k_c (Gl. 15) zusammengefasst.
  source: YangLiuRen2016
  pages: "42-45"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

BESONDERS HOHE RELEVANZ: dies ist die bislang einzige gefundene Quelle,
die die Komponentenmethode EXPLIZIT und vollständig auf eine momenten-
tragfähige Holzrahmenverbindung mit eingeklebten Gewindestangen
anwendet — direkter Bezug zum Kernthema der Arbeit. Wichtiger
Unterschied zu R2: der hier untersuchte Anschluss verwendet zusätzlich
Stahlkastenprofile (T-Stub-Modellierung) zur Kraftein-/-weiterleitung,
während R2 nach bisherigem Kenntnisstand ohne solche Kastenprofile
auskommt (reiner Kontakt + Gewindestangen, siehe Lippert-Auswertung
CLAIM-006 bis -025). Die generelle Modellierungslogik (Zerlegung in
Einzelkomponenten-Federn, Zusammenfassung zu äquivalentem z_eq/k_t/k_c,
siehe EN 1993-1-8) ist jedoch strukturell UNABHÄNGIG vom konkreten
Verbindungsmittel und könnte als methodisches Vorbild für eine
komponentenbasierte Modellierung von R2 dienen. Wie im übergeordneten
Vorbehalt (wiki/R2/COMMON/literature/README.md) festgehalten: keine
1:1-Übernahme von Werten oder Teilmodellen ohne eigenständige Prüfung
und explizite Entscheidung.
