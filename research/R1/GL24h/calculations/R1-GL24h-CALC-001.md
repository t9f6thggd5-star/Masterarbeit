---
calculation_id: R1-GL24h-CALC-001
scope:
  connection: R1
  material: GL24h
type: CALCULATION
inputs:
  normative_sources: FprEN-1995-1-1-2024
  literature:
  experimental_data:
  assumptions:
method: >
  Johansen-Tragfähigkeit je Scherfuge für den zweischnittigen
  Stabdübelanschluss (d=12mm, Holz-Seitenteil t_h,1=72mm GL24h,
  Stahl-Mittelteil mit wirksamer Einbindetiefe t_h,2=6mm — halbe
  Blechdicke, siehe R1-GL24h-DEC-003), Modi (a),(b),(d),(f) gemäß
  R1-GL24h-DEC-002, mit dem normativen Fließmoment M_y,k nach
  FprEN Tab. 11.7(2). Bauteilnummerierung gemäß R1-GL24h-DEC-003.
equations: >
  FprEN 1995-1-1:2024, Gl. 11.14 (Modi a,b,d,f); Gl. 11.15 (Beiwert β);
  Tab. 11.6 (28)-(30) (f_h,1,k, f_h,2,k, k_90, k_mat); Tab. 11.10 (6)
  (effektive Anzahl n_ef)
result:
  quantity: Governierende Johansen-Tragfähigkeit je Scherfuge (Modus f, normatives M_y,k)
  value: 11.247
  unit: kN
  original_value:
  original_unit:
source_file: >
  R1/COMMON/calculations/20260208_Berechnung_Rahmenecke_SB+SD.xlsx, Sheet
  "Rahmenecke GL24h SD", Zellen C36-C56 (per openpyxl mit data_only=True
  ausgelesen, Stand der abgelegten Datei am 2026-09-01)
certainty: CALCULATED
superseded_by:
---

Übernommen aus chat-2, KNOWLEDGE.md ("FprEN double-shear Johansen
interpretation") und unabhängig gegen die reale Excel-Datei verifiziert.

**Eingangswerte** (Zelle → Wert, laut Excel-Spalte "Norm"):
- M_y,k = 69070.88 Nmm (C36, FprEN Tab. 11.7(2))
- f_h,1,k = 30.3072 N/mm² (C39, FprEN Tab. 11.6(28))
- f_h,2,k = 600 N/mm² (C40, FprEN Tab. 11.6(28))
- k_90 = 1.53 (C41, FprEN Tab. 11.6(30) - PL)
- k_mat = 1 (C43, FprEN Tab. 11.6(29) - PL)
- β = 19.797 (C44, FprEN Gl. 11.15)
- n_ef = 5.4989 (C45/C47, FprEN Tab. 11.10(6)) — siehe auch
  R1-GL24h-OPQ-007 zur Unsicherheit der Materialklassifikation

**Ergebnisse je Modus** (kN): a = 26.185 (C49), b = 43.2 (C50),
d = 12.589 (C51), f = 11.247 (C52/C55, governierend, "Versagensmodus" C56).

**Historischer Hinweis zu einer abweichenden Lochleibungsfestigkeit:**
chat-2 (KNOWLEDGE.md §6) verwendet an anderer Stelle eine ältere
EC5-Formel f_{h,0,k}=0.082(1-0.01d)ρ_k mit ρ_k=385 kg/m³, was
f_{h,0,k}≈27.78 N/mm² ergibt. Dieser Wert wird in der aktuellen
Excel-Berechnung nicht verwendet — dort wird stattdessen der tabellierte
FprEN-2024-Wert f_h,1,k=30.3072 N/mm² (Tab. 11.6(28)) angesetzt, der hier
als maßgeblich übernommen wird. Der ältere Wert wird nicht als eigener
Eintrag geführt, da er im Ursprungsmaterial selbst als vorläufig markiert
war und durch den tabellierten Wert ersetzt wurde.

**Offener Punkt zur Gesamttragfähigkeit:** Wie diese
Scherfugen-Tragfähigkeit zur Gesamttragfähigkeit der Dübelgruppe
hochgerechnet wird (Faktor "2" für die Scherfugen), ist Gegenstand von
R1-GL24h-DEC-004 und R1-GL24h-OPQ-006 — siehe R1-GL24h-CALC-003 für die
in der Excel-Datei ausgewiesene Gesamttragfähigkeit.
