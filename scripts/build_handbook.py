#!/usr/bin/env python3
"""Generiert references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md deterministisch aus SKILL.md + Modulen 01–03.

Nutzung:
  python3 scripts/build_handbook.py          # Schreibt das Gesamthandbuch neu
  python3 scripts/build_handbook.py --check  # Prueft Synchronitaet ohne Schreiben (Exit 1 bei Abweichung)
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HANDBUCH_PATH = ROOT / "references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md"

MODULES: list[tuple[str, str, str]] = [
    (
        "MODUL 0: KI-HAUPTREGELWERK (`SKILL.md`)",
        "SKILL.md",
        "SKILL.md",
    ),
    (
        "MODUL 1: REAKTIONSMECHANISMEN, REAGENZIEN & SELEKTIVITÄT",
        "01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md",
        "references/01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md",
    ),
    (
        "MODUL 2: RETROSYNTHESE & NAMENSREAKTIONEN-KATALOG",
        "02_Retrosynthese_und_Namensreaktionen_Katalog.md",
        "references/02_Retrosynthese_und_Namensreaktionen_Katalog.md",
    ),
    (
        "MODUL 2b: ONTOLOGIE-REGISTER (`RXNO`/`MOP`) & `ReactionClassifier`-SMIRKS",
        "02b_Ontologie_RXNO_MOP_und_ReactionClassifier.md",
        "references/02b_Ontologie_RXNO_MOP_und_ReactionClassifier.md",
    ),
    (
        "MODUL 3: LABORPRAXIS, AUFARBEITUNG (`WORKUP`), TRENNUNG & ANALYTIK",
        "03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md",
        "references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md",
    ),
]


def _clean_module_text(raw: str) -> str:
    text = re.sub(r"<!-- TOC_START -->.*?<!-- TOC_END -->\n*", "", raw, flags=re.S)
    text = re.sub(r'^<a id="sec-[^"]+"></a>\n', "", text, flags=re.M)
    return text.strip()


def render_handbook() -> str:
    header = (
        "# KOMPLETTES HANDBUCH ORGANISCHE SYNTHESE, REAKTIONSMECHANISMEN, RETROSYNTHESE & LABORPRAXIS\n\n"
        "> **Hinweis (Automatisch generiert):** Dieses Master-Kompendium wird deterministisch durch `scripts/build_handbook.py` aus `SKILL.md` und den Modulen `01`, `02`, `02b`, `03` erzeugt. Änderungen **immer in den Quelldateien** vornehmen und anschließend `python3 scripts/build_handbook.py` ausführen.\n"
        "> **Kontext-Warnung für Agenten:** Diese Datei ist >650 KB groß — **nicht** pauschal komplett laden, sondern nur für Volltextsuchen oder Web-Chats mit einem einzelnen Upload-Slot verwenden.\n"
        "> **Quellenbasis:** `codex-organic-chem`, `scientific-agents`, `scientific-agent-skills`, `rsc-ontology/rxno` (inkl. `mop.obo`), `schwallergroup/ReactionClassifier` sowie *Organic Chemistry Lab Techniques* (Lisa Nichols, Chemistry LibreTexts, 162 Kapitel).\n\n"
        "---\n\n"
        "## Gesamt-Inhaltsverzeichnis\n\n"
        "1. **MODUL 0 (`SKILL.md`):** KI-Nutzungsanleitung, Ethik-Schranke, Anti-Halluzinations- & Valenz-Gesetz, Mechanismus-Pflicht (MechanismSpec 2.1), Prozesssicherheit & Labor-Logik\n"
        "2. **MODUL 1 (`01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md`):** Mechanismus-Entscheidungsmatrizen ($S_\\text{N}1/S_\\text{N}2/E1/E2/\\text{E1cb}$, $\\text{Ad}_\\text{E}$, $S_\\text{E}\\text{Ar}/S_\\text{N}\\text{Ar}$, Carbonyl/Enolat, Pericyclik), Reagenzien-Tabellen, Schutzgruppen & Orthogonalität, $\\text{p}K_\\text{S}$- & Lösungsmittel-Referenz\n"
        "3. **MODUL 2 (`02_Retrosynthese_und_Namensreaktionen_Katalog.md`):** Retrosynthetische Systematik (Synthons $a^n/d^n$, Umpolung, 1,1–1,6-Disconnections, Baldwin-Regeln), Katalog der Organischen Namensreaktionen\n"
        "4. **MODUL 2b (`02b_Ontologie_RXNO_MOP_und_ReactionClassifier.md`):** Vollständige Granularitäts-SMIRKS-Matrizen (`ReactionClassifier`), 84 `MOP`-Prozesse & 658 aktive `RXNO`-Reaktionsklassen\n"
        "5. **MODUL 3 (`03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md`):** Apparatur- & Schutzgastechnik, Kühlbäder, Quench-Kaskade, Säure-Base-Extraktion, Emulsionen & Trocknungsmittel, Umkristallisation, Destillation & Chromatographie (inkl. DC-Färberezepte), Nasschemische Tests, IR, NMR/`nmrglue`, MS/`matchms`/`pyOpenMS`, ICH-Validierung & Organometall-/Photoredox-/Elektrochemie\n\n"
        "---\n\n"
    )

    chunks: list[str] = [header]
    for title, src_name, rel_path in MODULES:
        src_text = _clean_module_text((ROOT / rel_path).read_text(encoding="utf-8"))
        chunks.append(
            "<!-- ====================================================================== -->\n"
            f"# {title}\n"
            f"<!-- Quelle: {src_name} -->\n\n"
            f"{src_text}\n\n"
        )
    return "".join(chunks).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Erzeugt oder prueft KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md")
    parser.add_argument("--check", action="store_true", help="Prueft Synchronitaet ohne zu schreiben")
    args = parser.parse_args()

    rendered = render_handbook()
    if args.check:
        if not HANDBUCH_PATH.is_file():
            print(f"FEHLER: {HANDBUCH_PATH} existiert nicht.", file=sys.stderr)
            return 1
        current = HANDBUCH_PATH.read_text(encoding="utf-8")
        if current != rendered:
            print(
                "FEHLER: KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md ist nicht synchron mit den Modulen. "
                "Bitte 'python3 scripts/build_handbook.py' ausfuehren.",
                file=sys.stderr,
            )
            return 1
        print("OK: KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md ist 100% synchron mit SKILL.md + Modulen 01–03.")
        return 0

    HANDBUCH_PATH.write_text(rendered, encoding="utf-8")
    print(f"OK: {HANDBUCH_PATH.name} aktualisiert ({len(rendered)} Zeichen, {len(rendered.splitlines())} Zeilen).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
