---
calculation_id: R2-GL24h-CALC-023
scope:
  connection: R2
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature: Bejtka-2005
  experimental_data:
  assumptions: R2-GL24h-DEC-008 (einseitige Lastausbreitung)
method: >
  Vollständig rechnerische (nicht messwertgestützte) Zugseiten-
  Steifigkeitskette `c_T,ges` nach FprEN 1995-1-1:2024 und Bejtka (2005),
  jetzt korrekt inkl. Stangenanteil: Serienschaltung je Stange aus
  elastischer Stangendehnung `c_t,1` und Verbundsteifigkeit `c_ax,f,par`
  (FprEN Tab. 11.13(3)), Parallelschaltung der 4 Stangen (`c_Stangex4`),
  in Serie mit starrer Ankerplatte `c_t,ep` (vernachlässigt, =1e99),
  ASSY-verstärkter Querdrucksteifigkeit `c_c,90,verstärkt` nach Bejtka
  (R2-COMMON-CALC-001) und Schubfeld `c_v` (Holz + Furnierplatten-
  verstärkung, R2-GL24h-CALC-003/R2-COMMON-ASS-003).

  **Zweck und Abgrenzung:** Dies ist ausschließlich ein rechnerischer
  Vergleichswert zur Untersuchung des Einflusses einzelner Parameter auf
  die Steifigkeit (Aufgabenstellung Phase 3, "Einflussfaktoren
  statistisch/rechnerisch untersuchen"). Für `S_j,ini` und alle sonstigen
  Aussagen zur tatsächlichen Verbindungssteifigkeit bleibt die
  messwertgestützte Kette **R2-GL24h-CALC-021** (53,300 kN/mm, mit
  gepooltem Versuchswert `c_Stange,4x=862,531 kN/mm` aus
  R2-GL24h-II-T-S-BR-22-RES-003) maßgeblich und unverändert. Dieser
  Eintrag supersediert CALC-021 NICHT — beide haben unterschiedliche
  Rollen (rein rechnerischer Vergleichswert vs. tatsächlich verwendete,
  teilweise messwertbasierte Kette).
equations: >
  FprEN 1995-1-1:2024, Tab. 11.13(3) (`c_ax,f,par`); Bejtka (2005), Gl.
  57-71 (`c_c,90,verstärkt`, siehe R2-COMMON-CALC-001); Serienfeder
  `(Σ1/c_i)^-1`; Parallelfeder `Σc_i`.
result:
  quantity: >
    Gesamt-Zugseitensteifigkeit c_T,ges, GL24h — rein rechnerischer
    Vergleichswert (FprEN + Bejtka, ohne Versuchsdaten) für die
    Parameterstudie
  value: 39.817
  unit: kN/mm
  original_value: 39817.493882163376
  original_unit: N/mm
source_file: >
  C:\Users\Lukas\OneDrive\Masterarbeit\Claude Masterarbeit\sources\R2\
  COMMON\calculations\20260109_Berechnung_Rahmenecke_eingeklebte
  Gewindestangen.xlsx, Sheet "Rahmenecke GL24h SD", Zellen C124-C174
  (Block "Steifigkeiten Zugseite (in Bearbeitung)", per openpyxl mit
  data_only=True ausgelesen und verifiziert am 2026-09-22, nach
  Korrektur durch den Nutzer im Chat)
certainty: CALCULATED
superseded_by:
---

## Vorgeschichte

Der Block "Steifigkeiten Zugseite (in Bearbeitung)" (Zeilen 124-178,
später 124-174) wurde in `R2-GL24h-DEC-009` als händische, vorerst
ungültige Berechnung des Nutzers gekennzeichnet — weder als
Eingangsgröße noch als Vergleichsbasis zu verwenden. Im Chat vom
2026-09-22 hat der Nutzer diesen Block eigenständig korrigiert
(Kombination aus prEN-Formeln und Bejtka-Herleitung), mit dem
ausdrücklichen Zweck, damit den Einfluss verschiedener Parameter auf
die Steifigkeit rechnerisch zu untersuchen (Phase 3 der
Aufgabenstellung).

## Gefundener und behobener Formelfehler

Bei der ersten Prüfung (Zellstand vor der Korrektur, `C170=43,045
kN/mm`, entspricht dem heutigen `C174`) fiel auf, dass die Formel für
`c_T,ges` zwar laut Zeilenbeschriftung `c_t,ep+c_c,90,verstärkt+
c_Stangex4+c_v` lauten sollte, tatsächlich aber direkt die
Verbundsteifigkeit einer **einzelnen** Stange (`c_ax,f,par=177,646
kN/mm`) referenzierte — ohne die elastische Stangendehnung `c_t,1`
(wurde berechnet, aber nirgends weiterverwendet) und ohne die
Parallelschaltung der vier Stangen.

**Korrektur (durch den Nutzer in der Excel-Datei umgesetzt):**

```
c_Stange   = (1/c_t,1 + 1/c_ax,f,par)^-1        (C136) = 33,279 kN/mm
c_Stangex4 = 4 · c_Stange                        (C137) = 133,115 kN/mm
```

`c_Stangex4=133,115 kN/mm` deckt sich exakt mit dem bereits unabhängig
in `R2-GL24h-CALC-014` dokumentierten Wert für dieselbe Netzwerk-
Reduktion (dort aus den alten CALC-002-Zellen hergeleitet) — gute
Gegenprobe zwischen zwei unabhängig entstandenen Rechnungen.

**Rechnung (C174):**

```
c_T,ges = (1/c_Stangex4 + 1/c_t,ep + 1/c_c,90,verstärkt + 1/c_v)^-1
        = (1/133,115 + 1/1e99 + 1/111,339 + 1/116,0)^-1
        = 39,817 kN/mm
```

Eingangswerte (Zelle → Wert, Stand nach Korrektur): `c_t,1=40,95
kN/mm` (C128), `c_ax,f,par=177,646 kN/mm` (C134, = K_SLS,w, FprEN Tab.
11.13(3)), `c_t,ep=1e99` (C140, vernachlässigt), `c_c,90,verstärkt=
111,339 kN/mm` (C151, Bejtka, siehe R2-COMMON-CALC-001, `A=1` einseitig
gemäß R2-GL24h-DEC-008), `c_v=116,0 kN/mm` (C170 = `c_v,H`(104,0) +
2·`c_v,P`(6,0), unverändert gegenüber R2-GL24h-CALC-003/
R2-COMMON-ASS-003).

## Einordnung

Dieser Wert (39,817 kN/mm) ist niedriger als sowohl der alte,
DEC-009-invalidierte Handrechnungswert (43,045 kN/mm, Formelfehler) als
auch die messwertgestützte Kette `R2-GL24h-CALC-021` (53,300 kN/mm) —
letzteres, weil der hier verwendete rein rechnerische Stangenanteil
(133,115 kN/mm) deutlich weicher ist als der entsprechende Versuchswert
(`c_Stange,4x=862,531 kN/mm`, RES-003), der in CALC-021 eingesetzt wird.
Das ist erwartungsgemäß und keine neue Diskrepanz — vgl. den bereits in
`R2-GL24h-CALC-014`/`R2-GL24h-HYP-001` diskutierten (aber laut DEC-009
inzwischen gegenstandslosen) Faktor zwischen rechnerischem und
gemessenem Stangenanteil.

Dieser Eintrag bildet die Ausgangsbasis (Baseline) für die geplante
Parametervariation (Einfluss von `E_90,mean`, Plattengeometrie,
Stangenzahl/-durchmesser, Einbindelänge auf `c_T,ges`).
