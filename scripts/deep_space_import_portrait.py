"""Import original Deep Space portrait frames into game data."""
import argparse
from pathlib import Path
import re
from PIL import Image, ImageOps

def main():
    p = argparse.ArgumentParser()
    p.add_argument("identity")
    p.add_argument("neutral", type=Path)
    p.add_argument("--blink", type=Path)
    p.add_argument("--size", type=int, choices=(256,512,1024), default=512)
    a = p.parse_args()
    if not re.fullmatch(r"[a-z0-9_]+", a.identity):
        p.error("Invalid identity")
    root = Path(__file__).resolve().parents[1]
    out = root / "data" / "deep-space" / "portraits" / a.identity
    frames = {}
    for name, source in (("neutral", a.neutral), ("blink", a.blink)):
        if source is None:
            continue
        with Image.open(source) as im:
            frames[name] = ImageOps.fit(ImageOps.exif_transpose(im).convert("RGB"), (a.size,a.size), Image.Resampling.LANCZOS)
    out.mkdir(parents=True, exist_ok=True)
    for name, frame in frames.items():
        target = out / (name + ".png")
        frame.save(target, optimize=True)
        print(target.relative_to(root), target.stat().st_size)
if __name__ == "__main__":
    main()
