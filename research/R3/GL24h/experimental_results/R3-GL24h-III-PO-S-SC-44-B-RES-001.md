---
result_id: R3-GL24h-III-PO-S-SC-44-B-RES-001
scope:
  connection: R3
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: >
  Keine eigenen RAW_MEASUREMENT-Einträge angelegt; Werte direkt aus der
  externen Auswertungsdatei des Nutzers: `common/general/Auswertung_Steifigkeiten_Push-Out-Versuche_FINAL.xlsx`, Blatt "Überblick" übernommen (Zeilen "III-PO-S-SC-44-B-1/2/3", Spalte "Fmax,SF [kN]").
n: 1
method: >
  Push-Out-Versuch, Prüfkörperserie "III-PO-S-SC-44-B". Höchstlast pro Scherfuge
  (Fmax,SF = Fmax,ges / 2 — Prüfkörper mit zwei Scherfugen, Wert direkt
  aus der Auswertungsdatei übernommen, nicht selbst nachgerechnet). Schraubenverbindung, Lasche am Riegel (Beam), 4×4. **Nur Prüfkörper 1 hat einen Wert** — Prüfkörper 2 und 3 sind in der Auswertungsdatei vollständig leer ('-' in allen Spalten, Stand 'entfällt') und wurden offenbar nicht ausgewertet oder nicht durchgeführt; die Ursache ist ungeklärt.
result:
  quantity: Höchstlast F_max pro Scherfuge (Mittelwert aus 1 Prüfkörper)
  value: 47.300
  unit: kN
  original_value:
  original_unit:
certainty: MEASURED
---

Einzelwerte (Fmax,SF, Blatt "Überblick"):

| Prüfkörper | Fmax,SF [kN] |
|---|---|
| III-PO-S-SC-44-B-1 | 47.300 |
| **Mittelwert** | **47.300** |

**n=1: dieses Ergebnis ist ein Einzelbefund** und wird nicht als typisches oder charakteristisches Verhalten der Serie dargestellt (CLAUDE.md Abschnitt 15). Auch die Steifigkeit von PK1 ist 'nv' (nicht verwertbar) — für diese Serie liegt daher kein Steifigkeits-Eintrag vor. Warum PK2/PK3 fehlen und ob PK1 selbst belastbar ist, ist ungeklärt und wird hier bewusst nicht geraten (CLAUDE.md Abschnitt 4) — bitte beim Nutzer klären.

**Update (2026-09-25, Nutzeraussage + Kurvenprüfung):** PK2 und PK3 sind
laut Nutzer durch Querdruck im Mittelholz versagt; Messdaten gibt es
dazu keine (Blätter leer). Für PK1 liegt die vollständige Kraft-Weg-
Kurve vor (Blatt "III-PO-S-SC-44-B-1", F_max = 93,969 kN, Maschine
94,6 kN); PK1 hat 0,4·F_est = 116 kN nie erreicht, deshalb ergibt die
Auswertung nach EN 26891 `#DIV/0!` ("nv"). Die Ursache des Versagens
wird jetzt als Querdruck am Kopf des Mittelholzes gedeutet, nicht mehr
als Querzug (R3-GL24h-INT-001, `CLAUDE_DRAFT`; Querdruckwiderstand
R3-GL24h-CALC-009 = 84,88 kN). Der hier angegebene Wert 47,3 kN je
Scherfuge ist damit keine Tragfähigkeit der Schraubengruppe.
