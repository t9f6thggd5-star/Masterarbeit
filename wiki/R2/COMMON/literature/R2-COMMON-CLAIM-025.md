---
claim_id: R2-COMMON-CLAIM-025
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Anhang C (letzter Abschnitt der Dissertation, PDF-Ende) vergleicht
    für alle 6 Prüfkonfigurationen der Lastausbreitungs-Versuchskörper
    (D0, D45, D67.5, D90, Z0, Z0E — siehe Kapitel 3/R2-COMMON-CLAIM-008)
    und je 4 Messebenen (h=20/50/60/70cm) die mit FE-Modellvariante "1-4"
    berechneten und die gemessenen Dehnungen bei 30kN Last. Textliches
    Gesamtfazit (PDF S. 195): die Übereinstimmung mit den
    Versuchsergebnissen ist für die Konfigurationen D0, D90 und Z0 SEHR
    GUT; bei den Konfigurationen D45 und D67.5 streuen die
    Versuchsergebnisse TEILWEISE STARK — das FE-Modell bildet aber auch
    hier die aus den Messwerten erkennbaren Tendenzen richtig ab.
  source: Lippert2002
  pages: "195"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Ergänzt R2-COMMON-CLAIM-008/009 um eine wichtige Einschränkung zur
Modellgüte: das FE-Modell (Variante 1-4), auf dem der gesamte
Lastausbreitungswinkel-Berechnungsvorschlag (Gl. 3.41) beruht, ist
NICHT für alle Kraft-Faserwinkel gleich gut validiert — bei
Zwischenwinkeln (45°, 67.5°) ist die Punktgenauigkeit geringer
(größere Streuung der Einzelmessungen) als bei den Extremwerten (0°,
90°) und bei reiner Zugbelastung (Z0). Dies ist ein zusätzlicher Hinweis
auf die in R2-COMMON-CLAIM-009 bereits dokumentierte, von Lippert selbst
konstatierte Unsicherheit des Berechnungsvorschlags — bei einer
möglichen Anwendung auf R2 (falls R2-Gewindestangen unter einem
Zwischenwinkel zur Faser eingeklebt sind) wäre dieser Umstand zusätzlich
zu berücksichtigen.

---
Hiermit ist die vom Nutzer beauftragte vollständige Auswertung von
Lippert2002 "der Reihe nach, Kapitel 1 bis Anhang C" abgeschlossen
(Kapitel 1-7 durch CLAIM-006 bis -022, Anhang A durch CLAIM-023/-024,
Anhang C durch diesen Claim; Kapitel 8 Literaturverzeichnis und Kapitel
9 Bezeichnungen wurden bewusst nur überflogen, nicht als eigene Claims
dokumentiert, da reine Quellenliste bzw. Formelzeichen-Glossar ohne
eigenständigen Aussagegehalt; Anhang B Dehnmeßrosetten wurde ebenfalls
nur überflogen, da reine Messtechnik-Mathematik ohne R2-Bezug).
