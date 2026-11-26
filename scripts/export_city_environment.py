#!/usr/bin/env python3
from pathlib import Path
import json,re,zipfile
from io import BytesIO
from PIL import Image
root=Path("data")
out=Path("city_environment_original.zip")
inventory=[]
written=set()
def add(z,p):
    if p.is_file() and str(p) not in written:
        z.write(p,str(p))
        written.add(str(p))
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
    for model in sorted((root/"models").rglob("*.model")):
        if not any(k in str(model).lower() for k in ("city","cities","building","settlement","colony","vegetation","tree")): continue
        add(z,model)
        entry={"model":str(model),"textures":[]}
        for kind,name in sorted(set(re.findall(r'texture\s+(\w+)\s+"([^"]+)"',model.read_text()))):
            tex=next((p for p in (model.parent/name,root/name.lstrip("/")) if p.is_file()),None)
            item={"kind":kind,"name":name,"path":str(tex) if tex else None}
            entry["textures"].append(item)
            if tex is None: continue
            add(z,tex)
            try:
                with Image.open(tex) as im:
                    item.update(size=im.size,mode=im.mode)
                    ref="reference/"+str(tex.relative_to(root))+".png"
                    if ref not in written:
                        b=BytesIO()
                        im.convert("RGBA").save(b,format="PNG")
                        z.writestr(ref,b.getvalue())
                        written.add(ref)
            except Exception as e: item["error"]=str(e)
        inventory.append(entry)
    environment=[]
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() in (".png",".dds",".jpg",".jpeg",".glsl",".frag",".vert") and any(k in str(p).lower() for k in ("terrain","planet","atmosphere","skybox","starfield","galaxy","cloud","geosphere","milkyway")):
            environment.append(str(p))
    z.writestr("inventory.json",json.dumps({"city_models":inventory,"environment_candidates":environment},indent=2))
print(f"{len(inventory)} city models; {len(environment)} environment candidates; {out.resolve()}")
