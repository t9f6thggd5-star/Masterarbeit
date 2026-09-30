---
decision_id: R3-COMMON-DEC-004
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Welcher innere Hebelarm z wird für Tragfähigkeit und Steifigkeit der
  R3-Rahmenecke (GL24h und GL75) angesetzt?
decision: >
  Die Druckresultierende liegt im Drittel der Druckzone (dreieckförmige
  Pressungsverteilung): z = Abstand Zugkraft zum Stützenrand − 1/3 ·
  Druckzonenbreite = 720 − 400/3 = 586,7 mm.
reason: >
  Nutzerentscheidung (Chat, 2026-09-28); entspricht dem im R3-Excel bereits
  verwendeten Wert (Sheet "Rahmenecke GL24h SD" D105 = D102 − D103 mit D102 =
  720 mm, D103 = N95/3 = 133,3 mm; GL75 H108 = H105 − H106, identisch
  586,7 mm).
alternatives_considered: >
  z = 640 mm (vorläufiger Wert aus chat-1, R3-GL24h-DEC-007, Herkunft nicht
  dokumentiert) — ersetzt.
date: "2026-09-28"
superseded_by:
---

Ersetzt R3-GL24h-DEC-007. Gilt für GL24h und GL75, da die Geometrie im Excel
für beide Materialien gleich ist.

**Ergänzung (2026-09-28), Begründung Unterschied zu R2 (Nutzer):** Bei R2
sind eine Lasteinleitungsplatte aus Stahl und eine Querdruckverstärkung
vorhanden, die keine Lastausbreitung zulassen; dort wird daher eine
rechteckige Spannungsverteilung angenommen (R2-COMMON-DEC-002). Bei R3 liegt
der Träger vollständig auf, die Pressung verteilt sich elastisch
dreieckförmig. Die Druckzonenbreite von 400 mm ist dabei eine Annahme; nach
Ansicht des Nutzers müsste die Druckzone der Teil auf der Druckseite des
Rotationspunkts (Nulllinie) sein, siehe R3-COMMON-OPQ-001.
