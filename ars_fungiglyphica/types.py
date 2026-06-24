"""
Ars Fungiglyphica — Canonical Fungal Imscriptions.

Fifteen canonical structural types for medicinal and psychoactive
fungi. The fruiting body morphology encodes pharmaceutical meaning.

Five invariants (fixed for all medicinal fungi):
  D=𐑦, R=𐑾, Phi=𐑬, f=𐑱, Sigma=𐑳

Seven discriminant primitives define the type taxonomy:
  T (fruiting body topology), C (extraction kinetics),
  Gamma (spore surface), G (coupling mode),
  Phi_c (criticality / self-modeling), H (chirality),
  Omega (winding / extraction cycles)

Author: Lando⊗⊙perator
"""
from __future__ import annotations
from typing import NamedTuple

PRIM_KEYS = ["Ð","Þ","Ř","Φ","ƒ","Ç","Γ","ɢ","⊙","Ħ","Σ","Ω"]
DISCRIMINANT_KEYS = ["Þ","Ç","Γ","ɢ","⊙","Ħ","Ω"]
INVARIANT = {"Ð":"𐑦","Ř":"𐑾","Φ":"𐑬","ƒ":"𐑱","Σ":"𐑳"}


class FungalType(NamedTuple):
    num: int
    name: str
    tier: str
    tuple12: tuple
    description: str
    representatives: list[str]


# ── Type 1: Bracket Polypore ──
_BRACKET_POLYPORE = FungalType(
    1, "Bracket Polypore", "O2_dagger",
    ('𐑦', '𐑶', '𐑾', '𐑬', '𐑱', '𐑤', '𐑲', '𐑵', '⊙', '𐑫', '𐑳', '𐑴'),
    "Shelf/bracket fruiting body. Hard perennial woody texture, pore surface on underside. Broadcast immune signaling via beta-glucans. Binary extraction: hot water decoction followed by alcohol extraction. Eternal chirality from ganoderic/triterpene acids.",
    ['ganoderma_lucidum', 'ganoderma_tsugae', 'trametes_versicolor', 'inonotus_obliquus', 'fomitopsis_betulina', 'ganoderma_applanatum', 'phellinus_linteus', 'polyporus_umbellatus']
)

# ── Type 2: Tooth Cascade ──
_TOOTH_CASCADE = FungalType(
    2, "Tooth Cascade", "O2",
    ('𐑦', '𐑥', '𐑾', '𐑬', '𐑱', '𐑧', '𐑲', '𐑠', '⊙', '𐑫', '𐑳', '𐑭'),
    "Cascading tooth/spine fruiting body. Soft annual, no cap-stipe distinction. Sequential neurotrophic factor release: erinacines cross blood-brain barrier then hericenones activate NGF synthesis. Integer winding triple extraction. The cascading teeth morphology IS the neurotrophic self-report.",
    ['hericium_erinaceus', 'hericium_coralloides', 'hericium_americanum', 'climacodon_septentrionalis']
)

# ── Type 3: Entomopathogenic Club ──
_ENTOMOPATHOGENIC_CLUB = FungalType(
    3, "Entomopathogenic Club", "O2",
    ('𐑦', '𐑰', '𐑾', '𐑬', '𐑱', '𐑤', '𐑲', '𐑵', '⊙', '𐑖', '𐑳', '𐑭'),
    "Parasitic on insects, club-shaped fruiting body emerging from host. Containment topology — the fungus contains the insect body within its morphological encoding. Broadcast signaling: cordycepin + polysaccharides. The caterpillar-fungus composite IS the prerequisite encoding.",
    ['cordyceps_militaris', 'ophiocordyceps_sinensis', 'tolypocladium_inflatum', 'cordyceps_cicadae']
)

# ── Type 4: Gilled Cap-and-Stipe ──
_GILLED_CAP_AND_STIPE = FungalType(
    4, "Gilled Cap-and-Stipe", "O2",
    ('𐑦', '𐑸', '𐑾', '𐑬', '𐑱', '𐑧', '𐑔', '𐑠', '⊙', '𐑖', '𐑳', '𐑭'),
    "Classic agaric: cap with gills on central stipe. Mesoscale granularity from gill surface area. Sequential compound release during extraction. Annulus and volva provide morphological self-report of spore maturity. The most common medicinal mushroom body plan.",
    ['lentinula_edodes', 'psilocybe_cubensis', 'agaricus_subrufescens', 'pleurotus_ostreatus', 'hypsizygus_tessulatus', 'flammulina_velutipes', 'agaricus_bisporus']
)

# ── Type 5: Rosette Cluster ──
_ROSETTE_CLUSTER = FungalType(
    5, "Rosette Cluster", "O2",
    ('𐑦', '𐑡', '𐑾', '𐑬', '𐑱', '𐑧', '𐑔', '𐑵', '⊙', '𐑖', '𐑳', '𐑭'),
    "Overlapping fan-shaped caps in rosette/cluster formation. Branching network topology from clustered fruiting. Broadcast immune signaling via beta-glucan D-fraction. The overlapping pattern IS the self-report of developmental stage.",
    ['grifola_frondosa', 'sparassis_crispa', 'pleurotus_citrinopileatus', 'pleurotus_djamor', 'meripilus_giganteus']
)

# ── Type 6: Jelly Gelatinous ──
_JELLY_GELATINOUS = FungalType(
    6, "Jelly Gelatinous", "O1",
    ('𐑦', '𐑡', '𐑾', '𐑬', '𐑱', '𐑧', '𐑔', '𐑝', '𐑢', '𐑒', '𐑳', '𐑷'),
    "Gelatinous, translucent fruiting body. Tremelloid or auricularioid. Conjunctive composition — all polysaccharides release simultaneously in warm water. Sub-critical: minimal morphological self-report. Single-step chirality from simple sugar polymers. Single-pass extraction.",
    ['tremella_fuciformis', 'auricularia_auricula_judae', 'tremella_mesenterica', 'dacryopinax_spathularia', 'exidia_glandulosa']
)

# ── Type 7: Puffball Spore Sac ──
_PUFFBALL_SPORE_SAC = FungalType(
    7, "Puffball Spore Sac", "O1",
    ('𐑦', '𐑰', '𐑾', '𐑬', '𐑱', '𐑘', '𐑲', '𐑵', '𐑢', '𐑒', '𐑳', '𐑷'),
    "Spherical enclosed fruiting body, spores mature internally. Fast instantaneous kinetics — rupture releases spore mass. Broadcast spore dispersal maps to broadcast immune signaling. Sub-critical: the exterior gives no pharmaceutical self-report; maturity only known by internal inspection (gleba color).",
    ['calvatia_gigantea', 'lycoperdon_perlatum', 'calvatia_cyathiformis', 'bovista_plumbea', 'lycoperdon_pyriforme']
)

# ── Type 8: Hypogean Ascomycete ──
_HYPOGEAN_ASCOMYCETE = FungalType(
    8, "Hypogean Ascomycete", "O2",
    ('𐑦', '𐑰', '𐑾', '𐑬', '𐑱', '𐑧', '𐑲', '𐑠', '⊙', '𐑒', '𐑳', '𐑭'),
    "Underground or cup-shaped ascomycete. Containment topology from subterranean development. Sequential volatile signaling — aroma compounds release in specific order encoding ripeness. Single-step chirality from simple amino acid and fatty acid derivatives. The underground development IS the scarcity signal.",
    ['tuber_melanosporum', 'tuber_magnatum', 'morchella_esculenta', 'tuber_aestivum', 'terfezia_boudieri', 'choiromyces_meandriformis']
)

# ── Type 9: Rust Smut Pathogen ──
_RUST_SMUT_PATHOGEN = FungalType(
    9, "Rust Smut Pathogen", "O1",
    ('𐑦', '𐑡', '𐑾', '𐑬', '𐑱', '𐑘', '𐑲', '𐑠', '𐑢', '𐑒', '𐑳', '𐑷'),
    "Obligate plant pathogen. Network topology from host tissue colonization. Fast instantaneous spore release. Sequential host tissue degradation. Sub-critical: no morphological self-report of pharmaceutical activity. Used in traditional medicine despite pathogen status.",
    ['ustilago_maydis', 'puccinia_graminis', 'ustilago_esculenta', 'gymnosporangium_juniperi_virginianae']
)

# ── Type 10: Lichen Symbiont ──
_LICHEN_SYMBIONT = FungalType(
    10, "Lichen Symbiont", "O2_dagger",
    ('𐑦', '𐑶', '𐑾', '𐑬', '𐑱', '𐑤', '𐑲', '𐑵', '⊙', '𐑫', '𐑳', '𐑴'),
    "Dual organism: fungus + alga/cyanobacterium. Box-product topology from lichen thallus structure. Broadcast immune + antibiotic signaling. Eternal chirality from unique lichen secondary metabolites (depsides, depsidones, usnic acid). Binary extraction. The symbiosis IS the pharmaceutical encoding.",
    ['usnea_barbata', 'cladonia_rangiferina', 'cetraria_islandica', 'lobaria_pulmonaria', 'parmelia_saxatilis', 'lecanora_esculenta']
)

# ── Type 11: Stinkhorn Emergence ──
_STINKHORN_EMERGENCE = FungalType(
    11, "Stinkhorn Emergence", "O2",
    ('𐑦', '𐑥', '𐑾', '𐑬', '𐑱', '𐑧', '𐑔', '𐑠', '⊙', '𐑫', '𐑳', '𐑭'),
    "Phallaceae: egg stage emergence with fetid gleba on receptacle. Bowtie crossing-point topology — insects land on gleba forming the fungus-insect interface. Slow activated kinetics from gelatinous egg matrix. Sequential volatile compound release: dimethyl oligosulfides attract insects, then polysaccharides mobilize. Self-modeling: the fetid odor IS the ripeness self-report. Eternal chirality from complex volatile compounds. Integer winding triple extraction.",
    ['phallus_impudicus', 'mutinus_caninus', 'clathrus_archeri', 'dictyophora_indusiata', 'phallus_rubicundus', 'clathrus_ruber', 'laternea_triscapa']
)

# ── Type 12: Coral Ramaria ──
_CORAL_RAMARIA = FungalType(
    12, "Coral Ramaria", "O2",
    ('𐑦', '𐑡', '𐑾', '𐑬', '𐑱', '𐑧', '𐑔', '𐑵', '⊙', '𐑖', '𐑳', '𐑭'),
    "Clavarioid/coral: upright branching, no cap-stipe distinction. Branching network topology — each branch terminus is an active growth point. Activated extraction from soft fleshy texture. Broadcast immune signaling: all branch surfaces release beta-glucans simultaneously. Self-modeling: branch tip coloration signals maturity. Two-step chirality from simpler terpenoid scaffolds. Integer winding — triple extraction.",
    ['ramaria_botrytis', 'clavaria_zollingeri', 'clavulinopsis_fusiformis', 'artomyces_pyxidatus', 'ramaria_formosa', 'clavicorona_pyxidata']
)

# ── Type 13: Cup Discus ──
_CUP_DISCUS = FungalType(
    13, "Cup Discus", "O1",
    ('𐑦', '𐑰', '𐑾', '𐑬', '𐑱', '𐑘', '𐑲', '𐑠', '𐑢', '𐑒', '𐑳', '𐑷'),
    "Pezizales: cup or disc-shaped with exposed hymenium. Containment topology — the cup contains the spore-bearing surface. Fast instantaneous spore discharge (phototropic ballistics). Fine powder from ascospores. Sequential release: ascospore germination triggers secondary metabolites. Sub-critical: cup morphology does not strongly self-report pharmaceutical quality. Single-step chirality. Single-pass extraction.",
    ['peziza_badia', 'aleuria_aurantia', 'sarcoscypha_coccinea', 'morchella_esculenta_var', 'gyromitra_esculenta', 'helvella_crispa', 'discina_perlata']
)

# ── Type 14: Earthball Globus ──
_EARTHBALL_GLOBUS = FungalType(
    14, "Earthball Globus", "O1",
    ('𐑦', '𐑰', '𐑾', '𐑬', '𐑱', '𐑤', '𐑲', '𐑵', '𐑢', '𐑖', '𐑳', '𐑷'),
    "Sclerodermataceae: spherical enclosed fruiting body with thick peridium, distinct from puffballs by solid gleba that matures to powdery spore mass. Frozen-order kinetics — the peridium must be broken mechanically. Fine powder from mature spores. Broadcast spore dispersal. Sub-critical: the exterior (thick peridium) gives no signal of internal maturity — gleba color only visible on rupture. Two-step chiral from complex spore metabolites. Single-pass extraction.",
    ['scleroderma_citrinum', 'scleroderma_polyrhizum', 'pisolithus_arhizus', 'scleroderma_verrucosum', 'astraeus_hygrometricus']
)

# ── Type 15: Myxomycete Plasmodium ──
_MYXOMYCETE_PLASMODIUM = FungalType(
    15, "Myxomycete Plasmodium", "O2_dagger",
    ('𐑦', '𐑡', '𐑾', '𐑬', '𐑱', '𐑘', '𐑲', '𐑠', '⊙', '𐑒', '𐑳', '𐑴'),
    "Myxogastria: plasmodial slime mold. Network topology — the acellular plasmodium forms a protoplasmic network that navigates nutrient gradients. Fast instantaneous cytoplasmic streaming (1 mm/s). Fine powder from spores. Sequential life cycle phases: plasmodium → sclerotium → fruiting bodies. Self-modeling CRITICAL: the plasmodium solves mazes, optimizes networks, and anticipates periodic stimuli — the ultimate morphological self-report. Single-step chirality from simple metabolites. Binary winding — two distinct life phases (trophic plasmodium, reproductive fruiting).",
    ['physarum_polycephalum', 'fuligo_septica', 'stemonitis_fusca', 'lycogala_epidendrum', 'arcyria_denudata', 'tubifera_ferruginosa', 'comatricha_nigra']
)

TYPES: list[FungalType] = [
    _BRACKET_POLYPORE,
    _TOOTH_CASCADE,
    _ENTOMOPATHOGENIC_CLUB,
    _GILLED_CAP_AND_STIPE,
    _ROSETTE_CLUSTER,
    _JELLY_GELATINOUS,
    _PUFFBALL_SPORE_SAC,
    _HYPOGEAN_ASCOMYCETE,
    _RUST_SMUT_PATHOGEN,
    _LICHEN_SYMBIONT,
    _STINKHORN_EMERGENCE,
    _CORAL_RAMARIA,
    _CUP_DISCUS,
    _EARTHBALL_GLOBUS,
    _MYXOMYCETE_PLASMODIUM,
]


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
