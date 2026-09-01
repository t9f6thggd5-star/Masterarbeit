---
open_question_id: R2-COMMON-OPQ-001
scope:
  connection: R2
  material: COMMON
status: OPEN
question: >
  Wie ist die genaue Druckzonenlänge/-verteilung am Rahmeneck-Innenknoten
  anzusetzen (rechteckige vs. dreieckige Pressungsverteilung), und wo
  liegt der resultierende Kraftangriffspunkt/Hebelarm?
context: >
  Bestimmt `A_c`, `c_c,90`, `c_c,0` sowie die Lage des
  Druckresultierenden und damit den Hebelarm `z` für das
  Momenten-Rotations-Modell der Druckseite. Ohne diese Geometrie können
  die Druckseiten-Federn `c_c,90`/`c_c,0` und die daraus kombinierte
  Rotationssteifigkeit nicht berechnet werden.
related_sources:
  - wiki/R2/COMMON/literature/R2-COMMON-CLAIM-013.md
  - wiki/R2/COMMON/literature/R2-COMMON-CLAIM-014.md
  - wiki/R2/COMMON/literature/R2-COMMON-CLAIM-018.md
  - wiki/R2/COMMON/literature/R2-COMMON-CLAIM-019.md
  - wiki/R2/COMMON/literature/R2-COMMON-CLAIM-027.md
  - wiki/R2/COMMON/literature/R2-COMMON-CLAIM-028.md
options_considered: >
  Aktuelle Druckverteilungsannahme aus dem Festigkeitsmodell übernehmen,
  oder ein gewähltes Dreiecks-/Rechtecks-Kontaktmodell mit eigener
  Herleitung ansetzen.
date_opened: "2026-09-01"
date_resolved:
resolution:
---

Übernommen aus chat-3, OPEN_QUESTIONS.md Punkt 1, und TASKS.md
("Blocked / needs input — P1 — Compression-zone length"). Diese Frage
blockiert laut TASKS.md direkt die Bearbeitung von `c_c,90`, `c_c,0` und
der finalen Rotationssteifigkeit (siehe auch R2-COMMON-OPQ-006).
Materialunabhängig geführt, da die Druckzonen-Geometrie primär von der
Rahmeneck-Konstruktion, nicht vom Holzwerkstoff abhängt.

**Update (2026-09-01, aus Lippert2002-Literaturauswertung):** Lippert
(2002) liefert für eine (in Geometrie und Material abweichende, aber
konstruktiv ähnliche) Rahmenecke mit eingeklebten Gewindestangen sowohl
eine experimentelle Methodik zur Ermittlung der Druckzonenhöhe aus
Dehnungsmessung/Spaltöffnung (Kapitel 5.6.3, siehe CLAIM-014) als auch
eine rechnerische Herleitung: die reale (näherungsweise quadratische)
Druckspannungsverteilung wird um einen Plastizierungsfaktor 0.7
abgemindert und anschließend flächengleich durch eine DREIECKSFÖRMIGE
Verteilung ersetzt, mit Höhe h_d = 0.4·h_z (h_z = Abstand Zugkraft–
Druckrand), siehe CLAIM-018 (Gl. 6.2). Für die konkreten
Versuchskörper deckt sich dieser theoretische Wert gut mit dem
gemessenen. Zusätzlich zeigt Lippert (CLAIM-014), dass eine
UNVERSTÄRKTE Druckzone eine lastabhängig wachsende ("weiche")
Druckzone aufweist, während eine VERSTÄRKTE Druckzone (z. B. durch
Schlitzblech) eine nahezu konstante Höhe zeigt — sowie vier alternative
Ansätze zur Kraftaufteilung zwischen Kontakt und Verstärkung, falls
beide gleichzeitig wirken (CLAIM-019). Diese Befunde sind NICHT direkt
auf R2 übertragbar (andere Geometrie/Material/Konstruktion, siehe
Einschränkungen in den genannten Claims) und lösen diese offene Frage
daher nicht, liefern aber ein mögliches methodisches Vorbild
(dreiecksförmige Druckzone mit h_d≈0.4·h_z als Ansatz, ggf. anzupassen)
für eine künftige eigenständige Bearbeitung. Status bleibt OPEN.

**Update (2026-09-01, aus Yang/Liu/Ren 2016-Literaturauswertung):**
Yang, Liu und Ren (2016) liefern für einen (in Geometrie, Material und
Konstruktion ebenfalls abweichenden — zusätzlich mit Stahlkastenprofilen
versehenen) Brettschichtholz-Rahmenanschluss mit eingeklebten
Gewindestangen einen ZWEITEN, methodisch unabhängigen Ansatz zur
Druckseite: Querdruck-Tragfähigkeit der Holzstütze über Lastausbreitung
nach Van der Put (2008, Ausbreitungswinkel 45° im elastischen Bereich)
kombiniert mit einer Bearing-width-Erweiterung c nach EN 1993-1-8 (Gl.
6-8, siehe CLAIM-027), sowie eine zugehörige Steifigkeitsformel
k_cc=E_w,90,l·b_c·(2c+a+d_n)/h_c (Gl. 16, siehe CLAIM-028). Bemerkens-
wert: in der dortigen Versuchsauswertung erwies sich GERADE die
Druckseite (k_cc, k_cs, k_srtc) als die für die Gesamt-Anfangs-
drehsteifigkeit MASSGEBENDE (weichste) Komponentengruppe, während die
Zugseite (Gewindestangen, k_grt) praktisch als unendlich steif gilt —
ein qualitativer Hinweis darauf, dass die in dieser offenen Frage
gesuchte Druckzonen-Geometrie/-Steifigkeit für die Gesamt-Rotations-
steifigkeit der Verbindung besonders wichtig sein könnte. Auch dieser
Ansatz ist NICHT direkt auf R2 übertragbar (siehe Einschränkungen in
CLAIM-027/028 und wiki/R2/COMMON/literature/README.md) und löst die
Frage nicht, liefert aber einen zweiten, unabhängigen methodischen
Vergleichspunkt zu Lipperts dreiecksförmigem Ansatz. Status bleibt OPEN.
