#!/usr/bin/env python3
"""Cheminformatik-Prüfskript für organische-synthese-wissen (v2.3-DE).

Implementiert die Prüfregeln aus SKILL.md (Abschnitt 1.2, 1.3 und 2.4):
- lone-pairs: Exakte Berechnung freier Elektronenpaare (N_LP) ohne externe Pakete
- sanitize: RDKit-Valenz-, Oktett-, Chiralitäts-, Metall- und Größencheck
- balance: Massen-, implizite+explizite H- und Ladungsbilanz (2-Varianten-Check)
- smarts: Funktionelle-Gruppen- und Warnmotiv-Erkennung (SMILES/SMARTS)
- --self-test: Selbsttest der Kernlogik
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter

VALENCE_ELECTRONS: dict[str, int] = {
    "H": 1,
    "B": 3,
    "C": 4,
    "N": 5,
    "O": 6,
    "F": 7,
    "Si": 4,
    "P": 5,
    "S": 6,
    "Cl": 7,
    "Br": 7,
    "I": 7,
}

METAL_ATOMIC_NUMBERS: set[int] = (
    {3, 4}
    | set(range(11, 14))
    | set(range(19, 32))
    | set(range(37, 51))
    | set(range(55, 58))
    | set(range(72, 83))
)

CANONICAL_SMARTS: dict[str, str] = {
    "Alkohol (sp3-C)": "[OX2H1][CX4]",
    "Primaerer Alkohol (ohne MeOH)": "[CX4H2][OX2H1]",
    "Sekundaerer Alkohol": "[CX4H1][OX2H1]",
    "Tertiaerer Alkohol": "[CX4H0]([OX2H1])([#6])([#6])[#6]",
    "Phenol": "c[OX2H1]",
    "Aldehyd": "[CX3H1](=O)[#6,H]",
    "Keton": "[#6][CX3](=O)[#6]",
    "Carbonsaeure": "[CX3](=O)[OX2H1]",
    "Carboxylat": "[CX3](=O)[O-]",
    "Carbonsaeureester": "[CX3](=O)[OX2H0][#6]",
    "Amid": "[CX3](=O)[NX3]",
    "Neutrales Amin": "[NX3;$(N-[#6]);!$(N-C=O);!$(N-S(=O)=O);!$(N-P=O);!$(N=*)]",
    "Primaeres Amin": "[NX3H2;$(N-[#6]);!$(N-C=O);!$(N-S(=O)=O);!$(N-P=O)]",
    "Ether (ohne Ester)": "[#6][OX2H0;!$(O-C=O)][#6]",
    "Alkylhalogenid": "[CX4][F,Cl,Br,I]",
    "Arylhalogenid": "c[F,Cl,Br,I]",
    "Alken": "C=C",
    "Alkin": "C#C",
    "Nitril": "C#N",
    "Boronsaeure": "[BX3]([OX2H1])[OX2H1]",
    "Nitrogruppe": "[$([NX3](=O)=O),$([NX3+](=O)[O-])]",
    "Thiol": "[#6][SX2H1]",
    "Sulfid": "[#6][SX2H0][#6]",
    "Sulfoxid": "[#6][SX3](=O)[#6]",
    "Sulfon": "[#6][SX4](=O)(=O)[#6]",
    "Alert: Saeurechlorid": "C(=O)Cl",
    "Alert: Epoxid": "C1OC1",
    "Alert: Michael-Akzeptor": "C=CC(=O)",
    "Alert: Brenzkatechin": "Oc1ccccc1O",
    "Alert: Rhodanin": "O=C1CSC(=S)N1",
}


def compute_lone_pairs(
    element: str, formal_charge: int, total_valence: int, radical_electrons: int = 0
) -> dict[str, object]:
    """Berechnet N_LP = (N_Valenzelektronen - Q_formal - V_gesamt - N_Radikale) / 2."""
    if element not in VALENCE_ELECTRONS:
        return {
            "valid": False,
            "error": f"Element '{element}' nicht in Hauptgruppen-Tabelle {sorted(VALENCE_ELECTRONS)}",
        }
    if total_valence < 0 or radical_electrons < 0:
        return {
            "valid": False,
            "element": element,
            "error": f"Negative Valenz ({total_valence}) oder Radikalzahl ({radical_electrons}) unzulaessig.",
        }
    n_val = VALENCE_ELECTRONS[element]
    numerator = n_val - formal_charge - total_valence - radical_electrons
    if numerator < 0 or numerator % 2 != 0:
        return {
            "valid": False,
            "element": element,
            "n_lone_pairs": numerator / 2,
            "error": f"Ungueltige Valenz/Elektronenzahl (Zaehler={numerator})",
        }
    n_lp = numerator // 2
    # Period-1/2 Oktett-/Duplett-Grenze pruefen (kein 4-e- H und kein 5-bindiges N/C/O/F!)
    if element == "H":
        own_electrons = 2 * total_valence + 2 * n_lp + radical_electrons
        if total_valence > 1 or own_electrons > 2:
            return {
                "valid": False,
                "element": element,
                "n_lone_pairs": n_lp,
                "error": f"Wasserstoff ueberschreitet Duplett-Grenze (V={total_valence}, Valenzelektronen={own_electrons} > 2).",
            }
    if element in {"B", "C", "N", "O", "F"}:
        shared_electrons = 2 * total_valence
        own_electrons = shared_electrons + 2 * n_lp + radical_electrons
        if total_valence > 4 or own_electrons > 8:
            return {
                "valid": False,
                "element": element,
                "n_lone_pairs": n_lp,
                "error": f"Oktettverletzung an Periode-2-Element '{element}' (V={total_valence}, Valenzelektronen={own_electrons} > 8).",
            }
    return {
        "valid": True,
        "element": element,
        "valence_electrons": n_val,
        "formal_charge": formal_charge,
        "total_valence": total_valence,
        "radical_electrons": radical_electrons,
        "n_lone_pairs": n_lp,
    }


def _load_rdkit():
    try:
        from rdkit import Chem  # type: ignore
        from rdkit.Chem import Descriptors, rdMolDescriptors  # type: ignore

        return Chem, Descriptors, rdMolDescriptors, None
    except Exception as exc:
        return None, None, None, str(exc)


def cmd_sanitize(smiles: str) -> dict[str, object]:
    Chem, Descriptors, rdMolDescriptors, err = _load_rdkit()
    if Chem is None:
        return {
            "ok": False,
            "tool_available": False,
            "error": f"RDKit nicht installiert ({err}). Installation z. B. via 'pip install rdkit'.",
        }
    mol = Chem.MolFromSmiles(smiles, sanitize=False)
    if mol is None:
        return {"ok": False, "tool_available": True, "smiles": smiles, "error": "SMILES nicht parsbar."}
    try:
        Chem.SanitizeMol(mol)
    except Exception as exc:
        return {
            "ok": False,
            "tool_available": True,
            "smiles": smiles,
            "error": f"Sanitization fehlgeschlagen: {exc}",
        }

    warnings: list[str] = []
    chiral = Chem.FindMolChiralCenters(mol, includeUnassigned=True)
    unassigned = [idx for idx, label in chiral if label == "?"]
    if unassigned:
        warnings.append(f"Unzugewiesene Stereozentren ('?') an Atom-Indizes: {unassigned}")

    dummies = [a.GetIdx() for a in mol.GetAtoms() if a.GetAtomicNum() == 0]
    if dummies:
        warnings.append(f"Dummy-/Wildcard-Atome (*) an Indizes: {dummies}")

    metals = [
        (a.GetIdx(), a.GetSymbol())
        for a in mol.GetAtoms()
        if a.GetAtomicNum() in METAL_ATOMIC_NUMBERS
    ]
    if metals:
        warnings.append(f"Metallatome vorhanden (Vorsicht bei Standardisierung): {metals}")

    heavy = mol.GetNumHeavyAtoms()
    if heavy > 80:
        warnings.append(f"Grosses Molekuel ({heavy} Schweratome > 80)")

    return {
        "ok": True,
        "tool_available": True,
        "canonical_smiles": Chem.MolToSmiles(mol, isomericSmiles=True),
        "formula": rdMolDescriptors.CalcMolFormula(mol),
        "exact_mass": round(Descriptors.ExactMolWt(mol), 6),
        "formal_charge": Chem.GetFormalCharge(mol),
        "heavy_atoms": heavy,
        "chiral_centers": chiral,
        "warnings": warnings,
    }


def _atom_and_charge_counts(Chem, smiles_list: list[str]) -> tuple[Counter[str], int, list[str]]:
    counts: Counter[str] = Counter()
    charge = 0
    errors: list[str] = []
    for smi in smiles_list:
        smi = smi.strip()
        if not smi:
            continue
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            errors.append(f"Ungueltiger SMILES: {smi}")
            continue
        charge += Chem.GetFormalCharge(mol)
        for atom in mol.GetAtoms():
            sym = atom.GetSymbol()
            counts[sym] += 1
            if sym != "H":
                counts["H"] += atom.GetTotalNumHs()
    return counts, charge, errors


def cmd_balance(rxn_smiles: str) -> dict[str, object]:
    Chem, _, _, err = _load_rdkit()
    if Chem is None:
        return {
            "ok": False,
            "tool_available": False,
            "error": f"RDKit nicht installiert ({err}). Installation z. B. via 'pip install rdkit'.",
        }
    parts = rxn_smiles.split(">")
    if len(parts) != 3:
        return {
            "ok": False,
            "tool_available": True,
            "error": "Erwartetes Format: 'Reactants > Reagents > Products' (genau 2 '>').",
        }
    reactants = [s for s in parts[0].split(".") if s.strip()]
    reagents = [s for s in parts[1].split(".") if s.strip()]
    products = [s for s in parts[2].split(".") if s.strip()]

    r_cnt, r_chg, r_err = _atom_and_charge_counts(Chem, reactants)
    a_cnt, a_chg, a_err = _atom_and_charge_counts(Chem, reagents)
    p_cnt, p_chg, p_err = _atom_and_charge_counts(Chem, products)
    all_errs = r_err + a_err + p_err
    if all_errs:
        return {"ok": False, "tool_available": True, "errors": all_errs}

    def delta(left_c: Counter[str], left_q: int) -> tuple[dict[str, int], int]:
        elems = set(left_c) | set(p_cnt)
        d = {e: p_cnt[e] - left_c[e] for e in sorted(elems) if p_cnt[e] - left_c[e] != 0}
        return d, p_chg - left_q

    d_no_reag, q_no_reag = delta(r_cnt, r_chg)
    d_with_reag, q_with_reag = delta(r_cnt + a_cnt, r_chg + a_chg)

    balanced_without = not d_no_reag and q_no_reag == 0
    balanced_with = not d_with_reag and q_with_reag == 0
    status = "balanced" if (balanced_without or balanced_with) else "unbalanced"

    return {
        "ok": status == "balanced",
        "tool_available": True,
        "status": status,
        "balanced_without_reagents": balanced_without,
        "balanced_with_reagents": balanced_with,
        "delta_without_reagents": {"atoms": d_no_reag, "charge": q_no_reag},
        "delta_with_reagents": {"atoms": d_with_reag, "charge": q_with_reag},
    }


def cmd_smarts(smiles: str) -> dict[str, object]:
    Chem, _, _, err = _load_rdkit()
    if Chem is None:
        return {
            "ok": False,
            "tool_available": False,
            "error": f"RDKit nicht installiert ({err}). Installation z. B. via 'pip install rdkit'.",
        }
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {"ok": False, "tool_available": True, "error": f"Ungueltiger SMILES: {smiles}"}
    matches: dict[str, int] = {}
    for label, pattern in CANONICAL_SMARTS.items():
        q = Chem.MolFromSmarts(pattern)
        if q is None:
            continue
        hits = mol.GetSubstructMatches(q)
        if hits:
            matches[label] = len(hits)
    return {"ok": True, "tool_available": True, "smiles": smiles, "matches": matches}


def run_self_test() -> int:
    # 1. Lone-pair checks (pure Python)
    assert compute_lone_pairs("N", 0, 3)["n_lone_pairs"] == 1
    assert compute_lone_pairs("N", 1, 4)["n_lone_pairs"] == 0
    assert compute_lone_pairs("O", -1, 1)["n_lone_pairs"] == 3
    assert compute_lone_pairs("H", -1, 0)["valid"] is True  # Hydrid H- (2 e-)
    assert compute_lone_pairs("H", -2, 1)["valid"] is False  # 4-Elektronen-H verboten (F2)
    assert compute_lone_pairs("C", 0, -2)["valid"] is False  # Negative Valenz verboten (F2)
    assert compute_lone_pairs("C", 0, 4, -2)["valid"] is False  # Negative Radikalzahl verboten (F2)
    assert compute_lone_pairs("C", 0, 5)["valid"] is False  # Pentavalentes C verboten
    assert compute_lone_pairs("N", 0, 5)["valid"] is False  # 5-bindiges neutrales N verboten
    # 2. Kanonische SMARTS Regression (F1)
    assert CANONICAL_SMARTS["Boronsaeure"] == "[BX3]([OX2H1])[OX2H1]"
    assert "$(N-[#6])" in CANONICAL_SMARTS["Primaeres Amin"]

    Chem, _, _, _ = _load_rdkit()
    if Chem is not None:
        assert cmd_sanitize("CCO")["ok"] is True
        assert cmd_sanitize("C(C)(C)(C)(C)C")["ok"] is False
        assert cmd_balance("CC(=O)C>>CC(O)C")["status"] == "unbalanced"
        assert cmd_balance("CC(=O)C.[H][H]>>CC(O)C")["status"] == "balanced"
        assert "Aldehyd" in cmd_smarts("CC=O")["matches"]
        assert "Boronsaeure" in cmd_smarts("OB(O)c1ccccc1")["matches"]
        assert "Boronsaeure" not in cmd_smarts("COB(OC)c1ccccc1")["matches"]
    print("OK: chem_check.py Selbsttest bestanden (RDKit=" + ("aktiv" if Chem else "nicht installiert") + ").")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Cheminformatik-Validierung (SKILL.md 1.2, 1.3, 2.4)")
    parser.add_argument("--self-test", action="store_true", help="Fuehrt interne Selbsttests aus")
    sub = parser.add_subparsers(dest="cmd")

    p_lp = sub.add_parser("lone-pairs", help="Berechnet freie Elektronenpaare N_LP")
    p_lp.add_argument("--elem", required=True)
    p_lp.add_argument("--charge", type=int, default=0)
    p_lp.add_argument("--valence", type=int, required=True)
    p_lp.add_argument("--radicals", type=int, default=0)

    p_san = sub.add_parser("sanitize", help="Prueft SMILES via RDKit SanitizeMol")
    p_san.add_argument("smiles")

    p_bal = sub.add_parser("balance", help="Prueft Massen-, H- und Ladungsbilanz")
    p_bal.add_argument("rxn_smiles")

    p_sm = sub.add_parser("smarts", help="Erkennt funktionelle Gruppen mittels kanonischer SMARTS")
    p_sm.add_argument("smiles")

    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if args.cmd == "lone-pairs":
        res = compute_lone_pairs(args.elem, args.charge, args.valence, args.radicals)
    elif args.cmd == "sanitize":
        res = cmd_sanitize(args.smiles)
    elif args.cmd == "balance":
        res = cmd_balance(args.rxn_smiles)
    elif args.cmd == "smarts":
        res = cmd_smarts(args.smiles)
    else:
        parser.print_help()
        return 0

    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res.get("ok", res.get("valid", False)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
