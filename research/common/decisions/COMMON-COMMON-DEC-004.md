---
decision_id: COMMON-COMMON-DEC-004
scope:
  connection: COMMON
  material: COMMON
type: DECISION
question: >
  Ist GL75 im Sinne der FprEN-1995-1-1:2024-Klassifikation als
  konventionelles Brettschichtholz (GL/SWB) oder als LVL/GLVL
  (Furnierschichtholz) zu behandeln — mit Konsequenz für materialabhängige
  Beiwerte (u. a. n_ef-Abstandsregeln, k_mat/k_4-Tabellen)?
decision: >
  GL75 wird projektweit als BauBuche (Pollmeier-Furnierschichtholz,
  hardwood GLVL) behandelt, nicht als konventionelles
  Brettschichtholz/SWB. Materialabhängige FprEN-Beiwerte sind für GL75
  konsequent aus der LVL/GLVL-Spalte/-Tabelle zu entnehmen, nicht aus der
  SWB-Spalte — auch dort, wo einzelne Excel-Berechnungsblätter (noch)
  SWB-Beiwerte für GL75 verwenden (siehe Konsequenz).
reason: >
  Mehrere unabhängige Belege bestätigen dieselbe Klassifikation: (1) Die
  Holzkennwerte-Tabelle (R2-Excel, Sheet "Holzkennwerte", Zelle J8/K8)
  weist für die Mittelwertbildung von GL75 explizit den
  Variationskoeffizienten "V_x=0.05 (für BauBuche)" aus, gegenüber
  "V_x=0.15 (für BSH)" für GL24h/GL28h (Zelle J7/K7) — ein anderer
  statistischer Umrechnungspfad, der nur für ein tatsächlich anderes
  Produkt Sinn ergibt. (2) Im selben Workbook zitiert der
  Stabdübel-Johansen-Nachweis für GL75 (Sheet "Rahmenecke GL75 SD",
  Zelle D42) explizit "FprEN EC5 - 2024, Tab. 11.6 (31) - hardwood
  GLVL-P" für den Beiwert k_4 — während die GL24h-Parallelrechnung eine
  softwood-/GL-Tabelle verwendet. (3) Es liegt bereits eine eigene ETA für
  das Produkt vor (`ETA-14-0354-2026`, "Träger BauBuche GL75", Hersteller
  Pollmeier Furnierwerkstoffe GmbH), was gegen ein generisches GL-Produkt
  spricht. (4) Unabhängig davon wurde in R1 (chat-2) bereits entschieden,
  softwood-typische n_ef-Abstandsregeln nicht auf GL75 zu übertragen,
  siehe R1-GL24h-DEC-005 — diese Einzelentscheidung wird durch die hier
  dokumentierte Klassifikation nachträglich bestätigt und generalisiert.
alternatives_considered: >
  GL75 pauschal als GL/SWB behandeln (so ursprünglich in chat-3/R2
  angenommen, siehe "R2 OPEN_QUESTIONS.md Punkt 8": "chat treated GL75 as
  GL/SWB ... exact product specification should be confirmed"). Verworfen,
  da durch die drei oben genannten Belege eindeutig widerlegt.
date: "2026-09-01"
---

Eigene Synthese (Claude), nicht aus chat-1/chat-2/chat-3 direkt
übernommen — dort blieb die GL75-Klassifikation jeweils als offene Frage
stehen (chat-3: OPEN_QUESTIONS.md Punkt 8 "Exact GL75 product
classification"; chat-2/R1: nur indirekt über R1-GL24h-DEC-005 behandelt).
Diese Entscheidung fasst die Beleglage projektweit zusammen und wird
unter COMMON/COMMON geführt, da sie R1, R2 und R3 gleichermaßen betrifft,
sobald dort GL75-Berechnungen materialabhängige FprEN-Tabellen
heranziehen.

**Wichtige offene Konsequenz für R2:** Der Querdruck-Festigkeitsnachweis
für GL75 im R2-Excel (Sheet "Rahmenecke GL75 SD", Zellen H67/H68 —
`k_c,90=1.2583`, `k_mat=1.4`) übernimmt exakt dieselben Beiwerte wie die
GL24h-Rechnung auf demselben Blatt, ohne erkennbare
LVL/GLVL-spezifische Herleitung nach Tab. 8.1. Ob diese Wiederverwendung
sachlich richtig ist oder ob für GL75/BauBuche andere `k_mat`/`k_c,90`-Werte
anzusetzen wären, ist damit noch nicht geklärt — siehe R2-GL75-OPQ-003.
Diese Entscheidung stellt nur die Materialklassifikation fest, nicht die
Korrektheit der bestehenden Excel-Formel für den Querdrucknachweis.

Löst chat-3 OPEN_QUESTIONS.md Punkt 8 auf (siehe R2-COMMON-OPQ-009,
status: RESOLVED, verweist hierher).
