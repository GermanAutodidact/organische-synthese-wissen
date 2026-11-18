# Changelog

Alle wesentlichen Änderungen an `organische-synthese-und-laborpraxis` (`organische-synthese-wissen`) werden hier dokumentiert.

## [2.3-DE] – 2026-11-18

### Fachliche Korrekturen & Skript-Fixes (P1)
- **Kanonische SMARTS (`SKILL.md` 2.4 & `scripts/chem_check.py`):** Boronsäure-SMARTS von `B(O)O` (traf fälschlich Boronsäureester) auf `[BX3]([OX2H1])[OX2H1]` korrigiert; `Primäres Amin` um `$(N-[#6])` zur Abgrenzung von Ammoniak/Hydrazin geschärft.
- **Valenz-/Duplett-Check (`scripts/chem_check.py`):** `compute_lone_pairs()` weist jetzt 4-Elektronen-Wasserstoff (`H`, `Q=-2`, `V=1`) sowie negative Valenz-/Radikalwerte zuverlässig ab (inkl. neuer `--self-test`-Regressionen).

### Handbuch, Navigation & Validator (P2–P4)
- **Handbuch-Generator (`scripts/build_handbook.py`):** Entfernt YAML-Frontmatter aus eingebetteten Modulen (kein rohes YAML mehr in Modul 0) und erzeugt klickbare `#mod-*`-Anker + exakte Zeilenbereiche im `Gesamt-Inhaltsverzeichnis`.
- **Quellenhinweise & Typo:** Einheitliche Upstream-Quellenhinweise am Anfang von Modul `01`, `02` und `02b` ergänzt; Überschriften-Typo in `02` (`1.5 Die 6 Goldenen…`) behoben.
- **Cross-Platform & Navigation (`SKILL.md`):** Negativ-Trigger (`Don't use for…`) im Frontmatter und Inhaltsverzeichnis mit Zeilen-Index ergänzt.
- **Validator-Härtung (`scripts/validate_kb.py`):** Dynamische Versionserkennung, exakte TOC-Zeilenindex-Prüfung, Prüfung relativer Markdown-Links/`#Anker`, ungeschlossener Codeblöcke, Trailing Whitespace, Handbuch-Frontmatter-Schutz und `evals/cases.json`-Modulvalidierung.

## [2.2-DE] – 2026-11-18

### Fachliche Korrekturen (P1)
- **Kühlbad-Tabelle (`references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md`):** Physikalisch unmögliche Trockeneis-Einträge unterhalb von $-78{,}5\,^\circ\text{C}$ korrigiert:
  - Ethylacetat ($-84\,^\circ\text{C}$), $n$-Hexan ($-94\text{ bis }-95\,^\circ\text{C}$) und Methanol ($-98\,^\circ\text{C}$) explizit als **Slush-Bäder mit flüssigem Stickstoff ($\text{N}_2\text{(fl.)}$)** klassifiziert.
  - Methanol + Trockeneis korrekt mit **$-72\,^\circ\text{C}$** als separaten Eintrag ergänzt.
- **Baldwin-Regeln (`references/02_Retrosynthese_und_Namensreaktionen_Katalog.md`):**
  - `endo-tet`-Spalte an Baldwin (1976) angepasst: 5-`endo-tet` und 6-`endo-tet` als disfavorisiert/verboten belassen; 3-, 4- und 7-`endo-tet` korrekt als nicht klassifiziert / Grenzfall gekennzeichnet.
  - Hinweis 4 (4,5-Epoxyalkohol-Öffnung) widerspruchsfrei formuliert (`5-exo-tet` zu THF vs. konventionell `6-endo-tet` zu THP inkl. Nicolaou-Regel).
- **Hypervalente Hauptgruppenelemente (`SKILL.md` 1.2):** $\text{S(IV)}$, $\text{S(VI)}$ und $\text{P(V)}$ aus dem Unterpunkt „Halogene“ in einen eigenen Unterpunkt verschoben.

### Neue Werkzeuge & Struktur (P2–P4)
- **Neues Prüfskript `scripts/chem_check.py`:** Pure-Python-Rechner für freie Elektronenpaare ($N_\text{LP}$ inkl. Periode-2-Oktettprüfung) sowie RDKit-gestützte CLI für `sanitize`, `balance` (inkl. `GetTotalNumHs()` & 2-Varianten-Check) und kanonische `smarts`.
- **Tool-Verweise bereinigt (`SKILL.md`):** Verweise auf externe Quellmodule (`mechanism_semantics.py`, `reaction.py`, `chem_normalize_structure` usw.) auf `scripts/chem_check.py` bzw. „falls in Laufzeitumgebung verfügbar“ präzisiert.
- **Modul 02 gesplittet:** Lange `ReactionClassifier`-SMIRKS-Matrizen sowie 84 `MOP`- und 658 `RXNO`-Einträge verlustfrei nach `references/02b_Ontologie_RXNO_MOP_und_ReactionClassifier.md` ausgelagert (`02` schrumpft von 335 KB auf 118 KB).
- **Inhaltsverzeichnisse & Zeilen-Indizes:** Anchored TOCs mit exakten Zeilenbereichen in `00`, `01`, `02`, `02b` und `03` ergänzt.
- **Deterministischer Handbuch-Generator (`scripts/build_handbook.py`):** `KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md` wird automatisch aus den Quelldateien erzeugt und per `--check` in der CI synchron gehalten.
- **Cross-Platform & Sicherheit:** Zweisprachige DE/EN-`description` ($\le 1024$ Zeichen) in `SKILL.md`, Dual-Use-/Ethik-Schranke und SDB/Abzug/PSA-Pflicht in `SKILL.md` & `prompts/WEBCHAT_SYSTEM_PROMPT.md`.
- **Qualitätssicherung & Recht:** Erweiterter CI-Validator (`scripts/validate_kb.py`), 12 Evaluation-Cases (`evals/cases.json`), `LICENSE` (`CC BY-NC-SA 4.0`), `NOTICE.md` und Formatierungskorrekturen (fehlende Leerzeichen).

## [2.1-DE] – 2026-11-18
- Abschnitt `0. KI-Nutzungsanleitung & Modul-Routing` in `SKILL.md` ergänzt.
- `prompts/WEBCHAT_SYSTEM_PROMPT.md` (<5.000 Zeichen) und Multi-Plattform-Tabelle in `README.md` hinzugefügt.

## [2.0-DE] – 2026-11-18
- Initialer GitHub-Export der konsolidierten 291-Quellen-Wissensdatenbank (`SKILL.md`, Module `00`–`03`, Handbuch, `scripts/validate_kb.py`, CI-Workflow).
