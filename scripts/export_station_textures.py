#!/usr/bin/env python3
from pathlib import Path
import re,json,zipfile
from io import BytesIO
from PIL import Image
root=Path("data")
out=Path("station_original_assets")
out.mkdir(exist_ok=True)
inventory=[]
for model in sorted((root/"models").rglob("*.model")):
    if not any(k in str(model.relative_to(root)).lower() for k in ("station","spaceport","starport","hangar","orbital","surfaceport","landingpad")): continue
    entry={"model":str(model),"textures":[]}
    written=set()
    with zipfile.ZipFile(out/("__".join(model.relative_to(root).with_suffix("").parts)+".zip"),"w",zipfile.ZIP_DEFLATED) as z:
        z.write(model,str(model))
        for kind,name in sorted(set(re.findall(r'texture\s+(\w+)\s+"([^"]+)"',model.read_text()))):
            candidates=[model.parent/name,root/name,root/name.lstrip("/")]
            tex=next((p for p in candidates if p.is_file()),None)
            item={"kind":kind,"name":name,"path":str(tex) if tex else None}
            entry["textures"].append(item)
            if tex is None or str(tex) in written: continue
            written.add(str(tex))
            z.write(tex,str(tex))
            try:
                with Image.open(tex) as im:
                    item.update(size=im.size,mode=im.mode)
                    buf=BytesIO()
                    im.convert("RGBA").save(buf,format="PNG")
                    z.writestr("reference/"+str(tex.relative_to(root)).replace("/","__")+".png",buf.getvalue())
            except Exception as e:
                item["error"]=str(e)
        z.writestr("manifest.json",json.dumps(entry,indent=2))
    inventory.append(entry)
(out/"inventory.json").write_text(json.dumps(inventory,indent=2))
print(f"{len(inventory)} candidate models exported to {out.resolve()}")
