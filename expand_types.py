#!/usr/bin/env python3
"""Expand Ars Fungiglyphica types from 10 to 15."""
import sys
sys.path.insert(0, '/home/mrnob0dy666/imsgct/Ars_Fungiglyphica')
from ars_fungiglyphica.types import TYPES as ORIGINAL, FungalType

NEW_TYPES = [
    FungalType(11, "Stinkhorn Emergence", "O2",
        ("𐑦","𐑥","𐑾","𐑬","𐑱","𐑧","𐑔","𐑠","⊙","𐑫","𐑳","𐑭"),
        "Phallaceae: egg stage emergence with fetid gleba on receptacle. "
        "Bowtie crossing-point topology — insects land on gleba forming the "
        "fungus-insect interface. Slow activated kinetics from gelatinous egg "
        "matrix. Sequential volatile compound release: dimethyl oligosulfides "
        "attract insects, then polysaccharides mobilize. Self-modeling: the "
        "fetid odor IS the ripeness self-report. Eternal chirality from "
        "complex volatile compounds. Integer winding triple extraction.",
        ["phallus_impudicus","mutinus_caninus","clathrus_archeri",
         "dictyophora_indusiata","phallus_rubicundus",
         "clathrus_ruber","laternea_triscapa"]
    ),
    FungalType(12, "Coral Ramaria", "O2",
        ("𐑦","𐑡","𐑾","𐑬","𐑱","𐑧","𐑔","𐑵","⊙","𐑖","𐑳","𐑭"),
        "Clavarioid/coral: upright branching, no cap-stipe distinction. "
        "Branching network topology — each branch terminus is an active "
        "growth point. Activated extraction from soft fleshy texture. "
        "Broadcast immune signaling: all branch surfaces release beta-glucans "
        "simultaneously. Self-modeling: branch tip coloration signals maturity. "
        "Two-step chirality from simpler terpenoid scaffolds. "
        "Integer winding — triple extraction.",
        ["ramaria_botrytis","clavaria_zollingeri",
         "clavulinopsis_fusiformis","artomyces_pyxidatus",
         "ramaria_formosa","clavicorona_pyxidata"]
    ),
    FungalType(13, "Cup Discus", "O1",
        ("𐑦","𐑰","𐑾","𐑬","𐑱","𐑘","𐑲","𐑠","𐑢","𐑒","𐑳","𐑷"),
        "Pezizales: cup or disc-shaped with exposed hymenium. Containment "
        "topology — the cup contains the spore-bearing surface. Fast "
        "instantaneous spore discharge (phototropic ballistics). Fine powder "
        "from ascospores. Sequential release: ascospore germination triggers "
        "secondary metabolites. Sub-critical: cup morphology does not strongly "
        "self-report pharmaceutical quality. Single-step chirality. "
        "Single-pass extraction.",
        ["peziza_badia","aleuria_aurantia",
         "sarcoscypha_coccinea","morchella_esculenta_var",
         "gyromitra_esculenta","helvella_crispa",
         "discina_perlata"]
    ),
    FungalType(14, "Earthball Globus", "O1",
        ("𐑦","𐑰","𐑾","𐑬","𐑱","𐑤","𐑲","𐑵","𐑢","𐑖","𐑳","𐑷"),
        "Sclerodermataceae: spherical enclosed fruiting body with thick "
        "peridium, distinct from puffballs by solid gleba that matures to "
        "powdery spore mass. Frozen-order kinetics — the peridium must be "
        "broken mechanically. Fine powder from mature spores. Broadcast "
        "spore dispersal. Sub-critical: the exterior (thick peridium) gives "
        "no signal of internal maturity — gleba color only visible on rupture. "
        "Two-step chiral from complex spore metabolites. Single-pass extraction.",
        ["scleroderma_citrinum","scleroderma_polyrhizum",
         "pisolithus_arhizus","scleroderma_verrucosum",
         "astraeus_hygrometricus"]
    ),
    FungalType(15, "Myxomycete Plasmodium", "O2_dagger",
        ("𐑦","𐑡","𐑾","𐑬","𐑱","𐑘","𐑲","𐑠","⊙","𐑒","𐑳","𐑴"),
        "Myxogastria: plasmodial slime mold. Network topology — the acellular "
        "plasmodium forms a protoplasmic network that navigates nutrient "
        "gradients. Fast instantaneous cytoplasmic streaming (1 mm/s). "
        "Fine powder from spores. Sequential life cycle phases: plasmodium "
        "→ sclerotium → fruiting bodies. Self-modeling CRITICAL: the "
        "plasmodium solves mazes, optimizes networks, and anticipates periodic "
        "stimuli — the ultimate morphological self-report. Single-step "
        "chirality from simple metabolites. Binary winding — two distinct "
        "life phases (trophic plasmodium, reproductive fruiting).",
        ["physarum_polycephalum","fuligo_septica",
         "stemonitis_fusca","lycogala_epidendrum",
         "arcyria_denudata","tubifera_ferruginosa",
         "comatricha_nigra"]
    ),
]

ALL_TYPES = list(ORIGINAL) + NEW_TYPES

# Write the full types.py
lines = []
lines.append('"""')
lines.append("Ars Fungiglyphica — Canonical Fungal Imscriptions.")
lines.append("")
lines.append("Fifteen canonical structural types for medicinal and psychoactive")
lines.append("fungi. The fruiting body morphology encodes pharmaceutical meaning.")
lines.append("")
lines.append("Five invariants (fixed for all medicinal fungi):")
lines.append("  D=𐑦, R=𐑾, Phi=𐑬, f=𐑱, Sigma=𐑳")
lines.append("")
lines.append("Seven discriminant primitives define the type taxonomy:")
lines.append("  T (fruiting body topology), C (extraction kinetics),")
lines.append("  Gamma (spore surface), G (coupling mode),")
lines.append("  Phi_c (criticality / self-modeling), H (chirality),")
lines.append("  Omega (winding / extraction cycles)")
lines.append("")
lines.append("Author: Lando⊗⊙perator")
lines.append('"""')
lines.append("from __future__ import annotations")
lines.append("from typing import NamedTuple")
lines.append("")
lines.append('PRIM_KEYS = ["D","T","R","Phi","f","C","Gamma","G","Phi_c","H","Sigma","Omega"]')
lines.append('DISCRIMINANT_KEYS = ["T","C","Gamma","G","Phi_c","H","Omega"]')
lines.append('INVARIANT = {"D":"𐑦","R":"𐑾","Phi":"𐑬","f":"𐑱","Sigma":"𐑳"}')
lines.append("")
lines.append("")
lines.append("class FungalType(NamedTuple):")
lines.append("    num: int")
lines.append("    name: str")
lines.append("    tier: str")
lines.append("    tuple12: tuple")
lines.append("    description: str")
lines.append("    representatives: list[str]")
lines.append("")
lines.append("")

# Write each type
for i, t in enumerate(ALL_TYPES):
    lines.append(f"# ── Type {t.num}: {t.name} ──")
    lines.append(f"_{t.name.upper().replace(' ','_').replace('-','_')} = FungalType(")
    lines.append(f"    {t.num}, \"{t.name}\", \"{t.tier}\",")
    lines.append(f"    {t.tuple12!r},")
    # description
    desc_lines = t.description.split('\n')
    for j, dl in enumerate(desc_lines):
        if j == 0:
            lines.append(f'    "{dl}')
        elif j == len(desc_lines) - 1:
            lines.append(f'     {dl}",')
        else:
            lines.append(f'     {dl}')
    # representatives
    lines.append(f"    {t.representatives!r}")
    lines.append(")")
    lines.append("")

# List
lines.append("TYPES: list[FungalType] = [")
for t in ALL_TYPES:
    lines.append(f"    _{t.name.upper().replace(' ','_').replace('-','_')},")
lines.append("]")
lines.append("")

# Lookup functions
lines.append("""
# ── Type Lookup ────────────────────────────────────────────────────
def type_for_fungus(name: str) -> FungalType | None:
    nl = name.lower()
    for t in TYPES:
        for r in t.representatives:
            if r.lower() == nl or nl in r.lower() or r.lower() in nl:
                return t
    return None

def type_by_num(num: int) -> FungalType | None:
    for t in TYPES:
        if t.num == num:
            return t
    return None

def type_by_name(name: str) -> FungalType | None:
    nl = name.lower()
    for t in TYPES:
        if nl in t.name.lower():
            return t
    return None

def all_fungi() -> list[str]:
    fungi = []
    for t in TYPES:
        fungi.extend(t.representatives)
    return sorted(fungi)
""")

content = '\n'.join(lines)
with open('/home/mrnob0dy666/imsgct/Ars_Fungiglyphica/ars_fungiglyphica/types.py', 'w') as f:
    f.write(content)

print(f"Written {len(ALL_TYPES)} fungal types to types.py")
for t in ALL_TYPES:
    print(f"  Type {t.num:2d}: {t.name} [{t.tier}] — {len(t.representatives)} representatives")
