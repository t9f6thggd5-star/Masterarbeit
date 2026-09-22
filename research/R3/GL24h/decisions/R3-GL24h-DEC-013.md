---
decision_id: R3-GL24h-DEC-013
scope:
  connection: R3
  material: GL24h
type: DECISION
question: >
  Müssen die aus der Auswertungsdatei
  `Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx` übernommenen
  Steifigkeitswerte K_ser (und K_e) analog zur bereits etablierten
  Fmax,SF = Fmax,ges/2-Konvention durch 2 geteilt werden, um die
  tatsächliche Steifigkeit je Scherfuge (Einzelverbindung) zu erhalten?
decision: >
  Ja. K_ser (und K_e) werden durch 2 geteilt. Alle mit R3-GL24h-DEC-012
  gepoolten RES-003-Werte (SC-11-B, SC-11-C, SC-44-C, SD-36, WD-36) sind
  dadurch um den Faktor 2 überschätzt und werden durch neue, korrigierte
  RES-004-Einträge ersetzt (RES-003 bleibt als historischer Eintrag mit
  `superseded_by` erhalten, CLAUDE.md-Nichtüberschreiben-Regel).
reason: >
  Nutzerhinweis (Chat, 2026-09-22): Der Prüfaufbau ist ein symmetrischer
  Doppelscher-Prüfkörper (Träger bzw. Stütze in der Mitte, je eine
  Holzlasche mit Schrauben links und rechts angeschlossen). Die vom
  Prüfstand gemessene Gesamtkraft teilt sich symmetrisch auf beide
  Scherfugen auf — jede Scherfuge (LINKS-Verbindung bzw.
  RECHTS-Verbindung) trägt real nur die halbe Gesamtkraft.

  Eigene Prüfung der Formelzellen in den Einzelblättern der
  Auswertungsdatei (u. a. `III-PO-S-SC-11-C-1`, `III-PO-S-SC-44-C-1`,
  stellvertretend für alle Serien geprüft, gleiche Blattvorlage) bestätigt:
  K_ser LINKS wird als `M21 = (0.4*M5)/M19` bzw. äquivalent
  `M22 = (P13-P12)/(M13-M12)` berechnet, wobei M5/P12/P13 direkt auf
  Spalte A ("Kraft [kN]", Kopfzeile "Maschine" — die *ungeteilte*
  Gesamtkraft des Prüfstands) zurückgehen. K_ser RECHTS verwendet exakt
  dieselbe, ungeteilte Kraftbasis (`S5 = '=M5'`, identischer F_est) mit
  der lokal an der rechten Seite gemessenen Verschiebung. Beide Seiten
  werden also mit der vollen Gesamtkraft im Zähler berechnet, nicht mit
  der halben.

  Im Blatt "Überblick" derselben Datei ist genau diese Halbierung für die
  Traglast bereits explizit umgesetzt: Spalte F ("Fmax,ges [kN]") = rohe
  Maschinenkraft (`=INDIRECT(...!M07)`), Spalte G ("Fmax,SF [kN]") =
  dieselbe Zelle geteilt durch 2 (`=INDIRECT(...!M07)/2`) — "SF" für
  "Scherfuge". Für die Steifigkeitsspalten (B "Kser LINKS", C "Kser
  RECHTS", D/E "Ke LINKS/RECHTS") existiert **keine** entsprechende
  `/2`-Spalte; sie verweisen unverändert auf die Rohwerte aus den
  Einzelblättern (`=...!M22` bzw. `=...!S22` für K_ser, `=...!M23`/
  `=...!S23` für K_e). Dieses Muster (undivided K_ser/K_e neben bereits
  halbiertem Fmax,SF) ist über mehrere geprüfte Prüfkörperblätter
  identisch (SC-11-C-1, SC-44-C-1, jeweils Beam- und Column-Serie "-S-"
  und "-B-").

  Da Zähler (Kraft) und Nenner (lokale Verschiebung je Seite) in der
  Steifigkeitsberechnung derselben Zwei-Scherfugen-Logik unterliegen wie
  bei Fmax, ist die konsistente Anwendung derselben /2-Korrektur auf
  K_ser (und K_e) geboten.
alternatives_considered: >
  Keine tragfähige Alternative gefunden. Denkbar wäre, dass die lokal
  gemessene Verschiebung selbst bereits eine um den Kraftanteil
  bereinigte Größe ist und keine weitere Korrektur nötig wäre — das
  betrifft aber nur eine hypothetische Eigenschaft des Nenners und ändert
  nichts an der hier eindeutig belegten Tatsache, dass der Zähler
  (Kraft) ungeteilt in beide Seiten eingeht, exakt wie bei Fmax vor der
  dortigen /2-Korrektur.
date: "2026-09-22"
superseded_by:
---

Auslöser: Nutzerfrage, ob die K_ser-Werte analog zu Fmax,SF =
Fmax,ges/2 ebenfalls halbiert werden müssen (Chat, 2026-09-22), im
Anschluss an R3-GL24h-DEC-012 (Poolung LINKS/RECHTS als zwei
unabhängige Verbindungen).

**Verhältnis zu DEC-012:** DEC-012 selbst bleibt inhaltlich korrekt —
LINKS und RECHTS sind tatsächlich zwei unabhängige Verbindungen, die
n=6-Poolung ist methodisch richtig. Der Fehler lag nicht in der
Poolungslogik, sondern in den zugrunde liegenden K_ser-*Werten* selbst
(Faktor 2 zu hoch, weil mit der ungeteilten Gesamtkraft statt der Kraft
je Scherfuge berechnet). Halbierung jedes Einzelwerts vor der Poolung
ist rechnerisch identisch zur Halbierung des bereits gepoolten
Mittelwerts (lineare Operation, Mittelwert und Standardabweichung
skalieren gleich, der Variationskoeffizient bleibt unverändert) — die
betroffenen RES-003-Werte werden daher einfach durch 2 geteilt, nicht
neu gepoolt.

**Betroffen:** Alle fünf R3/GL24h-Push-Out-Serien mit RES-003-Einträgen
(SC-11-B, SC-11-C, SC-44-C, SD-36, WD-36) — siehe jeweils neue
RES-004-Einträge. Die Gruppeneffizienz-Beobachtung (SC-44-C ≈ 76,5 % von
16× SC-11-C) bleibt durch die Halbierung unverändert, da beide Seiten
des Vergleichs mit demselben Faktor skalieren.

**Nicht behoben (außerhalb des Geltungsbereichs dieser Entscheidung):**
K_e (Wiederbelastungssteifigkeit) unterliegt derselben Problematik
(gleiche Formelstruktur, ungeteilte Kraft), wurde aber bislang nicht in
eigenen RES-003/RES-004-Einträgen gepoolt — falls K_e künftig benötigt
wird, gilt dieselbe /2-Korrektur; die K_e-Rohwerte in den bestehenden
RES-002-Tabellen sind entsprechend ebenfalls als "ungeteilt" zu lesen.

**Geltungsbereich:** Wie DEC-012 vorerst nur R3/GL24h, nicht rückwirkend
auf R1/R2 angewendet (dort andere Prüfkörpergeometrie, nicht geprüft).
