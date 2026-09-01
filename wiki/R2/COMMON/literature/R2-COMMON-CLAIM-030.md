---
claim_id: R2-COMMON-CLAIM-030
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Experimentelle Verifikation (Abschnitt 3, Tabellen 2/5/7/8):
    Material Douglas-Fir-Brettschichtholz GL36h (BS EN 1194), Riegel-
    querschnitt 135×420mm, Stützenquerschnitt 151×350mm, Gewindestangen/
    Schrauben Güte 8.8 (f_y=640MPa, f_u=800MPa), Epoxidharz-Kleber.
    Zwei Serien (JT2 mit Quersteife im Stahlkastenprofil, JT3 ohne),
    je 3 Wiederholungen. Ergebnisse: (1) Äquivalentes T-Stub-Modell
    (Tabelle 2, isolierte Zugversuche am Stahlkastenprofil): Zug-
    tragfähigkeit Abweichung Theorie/Versuch −9.2% (T1, ohne Steife)
    bzw. −4.5% (T2, mit Steife); Anfangssteifigkeit −2.8% bzw. −18.0%.
    (2) Momententragfähigkeit M_j,Rd des Gesamtanschlusses (Tabelle 5):
    JT2 (mit Steife) 64.1 kNm (Versuch) vs. 54.1 kNm (Theorie, −15.6%);
    JT3 (ohne Steife) 54.6 kNm vs. 51.8 kNm (−5.1%) — Theorie durchweg
    KONSERVATIV (unterschätzt die tatsächliche Tragfähigkeit). (3)
    Anfangsdrehsteifigkeit S_j,ini (Tabelle 7): JT2 2264 kNm/rad
    (Theorie) vs. 2187 kNm/rad (Versuch, +3.5%); JT3 1722 vs. 1760
    kNm/rad (−2.1%) — SEHR GUTE Übereinstimmung. (4) Rotationskapazität
    φ_Cd (Tabelle 8): JT2 0.051 rad (Theorie) vs. 0.056 rad (Versuch,
    −8.9%); JT3 0.085 vs. 0.105 rad (−19.0%). Duktilitätsfaktor
    (Verhältnis) im Mittel 2.7 (JT2) bzw. 4.4 (JT3) — als "zufrieden-
    stellende Duktilität" bewertet. Beobachtetes Versagensbild: deutliches
    Fließen des äquivalenten T-Stubs der äußeren beiden Schraubenreihen
    (bestätigt die Modellannahme), aber auch VORZEITIGES lokales
    Druckversagen ("premature local compressive yielding") an der
    Riegel-Druckfläche — von den Autoren als zu vermeidender Effekt
    benannt, ebenso wie vorzeitiges Versagen der Stütze auf Querdruck/
    Schub ("should be prevented ... using self-tapping screws or
    glued-in rods" zur Verstärkung).
  source: YangLiuRen2016
  pages: "48-53"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Zeigt, dass die Komponentenmethode für diesen (von R2 abweichenden)
Verbindungstyp insgesamt gut funktioniert — mit größeren Abweichungen
gerade bei der Rotationskapazität (bis −19%) und bei Serien ohne
Quersteife. Bemerkenswert und für R2 als allgemeine Warnung relevant:
die Autoren beobachteten VORZEITIGES lokales Druckversagen der
Holzkomponenten (Riegel, Stütze) als unerwünschten, die Modellgüte
beeinträchtigenden Effekt und empfehlen eine gezielte Verstärkung
(Vollgewindeschrauben oder eingeklebte Stangen) — dies deckt sich
qualitativ mit den bereits dokumentierten Lippert-Befunden zur
Druckzonenverstärkung (R2-COMMON-CLAIM-015/019/021) und ist ein
weiterer, unabhängiger Beleg dafür, dass unverstärkte Holzdruckzonen
bei konzentrierter Lasteinleitung generell zum vorzeitigen, das
rechnerische Modell störenden Versagen neigen. Kein Bezug zu den
konkreten R2-GL24h/GL75-Werten hergestellt oder herstellbar — dies
ist eine allgemeine Beobachtung aus einer anderen Versuchsserie.

---
Damit ist Yang/Liu/Ren (2016) vollständig ausgewertet (CLAIM-026 bis
-030, alle Abschnitte des 13-seitigen Papers inkl. Conclusions).
