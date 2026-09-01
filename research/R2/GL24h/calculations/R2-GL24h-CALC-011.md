---
calculation_id: R2-GL24h-CALC-011
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024, ETA-11-0190-2026
  literature:
  experimental_data:
  assumptions:
method: >
  Korrektur von R2-GL24h-CALC-006: für den Holzanteil-Term in Gl. 8.12
  wird jetzt der normativ vorgesehene, verstärkungsspezifische Wert
  `k_mat=1,75` (FprEN 1995-1-1:2024, 8.1.6.2(6)) verwendet statt des
  zuvor fälschlich aus dem Ausziehwiderstands-Kontext (Tab. 11.2, Gl.
  11.3(4)) übernommenen `k_mat=1,0`. Bedingung für `k_mat=1,75` geprüft
  und erfüllt: diskrete Auflagerung mit Einzellast und `l_s≥2h`
  (`l_s→∞`, keine weitere Einzellast in der Nähe vorhanden — Nutzerangabe
  2026-09-01), GL24h als Softwood-GL (Tab. 5.1), `l90,c=240mm≤400mm`.
  Übrige Eingangswerte unverändert gegenüber CALC-006.
equations: FprEN 1995-1-1:2024, Gl. 8.12; k_mat-Bedingung nach 8.1.6.2(6); Gl. 8.14 (l_1,ef, Zwischenauflager); Gl. 8.15 (l_2,ef).
result:
  quantity: Verstärkte Querdrucktragfähigkeit F_c,90, GL24h (korrigiert, k_mat=1,75)
  value: 384.124
  unit: kN
  original_value: 384124.211
  original_unit: N
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen H85-H109 (per
  openpyxl mit data_only=True und als Formeltext ausgelesen, Stand der
  abgelegten Datei am 2026-09-01. Die Datei wurde vom Nutzer während der
  Korrektur von "20260208_Berechnung_..." auf
  "20260109_Berechnung_..." umbenannt — derselbe Kalkulationsstand,
  nur neuer Dateiname.)
certainty: CALCULATED
superseded_by:
---

Korrektur zu R2-GL24h-CALC-006. Ursache des ursprünglichen Fehlers: das
Symbol `k_mat` wird in FprEN 1995-1-1:2024 an mehreren, inhaltlich
unabhängigen Stellen mit jeweils eigener Definition verwendet — u. a. in
8.1.6.1/8.1.6.2 (Querdruckfestigkeit, hier einschlägig) und separat in
der Ausziehwiderstandsformel (`f_w,k = k_screw·k_w·k_mat·d^-0,33·(…)`,
Tab. 11.2 Umfeld, Gl. 11.3). Der in CALC-006 verwendete Wert `k_mat=1,0`
stammte aus Letzterem und wurde für den Holzanteil-Term in Gl. 8.12
fälschlich wiederverwendet.

**Verifikations-Notiz (Zwischenstand vor Fertigstellung dieses
Eintrags):** Beim ersten Korrekturversuch des Nutzers wurde eine neue
Zelle `H86` ("k_mat Holz", `=1,75`) ergänzt, die Formel in `H104`
("Holzanteil") verwies zunächst aber weiterhin auf die alte Zelle `H85`
("k_mat Schraube", `=1`) — die Endzelle `H109` hatte dagegen bereits
eine eigene, korrekt auf `H86` verweisende Formel. Dadurch waren `H104`
(`159,151 kN`) und `H106` (`264,761 kN`) zwischenzeitlich inkonsistent
zu `H109` (`384,124 kN`). Vom Nutzer inzwischen behoben (`H104` verweist
jetzt ebenfalls auf `H86`); alle drei Zellen sind aktuell konsistent
(siehe Zellenkette unten).

**Aktuelle Zellenkette** (Sheet "Rahmenecke GL24h SD"): `k_mat
Holz=1,75` (H86, FprEN 8.1.6.2(6)), `b_90,c=160 mm` (H64), `l_1,ef=300
mm` (H91, Gl. 8.14 — Kontaktfläche bewusst als Zwischenauflager
behandelt, siehe R2-GL24h-OPQ-003, RESOLVED), Holzkennwerte!D20
(`f_c,90,mean≈3,3156 N/mm²`) →
Holzanteil `H104 = 1,75×160×300×3,3156/1.000 = 278,515 kN`.
Schraubenanteil `H105 = 9×min(F_w,k;F_c) = 9×11,734 = 105,610 kN`
(unverändert, kein `k_mat`-Bezug, siehe R2-GL24h-CALC-007). 1.
Versagensmodus `H106 = 278,515+105,610 = 384,124 kN`. 2. Versagensmodus
(Ebene Schraubenspitze) `H107 = 413,793 kN` (unverändert, ohne
`k_mat`-Bezug). Maßgebend ist der kleinere Wert: `F_c,90 = 384,124 kN`
(H109, Gl. 8.12).

**Nutzerangabe:** Dieser Wert stimmt laut Nutzer mit einer unabhängig
nach ETA-11/0190 durchgeführten Vergleichsrechnung überein
(`≈384,12 kN`). Diese ETA-Vergleichsrechnung selbst liegt bisher als
kein eigener `research/`-Eintrag vor (`certainty: SOURCE_CLAIM` für die
Übereinstimmung — von Claude nicht selbst nachgerechnet); falls
gewünscht, kann sie als eigener CALC-Eintrag dokumentiert werden.

**Konsequenzen für nachgelagerte Einträge (noch offen, nicht Teil
dieser Korrektur):**
- `F_c,90=384,124 kN` liegt jetzt **oberhalb** des gemessenen
  Gewindestangen-Zugversuchsmittels (`285,77 kN`,
  R2-GL24h-II-T-S-BR-22-RES-001) — die "maßgebende Komponente" in
  R2-GL24h-CALC-008 (bisher: verstärkte Querdruckresistenz,
  `248,846 kN`) müsste damit auf den Gewindestangen-Zugversuch
  wechseln, und `M_max` (bisher `139,354 kNm`) wäre neu zu berechnen.
- Verhältnis zu R2-COMMON-OPQ-002 (FprEN vs. ETA/Würth als primärer
  Vorbemessungswert): der dort genannte alte ETA/Würth-Vergleichswert
  (`≈356,3 kN`, mit `k_c,90=1,75` statt `k_mat=1,75`) liegt näher am
  jetzt korrigierten FprEN-Wert als zuvor, ist aber weiterhin ein
  anderer Rechenweg — nicht ohne Weiteres gleichzusetzen.
