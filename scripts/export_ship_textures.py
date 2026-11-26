#!/usr/bin/env python3
import argparse, zipfile, re, json, hashlib
from pathlib import Path
from PIL import Image
from io import BytesIO

p=argparse.ArgumentParser()
p.add_argument("ship",nargs="?",default="coronatrix")
a=p.parse_args()
folder=Path("data/models/ships")/a.ship
model=folder/(a.ship+".model")
assert model.is_file(), model
out=Path(a.ship+"_original_assets.zip")
manifest=[]
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
    z.write(model,str(model))
    for name in sorted(set(re.findall(r'texture\s+\w+\s+"([^"]+)"',model.read_text()))):
        path=folder/name
        with Image.open(path) as im:
            info={"path":str(path),"size":im.size,"mode":im.mode,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()}
            manifest.append(info)
            buf=BytesIO()
            im.convert("RGBA").save(buf,format="PNG")
            z.writestr("reference/"+path.stem+".png",buf.getvalue())
        z.write(path,str(path))
    z.writestr("manifest.json",json.dumps(manifest,indent=2))
print(out)
