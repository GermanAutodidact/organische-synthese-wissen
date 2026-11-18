#!/usr/bin/env python3
"""Validiert Struktur, Inhalte, Anker/Zeilenindizes, Links, Regressionsschutz und Sync des Repos."""

from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent


def parse_frontmatter(skill_md: pathlib.Path) -> tuple[dict[str, object], str]:
    text = skill_md.read_text(encoding="utf-8").replace("\r\n", "\n")
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


def strip_fenced_code_blocks(text: str) -> tuple[str, bool]:
    out: list[str] = []
    in_fence = False
    fence_char = ""
    fence_len = 0
    for line in text.splitlines():
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if m:
            marker = m.group(1)
            rest = line[m.end() :]
            if not in_fence:
                if marker[0] == "`" and "`" in rest:
                    out.append(line)
                    continue
                in_fence = True
                fence_char = marker[0]
                fence_len = len(marker)
                out.append("")
                continue
            if marker[0] == fence_char and len(marker) >= fence_len and line.strip() == marker:
                in_fence = False
                out.append("")
                continue
        out.append("" if in_fence else line)
    return "\n".join(out), in_fence


def check_toc_and_anchors(path: pathlib.Path, anchor_prefix: str = "sec-") -> list[str]:
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

    # Exakte Zeilennummern-Pruefung fuer Z. START–END im TOC
    lines = text.splitlines()
    for m in re.finditer(
        rf"\(#({re.escape(anchor_prefix)}[^)]+)\)\s*\|[^|]+\|\s*Z\.\s*(\d+)–(\d+)",
        toc_block,
    ):
        aid, s_s, e_s = m.groups()
        s_ln, e_ln = int(s_s), int(e_s)
        if e_ln < s_ln or s_ln < 2 or s_ln > len(lines):
            errors.append(f"{path.name}: Ungueltiger TOC-Zeilenbereich Z. {s_ln}–{e_ln} fuer '#{aid}'.")
            continue
        if lines[s_ln - 2].strip() != f'<a id="{aid}"></a>':
            errors.append(
                f"{path.name}: TOC-Zeilenindex fuer '#{aid}' veraltet (Z. {s_ln}, erwartet Anker in Z. {s_ln - 1})."
            )
    return errors


def check_regressions(files: list[pathlib.Path]) -> list[str]:
    errors: list[str] = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        stripped, unclosed = strip_fenced_code_blocks(text)
        if unclosed:
            errors.append(f"{f.name}: Ungeschlossener Fenced Code Block.")
        for i, line in enumerate(stripped.splitlines(), 1):
            if line != line.rstrip(" \t"):
                errors.append(f"{f.name}:{i}: Trailing Whitespace gefunden.")
            clean = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)
            if re.search(r":\*\*[A-Za-zÄÖÜäöü]", clean):
                errors.append(f"{f.name}:{i}: Fehlendes Leerzeichen nach ':**'.")
            if re.search(r"\),[A-Za-zÄÖÜäöü]", clean):
                errors.append(f"{f.name}:{i}: Fehlendes Leerzeichen nach '),'.")
            if re.search(r"Ethylacetat[^|\n]*\+\s*Trockeneis", line):
                errors.append(f"{f.name}:{i}: Physikalischer Fehler (EtOAc + Trockeneis).")
            if re.search(r"Hexan[^|\n]*(/\s*Trockeneis|\+\s*Trockeneis)", line):
                errors.append(f"{f.name}:{i}: Physikalischer Fehler (n-Hexan + Trockeneis).")
            if re.search(r"Methanol[^|\n]*\+[^\n]*Trockeneis[^\n]*-98", line):
                errors.append(f"{f.name}:{i}: Physikalischer Fehler (MeOH + Trockeneis -98 °C).")
            if "| **Boronsäure** | `B(O)O`" in line:
                errors.append(f"{f.name}:{i}: Fehlerhafter Boronsaeure-SMARTS 'B(O)O' (trifft Ester).")
    return errors


def check_relative_links(files: list[pathlib.Path]) -> list[str]:
    errors: list[str] = []
    anchors_by_file: dict[pathlib.Path, set[str]] = {}
    for f in files:
        stripped, _ = strip_fenced_code_blocks(f.read_text(encoding="utf-8"))
        anchors_by_file[f.resolve()] = set(re.findall(r'<a\s+id="([^"]+)"></a>', stripped))

    for f in files:
        stripped, _ = strip_fenced_code_blocks(f.read_text(encoding="utf-8"))
        for i, line in enumerate(stripped.splitlines(), 1):
            clean = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)
            for lm in re.finditer(r"!?\[[^\]]*\]\(([^)\s]+)\)", clean):
                href = lm.group(1)
                if href.startswith(("http://", "https://", "mailto:", "file://")) or "<" in href:
                    continue
                if href.startswith("#"):
                    aid = urllib.parse.unquote(href[1:])
                    if aid.startswith(("sec-", "mod-")) and aid not in anchors_by_file[f.resolve()]:
                        errors.append(f"{f.name}:{i}: Defekter Anker '{href}'.")
                else:
                    raw_p, _, raw_a = href.partition("#")
                    path_part = urllib.parse.unquote(raw_p.split("?", 1)[0])
                    resolved = (f.parent / path_part).resolve()
                    if not resolved.exists():
                        errors.append(f"{f.name}:{i}: Defekter relativer Link '{href}' (Ziel fehlt).")
                    elif raw_a and resolved in anchors_by_file:
                        aid = urllib.parse.unquote(raw_a)
                        if aid.startswith(("sec-", "mod-")) and aid not in anchors_by_file[resolved]:
                            errors.append(f"{f.name}:{i}: Defekter Ziel-Anker '{href}'.")
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
    if "don't use" not in desc.lower():
        errors.append("Frontmatter 'description' sollte einen Negativ-Trigger ('Don't use for...') enthalten.")

    meta = fm.get("metadata", {})
    version = str(meta.get("version", "?")) if isinstance(meta, dict) else "?"

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

    # TOC-Anker & Zeilenindizes
    toc_modules = [
        skill_md,
        ROOT / "references/00_INDEX_UND_KONTROLLLISTE.md",
        ROOT / "references/01_Reaktionsmechanismen_Reagenzien_und_Selektivitaet.md",
        ROOT / "references/02_Retrosynthese_und_Namensreaktionen_Katalog.md",
        ROOT / "references/02b_Ontologie_RXNO_MOP_und_ReactionClassifier.md",
        ROOT / "references/03_Laborpraxis_Aufarbeitung_Trennung_und_Analytik.md",
    ]
    for m in toc_modules:
        if m.is_file():
            errors.extend(check_toc_and_anchors(m, anchor_prefix="sec-"))

    handbook = ROOT / "references/KOMPLETTES_HANDBUCH_ORGANISCHE_SYNTHESE.md"
    if handbook.is_file():
        errors.extend(check_toc_and_anchors(handbook, anchor_prefix="mod-"))
        hb_text = handbook.read_text(encoding="utf-8")
        if re.search(r"^name:\s*organische-synthese-und-laborpraxis\s*$", hb_text, re.M):
            errors.append("KOMPLETTES_HANDBUCH enthaelt eingebettetes YAML-Frontmatter aus SKILL.md.")

    # Regressions-Lint & relative Links ueber alle Markdown-Dateien
    all_md = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    errors.extend(check_regressions(all_md))
    errors.extend(check_relative_links(all_md))

    # Webchat Prompt Limit
    wc = ROOT / "prompts/WEBCHAT_SYSTEM_PROMPT.md"
    if wc.is_file():
        wc_text = wc.read_text(encoding="utf-8")
        if "\n---\n" in wc_text:
            prompt_body = wc_text.split("\n---\n", 1)[1].strip()
            if len(prompt_body) > 5000:
                errors.append(f"Webchat-Prompt-Body zu lang ({len(prompt_body)} > 5000 Zeichen).")

    # Evals JSON inkl. Schema- & Modul-Check
    ev = ROOT / "evals/cases.json"
    if ev.is_file():
        all_files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts}
        all_basenames = {pathlib.Path(f).name for f in all_files}
        try:
            data = json.loads(ev.read_text(encoding="utf-8"))
            cases = data.get("cases", [])
            if len(cases) < 10:
                errors.append("evals/cases.json sollte mindestens 10 Testfaelle enthalten.")
            for c in cases:
                cid = c.get("id", "?")
                if not c.get("prompt"):
                    errors.append(f"evals/cases.json ({cid}): Pflichtfeld 'prompt' fehlt.")
                for mod in c.get("expected_modules", []):
                    mod_s = str(mod)
                    if "/" in mod_s:
                        ok = mod_s in all_files
                    elif "." in mod_s:
                        ok = mod_s in all_files or mod_s in all_basenames
                    else:
                        ok = any(b.startswith((mod_s + "_", mod_s + "-", mod_s + ".")) for b in all_basenames)
                    if not ok:
                        errors.append(f"evals/cases.json ({cid}): expected_module '{mod_s}' nicht gefunden.")
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
        f"OK: SKILL.md (v{version}) + 6 Referenzdateien + Handbuch-Sync + TOC-Zeilenindizes + "
        f"Links + Regressionsschutz + Evals + chem_check.py validiert (Checkliste: {checked}/{checked} abgeschlossen, 0 offen)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
