---
result_id: R2-GL24h-II-T-S-BR-22-RES-003
scope:
  connection: R2
  material: GL24h
  experiment_level: COMPONENT
type: EXPERIMENTAL_RESULT
derived_from: R2-GL24h-II-T-S-BR-22-RES-002
n: 6
method: >
  Poolung der beiden in R2-GL24h-II-T-S-BR-22-RES-002 dokumentierten
  K_ser-Mittelwerte ("oben" = 840,871 kN/mm, "unten" = 884,191 kN/mm,
  je n=3) zu einem gemeinsamen Stichprobenmittel. Begründung: "oben" und
  "unten" sind laut Nutzerangabe (Chat, 2026-09-16) zwei separat
  eingeklebte, geometrisch identische 2×2-M16-Stangengruppen an den
  beiden Enden desselben Prüfkörpers, die durch symmetrisches
  beidseitiges Ziehen unabhängig voneinander geprüft wurden — nicht zwei
  Messstellenpaare derselben Stangengruppe (Korrektur gegenüber der
  ursprünglichen Formulierung in RES-002, siehe dortiges Update). Beide
  Positionen bilden damit dieselbe Verbindungsart ab; bei gleicher
  Gruppengröße (n=3 je Position) entspricht das arithmetische Mittel der
  beiden Teilmittelwerte exakt dem gepoolten Mittelwert aller 6
  Einzelwerte: (840,871 + 884,191) / 2 = 862,531 kN/mm.
result:
  quantity: Anfangssteifigkeit K_ser einer eingeklebten 2×2-M16-Gewindestangengruppe (gepoolter Mittelwert oben+unten, GL24h)
  value: 862.531
  unit: kN/mm
  original_value:
  original_unit:
certainty: MEASURED
---

Rein rechnerische Poolung zweier bereits in RES-002 dokumentierter
Mittelwerte, keine neue Rohdatenquelle. Die in RES-002 dokumentierte,
erhebliche Streuung zwischen den drei Prüfkörpern (K_ser oben:
Faktor ~3,4 zwischen kleinstem und größtem Wert) bleibt bestehen und
wird durch diese Poolung nicht reduziert — der gepoolte Mittelwert ist
weiterhin mit Vorsicht als Eingangsgröße zu verwenden, nicht als eng
gesicherter charakteristischer Wert (vgl. CLAUDE.md Abschnitt 15).

Diese Größe deckt ausschließlich die 2×2-Stangengruppe selbst ab (freie
Stangendehnung + Verbund-/Einklebesteifigkeit), OHNE den
Querdruck-/Ankerplattenanteil `c_c,90`, da der Versuchsaufbau (Stangen
in einem freien Holzquerschnitt, ohne Ankerplatte) diesen Anteil nicht
enthält (vom Nutzer im Chat am 2026-09-16 bestätigt). Verwendet in
R2-GL24h-CALC-014 als Ersatz für den entsprechenden rein rechnerischen
Teilwert aus R2-GL24h-CALC-002.

**Update (2026-09-16):** Der Nutzer hat entschieden (R2-COMMON-DEC-003),
künftig durchgängig die in der Quelldatei selbst bereits vorliegenden
"Mean Anfangssteifigkeit"-Werte (Blatt "Überblick", Zellen B94:B97)
direkt anzusetzen statt sie bedarfsweise neu herzuleiten. Dieser Eintrag
ist davon inhaltlich nicht betroffen (der Wert war bereits identisch,
siehe `method`-Feld oben), gilt aber ab jetzt zusätzlich als direkt auf
Zelle B97 zurückgeführt.
