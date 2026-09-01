---
claim_id: R2-COMMON-CLAIM-016
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Ungleichmäßige Kraftverteilung innerhalb einer Gewindestangengruppe
    infolge Stahlteil-Verdrehung (Abschnitt 5.6.5): durch die elastische
    Verformung der Gewindestangen verdreht sich das am Gehrungsschnitt
    angeschlossene Stahlteil um einen Drehpunkt R. Die äußeren
    Zugstangen erfahren dadurch eine größere Verformung als die inneren
    Zugstangen — gemessen wurde ein über den gesamten Versuchsverlauf
    nahezu KONSTANTES Verhältnis von 150% (äußerer Wegaufnehmer-Weg zu
    innerem Wegaufnehmer-Weg). Da die Stangenkraft direkt proportional
    zum Weg angenommen wird, ergibt sich eine Kraftaufteilung von rund
    60% (äußere Zugstangen) zu 40% (innere Zugstangen) — bei nur zwei
    Stangenreihen. Text: "Im Querschnitt außenliegende Gewindestangen
    erhalten immer höhere Belastungen als weiter innen liegende
    Gewindestangen" (bereits in Abschnitt 5.2.6.2 als allgemeines
    Prinzip angekündigt).
  source: Lippert2002
  pages: "109,131-132"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Direkt relevant für die Bemessung von R2, sofern dort mehrere
Gewindestangenreihen (z. B. 4×M16) über ein gemeinsames Stahlteil
angeschlossen sind: eine zentrische Krafteinleitung (Annahme
gleichmäßiger Kraftaufteilung auf alle Stangen) kann laut diesem Befund
nicht ohne Weiteres vorausgesetzt werden — außenliegende Stangen werden
stärker beansprucht als innenliegende. Der konkrete Zahlenwert
(60%/40% bei zwei Reihen, M20/800mm-Stangen) ist eine versuchskörper-
spezifische Messung, keine allgemeingültige Formel, und wurde NICHT mit
der tatsächlichen R2-Stahlteil-Geometrie (Anzahl/Anordnung der
Stangenreihen, Stahlteil-Steifigkeit) abgeglichen. Ob und in welcher
Form die bestehende R2-Berechnung (research/R2/*/calculations/) diese
Ungleichverteilung bereits berücksichtigt oder von einer zentrischen/
gleichmäßigen Kraftaufteilung ausgeht, wurde in diesem Durchgang nicht
geprüft — dies wäre ein möglicher eigenständiger Prüfpunkt, sofern vom
Nutzer gewünscht.
