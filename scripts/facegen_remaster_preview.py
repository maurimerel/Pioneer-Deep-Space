#!/usr/bin/env python3
"""Offline preview of native FaceGen composition. Requires Pillow."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw
p=argparse.ArgumentParser()
p.add_argument("--root",type=Path,default=Path("data/facegen"))
p.add_argument("--race",default="race_0")
p.add_argument("--gender",type=int,choices=[0,1],default=1)
p.add_argument("--output",type=Path,default=Path("facegen_preview.png"))
p.add_argument("--count",type=int,default=12)
p.add_argument("--isolate",choices=["head","eyes","nose","mouth","hair","clothes","accessories"])
a=p.parse_args()
species=sorted(a.root.glob("species_*"))[0]
race=species/a.race
def parts(folder,prefix):
    result=[]
    for f in sorted(folder.glob(prefix+"*.png")):
        suffix=f.stem[len(prefix):]
        if suffix.isdigit() or suffix.split("_")[0]==str(a.gender):
            result.append(f)
    return result
layers=[
("head",parts(race/"head","head_"),0,0),
("clothes",parts(species/"clothes","cloth_"),0,135),
("eyes",parts(race/"eyes","eyes_"),0,41),
("nose",parts(race/"nose","nose_"),1,89),
("mouth",parts(race/"mouth","mouth_"),0,155),
("accessories",sorted((species/"accessories").glob("acc_*.png")),0,0),
("hair",parts(race/"hair","hair_"),0,0)]
def overlay(canvas,path,x,y):
    with Image.open(path) as source:
        im=source.convert("RGBA")
    pos=(0,0) if im.size==(295,285) else ((295-im.width)//2+x,y)
    canvas.alpha_composite(im,pos)
count=max(1,min(a.count,100))
sheet=Image.new("RGB",(295*4,315*((count+3)//4)),(28,28,28))
draw=ImageDraw.Draw(sheet)
for i in range(count):
    face=Image.new("RGBA",(295,285))
    bg=a.root/"backgrounds/general.png"
    if bg.exists(): overlay(face,bg,0,0)
    labels=[]
    for j,(name,files,x,y) in enumerate(layers):
        if not files: continue
        if a.isolate and name not in ("head",a.isolate): continue
        index=(i if not a.isolate or name==a.isolate else 0)%len(files)
        overlay(face,files[index],x,y)
        labels.append(name+":"+str(index))
    x,y=(i%4)*295,(i//4)*315
    sheet.paste(face,(x,y),face)
    draw.text((x+4,y+288)," ".join(labels[:4]),fill="white")
    draw.text((x+4,y+300)," ".join(labels[4:]),fill="white")
sheet.save(a.output)
print(a.output)
for name,files,_,_ in layers: print(name,len(files))
