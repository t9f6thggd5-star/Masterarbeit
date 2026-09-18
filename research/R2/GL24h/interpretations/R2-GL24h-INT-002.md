---
interpretation_id: R2-GL24h-INT-002
scope:
  connection: R2
  material: GL24h
type: INTERPRETATION
based_on:
  experimental_results:
  observations: R2-GL24h-CALC-022, R2-COMMON-CLAIM-002, R2-COMMON-CLAIM-013, R2-COMMON-CLAIM-030
interpretation: >
  Der berechnete Wert `S_j,ini ≈ 12.540,8 kNm/rad` (R2-GL24h-CALC-022)
  liegt in einer plausiblen Größenordnung im Vergleich zu bereits im
  Wiki dokumentierten Literaturwerten für artverwandte Rahmenecken-/
  Portalrahmenanschlüsse mit eingeklebten bzw. verklebten Stahlstangen:
  deutlich über kleineren Prüfkörpern (FragiacomoBatchelar2012b,
  315×90mm-Querschnitt, 2×Ø12mm: 1.617–2.276 kNm/rad;
  YangLiuRen2016 JT2/JT3, Douglas-Fir 135×420/151×350mm:
  1.722–2.264 kNm/rad) und in derselben Größenordnung wie ein
  Querschnitt ähnlicher Größe (Lippert2002, 160×700mm, M20-Stangen:
  22.000–81.000 kNm/rad, dort aber höher — plausibel durch größere
  Stangen/andere Konstruktion). Der Trend (größerer Querschnitt/
  Hebelarm → deutlich höhere Steifigkeit, konsistent mit der
  `z²`-Abhängigkeit der Kombinationsformel) passt. Dies ist ein reiner
  Größenordnungs-Check, keine Validierung — keine der Quellen ist
  geometrisch/materialseitig direkt mit R2 vergleichbar.
certainty: INTERPRETED
superseded_by:
authored_by: CLAUDE_DRAFT
reviewed: false
---

## Ausgangslage

Mit R2-GL24h-CALC-022 liegt erstmals ein vollständiger Zahlenwert für
die Anfangsrotationssteifigkeit der Rahmenecke R2/GL24h vor
(`S_j,ini ≈ 12.540,8 kNm/rad`, aus `c_T`, `c_C`, `z` über
R2-COMMON-HYP-001). Da dieser Wert auf mehreren noch unbestätigten
Annahmen beruht (Bejtka-`c_c,90`, `z`/`c_c,0`-Plattentiefenannahme,
Kombinationsformel selbst — siehe CALC-022), ist ein unabhängiger
Plausibilitätscheck gegen die im Wiki bereits erfassten
Literaturwerte für vergleichbare Anschlusstypen sinnvoll, bevor der
Wert der Betreuerin vorgelegt wird.

## Vergleichswerte aus der Literatur

| Quelle | Geometrie | Stangen | `S_j,ini` |
|---|---|---|---|
| FragiacomoBatchelar2012b (R2-COMMON-CLAIM-002) | Glulam GL10 (Radiata Pine), 315×90mm | 2×Ø12mm Grade 8.8 | 1.617–2.276 kNm/rad ("tensioned"), 1.656–1.940 kNm/rad ("fully epoxied") |
| YangLiuRen2016, JT2/JT3 (R2-COMMON-CLAIM-030) | Douglas-Fir GL36h, Riegel 135×420mm / Stütze 151×350mm | Schrauben/Stangen Güte 8.8, Stahlkastenprofil-Anschluss | 1.722–2.264 kNm/rad (Theorie), 1.760–2.187 kNm/rad (Versuch) — sehr gute Übereinstimmung |
| Lippert2002 (R2-COMMON-CLAIM-013) | BS16h, Gehrungsschnitt-Dachanschluss, 160×700mm | M20-Gewindestangen | 22.000–55.000 kNm/rad (Körper 1, unverstärkte Druckzone), 40.000–81.000 kNm/rad (Körper 2, verstärkt) |
| **R2/GL24h (diese Arbeit)** | Rahmenecke, eingeklebte Gewindestangen, Querschnittshöhe 800mm | 4×M16 | **12.540,8 kNm/rad** (R2-GL24h-CALC-022) |

## Einordnung

Der R2-Wert liegt zwischen den beiden Gruppen von Vergleichswerten,
und zwar in einer Weise, die zur groben `z²`-Abhängigkeit der
Kombinationsformel passt: die kleinen Prüfkörper (Querschnittstiefe
315–420mm) liegen bei `S_j,ini` im Bereich 1.600–2.300 kNm/rad, der
deutlich größere Lippert-Querschnitt (700mm) bei 22.000–81.000
kNm/rad. R2 (800mm, also nochmals etwas größer als Lippert) liegt mit
12.540,8 kNm/rad zwar unter dem Lippert-Bereich, aber in derselben
Größenordnung (10⁴) und weit über den kleineren Prüfkörpern — mit
kleineren Stangen (M16 statt M20) und anderer Verbindungskonstruktion
als plausible Erklärung für den Unterschied zu Lippert.

**Kein Alarmsignal, aber auch keine Validierung.** Keine der drei
Quellen ist geometrisch, materialseitig oder konstruktiv direkt mit R2
vergleichbar (andere Holzart/-güte, andere Stangenanzahl/-durchmesser,
andere Anschlusskonstruktion — bei Lippert zusätzlich ein
Gehrungsschnitt-Dachanschluss statt einer rechtwinkligen Rahmenecke).
Der Vergleich zeigt nur: die Größenordnung des R2-Werts ist mit dem
bekannten Zusammenhang "größerer Querschnitt/Hebelarm → höhere
Anfangssteifigkeit" konsistent, mehr nicht.

## Einordnung / Vorbehalt

Diese Interpretation ändert nichts an den bereits dokumentierten
Vorbehalten von R2-GL24h-CALC-022 (Kombinationsformel `CLAUDE_DRAFT`,
`z`/`c_c,0`-Annahme über R2-COMMON-OPQ-011 offen, Bejtka-`c_c,90` nicht
offiziell abgestimmt) — sie ist ein zusätzlicher, unabhängiger
Plausibilitätshinweis, kein Ersatz für die fachliche Absicherung mit
der Betreuerin oder einen späteren Abgleich mit eigenen
Rahmenecken-Vollverbindungsversuchen (COMMON-COMMON-DEC-003).
`CLAUDE_DRAFT`, `reviewed: false` — vom Forschenden zu prüfen.
