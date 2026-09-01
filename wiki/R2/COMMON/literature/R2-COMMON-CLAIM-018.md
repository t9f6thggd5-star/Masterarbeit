---
claim_id: R2-COMMON-CLAIM-018
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Modellierung der Druckkraftaufnahme durch Kontakt (Abschnitt 6.2.3):
    die tatsächliche (FE-berechnete und experimentell an Körper 1
    bestätigte) Druckspannungsverteilung im Gehrungsschnitt ist
    NICHTLINEAR (näherungsweise quadratisch); im Bereich der
    einspringenden Ecke sind die FE-Dehnungen zu hoch, da das lineare
    Materialmodell kein Druckplastizieren abbildet — die gemessenen
    Dehnungen deuten auf Plastizieren und Spannungsumlagerung hin. Zur
    Berücksichtigung des Plastizierens wird die maximale Dehnung
    pauschal auf 70% des berechneten Werts abgemindert; die
    (abgeminderte) quadratische Verteilung wird anschließend
    flächengleich durch eine GERADE (dreiecksförmige Druckzone) ersetzt
    (Klingler 2001). Die Höhe h_d dieser angenäherten dreiecksförmigen
    Druckzone beträgt nach Klingler (2001) 50% der Kontaktflächenhöhe
    h_f im Gehrungsschnitt; allgemeiner, bezogen auf den Abstand h_z
    zwischen resultierender Zugkraft und Druckrand, gilt h_f/h_z = 0.80
    und damit h_d = 0.80 · 0.5 · h_z = 0.4 · h_z (Gl. 6.2) — dies ist die
    in R2-COMMON-CLAIM-014 bereits referenzierte Formel, deren
    theoretischer Wert (h_d=39.9cm bei h_z=99.7cm) gut mit dem aus
    Messungen ermittelten Wert übereinstimmt.
  source: Lippert2002
  pages: "142-144"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Vervollständigt R2-COMMON-CLAIM-014 um die Herleitung: die Formel
h_d = 0.4·h_z ist kein empirischer Zufallswert, sondern folgt aus der
Kombination (a) einer FE-gestützten Abschätzung des Verhältnisses
Kontaktflächenhöhe/Zugkraft-Abstand (h_f/h_z=0.80) und (b) der
Ersetzung der (um Plastizieren auf 70% abgeminderten) quadratischen
Spannungsverteilung durch eine flächengleiche Dreiecksverteilung
(Faktor 0.5). Für eine mögliche Anwendung auf R2 (Bezug:
R2-COMMON-OPQ-001, Druckzonenhöhe/Steifigkeit) wäre zu prüfen, ob die
zugrunde liegenden Annahmen (insbesondere die 70%-Plastizierungs-
Abminderung und das Verhältnis h_f/h_z=0.80) für R2s Geometrie und
Werkstoffe (GL24h/GL75, ggf. mit Querdruckverstärkung) übertragbar
sind — dies wurde nicht geprüft und wäre eine eigenständige
Entscheidung.
