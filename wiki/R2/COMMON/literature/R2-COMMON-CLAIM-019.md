---
claim_id: R2-COMMON-CLAIM-019
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Kraftaufteilung zwischen Kontaktdruckzone und Verstärkung (Abschnitt
    6.2.4): FE- und Messergebnisse (Abb. 6.6) zeigen, dass bei
    unverstärkter Innenecke die höchste Druckdehnung im Voutenbereich
    am Gehrungsschnitt auftritt; bei Verstärkung (z. B. Schlitzblech)
    wird nur ein Teil der Kraft durch Kontakt übertragen — WIE GROSS
    dieser Teil ist, hängt entscheidend von der Nachgiebigkeit
    (Schlupf) der Verbindungsmittel der Verstärkung ab: nachgiebige
    Verbindungsmittel → Verstärkung übernimmt nur einen kleinen Teil;
    starre Verbindungsmittel → Verstärkung übernimmt den Großteil. Für
    Konstruktion/Bemessung werden VIER Möglichkeiten der Kraftaufteilung
    genannt: (1) Aufteilung nach dem Verhältnis der Tragfähigkeiten der
    beiden Komponenten (als Ersatz für ein nicht eindeutig bestimmbares
    Steifigkeitsverhältnis bei reiner Kontaktverbindung — das
    Holzbau-Handbuch, Reihe 2/Teil 2/Folge 2 (1991) nimmt Kontakt
    pauschal als unnachgiebig an, was laut Lippert NICHT der Realität
    entspricht); DIN 1052 (1996) verlangt bei etwa gleicher Nachgiebigkeit
    mehrerer Verbindungsmittel eine 1.5-fache Bemessung des Bauteils mit
    dem geringeren Kraftanteil. (2) Verstärkung wird mit voller
    Tragfähigkeit angesetzt, Rest über Kontakt. (3) Kontakt wird mit
    voller Tragfähigkeit ausgenutzt, Rest der Verstärkung zugewiesen.
    (4) Druckkraft wird VOLLSTÄNDIG der Verstärkung zugewiesen
    (vermeidet die Unsicherheit der Kraftaufteilung vollständig, ist die
    von Lippert als am sichersten dargestellte Variante).
  source: Lippert2002
  pages: "144-146"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

DIREKT METHODISCH RELEVANT für R2-COMMON-OPQ-008 (die Frage der
Kraftaufteilung zwischen unverstärkter Kontakt-Druckzone und
Querdruckverstärkung in R2, GL24h vs. GL75) — Lippert benennt hier
explizit, dass eine eindeutige, unstrittige Aufteilung nicht möglich
ist und schlägt vier alternative, jeweils in sich konsistente
Bemessungsansätze vor. Variante (4) (volle Zuweisung an die
Verstärkung) ist konservativ bezüglich der Verstärkung, aber NICHT
notwendigerweise konservativ für den unverstärkten Fall — welche
Variante der bestehenden R2-Berechnung (research/R2/*/calculations/)
implizit zugrunde liegt, wurde in diesem Durchgang NICHT geprüft. Dies
wäre ein möglicher, aber eigenständig zu entscheidender Ansatzpunkt zur
(Teil-)Klärung von OPQ-008, sollte aber nicht ungefragt in die
bestehende Berechnung übernommen werden.
