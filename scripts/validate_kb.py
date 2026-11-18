#!/usr/bin/env python3
"""Validiert Struktur, Inhalte, Anker, Regressionsschutz und Sync des organische-synthese-wissen Repos."""

from __future__ import annotations

import json
import pathlib
import re
import subprocess
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
    current_map_key: str | None = None
    for line in fm_block.splitlines():
        if not line.strip():
            continue
        if re.match(r"^\s{2,}[A-Za-z0-9_-]+:", line) and current_map_key is not None:
            sub_k, sub_v = line.strip().split(":", 1)
            cast_map = data[current_map_key]
            if isinstance(cast_map, dict):
                cast_map[sub_k.strip()] = sub_v.strip()
            continue
        current_map_key = None
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val == "":
                data[key] = {}
                current_map_key = key
            else:
                data[key] = val
    return data, body


def check_toc_and_anchors(path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if "<!-- TOC_START -->" not in text or "<!-- TOC_END -->" not in text:
        errors.append(f"{path.name}: TOC-Block (<!-- TOC_START --> ... <!-- TOC_END -->) fehlt.")
        return errors

    toc_block = text.split("<!-- TOC_START -->", 1)[1].split("<!-- TOC_END -->", 1)[0]
    links = re.findall(r"\]\(#([^)]+)\)", toc_block)
    anchors = re.findall(r'<a id="([^"]+)"></a>', text)
    if not links:
        errors.append(f"{path.name}: Keine TOC-Ankerlinks gefunden.")
    if len(anchors) != len(set(anchors)):
        errors.append(f"{path.name}: Doppelte <a id=...>-Anker vorhanden.")
    anchor_set = set(anchors)
    for link in links:
        if link not in anchor_set:
            errors.append(f"{path.name}: Defekter TOC-Anker '#{link}'.")
    return errors


def check_regressions(files: list[pathlib.Path]) -> list[str]:
    errors: list[str] = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if re.search(r":\*\*[A-Za-zÄÖÜäöü]", line):
                errors.append(f"{f.name}:{i}: Fehlendes Leerzeichen nach ':**'.")
            if re.search(r"\),[A-Za-zÄÖÜäöü]", line):
                errors.append(f"{f.name}:{i}: Fehlendes Leerzeichen nach '),'.")
            if re.search(r"Ethylacetat[^|\n]*\+\s*Trockeneis", line):
                errors.append(f"{f.name}:{i}: Physikalischer Fehler (EtOAc + Trockeneis).")
            if re.search(r"Hexan[^|\n]*(/\s*Trockeneis|\+\s*Trockeneis)", line):
                errors.append(f"{f.name}:{i}: Physikalischer Fehler (n-Hexan + Trockeneis).")
            if re.search(r"Methanol[^|\n]*\+[^\n]*Trockeneis[^\n]*-98", line):
                errors.append(f"{f.name}:{i}: Physikalischer Fehler (MeOH + Trockeneis -98 °C).")
    return errors


def main() -> int:
    errors: list[str] = []

    skill_md = ROOT / "SKILL.md"
    if not skill_md.is_file():
        print("FEHLER: SKILL.md fehlt.", file=sys.stderr)
        return 1

    fm, body = parse_frontmatter(skill_md)
    for required in ("name", "description"):
        if required not in fm or not fm[required]:
            errors.append(f"Pflichtfeld '{required}' fehlt im SKILL.md-Frontmatter.")

    desc = str(fm.get("description", ""))
    if len(desc) > 1024:
        errors.append(f"Frontmatter 'description' zu lang ({len(desc)} > 1024 Zeichen).")
    if "Use whenever" not in desc and "use when" not in desc.lower():
        errors.append("Frontmatter 'description' sollte auch englische Trigger-Hinweise enthalten.")

    if len(body.strip()) < 1000:
        errors.append("SKILL.md Body ist unerwartet kurz.")
    if len(skill_md.read_text(encoding="utf-8")) > 65_000:
        errors.append("SKILL.md ueberschreitet 65 KB Budget.")

    required_files = [
        "LICENSE",
        "NOTICE.md",
        "CHANGELOG.md",
        "prompts/WEBCHAT_SYSTEM_PROMPT.md",
        "evals/cases.json",
        "scripts/chem_check.py",
        "scripts/build_handbook.py",
        "references/00_INDEX_UND_KONTROLLLISTE.md",
        "references/01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md",
        "references/02_Retrosynthese_und_Namensreaktionen_Katalog.md",
        "references/02b_Ontologie_RXNO_MOP_und_ReactionClassifier.md",
        "references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md",
        "references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md",
    ]
    for rel in required_files:
        p = ROOT / rel
        if not p.is_file() or not p.read_text(encoding="utf-8").strip():
            errors.append(f"Pflichtdatei fehlt oder ist leer: {rel}")

    # Groessenbudgets fuer Kernmodule
    size_limits = {
        "references/01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md": 220_000,
        "references/02_Retrosynthese_und_Namensreaktionen_Katalog.md": 140_000,
        "references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md": 110_000,
    }
    for rel, limit in size_limits.items():
        p = ROOT / rel
        if p.is_file():
            sz = len(p.read_text(encoding="utf-8"))
            if sz > limit:
                errors.append(f"{rel} ueberschreitet Groessenbudget ({sz} > {limit} Zeichen).")

    # Checkliste
    index_path = ROOT / "references/00_INDEX_UND_KONTROLLLISTE.md"
    index_text = index_path.read_text(encoding="utf-8")
    checked = len(re.findall(r"^- \[x\]", index_text, re.M))
    unchecked = len(re.findall(r"^- \[ \]", index_text, re.M))
    if checked == 0 or unchecked > 0:
        errors.append(f"Kontrollliste unvollstaendig ([x]={checked}, [ ]={unchecked}).")

    # TOC-Anker
    toc_modules = [
        ROOT / "references/00_INDEX_UND_KONTROLLLISTE.md",
        ROOT / "references/01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md",
        ROOT / "references/02_Retrosynthese_und_Namensreaktionen_Katalog.md",
        ROOT / "references/02b_Ontologie_RXNO_MOP_und_ReactionClassifier.md",
        ROOT / "references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md",
    ]
    for m in toc_modules:
        if m.is_file():
            errors.extend(check_toc_and_anchors(m))

    # Regressions-Lint
    lint_files = [skill_md] + toc_modules + [ROOT / "references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md"]
    errors.extend(check_regressions([p for p in lint_files if p.is_file()]))

    # Webchat Prompt Limit
    wc = ROOT / "prompts/WEBCHAT_SYSTEM_PROMPT.md"
    if wc.is_file():
        wc_text = wc.read_text(encoding="utf-8")
        if "\n---\n" in wc_text:
            prompt_body = wc_text.split("\n---\n", 1)[1].strip()
            if len(prompt_body) > 5000:
                errors.append(f"Webchat-Prompt-Body zu lang ({len(prompt_body)} > 5000 Zeichen).")

    # Evals JSON
    ev = ROOT / "evals/cases.json"
    if ev.is_file():
        try:
            data = json.loads(ev.read_text(encoding="utf-8"))
            if len(data.get("cases", [])) < 10:
                errors.append("evals/cases.json sollte mindestens 10 Testfaelle enthalten.")
        except Exception as exc:
            errors.append(f"evals/cases.json ungueltiges JSON: {exc}")

    # Handbuch-Sync und chem_check Selbsttest
    for cmd in (
        [sys.executable, str(ROOT / "scripts/build_handbook.py"), "--check"],
        [sys.executable, str(ROOT / "scripts/chem_check.py"), "--self-test"],
    ):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            errors.append(f"Befehl fehlgeschlagen ({' '.join(cmd)}): {proc.stderr.strip() or proc.stdout.strip()}")

    if errors:
        for e in errors:
            print(f"FEHLER: {e}", file=sys.stderr)
        return 1

    print(
        f"OK: SKILL.md (v2.2-DE) + 6 Referenzdateien + Handbuch-Sync + TOC-Anker + "
        f"Regressionsschutz + chem_check.py validiert (Checkliste: {checked}/{checked} abgeschlossen, 0 offen)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
