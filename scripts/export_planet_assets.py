from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parents[1]
keys = ("terrain","planet","geosphere","geopatch","atmosphere","gasgiant","cloud","noise","perlin","ring")
out = root / "planet_original_assets.zip"
count = 0
with ZipFile(out, "w", ZIP_DEFLATED) as z:
    for folder in ("src", "data"):
        for p in sorted((root / folder).rglob("*")):
            rel = p.relative_to(root).as_posix()
            if p.is_file() and (any(k in rel.lower() for k in keys) or rel.startswith("data/shaders/")):
                z.write(p, rel)
                count += 1
with ZipFile(out) as z:
    assert z.testzip() is None
print(f"Archivos exportados: {count}")
print(f"ZIP: {out} ({out.stat().st_size / 1048576:.1f} MB)")
