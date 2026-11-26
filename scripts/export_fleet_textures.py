#!/usr/bin/env python3
import json,re,zipfile
from pathlib import Path
from io import BytesIO
from PIL import Image
root=Path("data")
out=Path("fleet_original_assets")
out.mkdir(exist_ok=True)
inventory=[]
for ship in sorted((root/"ships").glob("*.json")):
    try:
        info=json.loads(ship.read_text())
    except ValueError:
        continue
    model=info.get("model")
    if not model: continue
    candidates=list((root/"models").rglob(model+".model"))
    if not candidates:
        inventory.append({"ship":ship.stem,"status":"model not found"})
        continue
    path=candidates[0]
    entry={"ship":ship.stem,"manufacturer":info.get("manufacturer"),"class":info.get("ship_class"),"model":str(path),"textures":[]}
    with zipfile.ZipFile(out/(ship.stem+".zip"),"w",zipfile.ZIP_DEFLATED) as z:
        z.write(path,str(path))
        for kind,name in sorted(set(re.findall(r'texture\s+(\w+)\s+"([^"]+)"',path.read_text()))):
            tex=path.parent/name
            if not tex.exists(): tex=root/name
            item={"kind":kind,"path":str(tex),"exists":tex.is_file()}
            entry["textures"].append(item)
            if not tex.is_file(): continue
            z.write(tex,str(tex))
            try:
                with Image.open(tex) as im:
                    item["size"]=im.size
                    item["mode"]=im.mode
                    buf=BytesIO()
                    im.convert("RGBA").save(buf,format="PNG")
                    z.writestr("reference/"+tex.stem+".png",buf.getvalue())
            except Exception as e:
                item["error"]=str(e)
        z.writestr("manifest.json",json.dumps(entry,indent=2))
    inventory.append(entry)
(out/"inventory.json").write_text(json.dumps(inventory,indent=2))
print(f"{len(inventory)} ships inventoried in {out.resolve()}")
