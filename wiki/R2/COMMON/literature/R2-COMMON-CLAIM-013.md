---
claim_id: R2-COMMON-CLAIM-013
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Gemessene Drehfedersteifigkeit C_φ = M/φ des Gehrungsschnitt-
    Anschlusses (Abschnitt 5.6.2, Gl. 5.16, M = Kolbenkraft×Hebelarm,
    φ = gegenseitige Verdrehung der Rahmenschenkel aus Wegaufnehmern
    w1/w2). Ergebnisse (Tabelle 5.4, Bereich vom Belastungsbeginn bis
    Höchstwert, plus empfohlener Bemessungs-"Rechenwert"):
    Versuchskörper 1 (unverstärkte Druckzone, schließendes Moment):
    22000–55000 kNm/rad, Rechenwert 55000 kNm/rad. Versuchskörper 2
    (verstärkte Druckzone/Schlitzblech, schließendes Moment):
    40000–81000 kNm/rad, Rechenwert 70000 kNm/rad. Versuchskörper 2,
    1. öffnende Belastung: 25500–32500 kNm/rad, Rechenwert 30000 kNm/rad.
    Versuchskörper 2, 2. öffnende Belastung: ab 38000 kNm/rad (kein
    sinnvoller Maximalwert ermittelbar), Rechenwert 40000 kNm/rad. Die
    Drehfedersteifigkeit bei schließender Belastung nimmt mit steigender
    Last zunächst zu (Überwindung anfänglicher Passungenauigkeiten).
    Vergleich der Last-Verformungskurven (5.6.6.4): beide Körper haben
    bei schließender Belastung anfangs die GLEICHE Steifigkeit, bis bei
    Körper 1 die unverstärkte Druckzone versagt — Körper 2 behält seine
    Steifigkeit dank Verstärkung bis zum Versagen bei. Die öffnende
    Steifigkeit von Körper 2 ist geringer, bedingt durch kleineren
    Hebelarm und die im Vergleich zu Gewindestangen weichere
    Stabdübelverbindung des Schlitzblechs.
  source: Lippert2002
  pages: "126"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

DIREKT RELEVANT für R2-COMMON-OPQ-001 (gesuchte Steifigkeitswerte der
Rahmeneckverbindung). Wichtige Einschränkungen vor Übertragung auf R2:
(1) Geometrie/Maßstab weicht erheblich ab (16×70cm² BS16h,
M20-Gewindestangen, Dachneigung 18°, Prüfstands-Gehrungsschnitt) von
R2 (800mm-Bauteil, M16, GL24h/GL75) — die absoluten kNm/rad-Werte sind
NICHT direkt übertragbar, allenfalls die Größenordnung und der
qualitative Effekt der Druckzonen-Verstärkung (Erhalt der
Anfangssteifigkeit bis zum Bruch) sind aussagekräftig. (2) Es handelt
sich um eine GESAMT-Drehfedersteifigkeit des Anschlusses (Moment/
Verdrehung), nicht um Einzelfedersteifigkeiten der Komponenten (Zug-
stangen, Druckkontakt, Querstangen) wie im R2-Federmodell — ein
direkter Vergleich mit einzelnen c-Werten der R2-Steifigkeitskette ist
daher nicht ohne Weiteres möglich, wohl aber ein Vergleich auf Ebene
der Gesamt-Rahmeneckensteifigkeit, falls eine solche für R2 ermittelt
wird. (3) Der deutliche Unterschied zwischen Versuchskörper 1
(unverstärkt, Steifigkeitsverlust bei Druckzonenversagen) und
Versuchskörper 2 (verstärkt, Steifigkeit bis Bruch erhalten) ist ein
qualitativer Hinweis darauf, dass eine verstärkte/unverstärkte
Druckzone in R2 (GL24h vs. GL75, siehe R2-COMMON-OPQ-001) ebenfalls
das Last-Verformungsverhalten qualitativ unterschiedlich prägen könnte
— dies ist eine Interpretation von Claude, nicht im Original so
formuliert, und nicht verifiziert.
