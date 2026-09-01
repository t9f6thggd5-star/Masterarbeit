# Externer Quellenordner

Originalquellen (Normen, Fachliteratur, Bücher, Zeitschriften, Pläne,
Gutachten, eigene Rohmessdaten) liegen **nicht** in diesem Git-Repository,
sondern in einem separaten Ordner außerhalb davon — z. B. in OneDrive.
Der Grund steht in `CLAUDE.md` Abschnitt 1: diese Dateien können groß
werden, brauchen keine Versionshistorie, und ein separater Ordner
vermeidet Konflikte zwischen Cloud-Sync und Git.

Diese Datei beschreibt nur die **Struktur**, die der externe Ordner haben
muss, damit `bibliography/sources.yaml` und alle Templates konsistent
darauf verweisen können. Die eigentlichen Ordner/Dateien liegen dort, nicht
hier im Repository.

## Struktur

```
<externer Quellenordner>/
├── common/
│   ├── norms/          Normen und Regelwerke (z. B. DIN, Eurocode)
│   ├── literature/      wissenschaftliche Artikel, Konferenzbeiträge, Zeitschriften
│   ├── books/           Fachbücher
│   └── general/         sonstige allgemeine Unterlagen
│
└── R1/ R2/ R3/          (identisch aufgebaut, siehe CLAUDE.md Abschnitt 3)
    ├── COMMON/          Quellen, die für diese Verbindung unabhängig vom
    │                    Material gelten (Pläne, Normen, Literatur) —
    │                    siehe CLAUDE.md Abschnitt 1
    ├── GL24h/
    │   ├── experiments/
    │   │   ├── components/
    │   │   └── full_connection/
    │   └── plans/
    └── GL75/            (gleiche Unterordner)
```

## Regeln

Alle Regeln aus `CLAUDE.md` zu "Sources" gelten unverändert, unabhängig
vom Speicherort: Originalquellen werden nie verändert (Abschnitt 19,
Regel 1), jede Quelle bekommt einen Eintrag in `bibliography/sources.yaml`
mit einer stabilen ID und dem Pfad im externen Ordner, und Claims/Templates
referenzieren immer diese ID — nie einen rohen Dateipfad direkt.

`common/` ist zugleich die Quellenablage für die nicht-verbindungsspezifischen
Kapitel der Arbeit (Einleitung, Grundlagen, Stand der Technik, Methodik
usw., siehe `research/thesis/` und `wiki/thesis/`) — es gibt dafür keine
eigene Kategorie, weil dieselbe Quelle oft in mehreren Kapiteln zitiert
wird (siehe CLAUDE.md Abschnitt 1).

Eine Vorlage mit genau dieser Ordnerstruktur zum Entpacken in deinen
externen Speicherort (z. B. OneDrive) liegt als separates Paket bei.
