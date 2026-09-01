---
claim_id: R2-COMMON-CLAIM-020
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Lippert leitet drei vollständige, geschlossene Gleichgewichtsmodelle
    zur Ermittlung aller inneren Kräfte (Zugstangenkraft F_g,ax,
    Querstangenkraft/Umlenkkraft F_u, Querbelastung F_g,v, Druckkraft
    F_c,i) aus den äußeren Schnittgrößen M, N, V im Gehrungsschnitt
    her, jeweils für einen anderen Verbindungstyp: Abschnitt 6.3
    "Kraftaufteilung mit Kontakt bei schließendem Moment" (Zug über
    Gewindestangen, Druck über Kontakt ± Verstärkung — Gl. 6.3-6.20,
    Kräftegleichgewicht Gl. 6.14, aufgelöst nach F_g,ax,a in Gl. 6.19a/b);
    Abschnitt 6.4 "Kraftaufteilung mit Kontakt bei öffnendem Moment"
    (Zug über Verbindungsmittel an der Innenecke, Druck über Kontakt an
    der Außenecke — Gl. 6.21-6.33, analog aufgebaut, F_g,ax,i in Gl.
    6.32); Abschnitt 6.5 "Kraftaufteilung ohne Kontakt für wechselndes
    Moment" (Zug UND Druck ausschließlich über Gewindestangen, für
    wechselnde Beanspruchung — Gl. ab 6.34, in dieser Auswertung noch
    nicht extrahiert). Gemeinsame Modellbausteine aller drei Varianten:
    (a) die resultierende Stangenkraft je Gruppe wird über einen
    gewichteten Hebelarm a_g (Gl. 6.5/6.9/6.23, angenähert über den
    Schwerpunkt bzw. bei zwei Reihen über Gl. 6.5b) ermittelt; (b) die
    Umlenkkraft F_u ergibt sich aus der vektoriellen Differenz von
    Achsial- und Querkraftanteil der Zug-/Druckstangen (Gl. 6.15/6.28);
    (c) die Querbelastung der Querstangen wird proportional zur
    Umlenkkraft mit einem Beiwert r angesetzt (Gl. 6.16/6.29, r selbst
    wird in dieser Auswertung noch nicht näher hergeleitet); (d) die
    Querbelastung der Zugstangen wird proportional zur Zugkraft mit dem
    Faktor v nach Gl. 6.1 angesetzt (Gl. 6.18/6.30, siehe
    R2-COMMON-CLAIM-017).
  source: Lippert2002
  pages: "147-156"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Dies ist Lipperts vollständiges analytisches "Federmodell"-Äquivalent
für die Rahmenecke (Kräftegleichgewicht statt Federsteifigkeiten) und
strukturell am ehesten mit dem eigenen R2-Federmodell vergleichbar. Es
wurde in diesem Durchgang bewusst NICHT im Detail nachgerechnet oder
mit der R2-Berechnung verglichen — die Gleichungen sind in ihrer vollen
Form sehr umfangreich (siehe Originaltext PDF S.147-156) und eine
Übernahme/ein Abgleich mit R2 wäre ein eigenständiges, vom Nutzer zu
veranlassendes Projekt, kein Nebenprodukt dieser Literaturauswertung.
Bemerkenswert: das Modell behandelt DREI separate Fälle (schließend
mit Kontakt / öffnend mit Kontakt / wechselnd ohne Kontakt) mit jeweils
eigenen Gleichungssätzen statt eines einzigen, für alle Lastfälle
gültigen Federmodells — dies unterscheidet sich konzeptionell von einem
generischen Federmodell-Ansatz (wie er dem R2-Spring-Diagramm
zugrunde liegt, falls dieses lastfallunabhängig aufgebaut ist; nicht
verifiziert). Sollte das R2-Modell künftig gegen Lipperts Modell
plausibilisiert werden, wäre dies der zentrale Abschnitt dafür.
