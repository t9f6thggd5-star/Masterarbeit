---
calculation_id: R2-GL24h-CALC-014
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data: R2-GL24h-II-T-S-BR-22-RES-003
  assumptions: R2-COMMON-ASS-002
method: >
  Ersetzt in der Topologie von R2-GL24h-CALC-002 den rein rechnerischen
  Anteil "vier Stangen parallel, ohne Querdruck-/Ankerplattenanteil"
  durch den gepoolten Messwert R2-GL24h-II-T-S-BR-22-RES-003 (K_ser,
  n=6, 862,531 kN/mm) und schaltet den weiterhin rein rechnerischen
  Querdruckanteil `c_c,90` (R2-GL24h-CALC-001, 100,866 kN/mm, nicht Teil
  des Versuchsaufbaus) in Serie nach.
equations: >
  Netzwerkreduktion: die ursprüngliche Topologie aus CALC-002 (je Stange
  in Serie `c_t`, `c_t,ep`, `c_c,90/4`, `c_ax,f,par`; danach 4 Stangen
  parallel) ist rechnerisch äquivalent zu: [4 Stangen parallel aus nur
  `c_t` und `c_ax,f,par` (ohne `c_c,90/4`, ohne das unendlich steife
  `c_t,ep`)] in Serie mit dem vollen, ungeteilten `c_c,90`. Nachgewiesen
  durch Nachrechnung mit den CALC-002-Eingangswerten: rein rechnerischer
  "4 Stangen ohne c_c,90"-Anteil = 133,115 kN/mm; damit in Serie mit
  `c_c,90`=100,866 kN/mm ergibt sich 57.384,18 N/mm — identisch zum in
  CALC-002 dokumentierten Ergebnis (57,384 kN/mm). Serienfeder
  `(1/c_1+1/c_2)^-1`.
result:
  quantity: Vier Gewindestangen parallel inkl. Querdruckanteil, vor dem gemeinsamen Schubfeld, GL24h (teilweise messwertbasiert)
  value: 90.306
  unit: kN/mm
  original_value: 90305.792
  original_unit: N/mm
source_file: >
  Keine Excel-Datei zugrunde liegend — eigene Nachrechnung auf Basis von
  R2-GL24h-CALC-001 (c_c,90) und R2-GL24h-II-T-S-BR-22-RES-003 (K_ser
  gepoolt), siehe Freitext.
certainty: CALCULATED
superseded_by:
---

Ersetzt R2-GL24h-CALC-002 als aktuellen Wert für dieselbe Größe ("vier
Stangen parallel, vor dem gemeinsamen Schubfeld"); CALC-002 bleibt
dokumentiert und ist über dessen `superseded_by`-Feld auf diesen Eintrag
verwiesen (CLAUDE.md Abschnitt 13 — kein Löschen/Überschreiben).

**Rechnung:**
`c_Zugpfade,ges,neu = (1/862,531 + 1/100,866)^-1 = 90,306 kN/mm`
(90.305,792 N/mm).

Zum Vergleich der rein rechnerische Vorgänger-Teilwert (vor Einsetzen
des Messwerts): die 4 Stangen ohne `c_c,90` ergäben rechnerisch nur
133,115 kN/mm (`(1/(1/40,95+1/177,646))·4`) — der gemessene
Wert (862,531 kN/mm) liegt damit um den Faktor ≈6,48 über der
rechnerischen FprEN-Vorhersage für denselben Teilanteil. Dieser
auffällig große Faktor wurde hier zunächst nur als Beobachtung
festgehalten. **Update (2026-09-22):** eine gekennzeichnete, unbestätigte
Kandidatenliste möglicher Ursachen (u. a. Bezugslängen-Diskrepanz,
konservative FprEN-Verbundsteifigkeit, Gruppenwirkung,
Prüfkörperstreuung) liegt jetzt vor, siehe R2-GL24h-HYP-001
(`CLAUDE_DRAFT`, `reviewed: false`, keiner der Kandidaten bestätigt). Zu
beachten: die zugrunde liegende Messreihe RES-002/RES-003 zeigt selbst
eine erhebliche Streuung zwischen den drei Prüfkörpern (Faktor ~3,4 bei
K_ser oben) — der Faktor 6,48 ist entsprechend mit Vorsicht zu
interpretieren, nicht als scharfe Kennzahl.

Da der resultierende Wert (90,306 kN/mm) deutlich näher an `c_c,90`
allein (100,866 kN/mm) liegt als der alte rein rechnerische Wert
(57,384 kN/mm), ist `c_c,90` — also der nach wie vor nur rechnerische,
noch nicht durch die (an dieser Stelle blockierte, siehe
R2-COMMON-OPQ-001/006) Druckseiten-Steifigkeit gestützte Anteil — jetzt
der dominierende (weichste) Teil dieser Serienkette, nicht mehr die
Stangengruppe selbst.

Eingang in R2-GL24h-CALC-015 (neue Gesamt-Zugseitensteifigkeit `c_T`, in
Serie mit dem unveränderten Schubfeld R2-GL24h-CALC-003).

**Update (2026-09-22, R2-GL24h-DEC-009):** Der Nutzer hat klargestellt,
dass die Excel-Zeilen 124-178 (Sheet "Rahmenecke GL24h SD"), aus denen
der Vergleichswert 133,115 kN/mm sowie (über R2-GL24h-CALC-001) der hier
verwendete unverstärkte `c_c,90=100,866 kN/mm` stammen, eine händische,
vorerst ungültige Berechnung sind — weder als Eingangsgröße noch als
Vergleichsbasis zu verwenden (R2-GL24h-DEC-009). Damit gilt: **der
"Faktor ≈6,48" ist keine reale fachliche Diskrepanz und nicht mehr zu
interpretieren** — R2-GL24h-HYP-001 (oben verlinkt) ist entsprechend als
vorerst gegenstandslos markiert. Der hier dokumentierte Ergebniswert
selbst (90,306 kN/mm) verwendet ebenfalls den jetzt ungültigen
unverstärkten `c_c,90` und ist damit ebenfalls nicht mehr als aktuelle
Eingangsgröße zu verwenden. Für die tatsächlich aktuelle Zugseitenkette
gilt R2-GL24h-CALC-021 (verwendet direkt die Bejtka-basierte, ASSY-
verstärkte Querdrucksteifigkeit R2-COMMON-CALC-001, nicht den hier
dokumentierten Zwischenwert) — unberührt von diesem Update. Der
versuchsbasierte Kettenanteil dieses Eintrags (`c_Stange,4x=862,531
kN/mm`, RES-003) bleibt gültig und wird auch in CALC-021 weiterverwendet.
