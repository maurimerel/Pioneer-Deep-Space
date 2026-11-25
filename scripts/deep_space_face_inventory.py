#!/usr/bin/env python3
"""Inventory original facegen assets without modifying game data."""
import csv
from collections import Counter
from pathlib import Path
from PIL import Image
import sys

root = Path(__file__).resolve().parents[1] / "data/facegen"
out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("face_inventory.csv")
counts = Counter()
errors = []
with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["path", "width", "height", "mode", "alpha_min", "alpha_max", "alpha_bbox"])
    for path in sorted(root.rglob("*.png")):
        try:
            with Image.open(path) as im:
                alpha = im.convert("RGBA").getchannel("A")
                lo, hi = alpha.getextrema()
                writer.writerow([path.relative_to(root), *im.size, im.mode, lo, hi, alpha.getbbox()])
                counts[str(path.parent.relative_to(root))] += 1
        except Exception as exc:
            errors.append((str(path), str(exc)))
for group, count in sorted(counts.items()):
    print(f"{group}: {count}")
print(f"Total: {sum(counts.values())}; errors: {len(errors)}; CSV: {out}")
for path, error in errors:
    print(path, error, file=sys.stderr)
sys.exit(1 if errors or not counts else 0)
