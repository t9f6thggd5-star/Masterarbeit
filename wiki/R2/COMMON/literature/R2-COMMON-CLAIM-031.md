---
claim_id: R2-COMMON-CLAIM-031
scope:
  connection: R2
  material: COMMON
claim:
  text: >
    Detaillierte Komponentenstruktur des in CLAIM-001 genannten
    Sechs-Feder-Modells (Fig. 7, "Proposed modeling of extended column
    (left) and extended beam (right) semirigid moment connections with
    the component method"): Zugpfad = zwei parallele Zweige (je
    Gewindestange), jeder Zweig in Serie aus vier Komponenten (von
    "Boden" Richtung Anschlussebene): `c_t` (Bolt/Stange in Zug, Stahl),
    `c_t,ep` (Kopfplatte/"end plate" auf Biegung, Stahl), `c_c,90`
    (Holz, Querdruck), `c_ax,f,par` (stiftförmiges Verbindungsmittel
    parallel zur Faser, axial beansprucht — Verankerung/Ausziehen der
    Stange im Holz). Die beiden Stangenzweige vereinigen sich zu einem
    Knoten, von dort in Serie `c_v` (Holz, Schub) zum Zugkraft-Knoten
    T. Druckpfad = EIN Zweig, in Serie aus nur zwei Komponenten:
    `c_c,90` (Holz, Querdruck) und `c_c,0` (Holz, Druck parallel zur
    Faser) zum Druckkraft-Knoten C — kein Stahl-/Stangenanteil, kein
    `c_v`-Anteil auf der Druckseite. T und C sind über einen starren
    Balken mit Hebelarm `z` und Rotationswinkel `φ` verbunden (klassische
    Bauteilmethode/Komponentenmethode-Topologie, analog EN 1993-1-8).
  source: FragiacomoBatchelar2012a
  pages: "795 (Fig. 7)"
  source_type: LITERATURE
  certainty: SOURCE_CLAIM
contradicted_by:
---

Vom Nutzer als Bilddatei (Federmodell-Diagramm, Fig. 7 aus
FragiacomoBatchelar2012a) im Chat vom 2026-09-17 geteilt, zur Klärung
der Frage, ob die Schubfeld-Komponente `c_v` (siehe R2-GL24h-CALC-003,
R2-COMMON-ASS-003) nur am Zugpfad oder auch am Druckpfad wirkt. Das
Diagramm zeigt eindeutig: `c_v` sitzt ausschließlich im Zugpfad (in
Serie mit den beiden parallelen Stangenzweigen), nicht im Druckpfad.
Der Druckpfad besteht nur aus den zwei Holzkomponenten `c_c,90` und
`c_c,0` in Serie — strukturell identisch zu dem in dieser Arbeit
bereits unabhängig hergeleiteten Ansatz (siehe R2-GL24h-CALC-019).

Ergänzt/konkretisiert CLAIM-001 (die dort nur die Existenz und den
allgemeinen Zweck der Fig.-7-Topologie referenziert, nicht deren
genaue Verschaltung). Bestätigt außerdem die schon in CLAIM-003
formulierte Vermutung, dass die Druckseite (zumindest im "tensioned"-
Fall) primär von `c_c,90` dominiert wird — die Quelle selbst liefert
laut CLAIM-001 aber keine konkreten Steifigkeitswerte für die
einzelnen Federn, nur die Topologie.

**Wichtiger Vorbehalt (wie bei CLAIM-001/002/003):** Geometrie und
Material dieser Quelle (315×90mm, GL10 Radiata Pine, 2×Ø12mm) weichen
deutlich von R2 (GL24h/GL75, h=800mm, ASSY-Verstärkung) ab — die
Topologie (WAS in Serie/parallel zu WAS steht) ist als strukturelles
Vorbild übernehmbar, die konkreten Steifigkeitswerte NICHT.
