---
claim_id: R2-COMMON-CLAIM-008
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Experimentelle Untersuchung (Abschnitt 3.1) an 12 Versuchskörpern
    (6 Konfigurationen × 2, BS14h/BS11, 50×90×8cm, M12/8.8-Gewindestangen,
    epoxidverklebt, Einklebelänge 240mm, λ=20) zur Traglast eingeklebter
    Gewindestangen in Abhängigkeit vom Kraft-Faserwinkel α
    (0°/45°/67.5°/90°, axiale Zugbelastung): mittlere Bruchlast bei
    faserparalleler Einklebung (α=0°) 41.92 kN, bei geneigter Einklebung
    (Mittel aus 45°/67.5°/90°) 73.71 kN — eine Steigerung um ca. 70%.
    Als Ursache werden zwei Effekte genannt: (1) bei α>0° wirken
    Querfasern der Ringzugspannung um die Stange direkt entgegen
    (Spalten nur noch in einer Richtung möglich statt radial), (2) ein
    Effekt der Lastneigung selbst. Gemessene Steifigkeit der
    Gewindestangenverbindung (Tabelle 3.5): Einzelwerte 89.0–157.4 kN/cm,
    Mittelwert 122.2 kN/cm, umgerechnet auf die Klebefläche
    C = 1.25 N/mm³ (Gl. 3.10). Lippert vergleicht diesen Wert explizit
    mit der bekannten Literaturspanne 0.4–8.9 N/mm³ (Faktor 22 Streuung)
    und benennt dies selbst als klärungsbedürftig.
  source: Lippert2002
  pages: "37-48"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Direkter experimenteller Befund zur Traglaststeigerung bei geneigter
Krafteinleitung (relevant als Hintergrundwissen für die Bewertung der
Rahmenecke, in der die Gewindestangen typischerweise nicht rein
faserparallel beansprucht werden) und ein zweiter, unabhängiger
Literaturwert für die axiale Verbindungssteifigkeit C=1.25 N/mm³
(Gl. 3.10), der zusätzlich zur bereits in R2-COMMON-CLAIM-006
dokumentierten DIN-V-ENV-1995-2-Formel (0.4 N/mm³) und dem
Ehlbeck-Versuchswert (4.3–8.9 N/mm³) eine dritte Datenquelle zur
Größenordnung von c_ax,f darstellt. Wichtig: alle drei Werte stammen aus
unterschiedlichen Versuchskörpern/-randbedingungen (BS14h/BS11, M12,
240mm Einklebelänge) und wurden noch nicht mit den tatsächlichen R2-
Parametern (M16, GL24h/GL75) abgeglichen. Die von Lippert selbst
konstatierte Faktor-22-Streuung zwischen Norm- und Versuchswerten ist
ein Hinweis darauf, dass die axiale Verschiebungssteifigkeit eingeklebter
Gewindestangen generell mit erheblicher Unsicherheit behaftet ist — dies
sollte bei jeder Übernahme eines Einzelwerts in die R2-Steifigkeitskette
(Bezug: R2-COMMON-OPQ-001) explizit als Bandbreite/Sensitivität
kommuniziert werden, nicht als Festwert.
