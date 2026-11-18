# Organische Synthese & Laborpraxis — Wissensdatenbank & KI-Skill

Dieses private Repository enthält die konsolidierte, verifizierte Wissensdatenbank und das KI-Regelwerk (**Skill: `organische-synthese-und-laborpraxis`**) für **Organische Synthese, Reaktionsmechanismen, Retrosynthese, Stöchiometrie, Reagenzien-Selektivität, Prozesssicherheit und praktische Labor-Aufarbeitung**.

## Inhalt & Struktur

- **[`SKILL.md`](SKILL.md)** — Haupt-Regelwerk für KI-Agenten (Anti-Halluzinations-/Valenz-Gesetze, First-Principles- & Mechanismus-Pflicht nach `MechanismSpec 2.1`, kanonische SMARTS-Muster, physikalische/chemische Prozesssicherheit, Labor-Logik & 8-Punkte-Definition-of-Done).
- **[`references/00_INDEX_UND_KONTROLLLISTE.md`](references/00_INDEX_UND_KONTROLLLISTE.md)** — Vollständiger Kontroll-Index über alle **291 / 291** verlustfrei übertragenen Quellen und Kapitel.
- **[`references/01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md`](references/01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md)** — Mechanismus-Entscheidungsmatrizen ($S_\text{N}1/S_\text{N}2/E1/E2$, $\text{Ad}_\text{E}$, $S_\text{E}\text{Ar}/S_\text{N}\text{Ar}$, Carbonylchemie, Pericyclik), Reagenzien- & Bedingungen-Tabellen, Schutzgruppen-Orthogonalität, $\text{p}K_\text{S}$- und Lösungsmittel-Referenzen.
- **[`references/02_Retrosynthese_und_Namensreaktionen_Katalog.md`](references/02_Retrosynthese_und_Namensreaktionen_Katalog.md)** — Retrosynthetische Disconnection-Systematik ($a^n/d^n$-Synthons, Umpolung, Baldwin-Regeln, Ringgrößen-Strategien), Auswertung der `RXNO`/`MOP`-Ontologie und `ReactionClassifier`-SMIRKS-Taxonomie sowie Namensreaktionen-Katalog.
- **[`references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md`](references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md)** — Reaktionsführung, Kühlbäder, Inertgas-/Schlenk-Technik, Quench- & Workup-Kaskade, Säure-Base-Extraktion, Trocknungsmittel, Umkristallisation, Destillation, DC/Säulenchromatographie (inkl. Färbereagenzien) und Spektroskopie/Analytik.
- **[`references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md`](references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md)** — Verlustfreie Master-Zusammenführung aller Module 1 bis 4.

## Konsolidierte Primärquellen (291 Quellen)

1. **`codex-organic-chem`** — Struktur-Validierung, RDKit/SMARTS-Prüfung, Atom-/Ladungsbilanz, `MechanismSpec 2.1`, Semiempirik (`GFN2-xTB`, Fukui-Indizes, `CREST`).
2. **`scientific-agents`** — Fachspezifische Chemiker-Leitfäden (`organic-chemist`, `process-chemist`, `organometallic-chemist`, `catalysis-scientist`, `analytical-chemist`, `spectroscopist`, `mass-spectrometrist`, `computational-chemist`, `green-chemist`, `separation-processes-engineer`, u. a.).
3. **`scientific-agent-skills`** — Cheminformatik-, Spektroskopie- & Validierungs-Skills (`rdkit`, `datamol`, `nmrglue`, `matchms`, `pyopenms`, `torchdrug`).
4. **`ReactionClassifier`** — Hierarchische Reaktionstaxonomie (10 Superklassen, 62 Level-2-Klassen, SMIRKS-Templates).
5. **`rxno`** — Royal Society of Chemistry Reaction Ontology (`RXNO` & `MOP`).
6. **`libretexts_lab_techniques`** — Lisa Nichols: *Organic Chemistry Lab Techniques* (162 Kapitel, Kapitel 01–07).

## Verwendung in verschiedenen KI-Systemen

Das Repository folgt dem offenen **Agent-Skills-Standard (`SKILL.md` + `references/`)** und enthält direkt in `SKILL.md` (Abschnitt `0. KI-Nutzungsanleitung & Modul-Routing`) eine explizite Steuerungsanleitung für KIs.

| KI-System | Kompatibilität | Einrichtung |
| :--- | :---: | :--- |
| **Antigravity / Gemini CLI** | Direkt nativ | Ordner als `organische-synthese-und-laborpraxis/` unter `~/.gemini/skills/` bzw. `.agents/skills/` ablegen. |
| **Claude Code** | Direkt nativ | Repo/Ordner nach `~/.claude/skills/organische-synthese-und-laborpraxis/` oder `.claude/skills/` kopieren. |
| **OpenAI Codex CLI / Cursor / Windsurf / OpenCode** | Direkt nativ | Repo/Ordner in `.agents/skills/` (oder `.cursor/skills/`) legen. |
| **Claude Projects** | Über Knowledge | [`prompts/WEBCHAT_SYSTEM_PROMPT.md`](prompts/WEBCHAT_SYSTEM_PROMPT.md) in *Project Instructions* kopieren; `SKILL.md` + `references/01`–`03` (oder `KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md`) als *Project Knowledge* hochladen. |
| **ChatGPT (Custom GPT)** | Mit Kompakt-Prompt + Knowledge | **Wichtig:** `SKILL.md` (~49 KB) ist für das 8.000-Zeichen-Feld *Instructions* zu groß. Kopiere stattdessen [`prompts/WEBCHAT_SYSTEM_PROMPT.md`](prompts/WEBCHAT_SYSTEM_PROMPT.md) ins *Instructions*-Feld und lade `SKILL.md` + `references/01`–`03` (oder `KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md`) als *Knowledge*-Dateien hoch. |
| **Gemini Gems / NotebookLM** | Über Wissensdateien | [`prompts/WEBCHAT_SYSTEM_PROMPT.md`](prompts/WEBCHAT_SYSTEM_PROMPT.md) als System-Anweisung nutzen und `SKILL.md` + `references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md` als Quellen anhängen. |

## Validierung

```bash
python3 scripts/validate_kb.py
```
