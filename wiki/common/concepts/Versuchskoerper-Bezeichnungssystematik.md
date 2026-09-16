---
scope:
  connection: COMMON
  material: COMMON
source: >
  Nutzer (Diagramm/Screenshot im Chat, 2026-09-16; Ergänzung durch
  Nutzer im Chat, 2026-09-16) — eigene Projektkonvention zur Benennung
  von Prüfkörpern/-serien auf Verbindungsmittel-Ebene, keine externe
  Quelle (kein Eintrag in bibliography/sources.yaml nötig; analog zu
  Methodik-Entscheidungen, vgl. research/common/decisions/).
last_updated: "2026-09-16"
---

# Bezeichnungssystematik der Versuchskörper (Komponentenversuche)

Reine Definitions-/Navigationshilfe zum Lesen von Versuchskörper- und
Versuchsreihen-Bezeichnungen (z. B. `III-PO-S-SC-44-B-1`,
`II-T-S-BR-22`), kein eigener Claim und keine eigene fachliche Aussage —
trägt daher bewusst keine eigene ID (analog zu `wiki/common/
normative_basis/FprEN-1995-1-1-2024_Normstellen-Index.md`). Gilt für
Versuchskörper auf **Verbindungsmittel-Ebene** (`experiment_level:
COMPONENT`), nicht für Gesamtverbindungsversuche.

## Aufbau des Codes

Beispiel: `III-PO-S-SC-44-B-1`

| # | Segment | Werte | Bedeutung |
|---|---|---|---|
| 1 | Anschlusstyp | `II` = Eingeklebte Gewindestangen (= **R2**, Rahmenecke 2); `III` = Seitliche Holzlaschen (= **R3**, Rahmenecke 3) | Grundprinzip der untersuchten Verbindung |
| 2 | Versuchsart | `PO` = Push-Out; `T` = Tension / Zugversuch | Art des Komponentenversuchs |
| 3 | Holzart | `S` = Fichte / spruce (GL24h); `B` = Buche / beech (GL75) | Werkstoff des Prüfkörpers |
| 4 | Verbindungsmittelart | `SD` = Stahlstabdübel (steel dowel); `WD` = Holzdübel (wood dowel); `SC` = Schraube (screw); `BR` = eingeklebte Gewindestange (Bonded-in Rod) | Art des Verbindungsmittels |
| 5 | Verbindungsmittelanzahl | $n_\perp \times n_\parallel$, z. B. `11` = 1×1; `22` = 2×2; `44` = 4×4 | Anzahl Verbindungsmittel quer × längs |
| 6 | Lasche an | `B` = Beam (Riegel); `C` = Column (Stütze) — **nur bei Schrauben** | Bauteil, an dem die Lasche befestigt ist |
| 7 | Nr. des Versuchskörpers | laufende Nummer | Individueller Prüfkörper innerhalb der Serie |

Zerlegung des Beispiels `III-PO-S-SC-44-B-1`: Anschlusstyp III (seitliche
Holzlaschen), Push-Out-Versuch, Fichte/GL24h, Schrauben, 4×4-Anordnung,
Lasche am Riegel befestigt, Prüfkörper Nr. 1.

Zerlegung `II-T-S-BR-22`: Anschlusstyp II (eingeklebte Gewindestangen,
R2), Zugversuch, Fichte/GL24h, eingeklebte Gewindestangen (Bonded-in
Rods), 2×2-Anordnung. Analog `II-T-B-BR-22`: dieselbe Versuchsreihe,
jedoch Buche/GL75 (`B` an Position 3).

## Bekannte Versuchsreihen-Codes — eingeklebte Gewindestangen, Zugversuch (R2)

Vom Nutzer am 2026-09-16 im Chat explizit benannt:

| Code | Bedeutung | Vorhandener Ergebnis-Eintrag |
|---|---|---|
| `II-T-S-BR-22` | R2, GL24h (Fichte), 2×2 eingeklebte Gewindestangen, Zugversuch | `research/R2/GL24h/experimental_results/R2-GL24h-II-T-S-BR-22-RES-001.md` |
| `II-T-B-BR-22` | R2, GL75 (Buche), 2×2 eingeklebte Gewindestangen, Zugversuch | `research/R2/GL75/experimental_results/R2-GL75-II-T-B-BR-22-RES-001.md` |
| `II-T-S-BR-11` | R2, GL24h (Fichte), 1×1 eingeklebte Gewindestange, Zugversuch | `research/R2/GL24h/experimental_results/R2-GL24h-II-T-S-BR-11-RES-001.md` (Mittelwert 72,337 kN, n=3) |
| `II-T-B-BR-11` | R2, GL75 (Buche), 1×1 eingeklebte Gewindestange, Zugversuch | `research/R2/GL75/experimental_results/R2-GL75-II-T-B-BR-11-RES-001.md` (Mittelwert 73,367 kN, n=3) |

Messwerte selbst stehen nur in den verlinkten `EXPERIMENTAL_RESULT`-
Einträgen unter `research/` — diese Konzept-Datei hält bewusst nur die
Code-Definition, keine Zahlenwerte (CLAUDE.md Abschnitt 8: Messwerte und
Definitionen werden getrennt gehalten).

## Abgleich mit bereits verwendeten IDs im Projekt

Diese Systematik wird bereits in `research/` verwendet, z. B. in den
`result_id`-Werten der R2-Versuchsreihen: `R2-GL24h-II-PO-S-SD-34-RES-001`,
`R2-GL24h-II-PO-S-WD-34-RES-001`, `R2-GL75-II-PO-B-SD-23-RES-001`,
`R2-GL24h-II-T-S-BR-22-RES-001`, `R2-GL75-II-T-B-BR-22-RES-001` (siehe
`research/R2/GL24h/experimental_results/` bzw. `research/R2/GL75/
experimental_results/`). Bestätigt: **`II` (Eingeklebte Gewindestangen)
entspricht R2** — vom Nutzer am 2026-09-16 explizit bestätigt und durch
die bestehenden R2-Ergebnis-IDs gedeckt.

**`III` (Seitliche Holzlaschen) entspricht R3** — vom Nutzer am
2026-09-16 im Chat bestätigt. Zusätzlich gestützt durch Ausschluss:
laut `research/R1/GL24h/current_state.md` ist R1 = Schlitzblech +
Stabdübel-Anschluss (nicht seitliche Holzlaschen); für R3 selbst liegen
in `research/R3/GL24h/current_state.md` bzw. `research/R3/GL75/
current_state.md` noch keine inhaltlichen Einträge vor, die den
Anschlusstyp explizit benennen — die Zuordnung beruht daher auf der
Nutzeraussage, nicht auf einem bereits dokumentierten `research/`-Eintrag
für R3.

`T` (Versuchsart) = Tension/Zugversuch und `BR` (Verbindungsmittelart) =
eingeklebte Gewindestange (Bonded-in Rod) sind vom Nutzer am 2026-09-16
im Chat ebenfalls explizit bestätigt (siehe Tabelle oben).
