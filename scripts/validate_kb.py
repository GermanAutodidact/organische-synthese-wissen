#!/usr/bin/env python3
"""Validiert die Struktur und Vollständigkeit des organische-synthese-wissen Repositories."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def parse_frontmatter(skill_md: pathlib.Path) -> tuple[dict[str, object], str]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md muss mit YAML-Frontmatter ('---') beginnen.")
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        raise ValueError("Schließendes '---' im YAML-Frontmatter fehlt.")
    fm_block = text[4:end_idx]
    body = text[end_idx + 5 :]

    data: dict[str, object] = {}
    current_list_key: str | None = None
    for line in fm_block.splitlines():
        if not line.strip():
            continue
        if re.match(r"^\s+-\s+", line) and current_list_key is not None:
            item = re.sub(r"^\s+-\s+", "", line).strip()
            cast_list = data[current_list_key]
            assert isinstance(cast_list, list)
            cast_list.append(item)
            continue
        current_list_key = None
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val == "":
                data[key] = []
                current_list_key = key
            else:
                data[key] = val
    return data, body


def main() -> int:
    skill_md = ROOT / "SKILL.md"
    if not skill_md.is_file():
        print("FEHLER: SKILL.md fehlt.", file=sys.stderr)
        return 1

    fm, body = parse_frontmatter(skill_md)
    for required in ("name", "description"):
        if required not in fm or not fm[required]:
            print(f"FEHLER: Pflichtfeld '{required}' fehlt im Frontmatter.", file=sys.stderr)
            return 1

    if len(body.strip()) < 1000:
        print("FEHLER: SKILL.md Body ist unerwartet kurz.", file=sys.stderr)
        return 1

    expected_refs = [
        "references/00_INDEX_UND_KONTROLLLISTE.md",
        "references/01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md",
        "references/02_Retrosynthese_und_Namensreaktionen_Katalog.md",
        "references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md",
        "references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md",
    ]
    for rel_path in expected_refs:
        target = ROOT / rel_path
        if not target.is_file():
            print(f"FEHLER: Referenzdatei fehlt: {rel_path}", file=sys.stderr)
            return 1
        content = target.read_text(encoding="utf-8")
        if not content.strip():
            print(f"FEHLER: Referenzdatei ist leer: {rel_path}", file=sys.stderr)
            return 1
        if not re.search(r"^#\s+", content, re.M):
            print(f"FEHLER: Keine Markdown-Überschrift in {rel_path}", file=sys.stderr)
            return 1

    index_path = ROOT / "references/00_INDEX_UND_KONTROLLLISTE.md"
    index_text = index_path.read_text(encoding="utf-8")
    checked = len(re.findall(r"^- \[x\]", index_text, re.M))
    unchecked = len(re.findall(r"^- \[ \]", index_text, re.M))
    if checked == 0 or unchecked > 0:
        print(
            f"FEHLER: Kontrollliste unvollständig ([x]={checked}, [ ]={unchecked}).",
            file=sys.stderr,
        )
        return 1

    handbook = (ROOT / "references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md").read_text(
        encoding="utf-8"
    )
    if len(handbook) < 500_000:
        print("FEHLER: Gesamthandbuch ist unerwartet klein.", file=sys.stderr)
        return 1

    print(
        f"OK: SKILL.md + {len(expected_refs)} Referenzdateien validiert "
        f"(Quellen-Checkliste: {checked}/{checked} abgeschlossen, 0 offen)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
