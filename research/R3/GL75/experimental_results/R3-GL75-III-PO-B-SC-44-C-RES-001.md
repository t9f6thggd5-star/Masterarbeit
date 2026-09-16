---
result_id: R3-GL75-III-PO-B-SC-44-C-RES-001
scope:
  connection: R3
  material: GL75
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte vom Nutzer direkt
  im Gespräch mitgeteilt (Screenshot einer Tabelle, 2026-09-16), Quelle
  laut Nutzer dieselbe externe Auswertungsdatei:
  `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`,
  Blatt "Überblick" (Zeilen "III-PO-B-SC-44-C-1/2/3"). Diese Prüfkörper
  waren zum Zeitpunkt der ersten Durchsicht der Datei (2026-09-16, siehe
  R3-GL75-OPQ-001) noch als "offen" markiert; die Werte wurden vom Nutzer
  nachgereicht.
n: 3
method: >
  Push-Out-Versuch, Prüfkörperserie "III-PO-B-SC-44-C". Schraubenverbindung,
  Lasche an der Stütze (Column), 4×4. Ursprünglich (2026-09-16) nur als
  Fmax,ges (Gesamtlast) mitgeteilt; der Nutzer hat am selben Tag die
  entsprechenden Fmax,SF-Werte (Höchstlast pro Scherfuge) nachgereicht
  und explizit bestätigt, dass es sich um "die Werte geteilt durch 2"
  handelt. Rechnerische Kontrolle: Fmax,ges/2 stimmt für alle drei
  Prüfkörper mit den nachgereichten Fmax,SF-Werten überein (519.04/2=
  259.52, 550.00/2=275.00, 588.23/2≈294.12). Primärer Ergebniswert dieses
  Eintrags ist jetzt Fmax,SF, konsistent mit der Konvention der übrigen
  44er-Push-Out-Einträge dieser Wiki (z. B.
  R3-GL24h-III-PO-S-SC-44-C-RES-001) und damit direkt vergleichbar.
result:
  quantity: Höchstlast F_max pro Scherfuge, Fmax,SF (Mittelwert aus 3 Prüfkörpern)
  value: 276.213
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (vom Nutzer mitgeteilt, 2026-09-16 in zwei Schritten:
zunächst Fmax,ges, dann Fmax,SF):

| Prüfkörper | Fmax,ges [kN] | Fmax,SF [kN] |
|---|---|---|
| III-PO-B-SC-44-C-1 | 519.04 | 259.52 |
| III-PO-B-SC-44-C-2 | 550.00 | 275.00 |
| III-PO-B-SC-44-C-3 | 588.23 | 294.12 |
| **Mittelwert** | **552.423** | **276.213** |

Der Nutzer hat zusätzlich eine in der Auswertungsdatei verwendete
Formel für einen übergeordneten "Mittelwert" genannt (bezogen auf
Fmax,SF): `MIN(Mittelwert(C1:C3); Mittelwert(B1:B3))` — also das Minimum
der Gruppenmittelwerte von -44-C und -44-B (nicht der Mittelwert aller
6 Prüfkörper zusammen). Auf ausdrücklichen Nutzerwunsch (2026-09-16) wird
dieser kombinierte Wert hier **nicht** als eigener Eintrag geführt;
Lasche-an-Beam und Lasche-an-Column bleiben als separate Prüfkörpergruppen
dokumentiert (Scope Isolation, CLAUDE.md Abschnitt 4), siehe
R3-GL75-III-PO-B-SC-44-B-RES-001. Nicht weiter interpretiert.
