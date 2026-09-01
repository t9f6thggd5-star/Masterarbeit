---
scope:
  connection: COMMON
  material: COMMON
source: FprEN-1995-1-1-2024
last_updated: "2026-09-01"
---

# Normstellen-Index: FprEN 1995-1-1:2024

Reine Navigationshilfe, kein eigener Claim und keine eigene fachliche
Aussage — trägt daher bewusst keine eigene ID (analog zu
`current_state.md`, siehe `schema.yaml` Abschnitt "ID naming
convention") und wird nicht von `scripts/build_index.py` katalogisiert.
Zweck: schneller Sprung zur richtigen Seite im Normentwurf, ohne jedes
Mal neu suchen zu müssen. Seitenzahlen beziehen sich auf die konkret
abgelegte PDF-Datei (`common/norms/NA005-04-01-01AK_N3527_CEN-TC_250-
SC_5_N2196_FprEN_1995-1-1_v3f_2024-11-13_Clean.pdf`, Quelle
`FprEN-1995-1-1-2024` in `bibliography/sources.yaml`) — das ist ein
Norm**entwurf** (Formal Enquiry, Stand 2024-11-13), keine final
veröffentlichte EN; Kapitel-/Seitenzahlen können sich in einer späteren
finalen Fassung ändern. Vor Verwendung von Zahlenwerten den Status
prüfen (siehe Hinweis im sources.yaml-Eintrag).

Wird von Claude selbstständig ergänzt, wenn sich beim Nachschlagen
zeigt, dass ein Abschnitt wiederholt gebraucht wird — keine Rückfrage
nötig, da reine Seitenzahl-/Themen-Angaben ohne fachliche Wertung.

## Gesamtgliederung (Inhaltsverzeichnis, PDF-Seitenzahlen)

- 1 Scope — 10
- 2 Normative references — 10
- 3 Terms, definitions and symbols — 10 (3.1 Terms and definitions — 10; 3.2 Symbols and abbreviations — 20)
- 4 Basis of design — 44 (4.4 Stiffness values for structural analysis — 48; 4.5 Verification by the partial factor method — 51)
- 5 Materials — 53 (5.1 Strength and stiffness properties — 53; 5.2 Modification factors for service classes and load-duration — 57; 5.3 Modification factors for size effects — 60; 5.4 Specific material properties — 61; 5.5 Shrinkage and swelling values — 62)
- 6 Durability — 64
- 7 Structural analysis — 71
- 8 Ultimate limit states — 84 (8.1 Member resistance verification — 84; 8.2 Member buckling verification — 101; 8.3 Additional provisions for members with special geometries — 106; 8.4 Beams with composite cross-section — 132; 8.5 System strength — 137)
- 9 Serviceability limit states — 138 (9.2 Deformations — 138; 9.3 Vibrations — 141; 9.4 Compressive deformation perpendicular to grain — 152)
- 10 Fatigue — 153
- 11 Connections — 156 (11.1 General — 156; 11.2 Resistance of a single dowel-type fastener — 158; 11.3 Connection design with dowel-type fasteners — 179; 11.4 Spacings, edge and end distances — 196; 11.5 Brittle failure modes of connections with dowel-type fasteners loaded parallel to grain — 205; 11.6 Brittle failure of connections loaded perpendicular to grain — 214; 11.7 Shear connectors — 219; 11.8 Punched metal plate fasteners — 226; 11.9 Expanded tube fasteners — 226; 11.10 Bonded-in rods — 226; 11.11 Carpentry connections — 234)
- 12 Diaphragms — 243
- 13 Timber foundation piles — 269
- Annex A (informative) Additional guidance to Basis of design — 270
- Annex B (informative) Additional information to Structural Analysis — 273
- Annex C (normative) Additional provisions to Ultimate Limit States (u. a. CLT, Laminated timber decks) — 312
- Annex D (informative) Additional information to Ultimate Limit States (u. a. Built-up columns) — 327
- Annex E (informative) Additional information to Serviceability Limit States (u. a. Schwingungen) — 335
- Annex F (normative) Additional provisions to Connections (Stahlblech-Nagelplatten PMPF, Zwischenlagen) — 341
- Annex G (informative) Additional information to Connections (3D-Verbinder, Expanded tube fasteners) — 369
- Annex H (informative) Additional information to Diaphragms — 381
- Annex I (informative) Timber Foundation Piles — 396
- Annex M (normative) Material and product properties for design — 407
- Annex N (informative) Additional information on material and product properties — 422
- Bibliography — 430

## Vertiefter Index: bisher für R1/R2/R3 konkret nachgeschlagene Abschnitte

Nur Abschnitte, deren Inhalt in diesem Projekt tatsächlich per
Volltextsuche im PDF verifiziert wurde (nicht aus dem Gedächtnis
übernommen). Wird laufend ergänzt.

| Abschnitt | Seite | Thema | Verwendet in |
|---|---|---|---|
| Table 5.1 | ~51–53 | Produkt-/Werkstoffklassifikation (u. a. GL als Teilgruppe von PL, PL Teilgruppe von SWB) | R2-GL24h-DEC-003 (SWB-Klassifikation) |
| 8.1.6.1 | 85–89 | Querdrucktragfähigkeit, allgemein (Gl. 8.5–8.11, Tab. 8.1 k_mat, Tab. 8.2 Ausbreitungswinkel α) | R2-GL24h-CALC-005/010 |
| 8.1.6.2 | 90–93 | Querdrucktragfähigkeit, Verstärkung (Gl. 8.12–8.16, k_mat=1,75-Fall nach 8.1.6.2(6)) | R2-GL24h-CALC-006/011 |
| 9.4 | 152 | Verformungsmodell Querdruck (Gl. 9.31) | bisher nur diskutiert, kein CALC-Eintrag |
| 11.2.3.2 | 170–171 | Johansen-Traglast/Versagensmoden Stiftverbindungsmittel, detailliert (Gl. 11.14/11.15) | R2-COMMON-OPQ-008 (Klärung "Stütze auf Zug"-Block) |
| 11.2.3.3 | 171–172 | Vereinfachtes Verfahren Dübelwirkung (Gl. 11.16–11.18, Tab. 11.4) | — |
| 11.2.3.4 | 172 | Holzdübel-Verbindungen | — |
| 11.2.3.7 | 177 | Dübelwirkung bei mehreren Scherfugen; Tab. 11.7 (charakteristisches Fließmoment) | — |
| 11.5.2–11.5.3 | 207–208 | Sprödbruch, Vereinfachung/Bemessungswiderstand (Gl. 11.36–11.39) | R2-COMMON-OPQ-008 (ursprüngliche, inzwischen widerlegte Vermutung) |
| 11.10.5.1–11.10.5.2 | 231–232 | Eingeklebte Stangen: Verankerungs-/Holzzugtragfähigkeit (Gl. 11.89–11.92, Fig. 11.38 A_ef) | R2-COMMON-OPQ-008 |
| 11.10.6 | 233 | Eingeklebte Stangen, Querlast (Gl. 11.93) | — |

## Noch nicht nachgeschlagene, aber vermutlich relevante Abschnitte

Nicht verifiziert — nur aus der Gesamtgliederung abgeleitete Vermutung,
welche Kapitel für R1 (Schlitzblech/Stabdübel) und R3
(Außenlaschen/Stabdübel) relevant werden könnten: 11.3 (Connection
design with dowel-type fasteners, S.179), 11.4 (Spacings/edge/end
distances, S.196), 11.7 (Shear connectors, S.219), Annex F.3
(Punched metal plate fasteners, S.341, falls für R1/R3 relevant).
