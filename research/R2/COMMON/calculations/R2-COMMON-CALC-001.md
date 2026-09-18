---
calculation_id: R2-COMMON-CALC-001
scope:
  connection: R2
  material: COMMON
type: CALCULATION
inputs:
  normative_sources:
  literature: Bejtka-2005
  experimental_data:
  assumptions:
method: >
  Theoretische Herleitung des wirksamen Elastizitätsmoduls `E_tot` einer
  mit Vollgewindeschrauben (ASSY) verstärkten, querdruckbeanspruchten
  Kontaktzone, nach Bejtka (2005), Dissertation KIT, Abschnitt 3.5.2
  "Steifigkeit verstärkter Bauteile" (Gl. 57-67). Basiert auf derselben
  Theorie des verschieblichen Verbundes (Volkersen 1953) wie der
  Ausziehwiderstand (Abschnitt 3.3.4), hier auf Druck statt Zug
  angewendet. Material-/verbindungsunabhängiges Modell — nicht
  GL24h- oder GL75-spezifisch, daher `material: COMMON`. Anwendbarkeits-
  bedingung (Bejtka, Bild 3-30): das Modell gilt nur für Verstärkungen
  mit einer steifen Kontaktplatte (z. B. Stahlplatte) an der
  Lasteinleitung — ohne Platte ist laut Bejtkas eigenem Vergleich
  (Tab. 3-3) nur die unverstärkte `E_90` anzusetzen.
equations: >
  Bejtka (2005), Gl. 57-71 — vollständige Herleitung siehe Freitext
  unten. Kernergebnis: Gl. 67 (E_tot), mit Hilfsgrößen `f_LA` (Gl. 68),
  `c_v` (Gl. 10), `ω` (Gl. 71), `ψ` (Gl. 70), `φ` (Gl. 69).
result:
  quantity: >
    Geschlossene Formel für E_tot (Gl. 67) — kein einzelner
    Zahlenwert, siehe Freitext für eine erste Beispielrechnung
    (R2/GL24h, Zugseite)
  value: 111.339
  unit: kN/mm
  original_value:
  original_unit:
source_file:
certainty: CALCULATED
superseded_by:
---

Dokumentiert die theoretische Herleitung hinter der Diskussion vom
2026-09-16/17 zur Frage, ob ASSY-Verstärkung die Steifigkeit (nicht nur
die Tragfähigkeit) der Querdruckzone beeinflusst. FprEN 1995-1-1:2024
(8.1.6.2(6), NOTE) und ETA 11/0190 (Anhang A.3) liefern dazu nur
qualitative Hinweise bzw. reine Tragfähigkeitsmodelle, keine Formel —
Bejtka (2005) ist die einzige gefundene Quelle mit einem vollständigen,
FE-verifizierten (Korrelationskoeffizient 1,0 gegenüber FE-Rechnungen)
geschlossenen Ansatz.

## Herleitung (Gl. 57-66)

Ausgangsgröße ist die gesamte Zusammendrückung `Δu` des Holzes
rechtwinklig zur Faser über die Schraubenlänge `l_S`:

**Gl. 57:** `Δu = u_H(0) − u_H(l_S)` — Eindrückung an der Lasteinleitung
minus Eindrückung an der Schraubenspitze.

**Gl. 58:** `u_H(0) = u_S(0) = u_S(l_S) + ε_S·l_S` — bei "harter"
Lasteinleitung (Stahlplatte, siehe Anwendbarkeitsbedingung oben) sind
Holz- und Schraubenkopf-Eindrückung identisch; die
Schraubenkopfverschiebung ist die Spitzenverschiebung plus die
elastische Schraubenstauchung dazwischen.

**Gl. 59:** `u_S(l_S) = s(l_S) + u_H(l_S)` — die Schraubenspitzen-
verschiebung ist die dortige Holzeindrückung plus der Verbund-Schlupf
`s(l_S)` zwischen Schraube und Holz (Volkersen-Term).

**Gl. 60:** Einsetzen von (59) in (58):
`u_H(0) = s(l_S) + u_H(l_S) + ε_S·l_S`.

**Gl. 61:** Vereinfachung auf die gesuchte Größe:
`Δu = s(l_S) + ε_S·l_S` — die Gesamtstauchung zerfällt in
Verbund-Schlupf an der Spitze plus elastische Schraubendehnung.

**Gl. 62:** Geschlossene Formel für `s(l_S)` aus der Verbundtheorie
(analog Gl. 38 für ein Einzelelement, hier für `n` Schrauben
verallgemeinert), bereits durch den Lastausbreitungsfaktor `f_LA`
(Gl. 68/41) geteilt — die lineare Lastausbreitung ist damit an dieser
Stelle schon eingebaut.

**Gl. 63:** `ε_S ≈ 0,7·N_S,0/(E_S·A_S)` — Schraubendehnung. Der Faktor
`0,7` folgt aus der Annahme eines parabelförmigen (nicht konstanten)
Normalkraftverlaufs entlang der Schraubenachse infolge des Verbunds mit
dem Holz; die für die Dehnung maßgebende mittlere Kraft beträgt daher
nur ≈70 % der Kopfkraft `N_S,0`.

**Gl. 64:** Vollständige `Δu`-Formel durch Einsetzen von Gl. 62 und 63
in Gl. 61 — abhängig von den noch unbekannten Kräften `N_H,0`
(Holzoberfläche) und `N_S,0` (je Schraube).

**Gl. 65:** Kräfteverhältnis `Θ = N_H,0/N_S,0` aus derselben
"harte Lasteinleitung"-Bedingung (Gl. 39/58) — beschreibt, wie sich die
eingeleitete Kraft zwischen dem direkten Holzpfad und den `n` Schrauben
aufteilt (Parallelfeder-artige Kopplung über den Verbund).

**Gl. 66:** Definition `E_tot = (N_H,0/n + N_S,0)·n·l_S/(A_H·Δu)` —
Hookesches Gesetz rückwärts: Gesamtkraft bezogen auf `A_H`, geteilt
durch die Gesamtdehnung `Δu/l_S`.

**→ Gl. 67:** Einsetzen von Gl. 64 (`Δu`) und Gl. 65 (`Θ`, daraus `ψ`
in Gl. 70) in Gl. 66 eliminiert die unbekannten Einzelkräfte
`N_H,0`/`N_S,0` vollständig — übrig bleibt die geschlossene Formel:

```
E_tot = [E_90·f_LA·n·l_S·(ψ/n+1)·ω·sinh(ω·l_S)]
        / [φ−ψ+n·(ψ/n+1)·cosh(ω·l_S)+0,7·f_LA·l_S·φ·ω·sinh(ω·l_S)]
```

mit den Hilfsgrößen:
- `φ = E_90·A_H/(E_S·A_S)` (Gl. 69) — Steifigkeitsverhältnis Holz-
  querschnitt zu Schraubenquerschnitt.
- `ω = √[(1/(E_S·A_S)+n/(E_90·A_H))·c_v]` (Gl. 71) — Abklingkonstante.
- `c_v = 234·(ρ·d)^0,2/l_S^0,6` [N/mm²] (Gl. 10) — empirischer
  Bettungsmodul aus 413 Push-in-Versuchen, `d` = Schrauben-
  **Nenn**durchmesser.
- `f_LA = 1+A·(l_S/l_ef)·tanα` (Gl. 68) — Lastausbreitungsfaktor,
  `A=0/1/2` für keine/einseitige/beidseitige Ausbreitung, `l_ef` =
  rohe "Länge der Lasteinleitung" (unabhängiger geometrischer
  FE-Parameter aus Bejtkas eigener Studie, 10d-40d variiert — nicht die
  FprEN-Ersatzlänge aus Gl. 9.31).
- `ψ = (n+φ·cosh(ω·l_S))/(cosh(ω·l_S)-1)·f_LA` (Gl. 70).

Rückrechnung auf die Feder: `c_c,90,verstärkt = E_tot·A_H/l_S` (`E_tot`
ist bei Bejtka explizit "bezogen auf die Fläche A_H... und auf die
Länge l_S" definiert — eine erneute Einsetzung in die alte FprEN-
Formel mit `A`/`A_ef` (Gl. 9.31) würde die Lastausbreitung doppelt
zählen, da sie über `f_LA` bereits in `E_tot` enthalten ist). Diese
Rückrechnung ist keine eigenständige Herleitung, sondern nur die
Umkehrung der Definition aus Gl. 66: für einen homogenen Stab gilt
`F=(E·A/l)·u`, also `c=E·A/l`; genau so wurde `E_tot` in Gl. 66 aus
`N_ges` und `Δu` definiert (`E_tot=N_ges·l_S/(A_H·Δu)`), sodass
`E_tot·A_H/l_S` unmittelbar wieder `N_ges/Δu = c` ergibt.

## Umsetzung in Excel

Zur Nachvollziehbarkeit die konkrete Umsetzung von Gl. 67-71 im
R2-Excel, Sheet "Rahmenecke GL24h SD", ab Zeile 98 (Zugseite, `A=1`):

| Zelle | Größe | Formel | Gl. |
|---|---|---|---|
| L98 | `A_S` [mm²] | `=(PI()*L54^2)/4` | — |
| L99 | `c_v` [N/mm²] | `=234*(((Holzkennwerte!D21*L53)^0.2)/L67^0.6)` | 10 |
| L100 | `f_LA` [-] | `=1+1*(L65/L35)*TAN(RADIANS(L38))` | 68 |
| L101 | `φ` [-] | `=(Holzkennwerte!D35*L42)/(210000*L98)` | 69 |
| L102 | `ψ` [-] | `=(L58+L101*COSHYP(L103*L65))/(COSHYP(L103*L65)-1)*L100` | 70 |
| L103 | `ω` [mm⁻¹] | `=SQRT((1/(210000*L98)+L58/(Holzkennwerte!D35*L42))*L99)` | 71 |
| L104 | `E_tot` [N/mm²] | `=(Holzkennwerte!D35*L100*L58*L65*(L102/L58+1)*L103*SINHYP(L103*L65))/(L101-L102+L58*(L102/L58+1)*COSHYP(L103*L65)+0,7*L100*L65*L101*L103*SINHYP(L103*L65))` | 67 |

`L65`="Gewindelänge im Holz l_w" und `L67`="l_r" sind hier zahlengleich
(beide 580mm) — **geklärt am 2026-09-18:** kein Zufall, sondern
dieselbe Größe unter zwei Namen. `l_r` ist die offizielle FprEN-
1995-1-1:2024-Bezeichnung (Abschnitt 8, Schraubenverstärkung der
Querdruckzone, Fig. 8.5): "the reinforced length of the threaded part
of the screw or rod in the timber member" — inhaltlich identisch mit
dem, was die Excel-Datei unter dem beschreibenden Label `l_w`
("Gewindelänge im Holz") führt, und passend zum ASSY-Verstärkungs-
kontext von R2. `l_r` wird in der Excel-Datei separat (als fester
Zahlenwert, nicht per Formel mit `L65` verknüpft) für zwei Formeln
verwendet: die Gruppen-Effektivlänge `l_2,ef` (Gl. 8.15, Zeile 70) und
als `l_S`-Eingang in Bejtkas eigener `c_v`-Formel (Gl. 10, Zeile
99/101, s. Tabelle oben). Da beide Größen per Definition identisch
sind, besteht hier kein Risiko eines stillen Auseinanderlaufens.
`L38`="Lastausbreitungswinkel" (45°)
ist derselbe Winkel wie in der FprEN-Ausbreitung (Tab. 8.2), hier als
`tanα` in `f_LA` verwendet.

**Hinweis (deutsche Excel-Version):** die Hyperbelfunktionen heißen
lokalisiert `SINHYP`/`COSHYP`/`TANHYP`, nicht `SINH`/`COSH`/`TANH` —
die englischen Funktionsnamen werden nicht erkannt und führen zu
`#NAME?`-Fehlern (getroffen bei einem ersten Formulierungsversuch von
L102/Gl. 70).

## Beispielrechnung (R2/GL24h, Zugseite, A=1)

Zur Veranschaulichung mit den tatsächlichen R2-Werten durchgerechnet
(9×ASSY plus VG 4 CSMP 8×580, `d=8mm`, `d_1=5mm`, `A_H=38.400 mm²`
[160×240], `l_S=580mm`, `l_ef=240mm`, `ρ=420 kg/m³`, `E_90=300 N/mm²`,
`E_S=210.000 N/mm²`, `α=45°`, `A=1` einseitig gemäß R2-GL24h-DEC-008):

`A_S=19,635 mm²` → `c_v=26,087 N/mm²` (Gl. 10) → `φ=2,7938` (Gl. 69) →
`ω=5,1679×10⁻³ mm⁻¹`, `ω·l_S=2,9974` (Gl. 71) → `f_LA=3,4167` (Gl. 68)
→ `cosh(ω·l_S)=10,0415`, `sinh(ω·l_S)=9,9916` → `ψ=14,0024` (Gl. 70) →
`E_tot=1.681,68 N/mm²` (Gl. 67, Faktor ≈5,61 gegenüber reinem
`E_90=300 N/mm²`) → `c_c,90,verstärkt=E_tot·A_H/l_S=111,339 kN/mm`.

Gegenüber dem unverstärkten Zugseiten-Wert (`100,866 kN/mm`,
R2-GL24h-CALC-001) ein Zuwachs von `+10,4 %`.

## Warum ist der Zuwachs nur ~10%, obwohl E_tot ≈ 5,6×E_90 beträgt?

Auf den ersten Blick widersprüchlich: `E_tot=1.681,68 N/mm²` ist das
`5,606`-fache von `E_90=300 N/mm²`, der resultierende Zuwachs bei
`c_c,90` beträgt aber nur `+10,4 %`. Grund ist, dass die verstärkte
und die unverstärkte Formel durch fundamental unterschiedliche
Bezugslängen teilen (`c_c,90 ~ E·A/l` reagiert genauso auf die Länge
im Nenner wie auf das E-Modul im Zähler):

- **Unverstärkt** (R2-GL24h-CALC-001, FprEN Gl. 9.31): Bezugslänge
  `h_ef=140mm` (Gl. 8.11, `min(0,4h;140)`) — eine kurze effektive
  Ausbreitungstiefe. Zusätzlich bekommt diese Formel über die durch
  45°-Ausbreitung vergrößerte Fläche `A_ef=60.800mm²` (statt der
  reinen Plattenfläche `A=38.400mm²`) einen "Ausbreitungs-Bonus":
  gegenüber einer naiven Rechnung nur mit `A_H` (`E_90·A_H/h_ef ≈
  82.286 N/mm`) liefert die tatsächliche Formel `100.866 N/mm`, Faktor
  `≈1,226`.
- **Verstärkt** (Bejtka, Rückrechnung): Bezugslänge `l_S=580mm` — die
  volle Schraubenlänge, `4,14`-mal länger als `h_ef`. Die
  Lastausbreitung steckt hier schon in `E_tot` selbst (über `f_LA`),
  daher wird bewusst nur mit der reinen Kontaktfläche `A_H`
  gerechnet, ohne zusätzlichen Flächen-Bonus (sonst Doppelzählung,
  siehe oben).

Rechnerische Zerlegung: `5,606 (E-Zuwachs) ÷ 4,143 (Längenverhältnis
l_S/h_ef) ÷ 1,226 (Ausbreitungs-Bonus, den nur die unverstärkte
Formel bekommt) ≈ 1,104` → deckt sich mit dem beobachteten `+10,4 %`.
Der eigentliche Steifigkeitsgewinn durch die Schrauben wird also
größtenteils dadurch kompensiert, dass Bejtkas Modell ihn über die
viel längere Schraubenlänge verteilt statt über eine kurze
Ausbreitungstiefe — physikalisch plausibel, da die Schraube über
ihre gesamte Länge Kraft einleitet.

**Status:** Diese Beispielrechnung ist eine erste Verifikation der
Methode anhand der R2-Geometrie, aber **noch nicht** offiziell in die
`c_c,90`-Kette übernommen — R2-GL24h-CALC-001 bleibt bis auf Weiteres
der gültige, im Wiki referenzierte Wert für die unverstärkte
Zugseiten-Steifigkeit. Die Druckseite (`A=2`) sowie die formale
Übernahme (inkl. Konsequenzen für CALC-014/015/INT-001) sind mit dem
Nutzer noch nicht abschließend besprochen — siehe R2-COMMON-OPQ-006 und
die "Nächste Schritte"-Abschnitte in den `current_state.md`-Dateien.
