---
open_question_id: R2-COMMON-OPQ-013
scope:
  connection: R2
  material: COMMON
status: OPEN
question: >
  Welche Länge gehört in den Nenner der Schubfeldsteifigkeit c_v: die
  Feldlänge l_v = 800 mm (bisher, c_v = G·b·h_v/l_v) oder der innere
  Hebelarm z (c_v = G·b·h_v/z)?
context: >
  Kinematik (Claude, 2026-09-30, nicht geprüft): Die Schubverzerrung γ des
  Feldes dreht die Ecke um γ. Mit T als Schubkraft im Feld ist γ = T/(G·b·h_v);
  als Feder in Reihe zur Zugseite am Hebelarm z gilt δ = γ·z, also
  c_v = G·b·h_v/z. Der Stahlbau rechnet ebenso mit z im Nenner
  (DIN EN 1993-1-8:2025-04, A.4.2, Gl. (A.13), S. 150: k_wp = 0,38·A_wp/(β·z)).
  Mit l_v statt z ist das Schubfeld um den Faktor l_v/z zu weich.
  R2/GL24h: z = 560 mm, c_v = 116.0 → 165.7 kN/mm; S_j,ini 10 155 → ≈ 11 083 kNm/rad (+9 %).
  Offen außerdem der Übertragungsparameter β und ob T die maßgebende
  Schubkraft im Feld ist.
related_sources: Buchholz2025, DIN-EN-1993-1-8-2025
options_considered: >
  (a) l_v = 800 mm beibehalten; (b) z verwenden. Aufgenommen auf Wunsch des
  Nutzers (2026-09-30).
date_opened: "2026-09-30"
date_resolved:
resolution:
---
