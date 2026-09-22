---
open_question_id: R3-GL24h-OPQ-022
scope:
  connection: R3
  material: GL24h
status: OPEN
question: >
  Wie groß ist die tatsächliche Anfangssteifigkeit der Beam-seitigen
  ASSY-Schraubengruppe (c_ax+br,perp) für 4×4 (16 Schrauben) bzw. die
  reale 4×8-Gruppe (32 Schrauben, eine Laschenseite)? Der aktuell
  verwendete Wert (c32,Beam ≈ 147,47 kN/mm, R3-GL24h-CALC-008) beruht
  vollständig auf der unbelegten Vereinfachungsannahme R3-GL24h-ASS-004
  (Beam/Column-Steifigkeitsverhältnis wird als schraubenzahl-
  unabhängig angenommen), nicht auf einer eigenen empirischen oder
  normativen Bestimmung des Beam-seitigen Gruppeneffekts.
context: >
  Für die Beam-Seite fehlen verwertbare 4×4-Steifigkeitsdaten
  vollständig: III-PO-S-SC-44-B-2/3 enthalten keine einzige Kraft-Weg-
  Messreihe, und die Steifigkeit von PK1 ist in der Auswertungsdatei
  manuell als "nv" markiert (kein Formelfehler, sondern bewusste
  Markierung) — Ursache laut Nutzerhinweis 2026-09-22: Querzugversagen
  im Holz, ein anderer Versagensmechanismus als die eigentliche
  ASSY-Schraubengruppen-Steifigkeit (siehe R3-GL24h-OPQ-021). Auch der
  einzige Fmax-Wert dieser Serie (n=1, 47,3 kN) gilt aus demselben
  Grund nicht als belastbare Datenbasis für eine indirekte Ableitung.
related_sources:
options_considered: >
  1. Übertragung des Column-kalibrierten Potenzgesetz-Exponenten α
     (R3-GL24h-ASS-003) auf die Beam-Seite — vom Nutzer verworfen
     (2026-09-22), da die Faserrichtung wechselt und keine empirische
     Grundlage für die Übertragbarkeit besteht.
  2. Kreuzverhältnis-/Verschiebungsfaktor-Methode über das Beam/Column-
     Tragfähigkeitsverhältnis (11er zu 44er) — verworfen, da sie
     vollständig vom einzigen, nicht belastbaren 44-B-Fmax-Wert abhängt.
  3. Normative n_ef-Formel (FprEN 1995-1-1 Tab. 11.10(6)), im Push-Out-
     Workbook für die Column-Seite mit n_ef≈12,48 (4×4) hinterlegt,
     grundsätzlich faserrichtungsunabhängig — führt aber rechnerisch
     zwangsläufig auf dasselbe Beam/Column-Verhältnis wie die gewählte
     Vereinfachung (mathematisch äquivalent, siehe Diskussion
     2026-09-22), liefert also keine unabhängige Information.
  4. Literaturrecherche (2026-09-22): keine validierte Formel für die
     Steifigkeits-Gruppeneffizienz axial beanspruchter Schraubenreihen
     in Abhängigkeit vom Faserwinkel gefunden. Stamatopoulos & Malo
     (2017) zeigen zwar, dass der Tragfähigkeits-Gruppeneffekt bei
     Gewindestangenpaaren vom Faserwinkel abhängt (n_ef 1,72–1,94 je
     nach Winkel 15°–90°), liefern aber keine direkt anwendbare Formel.
  Gewählt (Nutzerentscheidung 2026-09-22): konstantes Beam/Column-
  Verhältnis c1,Beam/c1,Column = 0,8028 als bewusste, vorläufige
  Vereinfachung (R3-GL24h-ASS-004) — mathematisch äquivalent zu
  Option 1 und 3, jetzt aber explizit als Vereinfachung markiert statt
  stillschweigend vorausgesetzt.
date_opened: "2026-09-22"
date_resolved:
resolution:
---

Aufgeworfen im Zuge der Hochrechnung der ASSY-Schraubengruppen-
Steifigkeit von 16 auf 32 Schrauben (R3-GL24h-CALC-007/008). Der
Column-seitige Wert (CALC-007) ist empirisch kalibriert und direkt aus
Messdaten hochgerechnet; der Beam-seitige Wert (CALC-008) beruht
dagegen vollständig auf einer nicht empirisch geprüften
Vereinfachungsannahme — dieser Unterschied im Vertrauensniveau der
beiden Werte sollte bei der weiteren Verwendung (Zugpfad-
Gesamtsteifigkeitskette, S_j,ini) im Blick behalten werden.

Wird als gelöst betrachtet, sobald entweder (a) ein neuer, verwertbarer
Push-Out-Versuch für die Beam-seitige 4×4-Konfiguration vorliegt, oder
(b) eine belastbare, faserwinkelabhängige normative/wissenschaftliche
Methode gefunden wird, die unabhängig von den fehlenden 44-B-Daten
anwendbar ist.
