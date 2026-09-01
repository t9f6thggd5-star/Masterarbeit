---
open_question_id: R2-COMMON-OPQ-008
scope:
  connection: R2
  material: COMMON
status: OPEN
question: >
  Welche Rolle spielen vier Excel-Inhalte, die in chat-3 nicht besprochen
  wurden, im tatsächlichen R2-Versuchs-/Rechenkonzept: (1) der
  vollständige Stabdübel-Johansen-Nachweis ("Tragfähigkeit Stabdübel",
  Spalten A-D je Blatt), (2) der Block "Tragfähigkeit Stütze auf Zug"
  (Zellen F/G43-52 bzw. G43-52 — Rolle im Rechenschema und
  Mittelwertbasis inzwischen geklärt, siehe Detailbefund unten; die
  Zellbeschriftung "Gl. 11.14" bleibt normativ nicht eindeutig
  zugeordnet, wird vom Nutzer aber nicht weiterverfolgt), (3) der
  Abschnitt
  "innerer Hebelarm Rahmeneck"/"maximales Moment"/"Zylinderkraft" (Zellen
  F/G113-133 bzw. G74-96), und (4) die beiden Vorspannungs-Arbeitsblätter
  "VSP GL24h "/"VSP GL75 " (enthalten `#DIV/0!`/`#REF!`-Fehler,
  referenzieren ASSY-Schraubengruppen und eine Annahme
  "L_eff=450 mm, F/8 je Schraube")?
context: >
  Der Nutzer hat entschieden (2026-09-01), reale Versuchsdaten aus diesen
  Blöcken direkt als Versuchsergebnisse (RES) zu übernehmen (siehe
  R2-GL24h-II-PO-S-SD-34-RES-001 u. a.), die Blöcke selbst aber vorerst
  nur als offene Frage zu dokumentieren, statt sie als vollständige
  eigene Berechnungen (CALC) auszuarbeiten, solange ihr Zweck im
  R2-Gesamtkonzept ungeklärt ist. Auffällig: der Stabdübel-Nachweis
  taucht in einem Excel auf, das eigentlich die eingeklebte-
  Gewindestangen-Verbindung (R2) behandelt — möglich wäre, dass er eine
  Hilfskonstruktion/Prüfstands-Lagerung (z. B. Anschluss der Probe an ein
  Widerlager) statt der eigentlichen R2-Rahmenecke selbst beschreibt; dies
  ist aber nicht bestätigt. Die Bezeichnungen der Versuchsreihen
  unterscheiden sich zudem zwischen den Blättern ("SD" auf Blatt
  "...GL24h SD", aber "WD" in der zugehörigen Push-Out-Versuchsreihen-ID
  auf Blatt "...GL24h HD") — auch diese Kürzel sind nicht dokumentiert.
  Der Block "Stütze auf Zug" wurde ursprünglich als mögliche
  Blockscher-/Sprödbruchprüfung der Gewindestangengruppe nach FprEN
  Fig. 11.38 vermutet; per Volltextprüfung des Normtexts (2026-09-01)
  ist das widerlegt — Fig. 11.38/Gl. 11.92 (Klausel 11.10.5.2) betreffen
  stattdessen die Zugtragfähigkeit des Holzquerschnitts um eingeklebte
  Stangen, während die im Excel zitierte Formel "Gl. 11.14" tatsächlich
  die Johansen-Traglastformel ist — beides passt nur teilweise/nicht
  eindeutig, siehe Detailbefund unten. Die "VSP"-Blätter sind strukturell ähnlich zur
  R3-Annahme "F/8 je Schraube" (siehe R3-GL24h-ASS-002), aber in R2 nicht
  einmal ansatzweise im Chat erwähnt.
related_sources:
options_considered: >
  (a) Nur dokumentieren und auf Klärung durch den Nutzer warten (gewählt);
  (b) eigene Interpretation als CALC-Einträge ausformulieren (verworfen,
  da Zweck ungeklärt — Gefahr einer erfundenen Interpretation, siehe
  CLAUDE.md Abschnitt 19).
date_opened: "2026-09-01"
date_resolved:
resolution:
---

Eigener Fund (Claude) beim Cross-Check der R2-Excel-Datei
(`R2/COMMON/calculations/20260208_Berechnung_Rahmenecke_eingeklebte
Gewindestangen.xlsx`, Sheets "Rahmenecke GL24h SD/HD", "Rahmenecke GL75
SD", Stand 2026-09-01) gegen chat-3 — keiner dieser vier Blöcke wird in
SUMMARY.md, STATE.md, DECISIONS.md, KNOWLEDGE.md, TASKS.md oder
OPEN_QUESTIONS.md von chat-3 erwähnt. Rein rechnerisch sind alle vier
Blöcke in sich nachvollziehbar (Formeln/Normverweise vorhanden), nur ihr
Platz im Gesamtkonzept der R2-Verbindung ist offen.

**Teilweise Klärung von Punkt (2), 2026-09-01:** Bei der Dokumentation
der korrigierten `M_max`-Berechnung (R2-GL24h-CALC-012) hat sich
gezeigt, dass der Block "Tragfähigkeit Stütze auf Zug" (`H43-H52`) im
Excel als einer von drei `MIN()`-Kandidatenwerten für die
`M_max`-maßgebende Komponente verwendet wird (`H123=MIN(H40;H52;H109)`).
Seine Stelle im Rechenschema ist damit belegt.

**Weitere Prüfung der normativen Herleitung, 2026-09-01 (Claude,
CLAUDE_DRAFT, noch nicht vom Forschenden bestätigt):** Auf Nachfrage des
Nutzers wurde die tatsächliche Norm-Textstelle zu "Figure 11.38" per
Volltextsuche im FprEN-PDF verifiziert (nicht nur aus dem Kontext
geraten). Ergebnis, mit Widersprüchen:

- Der ursprüngliche Verdacht ("Blockscher-/Sprödbruchprüfung nach Fig.
  11.38") ist **so nicht korrekt**. Figure 11.38 gehört zu Klausel
  11.10.5.2 "Capacity of the timber member" (Zugtragfähigkeit des
  Holzquerschnitts um eingeklebte Stangen, Gl. 11.92:
  `F_t,0,Rd = k_mod·f_t,0,k/γ_M · A_ef`), **nicht** zu einem
  Blockscher-/Sprödbruchnachweis. `A_ef` ist dort ein Quadrat mit
  maximaler Seitenlänge `6d`, begrenzt durch Holzrand oder Mittellinie
  zum Nachbarstab — strukturell passend zu den Eingaben
  `a=88 mm`/`b=80 mm`/`A_ef=7.040 mm²` im Excel.
- Die Excel-Zellen D49-D52 zitieren jedoch explizit
  "FprEN EC5 - 2024, Gl. 11.14 (a)-(d)" als Normquelle — das ist im
  tatsächlichen Normtext (S. 170) die Johansen-Traglastformel für den
  Stiftverbindungsmittel-Versagensmodus (Ausziehen/Lochleibung,
  Klausel 11.2.3.2), inhaltlich unpassend zu einer
  "Zugtragfähigkeit je Stange". Diese Zellbeschriftung ist damit
  entweder ein Kopier-/Beschriftungsfehler (ähnlich dem bereits in
  R2-GL24h-CALC-011 gefundenen `k_mat`-Verwechslungsfehler) oder bezieht
  sich auf einen anderen, hier nicht erkennbaren Berechnungsschritt.
- Der tatsächliche Zellwert `H50` (`=Holzkennwerte!D17*H48*10^-3`)
  verwendet `Holzkennwerte!D17 = f_t,0,mean` — den **Mittelwert** der
  Zugfestigkeit (nach Eurocode 0 Anhang D aus dem 5%-Fraktilwert
  `f_t,0,k` zurückgerechnet), **nicht** den charakteristischen Wert
  `f_t,0,k` und ohne `k_mod`/`γ_M`. Die Zellbeschriftung nennt den Wert
  dennoch `F_t,0,Rk` (H50) bzw. nach Multiplikation mit 4
  `F_t,0,Rd` (H52) — Bezeichnungen, die einen charakteristischen bzw.
  Bemessungswert nach Gl. 11.92 suggerieren, obwohl rechnerisch ein
  Mittelwert ohne Sicherheitsbeiwerte verwendet wird.
- Eine mögliche, in sich konsistente Lesart: Da auch `H40`
  (Gewindestangen-Zugversuchsmittel) ein **Mittelwert** aus
  Versuchsdaten ist, könnte `H52` bewusst ebenfalls auf Mittelwertbasis
  berechnet sein, um einen Vergleich zwischen gleichartigen Größen
  (Mittelwert Holz-Zugtragfähigkeit vs. Mittelwert
  Gewindestangen-Zugversuch) im `MIN()` zu ermöglichen, statt eines
  formalen EC5-Bemessungsnachweises. Dies ist jedoch eine Interpretation
  (Claude) und nicht durch chat-3 oder eine Nutzerangabe belegt.

**Klärung durch den Nutzer, 2026-09-01:** Punkt (b) ist geklärt — alle
Tragfähigkeiten in dieser Tabelle (nicht nur `H52`) werden bewusst mit
Mittelwerten der Holzfestigkeiten gerechnet, nicht mit charakteristischen
oder Bemessungswerten. Die "Rk"/"Rd"-Beschriftungen sind damit reine
Beschriftungsabweichungen (nicht bereinigt, aber kein Rechenfehler) —
kein weiterer Klärungsbedarf. Zu Punkt (a) (Bezug der Zitate "Gl. 11.14"
in D49-D52 zur Stangen-/Holzzugtragfähigkeit) hat der Nutzer erklärt,
den Bezug selbst nicht zu kennen, und stuft dies nicht als eine zu
klärende Frage ein — wird daher nicht weiterverfolgt. Punkt (c) (Bezug
von `a=88 mm`/`b=80 mm` zur `6d`-/Stababstands-Begrenzung aus Fig. 11.38)
bleibt unbeantwortet, ist aber vom Nutzer nicht separat aufgegriffen
worden.

Der Block "Tragfähigkeit Stütze auf Zug" ist damit im Rahmen dieser
Frage ausreichend geklärt (Rolle im Rechenschema: MIN-Kandidat für
`M_max`, siehe R2-GL24h-CALC-012; Mittelwertbasis: bestätigt
beabsichtigt; genaue Normzuordnung der Zellbeschriftung: vom Nutzer
bewusst nicht weiterverfolgt). Die übergeordnete Frage (1), (3) und (4)
bleiben unverändert offen — die Frage bleibt daher insgesamt OPEN.
