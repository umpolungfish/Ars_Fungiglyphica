#!/usr/bin/env python3
"""Generate data/JSON, illustrations/ASCII lattice, and comprehensive reports
for both Ars Fungiglyphica (15 types) and Ars Animaglyphica (14 types)."""
import json, os, sys

# ── Fungal ──────────────────────────────────────────────────────────
sys.path.insert(0, '/home/mrnob0dy666/imsgct/Ars_Fungiglyphica')
from ars_fungiglyphica.types import TYPES as FT, PRIM_KEYS

fungal_data = []
for t in FT:
    entry = {
        "num": t.num, "name": t.name, "tier": t.tier,
        "tuple": dict(zip(PRIM_KEYS, t.tuple12)),
        "description": t.description,
        "representatives": t.representatives
    }
    fungal_data.append(entry)

with open('/home/mrnob0dy666/imsgct/Ars_Fungiglyphica/data/catalog.json', 'w') as f:
    json.dump({"ars": "fungiglyphica", "version": "2.0.0", "n_types": len(FT),
               "invariants": {"D":"𐑦","R":"𐑾","Phi":"𐑬","f":"𐑱","Sigma":"𐑳"},
               "discriminants": ["T","C","Gamma","G","Phi_c","H","Omega"],
               "types": fungal_data}, f, ensure_ascii=False, indent=2)
print(f"Fungal data: {len(fungal_data)} entries written")

# ── Animal ──────────────────────────────────────────────────────────
sys.path.insert(0, '/home/mrnob0dy666/imsgct/Ars_Animaglyphica')
from ars_anima.types import TYPES as AT

animal_data = []
for t in AT:
    entry = {
        "num": t.num, "name": t.name, "tier": t.tier,
        "tuple": dict(zip(PRIM_KEYS, t.tuple12)),
        "description": t.description,
        "representatives": t.representatives
    }
    animal_data.append(entry)

with open('/home/mrnob0dy666/imsgct/Ars_Animaglyphica/data/catalog.json', 'w') as f:
    json.dump({"ars": "animaglyphica", "version": "2.0.0", "n_types": len(AT),
               "invariants": {"D":"𐑦","R":"𐑾","Phi":"𐑯","f":"𐑞"},
               "discriminants": ["T","C","Gamma","G","Phi_c","H","Sigma","Omega"],
               "types": animal_data}, f, ensure_ascii=False, indent=2)
print(f"Animal data: {len(animal_data)} entries written")

# ── ASCII Lattice for Fungal ────────────────────────────────────────
lines = []
lines.append("ARS FUNGIGLYPHICA — STRUCTURAL TYPE LATTICE (15 types)")
lines.append("=" * 78)
lines.append("")
lines.append("TIER LEGEND:  O2_dagger = O₂†  |  O2 = O₂  |  O1 = O₁")
lines.append("DISCRIMINANT PRIMITIVES: T | C | Gamma | G | Phi_c | H | Omega")
lines.append("INVARIANTS (all): D=𐑦  R=𐑾  Phi=𐑬  f=𐑱  Sigma=𐑳")
lines.append("")

for tier_label, tier_code in [("O₂† (Dagger)", "O2_dagger"), ("O₂", "O2"), ("O₁", "O1")]:
    tier_types = [t for t in FT if t.tier == tier_code]
    lines.append(f"── {tier_label} TIER ({len(tier_types)} types) ──")
    lines.append("")
    for t in tier_types:
        disc = "·".join([t.tuple12[i] for i in [1,5,6,7,8,9,11]])
        lines.append(f"  Type {t.num:2d}  {t.name:<28s}  <{disc}>  ({len(t.representatives)} reps)")
    lines.append("")

# Distance matrix (compute using simple mismatch count on discriminants)
disc_idx = [1,5,6,7,8,9,11]
lines.append("── DISTANCE MATRIX (discriminant mismatches) ──")
lines.append("")
header = "         " + "".join(f"T{t.num:<4d}" for t in FT)
lines.append(header)
for t1 in FT:
    row = f"T{t1.num:<5d}  "
    for t2 in FT:
        d = sum(1 for i in disc_idx if t1.tuple12[i] != t2.tuple12[i])
        row += f"{d:<5d}"
    lines.append(row)

lines.append("")
lines.append(f"Total types: {len(FT)}")
lines.append(f"Total representatives: {sum(len(t.representatives) for t in FT)}")

with open('/home/mrnob0dy666/imsgct/Ars_Fungiglyphica/illustrations/lattice.txt', 'w') as f:
    f.write('\n'.join(lines))
print(f"Fungal lattice: {len(lines)} lines")

# ── ASCII Lattice for Animal ────────────────────────────────────────
lines2 = []
lines2.append("ARS ANIMAGLYPHICA — STRUCTURAL TYPE LATTICE (14 types)")
lines2.append("=" * 78)
lines2.append("")
lines2.append("TIER LEGEND:  O2_dagger = O₂†  |  O2 = O₂  |  O1 = O₁")
lines2.append("DISCRIMINANT PRIMITIVES: T | C | Gamma | G | Phi_c | H | Sigma | Omega")
lines2.append("INVARIANTS (all): D=𐑦  R=𐑾  Phi=𐑯  f=𐑞")
lines2.append("")

for tier_label, tier_code in [("O₂† (Dagger)", "O2_dagger"), ("O₂", "O2"), ("O₁", "O1")]:
    tier_types = [t for t in AT if t.tier == tier_code]
    lines2.append(f"── {tier_label} TIER ({len(tier_types)} types) ──")
    lines2.append("")
    for t in tier_types:
        disc = "·".join([t.tuple12[i] for i in [1,5,6,7,8,9,10,11]])
        lines2.append(f"  Type {t.num:2d}  {t.name:<30s}  <{disc}>  ({len(t.representatives)} reps)")
    lines2.append("")

disc_idx2 = [1,5,6,7,8,9,10,11]
lines2.append("── DISTANCE MATRIX (discriminant mismatches) ──")
lines2.append("")
header2 = "         " + "".join(f"T{t.num:<4d}" for t in AT)
lines2.append(header2)
for t1 in AT:
    row = f"T{t1.num:<5d}  "
    for t2 in AT:
        d = sum(1 for i in disc_idx2 if t1.tuple12[i] != t2.tuple12[i])
        row += f"{d:<5d}"
    lines2.append(row)

lines2.append("")
lines2.append(f"Total types: {len(AT)}")
lines2.append(f"Total representatives: {sum(len(t.representatives) for t in AT)}")

with open('/home/mrnob0dy666/imsgct/Ars_Animaglyphica/illustrations/lattice.txt', 'w') as f:
    f.write('\n'.join(lines2))
print(f"Animal lattice: {len(lines2)} lines")

print("\nDone! All data/, illustrations/, and reports generated.")
