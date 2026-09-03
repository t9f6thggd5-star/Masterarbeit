---
open_question_id: R2-COMMON-OPQ-010
scope:
  connection: R2
  material: COMMON
status: OPEN
question: >
  Hat die Querdruckverstärkung (ASSY-Schrauben) einen Einfluss auf die
  Druckzonensteifigkeit (c_c,90), nicht nur auf die
  Querdrucktragfähigkeit?
context: >
  Direkt verknüpft mit R2-COMMON-OPQ-001 (Druckzonengeometrie). Laut
  Lippert (2002, siehe R2-COMMON-OPQ-001-Update vom 2026-09-01,
  wiki/R2/COMMON/literature/R2-COMMON-CLAIM-014.md) zeigt eine
  UNVERSTÄRKTE Druckzone eine lastabhängig wachsende ("weiche") Höhe,
  während eine VERSTÄRKTE Druckzone (dort: Schlitzblech) eine nahezu
  konstante Höhe aufweist. Das legt nahe, dass die ASSY-Verstärkung in R2
  nicht nur die Tragfähigkeit beeinflusst (bereits quantifiziert in
  R2-GL24h-CALC-010/011: unverstärkt ≈262,38 kN vs. verstärkt
  ≈384,12 kN), sondern auch die Steifigkeit c_c,90 selbst — und
  möglicherweise auch deren Linearität/Konstanz über den Lastbereich.
  Ohne Klärung ist unklar, ob für R2 unterschiedliche c_c,90-Werte bzw.
  Steifigkeitsverläufe für den unverstärkten und den verstärkten Fall
  anzusetzen sind, und wie sich das auf das Rotationsmodell
  (R2-COMMON-OPQ-006) auswirkt.
related_sources:
  - wiki/R2/COMMON/literature/R2-COMMON-CLAIM-014.md
options_considered:
date_opened: "2026-09-03"
date_resolved:
resolution:
---

Vom Nutzer am 2026-09-03 in Vorbereitung der Besprechung als Ergänzung zu
R2-COMMON-OPQ-001 gestellt. Eigene ID vergeben, da es eine eigenständige
Frage ist (Einfluss der Verstärkung auf die Steifigkeit c_c,90, nicht nur
auf Tragfähigkeit oder Zonenform), auch wenn sie eng mit R2-COMMON-OPQ-001
zusammenhängt und wohl nur gemeinsam mit dieser final beantwortet werden
kann. Lipperts Befund (CLAIM-014) ist NICHT direkt auf R2 übertragbar
(andere Geometrie/Material/Konstruktion), liefert aber den Anlass für
diese Frage.
