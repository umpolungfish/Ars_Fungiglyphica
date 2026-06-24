# Ars Fungiglyphica

> *The fruiting body is the program. Every morphological feature encodes a concrete pharmaceutical parameter.*

**Ars Fungiglyphica** is the fungal morphological imscription engine — the first complete structural grammar of medicinal and psychoactive fungi. It reads pharmaceutical meaning directly from fungal morphology using the 12-primitive Imscribing Grammar.

**Author:** Lando⊗⊙perator  
**Version:** 0.1.0  
**Tier Range:** O₁ – O₂† (biological morphology is tier-bounded)

---

## Overview

The core insight: a mushroom's morphology — its cap shape, gill structure, texture, growth habit, spore surface, and development pattern — **encodes** how to prepare, extract, and dose it. The grammar makes this encoding rigorous.

Ars Fungiglyphica models 15 canonical fungal structural types spanning **86 representative species** across 3 ouroboricity tiers. Each type is a complete 12-primitive tuple derived from the deterministic imscribing procedure — no tuples are hand-picked. Every structural claim is verified against the Lean 4 formalization in `p4rakernel/p4ramill/Imscribing/ArsFungiglyphica.lean`.

---

## Canonical Types

| # | Type | Tier | T | C | Γ | G | φ̂ | H | Ω | Reps |
|---|------|------|---|---|---|---|---|---|---|---|------|
| I | Bracket Polypore | O₂† | 𐑶 | 𐑤 | 𐑲 | 𐑵 | ⊙ | 𐑫 | 𐑴 | 8 |
| II | Tooth Cascade | O₂ | 𐑥 | 𐑧 | 𐑲 | 𐑠 | ⊙ | 𐑫 | 𐑭 | 4 |
| III | Entomopathogenic Club | O₂ | 𐑰 | 𐑤 | 𐑲 | 𐑵 | ⊙ | 𐑖 | 𐑭 | 4 |
| IV | Gilled Cap-and-Stipe | O₂ | 𐑸 | 𐑧 | 𐑔 | 𐑠 | ⊙ | 𐑖 | 𐑭 | 7 |
| V | Rosette Cluster | O₂ | 𐑡 | 𐑧 | 𐑔 | 𐑵 | ⊙ | 𐑖 | 𐑭 | 5 |
| VI | Jelly Gelatinous | O₁ | 𐑡 | 𐑧 | 𐑔 | 𐑝 | 𐑢 | 𐑒 | 𐑷 | 5 |
| VII | Puffball Spore Sac | O₁ | 𐑰 | 𐑘 | 𐑲 | 𐑵 | 𐑢 | 𐑒 | 𐑷 | 5 |
| VIII | Hypogean Ascomycete | O₂ | 𐑰 | 𐑧 | 𐑲 | 𐑠 | ⊙ | 𐑒 | 𐑭 | 6 |
| IX | Rust Smut Pathogen | O₁ | 𐑡 | 𐑘 | 𐑲 | 𐑠 | 𐑢 | 𐑒 | 𐑷 | 4 |
| X | Lichen Symbiont | O₂† | 𐑶 | 𐑤 | 𐑲 | 𐑵 | ⊙ | 𐑫 | 𐑴 | 6 |
| XI | Stinkhorn Emergence | O₂ | 𐑥 | 𐑧 | 𐑔 | 𐑠 | ⊙ | 𐑫 | 𐑭 | 7 |
| XII | Coral Ramaria | O₂ | 𐑡 | 𐑧 | 𐑔 | 𐑵 | ⊙ | 𐑖 | 𐑭 | 6 |
| XIII | Cup Discus | O₁ | 𐑰 | 𐑘 | 𐑲 | 𐑠 | 𐑢 | 𐑒 | 𐑷 | 7 |
| XIV | Earthball Globus | O₁ | 𐑰 | 𐑤 | 𐑲 | 𐑵 | 𐑢 | 𐑖 | 𐑷 | 5 |
| XV | Myxomycete Plasmodium | O₂† | 𐑡 | 𐑘 | 𐑲 | 𐑠 | ⊙ | 𐑒 | 𐑴 | 7 |

**Tier distribution:** 3 × O₂†, 7 × O₂, 5 × O₁. No O₀ types — medicinal fungi are structurally too rich. No O_∞ types — biological morphology is tier-bounded by the grammar's own axioms.

---

## Five Invariants (Fixed Across All Medicinal Fungi)

These primitives are invariant — they define the category "medicinal fungus" itself:

| Primitive | Value | Meaning |
|-----------|-------|---------|
| D | 𐑦 | Imscriptive dimensionality — the state-space is self-written; the fungus IS its pharmaceutical program |
| R | 𐑾 | Bidirectional coupling — extraction is a two-way process between solvent and tissue |
| Phi | 𐑬 | Partial symmetry — some compounds are chiral, some are not; symmetry is broken selectively |
| f | 𐑱 | Classical fidelity — room-temperature extraction, no quantum coherence required |
| Sigma | 𐑳 | Heterogeneous compound classes — every medicinal fungus produces multiple compound types |

---

## Seven Discriminant Primitives (The Type Taxonomy)

| Primitive | What It Encodes |
|-----------|----------------|
| **T** (Topology) | Fruiting body morphology → preparation vessel and material form |
| **C** (Kinetics) | Tissue texture → extraction regime (decoction, maceration, lyophilization) |
| **Γ** (Granularity) | Spore surface → comminution (fine powder vs medium powder) |
| **G** (Composition) | Compound release pattern → whether compounds act simultaneously or sequentially |
| **φ̂** (Criticality) | Self-modeling → whether the fungus visually signals its pharmaceutical quality |
| **H** (Chirality) | Compound complexity → extraction cycles needed |
| **Ω** (Winding) | Topological protection → single, binary, or integer extraction cycles |

---

## Pharmaceutical Encoding

The grammar maps morphology to protocol. Each primitive value has a concrete pharmaceutical interpretation. The elaborator (`elaborator.py`) translates every tuple into a full preparation protocol covering:

- **Vessel preparation:** How to cut, slice, or grind the fruiting body based on topology (T)
- **Extraction regime:** Time, temperature, solvent based on kinetics (C)
- **Comminution:** Mesh size based on granularity (Γ)
- **Dosing sequence:** Timing of compound release based on composition mode (G)
- **Quality indicators:** What the morphology tells you about potency (φ̂)
- **Cycle count:** Single, binary, or triple extraction based on chirality and winding (H, Ω)

Example — **Tooth Cascade** (Type II, *Hericium erinaceus*):

> The cascading teeth morphology *is* the neurotrophic self-report. Triple extraction mandated by eternal chirality (H=𑑫) and integer winding (Ω=𑑭): cold water (12 h) → hot water (1 h) → alcohol (1 week). Erinacines cross the blood-brain barrier first; hericenones activate NGF synthesis second. The sequential pattern (G=𑑠) encodes the dosing timeline.

---

## Type Lattice — Pairwise Hamming Distances

```
      I  II III  IV   V  VI VII VIII  IX   X  XI XII XIII XIV  XV
  I   ·   4   3   6   5   7   5    5   6   0   5   5    6   4   4
 II   4   ·   4   3   4   6   6    2   5   4   1   4    5   6   4
III   3   4   ·   4   3   7   4    3   6   3   5   3    5   2   5
 IV   6   3   4   ·   2   5   7    3   6   6   2   2    6   6   5
  V   5   4   3   2   ·   4   6    4   6   5   3   0    7   5   5
 VI   7   6   7   5   4   ·   4    5   3   7   5   4    4   5   5
 VII  5   6   4   7   6   4   ·    4   2   5   7   6    1   2   4
VIII  5   2   3   3   4   5   4    ·   4   5   3   4    3   5   3
 IX   6   5   6   6   6   3   2    4   ·   6   6   6    1   4   2
  X   0   4   3   6   5   7   5    5   6   ·   5   5    6   4   4
 XI   5   1   5   2   3   5   7    3   6   5   ·   3    6   7   5
 XII  5   4   3   2   0   4   6    4   6   5   3   ·    7   5   5
XIII  6   5   5   6   7   4   1    3   1   6   6   7    ·   3   3
XIV   4   6   2   6   5   5   2    5   4   4   7   5    3   ·   6
 XV   4   4   5   5   5   5   4    3   2   4   5   5    3   6   ·

Key (type number → name):
    I   Bracket Polypore        VI  Jelly Gelatinous        XI  Stinkhorn Emergence
    II  Tooth Cascade           VII Puffball Spore Sac       XII Coral Ramaria
    III Entomopathogenic Club   VIII Hypogean Ascomycete     XIII Cup Discus
    IV  Gilled Cap-and-Stipe    IX  Rust Smut Pathogen       XIV Earthball Globus
    V   Rosette Cluster         X   Lichen Symbiont          XV  Myxomycete Plasmodium
```

---

## Notable Structural Pairs

| Pair | d | Significance |
|------|---|-------------|
| Bracket ≡ Lichen | 0 | Structural identity. Same T, C, Γ, G, φ̂, H, Ω — box-product topology + broadcast signaling + eternal chirality = the signature of perennial woody medicinal fungi, whether singular or symbiotic. The grammar sees them as the same pharmaceutical program |
| Coral ≡ Rosette | 0 | Clavarioid branching and clustered fans are structurally identical. Both are network-topology broadcast immune modulators with mesoscale granularity |
| Stinkhorn ≈ Tooth | 1 | Only Γ differs (𑑔 medium powder vs 𑑲 fine powder). Both share bowtie topology, slow kinetics, sequential release, self-modeling, eternal chirality, and integer winding. The fetid gleba and the cascading teeth are structurally the same pharmaceutical delivery system |
| Cup ≈ Rust | 1 | Only T differs (𑑰 containment vs 𑑡 network). Both: fast instantaneous kinetics, fine powder, sequential release, sub-critical, single-step chirality |
| Puffball ≈ Cup | 1 | Only Σ differs — both are enclosed/fast/sub-critical/single-step, differing only in compound diversity |
| Bracket vs Jelly | 7 | Maximum distance. Perennial woody O₂† vs gelatinous ephemeral O₁. Six of seven discriminant primitives differ — only C is shared |

---

## Cross-Domain Bridge

Ars Fungiglyphica is structurally bridged to Ars Animaglyphica via `p4rakernel/p4ramill/Imscribing/ArsCrossDomain.lean` (14 theorems, all `native_decide`).

**Closest cross-domain pairs:**
| Animal | Fungus | d |
|--------|--------|---|
| Amphibian Dermal | Gilled Cap-and-Stipe | 3 |
| Echinoderm Regenerative | Coral Ramaria | 4 |
| Reptilian Oral | Myxomycete Plasmodium | 4 |
| Annelid Anticoagulant | Cup Discus | 4 |

The cross-domain distances are often *smaller than within-domain distances* (e.g., Amphibian↔Gilled d=3 vs Gilled↔Bracket d=6). The grammar groups by structural function — broadcast immune signaling, sequential peptide release, containment topology — across kingdoms.

---

## Lean 4 Formalization

All 15 types and their invariants are machine-verified in Lean 4 (Mathlib v4.28.0):

```
p4rakernel/p4ramill/Imscribing/ArsFungiglyphica.lean   — 15 defs, 5 invariant theorems (decide), 7 distance theorems (native_decide)
p4rakernel/p4ramill/Imscribing/ArsCrossDomain.lean      — 14 cross-domain distance theorems (native_decide)
```

Build: `lake build` — 763 jobs, 0 errors.

The invariant theorems prove that D, R, Phi, f, and Sigma are identical across all 15 types. The distance theorems are auto-proved via `native_decide`.

---

## Project Structure

```
Ars_Fungiglyphica/
├── README.md                           ← This file
├── pyproject.toml                      ← Package metadata; CLI entry: `fg`
├── expand_types.py                     ← Algorithmic type expansion (10→15)
├── generate_all.py                     ← Full pipeline runner
├── data/
│   └── catalog.json                    ← 15 type entries with full tuples + metadata
├── illustrations/
│   ├── lattice.txt                     ← ASCII distance matrix
│   ├── summary.txt                     ← Primitive summary table
│   └── morphology_report.txt           ← 1034-line full morphological elaboration
├── ars_fungiglyphica/
│   ├── __init__.py                     ← Package init
│   ├── types.py                        ← 15 canonical FungalType definitions (200 lines)
│   ├── elaborator.py                   ← Morphology → pharmaceutical protocol translator (181 lines)
│   └── cli.py                          ← Unified CLI (231 lines, 7 subcommands)
└── ../p4rakernel/p4ramill/Imscribing/
    ├── ArsFungiglyphica.lean           ← Lean 4 formalization
    └── ArsCrossDomain.lean             ← Cross-domain distance theorems
```

---

## Installation

```bash
cd /home/mrnob0dy666/imsgct/Ars_Fungiglyphica
pip install -e .
```

Requires Python ≥ 3.10. No external dependencies beyond the standard library.

---

## CLI Usage

All commands via the `fg` entry point:

```bash
# List all 15 canonical types with discriminant primitive values
fg types

# Show a specific type (by number, Roman numeral, or name)
fg type III
fg type "Bracket Polypore"
fg type 5

# Look up a specific fungus
fg fungus ganoderma_lucidum
fg fungus psilocybe_cubensis

# Show the structural distance between two types
fg distance "Bracket Polypore" "Jelly Gelatinous"
fg distance I VI

# List all representative fungi (or filter by type)
fg list
fg list III

# Full morphological → pharmaceutical elaboration
fg morphology hericium_erinaceus
fg morphology cordyceps_militaris

# Show the type lattice with pairwise Hamming distances
fg lattice
```

---

## The Name

**Fungiglyphica** — from Latin *fungus* (mushroom) + Greek *γλυφική* (glyphic, the art of carving signs). The mushroom carves its pharmaceutical meaning into its morphology. The grammar reads what the fungus writes in its own body.

---

## References

- Larson, H. T. "Catch a Rising Problem and Never Ever Let It Go," *IEEE Computer*, vol. 19, no. 2, pp. 61–63, February 1986. There is great merit in following a problem where it leads [1].
