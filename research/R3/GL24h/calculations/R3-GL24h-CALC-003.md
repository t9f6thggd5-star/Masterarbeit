---
calculation_id: R3-GL24h-CALC-003
scope:
  connection: R3
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: ETA-11-0190-2026
  literature:
  experimental_data:
  assumptions:
method: >
  **Korrigiert 2026-09-22 (siehe Superseded-Hinweis unten):** entgegen der
  ursprünglich aus chat-1 übernommenen Beschreibung ("Summe der axialen
  Einzelschrauben-Steifigkeiten") handelt es sich bei diesem Wert NICHT um
  eine Summe von Einzelschrauben-Steifigkeiten, sondern um den normativen
  Gruppensteifigkeits-Theoriewert K_ax,v,f,alpha nach FprEN 1995-1-1,
  Gl. 11.29 — eine Kombination aus axialem (K_SLS,ax) und lateralem
  (K_SLS,v) Verschiebungsmodul in Abhängigkeit vom Faserwinkel α (siehe
  Quellzelle unten). Rein rechnerisch-theoretisch ermittelt, NICHT aus
  Versuchsdaten. Verwendet identisch für beide Anschlussseiten (Column
  und Beam), ohne Differenzierung nach Faserrichtung der Lasche.
equations: >
  I29 = I28·sin(α)·(sin(α) − I12·cos(α)) + I27·cos(α)·(cos(α) + I12·sin(α))
  mit I27 = K_SLS,ax (axiales Verschiebungsmodul, FprEN Tab. 11.13(1)),
  I28 = K_SLS,v (mittleres Verschiebungsmodul, FprEN Tab. 11.12(5))
result:
  quantity: Axiale Steifigkeit der ASSY-Schraubengruppe (normativer
    Theoriewert, nicht versuchsbasiert)
  value: 199.1466
  unit: kN/mm
  original_value:
  original_unit:
source_file: >
  R3/COMMON/calculations/20260208_Berechnung_Rahmenecke_seitl.
  Holzlaschen.xlsx, Sheet "Rahmenecke GL24h SD" Zelle I29 bzw. Sheet
  "Rahmenecke GL24h HD" Zelle I28 (beide 199,14614238271503 ≈ 199,1466,
  Zellwert per openpyxl verifiziert); Stand August 2026 trotz Dateiname
  vom 08.02.2026. **Korrigiert 2026-09-22:** die dokumentierte Zellreferenz
  H30 (SD) war veraltet/falsch (vgl. Zeilenverschiebungs-Problematik wie
  bei CALC-004) — die tatsächliche Formelzelle ist I29 (SD) bzw. I28 (HD),
  Label "Anfangssteifigkeit K_ax,v,f,alpha", Norm "FprEN EC5 - 2024,
  Gl. 11.29". Der Zahlenwert war stets korrekt, nur die Methode-
  Beschreibung ("Summe der Einzelschraubensteifigkeiten") war unzutreffend.
certainty: CALCULATED
superseded_by: R3-GL24h-CALC-007 (Column-Seite, c_ax+br,par),
  R3-GL24h-CALC-008 (Beam-Seite, c_ax+br,perp)
---

Übernommen aus chat-1, KNOWLEDGE.md ("ASSY: 32 screws/group, 8×4 layout,
updated c_ax=199.1466 kN/mm, derived as sum of single-screw axial
stiffnesses").

**Wichtiger Hinweis zur Versionsgeschichte:** chat-1 nennt explizit einen
früheren Wert `c_ax = 191,11 kN/mm`, der durch diesen aktualisierten Wert
(199,1466 kN/mm) ersetzt wurde. Der frühere Wert wurde im Ursprungsmaterial
nie als eigener `research/`-Eintrag geführt, daher existiert kein
Ziel-Eintrag für ein `superseded_by`-Feld — die Korrektur wird hier nur
dokumentiert (analog zu R3-GL24h-DEC-006 für die Plattenlängen-Korrektur).

**Nachvollziehbarkeit (ursprünglich, bis 2026-09-22):** die genaue
Herleitung der Einzelschrauben-Axialsteifigkeit (vermutlich nach
ETA-11/0190, Gleichungen 4.38–4.43 laut chat-1/SOURCES.md) war in den
übernommenen Chat-Dateien nicht im Detail enthalten — nur das Endergebnis
und die (wie sich jetzt zeigt: unzutreffende) Methodenbeschreibung
("Summe der Einzelschraubensteifigkeiten") waren überliefert.

**SUPERSEDED 2026-09-22:** Im Zuge der Herleitung des Zugpfad-
Steifigkeitsketten-Formel für `c_t,sleeve` (Sheet "VSP GL24h ohne
Druckkontakt", Zelle C17) wurde die tatsächliche Quellzelle dieses Werts
identifiziert (siehe `source_file` oben) — es handelt sich um den
**normativen EC5-Theoriewert** K_ax,v,f,alpha (FprEN 1995-1-1 Gl. 11.29),
nicht um eine Ableitung aus Versuchsdaten, und er wird im Original für
Column- und Beam-Seite identisch (undifferenziert) verwendet.

Mit R3-GL24h-CALC-007 (Column, `c_ax+br,par` ≈ 183,684 kN/mm) und
R3-GL24h-CALC-008 (Beam, `c_ax+br,perp` ≈ 147,466 kN/mm) liegen jetzt aus
den tatsächlichen Push-Out-Versuchen (III-PO-S-SC-11/44-B/C) abgeleitete,
seitenspezifische Werte vor. Auf ausdrücklichen Nutzerhinweis
(2026-09-22: "der Assy Gruppenwert ist ungültig... jetzt liegen
Versuchsergebnisse vor und wir ermitteln die exakten Werte") wird dieser
Eintrag hiermit als überholt markiert. Der Wert 199,1466 kN/mm bleibt als
historischer, rein normativ-theoretischer Referenzwert dokumentiert
(z. B. zum Vergleich Theorie vs. Versuch), darf aber ab sofort **nicht
mehr** in der aktiven Zugpfad-Steifigkeitskette (`c_t,sleeve`) verwendet
werden — dafür sind CALC-007/CALC-008 maßgeblich.
