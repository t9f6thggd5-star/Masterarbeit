---
decision_id: R3-COMMON-DEC-011
scope:
  connection: R3
  material: COMMON
type: DECISION
question: >
  Gibt es an der Stoßfuge zwischen den Laschenhälften (Eckfuge Riegel/Stütze)
  einen Spalt, oder liegen die Laschenhälften an?
decision: >
  Künftig wird angenommen, dass kein Spalt vorhanden ist: Die Laschenhälften
  liegen an der Stoßfuge an (Druckkontakt). Die Berechnungen werden auf diesen
  Zustand umgestellt.
reason: >
  Nutzerentscheidung (Chat, 2026-09-30): "Wir wissen es nicht 100 %, ich
  möchte aber jetzt in Zukunft davon ausgehen, dass es keinen Spalt gibt."
alternatives_considered: >
  Variante ohne Kontakt (R3-GL24h-DEC-004, bisherige Hauptvariante, damals
  nach Rücksprache mit der Betreuung festgelegt, weil die Lasche in der
  Eckfuge gestoßen ist). Ob sie als Vergleichsfall weitergeführt wird, ist
  noch nicht entschieden.
date: "2026-09-30"
superseded_by:
---

Ersetzt R3-GL24h-DEC-004. Beantwortet R3-GL24h-OPQ-009 als Annahme (der
tatsächliche Zustand am Prüfkörper bleibt unsicher). Gilt für GL24h und GL75.

**Betroffen (zu überarbeiten, Schritt für Schritt mit dem Nutzer):**
1. Druckseite (R3-COMMON-DEC-009): bisher gesamte Druckkraft über den Kontakt
   Riegel/Stütze; mit Kontakt der Laschenhälften geht ein Teil der Druckkraft
   über die Laschen der Druckseite (Hinweis Buchholz2025).
2. Vorspannung (R3-COMMON-OPQ-007): Die Vorspannkraft schließt sich über die
   Laschenhälften an der Stoßfuge (verspannter Verband wie bei einer
   Schraubenverbindung), nicht mehr über ASSY und Fuge Riegel/Stütze.
3. Zugkette: Bedeutung (b) von c_c,0 bei Buchholz (Kontakt der Laschenhälften)
   wird relevant (R3-COMMON-OPQ-004).
4. Excel: Blätter "VSP GL24h/GL75 ohne Druckkontakt".

Die Änderung ist der Betreuung mitzuteilen, da R3-GL24h-DEC-004 mit ihr
abgestimmt war.
