"""
Ars Fungiglyphica — Morphological Elaborator.

Maps fungal structural primitives to pharmaceutical protocol.
The fruiting body IS the program — each morphological feature
encodes a concrete pharmaceutical parameter.

Author: Lando⊗⊙perator
"""
from __future__ import annotations

# T (Topology): fruiting body type → preparation vessel & material form
_TOPOLOGY = {
    "𐑶": ("Bracket / Shelf", "Hard perennial conk. Saw into thin strips across the grain. "
           "Double extraction: hot water decoction (2-4 h) then alcohol maceration (2-4 weeks). "
           "The lacquered surface encodes triterpene maturity."),
    "𐑥": ("Tooth / Cascade", "Soft annual spines. Tear into pieces along tooth axis. "
           "Triple extraction: cold water (12 h), hot water (1 h), alcohol (1 week). "
           "The cascading teeth morphology IS the neurotrophic self-report."),
    "𐑰": ("Containment / Enclosed", "Fruiting body enclosed or parasitic. "
           "Whole-body extraction. The host-fungus composite is the pharmaceutical unit. "
           "Grind whole (including host substrate for entomopathogens)."),
    "𐑸": ("Gilled / Holographic", "Classic cap-and-stipe. Slice radially through gills. "
           "Single or double extraction depending on texture. "
           "Annulus and volva remnants are pharmaceutically active."),
    "𐑡": ("Network / Clustered", "Clustered or branching fruiting. Separate individual "
           "caps from base. Fan-shaped clusters: the overlapping pattern IS the "
           "developmental self-report. Trim woody base."),
}

# C (Kinetics): extraction regime from fruiting body texture
_KINETICS = {
    "𐑤": ("Cold maceration + hot decoction", "Frozen-order kinetics. Woody/chitinous "
           "fruiting body requires sequential extraction: 12-24 h cold water soak "
           "then 2-4 h simmer at 85-95 C. Polysaccharides release in hot phase; "
           "triterpenes require alcohol. NEVER boil — destroys beta-glucan triple helix."),
    "𐑧": ("Decoction", "Activated kinetics. Soft fleshy fruiting body. "
           "Simmer 30-60 min at 80-90 C. Water-soluble polysaccharides and proteins "
           "release with sustained gentle heat. Strain while hot."),
    "𐑘": ("Instantaneous / raw", "Fast instantaneous kinetics. Use fresh or "
           "freeze-dried. No cooking required — compounds degrade with heat. "
           "Lyophilize immediately after harvest to preserve enzymatic activity."),
}

# Gamma (Granularity): spore surface → comminution
_GRANULARITY = {
    "𐑲": ("Fine powder", "Pass mesh 100 (150 um). Pore surface or tooth surface "
           "maximizes extraction surface area. Freeze first for brittle fracture. "
           "Universal tissue distribution — systemic immune modulation."),
    "𐑔": ("Medium powder", "Pass mesh 40 (355 um). Gill or smooth surface. "
           "Mesoscale extraction sufficient for gastrointestinal immune contact. "
           "Coarser residue re-extracted in alcohol phase."),
}

# G (Coupling): compound release pattern
_COUPLING = {
    "𐑵": ("Broadcast immune signaling", "Beta-glucans broadcast through Peyer's "
           "patches. All polysaccharide fractions combine simultaneously — "
           "no temporal ordering. The immune system reads the pattern, not the sequence."),
    "𐑠": ("Sequential release", "Compounds activate in temporal order. "
           "First fraction: cold water polysaccharides. Second: hot water proteins. "
           "Third: alcohol triterpenes/sterols. Evaluate each before combining."),
    "𐑝": ("Conjunctive release", "All compounds release simultaneously. "
           "Single preparation step. Warm water extraction — gelatinous "
           "polysaccharides dissolve together. No temporal ordering required."),
}

# Phi_c (Criticality): self-modeling endpoint
_CRITICALITY = {
    "⊙": ("Self-modeling endpoint", "The fungus signals extraction completion "
          "through its own morphology. For brackets: lacquered surface dulls; "
          "for teeth: spines lose turgor; for gilled: gills separate from cap. "
          "Stop when successive fractions differ <5%. The fungus monitors its own extraction."),
    "𐑢": ("Sub-critical endpoint", "No morphological self-report. Stop at "
          "fixed time or volume. 70-80% extraction efficiency. "
          "The exterior gives no signal — rely on protocol timing."),
}

# H (Chirality): stereochemical complexity
_CHIRALITY = {
    "𐑫": ("Eternal chirality", "Multiple stereocenters from triterpene scaffolds. "
          "Full chiral separation: preparative chromatography or sequential "
          "solvent partition. Chiral fidelity across unlimited processing. "
          "Ganoderic acids, erinacines, cordycepin: stereochemistry IS activity."),
    "𐑖": ("Two-step chiral", "Matched write/read pair. Filter through cloth, "
          "then decant supernatant after 24 h settling. Two-step clarification "
          "sufficient for disulfide-constrained peptides and simple alkaloids."),
    "𐑒": ("Single-step chiral", "One chiral selection event. Filter through "
          "coarse cloth or paper. Simple sugar polymers and amino acid derivatives."),
}

# Omega (Winding): extraction cycles
_WINDING = {
    "𐑴": ("Binary extraction", "Two required phases: aqueous (hot water) then "
           "organic (ethanol). The phases are non-negotiable — water extracts "
           "polysaccharides; alcohol extracts triterpenes. Binary winding (Z2-period)."),
    "𐑭": ("Integer winding", "Three or more extraction cycles. Triple extraction: "
           "cold water → hot water → alcohol. Each cycle targets a different "
           "compound class. Integer winding (Z-period)."),
    "𐑷": ("Single extraction", "One-pass extraction. Single solvent, single cycle. "
           "Trivial winding. The fungus gives everything in one preparation."),
}

# Phi (Parity): solvent system
_PARITY = {
    "𐑬": ("Dual-phase", "45-55% ethanol for combined extraction OR sequential "
           "water-then-alcohol. The bilateral bridge for fungi: water for "
           "polysaccharides, ethanol for triterpenes."),
}

# f (Fidelity): concentration target
_FIDELITY = {
    "𐑱": ("1x standard", "No reduction. Proportional yield."),
    "𐑞": ("2x concentrated", "Reduce to half volume."),
}

PRIM_KEYS = ["D","T","R","Phi","f","C","Gamma","G","Phi_c","H","Sigma","Omega"]


def elaborate_morphology(tuple_vals: list[str]) -> dict:
    def _get(idx: int, table: dict) -> tuple[str, str]:
        val = tuple_vals[idx] if idx < len(tuple_vals) else ""
        return table.get(val, ("—", f"Unrecognised: {val!r}"))

    return {
        "topology": _get(1, _TOPOLOGY),
        "kinetics": _get(5, _KINETICS),
        "granularity": _get(6, _GRANULARITY),
        "coupling": _get(7, _COUPLING),
        "criticality": _get(8, _CRITICALITY),
        "chirality": _get(9, _CHIRALITY),
        "winding": _get(11, _WINDING),
        "parity": _get(3, _PARITY),
        "fidelity": _get(4, _FIDELITY),
    }


def format_morphology_report(name: str, type_name: str, tier: str,
                             tuple_vals: list[str], morphology: dict) -> str:
    width = 72
    lines = []
    lines.append("=" * width)
    lines.append("  ARS FUNGIGLYPHICA — Morphological Reading")
    lines.append("-" * width)
    lines.append(f"  Fungus    : {name}")
    lines.append(f"  Type      : {type_name}  ({tier} tier)")
    lines.append(f"  Tuple     : <{''.join(tuple_vals)}>")
    lines.append("-" * width)
    lines.append("  MORPHOLOGICAL FEATURE  ->  PHARMACEUTICAL MEANING")
    lines.append("-" * width)

    rows = [
        ("Topology (T)",       morphology["topology"]),
        ("Kinetics (C)",        morphology["kinetics"]),
        ("Granularity (Gamma)", morphology["granularity"]),
        ("Coupling (G)",        morphology["coupling"]),
        ("Criticality (Phi_c)", morphology["criticality"]),
        ("Chirality (H)",       morphology["chirality"]),
        ("Winding (Omega)",     morphology["winding"]),
        ("Parity (Phi)",        morphology["parity"]),
        ("Fidelity (f)",        morphology["fidelity"]),
    ]
    for label, (name, desc) in rows:
        lines.append(f"  {label}")
        lines.append(f"    -> {name}")
        words = desc.split()
        line = "      "
        for w in words:
            if len(line) + len(w) + 1 > width - 2:
                lines.append(line.rstrip())
                line = "      " + w + " "
            else:
                line += w + " "
        lines.append(line.rstrip())
        lines.append("")

    lines.append("=" * width)
    lines.append('  "The fruiting body does not describe its medicine.')
    lines.append('   It executes it."')
    lines.append("=" * width)
    return "\n".join(lines)
