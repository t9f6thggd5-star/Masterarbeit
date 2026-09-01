---
claim_id: R2-COMMON-CLAIM-017
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Grundlage des mechanischen Modells (Abschnitt 6.2.1) ist eine 3D-FE-
    Untersuchung eines halben Rahmenschenkels (16×70cm², 4 Zugstangen in
    2 Reihen, 2 Querstangen in 1 Reihe; Stahl isotrop-linear-elastisch,
    Holz anisotrop-linear-elastisch, Klebefuge nicht modelliert),
    durchgeführt von Klingler (2001) im Rahmen einer Diplomarbeit,
    Parametervariation: Gewindestangenlänge 500-1500mm, -durchmesser
    10-28mm, Achs-/Randabstände 4d/2d, Ausführung der Innenecke (mit/
    ohne Verstärkung), Schlupf in den Verbindungsmitteln der
    Verstärkung. Lippert weist ausdrücklich darauf hin, dass die
    Modellannahmen NUR für den untersuchten Parameterbereich gelten und
    für eine Verallgemeinerung (insb. Körperabmessungen, Anzahl/Abstände
    der Zug-/Querstangen) weitere Parameterstudien erforderlich wären.
    Abschnitt 6.2.2 (Zugkraftaufnahme): die Kraftaufteilung auf einzelne
    Gewindestangenreihen erfolgt über eine LINEARE Dehnungsverteilung,
    deren Bezugshöhe nach Klingler (2001) 40% der Querschnittshöhe OHNE
    Voute beträgt — dieser Wert stimmt mit den in Abschnitt 5.6.5
    gemessenen Stahlteil-Verformungen überein (siehe R2-COMMON-
    CLAIM-016). Zusätzlich erhalten die Zugstangen durch die Verformung
    des Anschlusselements eine Querbelastung, angegeben als Anteil v der
    Zugkraft nach Aicher u. a. (1997), Gl. 6.1: v ≈ 3.6·e^(-0.06·β) für
    Gehrungswinkel β zwischen 45° und 60° (Tabelle 6.1: v=0.24 bei
    β=45°, v=0.14 bei β=54°, v=0.10 bei β=60° — entspricht 6-15% der
    Achsialbelastung je nach Stangendurchmesser). Klingler (2001)
    bestätigt für β=54° ein ähnliches Ergebnis unabhängig davon.
  source: Lippert2002
  pages: "140-142"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Direkt relevant für die Modellierung der Kraftverteilung auf mehrere
Gewindestangenreihen in R2 (falls R2 mehrere Reihen verwendet, siehe
auch R2-COMMON-CLAIM-016 zur gemessenen 60/40-Verteilung). Die
40%-Bezugshöhen-Regel und der Querkraftanteil v sind konkrete,
übernahmefähige Näherungsformeln — ALLERDINGS ausdrücklich nur für den
oben genannten Parameterbereich (Geometrie/Stangenzahl der Lippert-
Versuchskörper) validiert. Ob R2s Geometrie (M16, GL24h/GL75, 800mm)
innerhalb oder außerhalb dieses validierten Bereichs liegt, wurde nicht
geprüft. Eine Übernahme dieser Formeln in die R2-Berechnung wäre eine
eigenständige methodische Entscheidung.
