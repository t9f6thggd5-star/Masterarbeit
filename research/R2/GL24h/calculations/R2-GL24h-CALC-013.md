---
calculation_id: R2-GL24h-CALC-013
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Unverstärkte FprEN-Querdruckfestigkeitsverifikation unter der
  Ankerplatte, auf dem separaten Excel-Blatt "Rahmenecke GL24h HD"
  (rechnerisch identisch zum Verfahren auf Blatt "Rahmenecke GL24h SD",
  siehe R2-GL24h-CALC-010) — beidseitige Lastausbreitung `l_ef =
  b_Stahlplatte + 2·Δl` (Gl. 8.5/8.7/8.9).
equations: FprEN 1995-1-1:2024, Gl. 8.5 (σ_c,90); Gl. 8.7 (k_c,90); Gl. 8.9 (A_ef); Tab. 8.1 (k_mat).
result:
  quantity: Unverstärkte Querdrucktragfähigkeit F_v,R, GL24h (Blatt "Rahmenecke GL24h HD")
  value: 262.376
  unit: kN
  original_value:
  original_unit:
source_file: >
  R2/COMMON/calculations/20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h HD", Zellen I55-I71 (per
  openpyxl mit data_only=True ausgelesen, Stand der abgelegten Datei am
  2026-09-01, Datei-mtime 1788273961000)
certainty: CALCULATED
superseded_by:
---

Eigenständig aus der R2-Excel-Datei erschlossen. Für dieses Blatt
existierte bisher kein eigener CALC-Eintrag (kein "superseded"-Vorgänger)
— der Nutzer hat die bereits auf Blatt "Rahmenecke GL24h SD" korrigierte
Lastausbreitung (siehe R2-GL24h-CALC-010) mitgeteilt auch hier auf
zweiseitig umgestellt zu haben ("bei GL24h HD und GL75 SD habe ich die
Lastausbreitung ebenfalls korrigiert").

**Kette:** Struktur identisch zu R2-GL24h-CALC-010, jedoch auf Blatt
"Rahmenecke GL24h HD" mit Spalte `I` statt `H` und Bezug auf
`Holzkennwerte!E20` statt `Holzkennwerte!D20` (beide Zellen enthalten
denselben `f_c,90,mean`-Wert für GL24h — unterschiedliche Zellreferenz
vermutlich durch die abweichende Blattstruktur bedingt, nicht durch
einen unterschiedlichen Eingangswert). `F_v,R = 262,376 kN` (I71).

**Cross-Check:** Der Wert ist identisch zum korrigierten Ergebnis von
R2-GL24h-CALC-010 (262,376 kN, Blatt "Rahmenecke GL24h SD") — plausibel,
da beide Blätter dieselbe Ankerplattengeometrie und denselben
`f_c,90,mean` für GL24h verwenden. Dies ist ein positiver interner
Konsistenz-Check zwischen den beiden Excel-Blättern, aber kein
unabhängiger externer Nachweis.

Was die Blätter "SD" und "HD" inhaltlich voneinander unterscheidet
(vermutlich unterschiedliche Versuchsreihen/Prüfkörper-Varianten, siehe
auch die abweichende Kürzel-Beobachtung "SD" vs. "WD" in
R2-COMMON-OPQ-008), ist weiterhin nicht aus chat-3 belegt.
