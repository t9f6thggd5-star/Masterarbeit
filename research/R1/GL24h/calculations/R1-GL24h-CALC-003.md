---
calculation_id: R1-GL24h-CALC-003
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Hochrechnung der Scherfugen-Tragfähigkeit (R1-GL24h-CALC-001/002) auf
  die gesamte Dübelgruppe (n_90=4 Reihen, n_ef≈5.499 wirksame Dübel je
  Reihe, m=2 Scherfugen) für beide Fließmoment-Basen. Die konkrete
  Kombinationsformel ist in der Excel-Datei nicht als sichtbare Formel,
  sondern nur als Ergebniswert hinterlegt — siehe Hinweis unten und
  R1-GL24h-DEC-004/OPQ-006.
equations: >
  Rekonstruiert aus den Zellwerten: F_D,k,ges ≈ F_D,k(governierender Modus)
  × n_ef × n_90 × m
result:
  quantity: Gesamttragfähigkeit der Dübelgruppe (experimentelle M_y,k-Basis) — angesetzt als F_est
  value: 627.16
  unit: kN
  original_value: 627.1601647077889
  original_unit: kN
source_file: >
  R1/COMMON/calculations/20260208_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Zellen C27, C57, C66 (per openpyxl mit
  data_only=True ausgelesen, Stand der abgelegten Datei am 2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-2 (F=627.16 kN wird dort in KNOWLEDGE.md §8 als
Lastniveau für die Verformungsabschätzung verwendet) und unabhängig gegen
die reale Excel-Datei verifiziert.

**Zwei parallel geführte Basen:**
- Normative M_y,k-Basis: F_D,k,ges ≈ 494.767 kN (Zelle C57, "min.
  Tragfähigkeit F_D,k,ges").
- Experimentelle M_y,k-Basis: F_D,k,ges ≈ 627.160 kN (Zelle C66, "min.
  Tragfähigkeit F_D,k,ges").

Die experimentelle Basis (627.16 kN) ist identisch mit der in Zelle C27
("Höchstlast F_est", Vermerk "Es liegen keine Versuchsergebnisse vor")
angesetzten Last — d. h. die in der Verformungsabschätzung
(R1-GL24h-CALC-005) verwendete Last F ist keine unabhängig gemessene
Höchstlast, sondern die rechnerisch auf Basis des experimentellen
Stabdübel-Fließmoments hochgerechnete Gruppentragfähigkeit.

**Rekonstruktion der Hochrechnung (nicht als Excel-Formel sichtbar, nur
als Zahlenwert):** F_D,k(Modus f, C55=11.247 kN) × n_ef (C45=5.4989) ×
n_90 (C22=4) × m (C6=2) ≈ 494.77 kN — stimmt mit C57 überein. Dieselbe
Rechnung mit dem Modus-d-Wert aus R1-GL24h-CALC-002 (14.257 kN) ergibt
analog ≈ 627.9 kN, nahe an C66=627.16 kN (kleine Abweichung vermutlich
durch Rundung/leicht abweichende Zwischenwerte in der eigentlichen
Excel-Formel). Da die tatsächliche Formel nicht einsehbar ist, wird diese
Rekonstruktion nicht als endgültige Bestätigung der Faktor-2-Handhabung
gewertet — siehe R1-GL24h-OPQ-006.
