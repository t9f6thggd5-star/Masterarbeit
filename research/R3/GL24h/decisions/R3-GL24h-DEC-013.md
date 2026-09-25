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
  Steifigkeit je Scherfuge (eine Laschenseite) zu erhalten?
decision: >
  Ja. K_ser (und K_e) werden für das Federmodell durch 2 geteilt. Die
  Werte der Auswertungsdatei sind dabei nicht falsch: Sie geben die
  Steifigkeit des doppelseitigen Prüfkörpers an (Gesamtkraft /
  Verschiebung einer Seite). Das Federmodell braucht die Steifigkeit einer
  Laschenseite; die Halbierung ist eine Umrechnung der Bezugsgröße, keine
  Fehlerkorrektur. Die mit R3-GL24h-DEC-012 gepoolten RES-003-Werte
  (SC-11-B, SC-11-C, SC-44-C, SD-36, WD-36) beziehen sich auf den
  Prüfkörper und werden für das Federmodell durch die RES-004-Einträge je
  Scherfuge ersetzt (RES-003 bleibt mit `superseded_by` erhalten).
reason: >
  Der Prüfkörper ist ein symmetrischer Doppelscher-Prüfkörper (Träger
  bzw. Stütze in der Mitte, je eine Holzlasche mit Schrauben links und
  rechts; Nutzerhinweis 2026-09-22). Beide Seiten wirken parallel, jede
  trägt F_ges/2 und verschiebt sich dabei um v. Die Auswertungsdatei
  rechnet K = F_ges / v (Einzelblätter: `M22 = (P13-P12)/(M13-M12)`,
  Kraft aus Spalte A "Maschine", ungeteilt; RECHTS analog mit derselben
  Kraftbasis). Daraus folgt K_Datei = F_ges/v = 2 · (F_ges/2)/v =
  2 · K_eine Seite. Im Blatt "Überblick" ist dieselbe Umrechnung für die
  Traglast bereits als eigene Spalte umgesetzt (G "Fmax,SF" =
  F_ges/2); für die Steifigkeitsspalten (B/C K_ser, D/E K_e) gibt es
  keine solche Spalte. Für das Federmodell wird daher analog
  K_SF = K_Datei/2 angesetzt.
alternatives_considered: >
  K_Datei unverändert verwenden — nur richtig, wenn im Modell beide
  Laschenseiten zusammen als eine Feder abgebildet würden. Im Zugpfad von
  R3 wird die Schraubengruppe aber je Laschenseite angesetzt (CALC-007/008),
  daher verworfen.
date: "2026-09-22"
superseded_by:
---

Auslöser: Nutzerfrage, ob die K_ser-Werte analog zu Fmax,SF =
Fmax,ges/2 ebenfalls halbiert werden müssen (Chat, 2026-09-22), im
Anschluss an R3-GL24h-DEC-012 (Poolung LINKS/RECHTS als zwei
unabhängige Verbindungen).

**Umformulierung (2026-09-25, auf Wunsch des Nutzers):** Die Fassung vom
2026-09-22 bezeichnete die Werte der Auswertungsdatei als "um Faktor 2 zu
hoch" bzw. "überschätzt". Das war missverständlich: Die Datei gibt
korrekt die Steifigkeit des doppelseitigen Prüfkörpers an; die
Halbierung ist nur die Umrechnung auf eine Laschenseite. Inhalt der
Entscheidung und alle Zahlenwerte (RES-004) bleiben unverändert.

**Verhältnis zu DEC-012:** DEC-012 bleibt inhaltlich korrekt — LINKS und
RECHTS sind zwei unabhängige Verbindungen, die n=6-Poolung ist richtig.
Halbierung jedes Einzelwerts vor der Poolung ist rechnerisch identisch zur
Halbierung des gepoolten Mittelwerts (Mittelwert und Standardabweichung
skalieren gleich, der Variationskoeffizient bleibt unverändert).

**Betroffen:** Alle fünf R3/GL24h-Push-Out-Serien mit RES-003-Einträgen
(SC-11-B, SC-11-C, SC-44-C, SD-36, WD-36), siehe jeweils RES-004. Die
Gruppeneffizienz-Beobachtung (SC-44-C ≈ 76,5 % von 16× SC-11-C) bleibt
unverändert, da beide Seiten des Vergleichs gleich skalieren.

**K_e:** Für die Wiederbelastungssteifigkeit gilt dieselbe Umrechnung; die
K_e-Werte in den RES-002-Tabellen beziehen sich ebenfalls auf den
doppelseitigen Prüfkörper.

**Geltungsbereich:** Wie DEC-012 vorerst nur R3/GL24h, nicht auf R1/R2
übertragen (dort andere Prüfkörpergeometrie).
