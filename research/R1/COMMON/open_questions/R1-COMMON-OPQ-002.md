---
open_question_id: R1-COMMON-OPQ-002
scope:
  connection: R1
  material: COMMON
status: RESOLVED
question: >
  Warum stimmen die Mittelwerte der Anfangssteifigkeit K_ser im Blatt
  "Diagramme Steifigkeiten" (Zellen H6 für GL24h und H35 für GL75) nicht
  mit dem rechnerischen Mittelwert der sechs Einzelwerte überein, und
  welcher Wert ist für die weitere Auswertung (Mittelwertlinie in den
  Diagrammen, Variationskoeffizient) zu verwenden?
context: >
  Fund (Claude, Nutzer bestätigt) bei der Durchsicht des Blattes
  "Diagramme Steifigkeiten" in "Auswertung Steifigkeiten_0703_Zugversuche_
  Stahl-Holz-Stabdübel.xlsx" (R1/COMMON/calculations, Stand 2026-09-21).
  Die Zellen H6 und H35 enthalten feste Zahlenwerte und keine Formel;
  der K_e-Mittelwert (H7, H36) ist dagegen als Formel =SUM(..)/6
  hinterlegt.
  GL24h: H6 = 259,83 kN/mm; Mittelwert von B6:G6 = 279,52 kN/mm (Abweichung
  −7,0 %). Standardabweichung 53,34 kN/mm; Variationskoeffizient J11 =
  G11/H6 = 20,5 % statt 19,1 % mit dem berechneten Mittelwert.
  GL75: H35 = 729,16 kN/mm; Nachrechnung von B35:G35 durch Claude ergibt
  727,74 kN/mm (Abweichung +0,2 %); der Nutzer nannte 727,54 kN/mm — die
  Differenz zwischen 727,74 und 727,54 ist ungeklärt (vermutlich
  Tippfehler, nicht geprüft). Standardabweichung 64,31 kN/mm;
  Variationskoeffizient 8,8 %.
  H6/I6 und H35/I35 speisen die Mittelwertlinie in den Diagrammen
  "Versuchsnummern / Steifigkeit K_ser" (GL24h und GL75) und die
  Variationskoeffizienten J11 und J40. Woher die festen Werte stammen
  (frühere Datenversion, Handeintrag, andere Versuchsauswahl) ist nicht
  bekannt. Die Blätter der Einzelversuche wurden nicht verändert.
related_sources:
options_considered: >
  (a) H6 und H35 durch Formeln ersetzen (=SUM(B6:G6)/6 bzw.
  =SUM(B35:G35)/6, analog zu H7 und H36); (b) festen Wert beibehalten,
  falls er eine bewusste Auswahl (z. B. Ausschluss einzelner Versuche)
  darstellt und dies dokumentiert wird. Bisher kein Hinweis auf (b).
date_opened: "2026-09-21"
date_resolved: "2026-09-21"
resolution: >
  Die festen Werte in H6 (259,83) und H35 (729,16) waren fehlerhaft. Richtig
  sind die rechnerischen Mittelwerte 279,52 kN/mm (GL24h) und 727,74 kN/mm
  (GL75), vom Nutzer am 2026-09-21 bestätigt. Option (a) umgesetzt: In der
  Datei "Kopie von Auswertung Steifigkeiten_0703_Zugversuche_Stahl-Holz-
  Stabdübel kopie.xlsx" (R1/COMMON/calculations) stehen H6 und H35 als
  Formeln (Mittelwert von B6:G6 bzw. B35:G35); der Variationskoeffizient
  J11 beträgt damit 19,1 %, J40 8,8 %. Die genannten 727,54 kN/mm waren
  ein Zahlendreher des Nutzers. Die Herkunft der ursprünglichen festen
  Werte wurde nicht weiter verfolgt. Die Originaldatei (ohne "Kopie")
  enthält weiterhin die festen Werte.
---

Aufgenommen auf Wunsch des Nutzers (2026-09-21) und am selben Tag vom
Nutzer als gelöst gemeldet (siehe `resolution`). Verwandt: R1-GL75-OPQ-001
(Rohdichte in derselben Auswertungs-Excel, weiter OPEN).

**Arbeitsstand (2026-09-21):** Der Nutzer hat in der Datei "Kopie von
Auswertung Steifigkeiten_0703_Zugversuche_Stahl-Holz-Stabdübel kopie.xlsx"
(R1/COMMON/calculations) H6 und H35 durch Formeln (=MITTELWERT(B6:G6) bzw.
=MITTELWERT(B35:G35)) ersetzt; Claude rechnet vorläufig mit dieser Kopie
weiter. Ergebnis: GL24h 279,52 kN/mm (Variationskoeffizient 19,1 %), GL75
727,74 kN/mm (8,8 %). Die vom Nutzer zunächst genannten 727,54 kN/mm für
GL75 waren ein Zahlendreher; der Nutzer bestätigte 727,74 kN/mm als
richtig. Die Frage ist damit gelöst; die Ursache der ursprünglich festen
Werte 259,83 und 729,16 wurde nicht weiter verfolgt.
