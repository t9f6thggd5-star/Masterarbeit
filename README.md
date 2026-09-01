# Master Thesis Research Wiki

Forschungswissensbasis für eine Masterarbeit zu drei biegesteifen
Holzrahmenecken (R1, R2, R3), jeweils untersucht mit den Materialien
GL24h und GL75. Aufgebaut auf dem Konzept von
[le0nce/LLM-Wiki](https://github.com/le0nce/LLM-Wiki), aber als
eigenständiges Repository mit einer für wissenschaftliches Arbeiten
erweiterten Datenstruktur.

## Zwei Speicherorte

Dieses Projekt besteht bewusst aus zwei getrennten Orten:

1. **Dieses Git-Repository** — Text/YAML: `CLAUDE.md`, `schema.yaml`,
   `research/`, `wiki/`, `bibliography/`, `templates/`. Klein, versioniert,
   jede Änderung nachvollziehbar per Commit-Historie.
2. **Ein externer Quellenordner außerhalb dieses Repositories** (z. B. in
   OneDrive) — die Originalquellen selbst: Normen, Fachliteratur, Bücher,
   Pläne, eigene Rohmessdaten. Siehe [`EXTERNAL_SOURCES.md`](./EXTERNAL_SOURCES.md)
   für die genaue Struktur; eine passende Ordnervorlage zum Entpacken in
   deinen externen Speicherort liegt als separates Paket bei.

Der Grund für die Trennung: Rohdaten können groß werden (Git hat
Dateigrößenlimits) und brauchen keine Versionshistorie; ein separater
Ordner vermeidet außerdem Konflikte zwischen Cloud-Sync (OneDrive) und
Git, wenn beide denselben Ordner verwalten wollen.

## Grundidee

Quellen werden **unverändert** im externen Quellenordner abgelegt. Claude
verdichtet daraus eine verlinkte Wissensbasis in `wiki/`. Der eigene
Forschungsprozess (Verarbeitung, Berechnungen, Annahmen, Interpretationen,
Schlussfolgerungen) liegt getrennt davon in `research/`. Jede Aussage im
Wiki muss auf eine Quelle (per ID aus `bibliography/sources.yaml`) oder
einen `research/`-Eintrag zurückführen — eine Quelle wird nicht automatisch
als Fakt behandelt, sondern eingeordnet (normativ, Quellenbehauptung,
empirische Evidenz oder eigene Synthese).

Die vollständigen Regeln für Claude stehen in [`CLAUDE.md`](./CLAUDE.md),
das kontrollierte Vokabular (erlaubte Typen/Status-Werte, ID-Schema) in
[`schema.yaml`](./schema.yaml).

## Struktur (dieses Git-Repository)

```
master-thesis-research-wiki/
├── CLAUDE.md              Regeln für Claude (wissenschaftliche Strenge)
├── EXTERNAL_SOURCES.md    Struktur des externen Quellenordners
├── schema.yaml            kontrolliertes Vokabular / ID-Schema
├── README.md              diese Datei
├── .gitignore
│
├── research/              aktueller Forschungsstand (kein Quellenmaterial)
│   ├── common/            Methodik, Annahmen, Entscheidungen, offene Fragen
│   ├── thesis/            Abstract, Einleitung, Grundlagen, Stand der
│                          Technik, Methodik, Diskussion, Grenzen der
│                          Arbeit, Schluss, Ausblick, general
│   └── R1/ R2/ R3/        je GL24h/ und GL75/, je experiment_processing/,
│                          experimental_results/, calculations/,
│                          assumptions/, hypotheses/, interpretations/,
│                          conclusions/, decisions/, open_questions/,
│                          current_state.md
│
├── wiki/                  verlinkte Wissensbasis (Claude-Output)
│   ├── common/            normative_basis/, concepts/, methods/, literature/
│   ├── thesis/            verdichtetes Wissen: Abstract, Einleitung,
│                          Grundlagen, Stand der Technik, Methodik,
│                          Diskussion, Grenzen der Arbeit, Schluss,
│                          Ausblick, general
│   ├── R1/ R2/ R3/        je GL24h/ und GL75/, je experiments/,
│                          calculations/, assumptions/, results/
│   └── cross_connection/  einziger Ort für Vergleiche zwischen R1/R2/R3
│                          bzw. GL24h/GL75
│
├── bibliography/          sources.yaml (Quellenverzeichnis) + references.bib
├── templates/             Vorlagen für alle Eintragstypen (siehe dort)
├── scripts/               build_index.py, lint.py — siehe _index/README.md
└── _index/                automatisch erzeugter Katalog + Lint-Report
                           (catalog.yaml, INDEX.md, lint_report.md — nie
                           von Hand bearbeiten, siehe _index/README.md)
```

Der externe Quellenordner (nicht Teil dieses Repositories) ist separat in
[`EXTERNAL_SOURCES.md`](./EXTERNAL_SOURCES.md) beschrieben.

**Wichtigste Regeln:** R1, R2 und R3 sind strukturell und epistemisch
gleichwertig — keine Verbindung und kein Material gilt als Standardfall
oder Default (CLAUDE.md Abschnitt 3). `common/` (im externen Quellenordner
wie auch in `research/`/`wiki/`) ist technisches Wissen, das für alle drei
Verbindungen gilt, und ist zugleich die einzige Quellenablage für die
Rahmenkapitel — eine Quelle wird nicht nach Zielkapitel sortiert, da
dieselbe Quelle oft in mehreren Kapiteln zitiert wird. `thesis/` (nur unter
`research/` und `wiki/`) ist die eigentliche kapitelspezifische Synthese
der Rahmenkapitel und damit weder verbindungsspezifisch noch technischer
Vergleich zwischen den Verbindungen (das bleibt `cross_connection/`
vorbehalten). Claude-Vorschläge für Interpretationen, Schlussfolgerungen
und Hypothesen werden als `CLAUDE_DRAFT` markiert und gelten erst nach
deiner Bestätigung (`reviewed: true`) als geprüft (CLAUDE.md Abschnitt 14).

## Workflow

1. Quelle in den passenden Ordner im externen Quellenordner legen
   (unverändert).
2. Eintrag in `bibliography/sources.yaml` (und ggf. `references.bib`)
   anlegen — Pfad zeigt auf den externen Speicherort.
3. Mit Claude über die Quelle sprechen — Claude verdichtet relevante
   Aussagen als strukturierte Claims/Konzepte nach `templates/claim.md` in
   `wiki/`.
4. Eigene Versuche/Berechnungen als `research/`-Einträge nach den
   passenden Templates anlegen (Rohmessung → Verarbeitung → Ergebnis →
   Interpretation → Schlussfolgerung, siehe CLAUDE.md Abschnitt 7).
5. Fragen an Claude stellen, die sich klar auf einen Scope beziehen, z. B.:
   - „Welche unterschiedlichen Positionen gibt es in der Literatur zu X?“
   - „Welche dieser Aussagen sind normativ, welche empirisch?“
   - „Welche Studien widersprechen sich, und warum könnte das sein?“
   - „Vergleiche R1 und R2 hinsichtlich Y“ (nur explizit, siehe
     `wiki/cross_connection/`).
6. Die eigentliche Masterarbeit wird **aus** dieser Recherche geschrieben,
   nicht automatisch aus dem Wiki generiert — das Wiki ist
   Recherche-Werkzeug, nicht wissenschaftliche Quelle.

## Nutzung mit GitHub Desktop

1. Eigenen GitHub-Account verwenden (kein Fork von `le0nce/LLM-Wiki`).
2. Mit GitHub Desktop ein neues, leeres Repository lokal anlegen.
3. Inhalt dieses Pakets (ohne den externen Quellenordner) in den lokalen
   Repository-Ordner entpacken.
4. In GitHub Desktop committen ("Initial master thesis research wiki
   structure").
5. Über „Publish repository“ **privat** veröffentlichen.
6. Einmalig pro Klon/Rechner den mitgelieferten Pre-Commit-Hook aktivieren
   (regeneriert `_index/` und lässt den Lint vor jedem Commit laufen,
   siehe `_index/README.md`):
   ```
   git config core.hooksPath .githooks
   ```
   Das lässt sich z. B. über „Repository → Open in Command Prompt/Terminal“
   in GitHub Desktop einmalig ausführen.

Die Ordnervorlage für den externen Quellenordner separat an einen Ort
außerhalb des Git-Repository-Ordners entpacken (z. B. in OneDrive).

Noch keine echten Normen/Versuchsdaten einpflegen, bevor nicht geklärt
ist, was aus urheberrechtlichen bzw. Vertraulichkeitsgründen überhaupt
gespeichert werden darf.
