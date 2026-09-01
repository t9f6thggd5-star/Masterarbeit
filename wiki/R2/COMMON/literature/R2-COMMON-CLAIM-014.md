---
claim_id: R2-COMMON-CLAIM-014
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Ermittlung der Druckzonenhöhe (Abschnitt 5.6.3): aus der gemessenen
    Dehnungsverteilung im Gehrungsschnitt wird die Nullinienlage x_0
    bestimmt (Tabelle 5.5, Versuchskörper 2, schließend: x_0 steigt von
    33.4cm bei 50kN auf 34.8cm bei 200kN Kolbenkraft — nahezu
    unveränderlich, da das Schlitzblech den inneren Hebelarm fixiert und
    das schrittweise Versagen der Druckzone verhindert). Bei
    Versuchskörper 1 (unverstärkt) wandert dagegen die Nullinie mit
    zunehmender Last zur äußeren Ecke (Tabelle 5.5-Vergleichswerte h_q:
    47.3cm bei 50kN → 45.9cm bei 200kN), der innere Hebelarm sinkt
    ("weiche Aufnahme der Druckkraft"). Zusätzlich wurde bei
    Versuchskörper 2 die Spaltöffnung visuell gemessen (Tabelle 5.6) und
    daraus die Höhe der Druckkontaktzone h_q ermittelt. Nach Klingler
    (2001) kann der (quadratische) Druckspannungsverlauf durch eine
    dreiecksförmige Verteilung mit h_d = 0.8·h_q angenähert werden
    (gleiche resultierende Druckkraft). Mit gemessenem h_q ≈ 99.7cm/2
    [Anm.: Originaltext bezieht sich auf h_z=99.7cm, siehe Gl. 6.2 in
    Kapitel 6] ergibt sich eine theoretische Höhe h_d = 0.4·h_z = 39.9cm,
    die "gut" mit der aus x_0 ermittelten Höhe übereinstimmt (Cross-Check
    zwischen Messung und dem in Kapitel 6 hergeleiteten mechanischen
    Modell).
  source: Lippert2002
  pages: "127-129"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Dies ist der Kernbefund zur "Druckzonenhöhe" aus Kapitel 5, unmittelbar
relevant für R2-COMMON-OPQ-001 — sowohl methodisch (wie man aus
Dehnungsmessungen und Spaltöffnung auf die Druckzonenhöhe rückschließt)
als auch inhaltlich (die triangulare Näherung h_d=0.8·h_q nach Klingler
2001, und der Querverweis auf Gl. 6.2 aus Kapitel 6, der die
Druckzonenhöhe rechnerisch aus dem mechanischen Modell herleitet — Gl.
6.2 wird bei Auswertung von Kapitel 6 im Detail dokumentiert). Wichtiger
qualitativer Befund: ein UNVERSTÄRKTER Kontaktstoß (wie bei
Versuchskörper 1) zeigt eine lastabhängig WACHSENDE, "weiche" Druckzone
(Nullinie wandert), während ein durch Schlitzblech VERSTÄRKTER
Kontaktstoß (Versuchskörper 2) eine nahezu KONSTANTE Druckzonenhöhe über
den gesamten Lastbereich zeigt. Eigene Einordnung (Claude): sollte für
R2 unterschieden werden müssen, ob die Druckzone (GL24h oder GL75,
mit oder ohne Verstärkung — Bezug: bereits dokumentierte
Querdruck-Korrekturen R2-GL24h-CALC-012, R2-GL75-CALC-004) eher dem
"weichen" oder dem "steifen" Fall entspricht, wäre dies ein direkter
Ansatzpunkt zur (Teil-)Beantwortung von R2-COMMON-OPQ-001 — dies wurde
in diesem Durchgang nicht geprüft und erfordert eine explizite,
eigenständige Untersuchung.
