---
assumption_id: R1-COMMON-ASS-002
scope:
  connection: R1
  material: COMMON
type: ASSUMPTION
statement: >
  Die Druckseite der R1-Rahmenecke wird vorläufig als starr angesetzt
  (c_c,tot → ∞). Damit wird Buchholz2025 Gl. (3) zu C_rot,t+c = z² ·
  c_t,tot. Der innere Hebelarm bleibt dabei z = 550 mm.
reason: >
  Arbeitsannahme des Nutzers (2026-09-26): Die Druckseite ist voraussichtlich
  um ein Vielfaches steifer als die Zugseite, weil die Druckkraft nicht nur
  über Stabdübel und Blech, sondern zusätzlich über Kontaktpressung
  zwischen den Hölzern übertragen wird (so auch beschrieben in
  Buchholz2025, Abschn. 4.2). Die Druckversuche sind noch nicht
  ausgewertet.
basis: >
  Nutzer, 2026-09-26. Wird ersetzt, sobald die Druckversuche ausgewertet
  sind (Messkanal der Gesamtverformung, R1-COMMON-OPQ-005 (c)).
supported_by: Buchholz2025
contradicted_by:
certainty: ASSUMED
superseded_by:
---

**Folgen:**
- Obere Grenze der Steifigkeit, Φ wird eher unterschätzt. Einfluss bei
  endlicher Druckseite auf C_rot,t+c: c_c,tot = 5 · c_t,tot → −17 %,
  10 · c_t,tot → −9 %.
- Weicht von Buchholz2025 Gl. (1) ab: Dort liegen c_v,f der Druckgruppe
  und zweimal c_c,0 in Reihe, ein paralleler Kontaktpfad ist nicht
  enthalten. Mit Gl. (1) und gleichem c_v,f wie auf der Zugseite wäre
  c_c,tot sogar kleiner als c_t,tot.
- Zahlen (C_rot,v,f nach R1-GL24h-DEC-010 bzw. R1-GL75-DEC-001,
  Kombination nach R1-COMMON-DEC-004): GL24h C_rot,t+c = 0,55² · 279,52 =
  84.555 kNm/rad, C_rot,tot = 84.555 + 4 · 21.111 ≈ 169.000 kNm/rad;
  GL75 C_rot,t+c = 0,55² · 727,74 = 220.141 kNm/rad, C_rot,tot ≈
  442.100 kNm/rad.
- Hebelarm z bei Kontaktpressung: siehe R1-COMMON-OPQ-006.
