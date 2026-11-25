# Portrait audit

Verified source: src/FaceParts.cpp, src/FaceParts.h, data/pigui/libs/face.lua, src/pigui/PiGui.cpp, COMPILING.txt.

FaceParts scans data/facegen/species_* and uses SDL surfaces, selectors and deterministic seeded descriptors. Output 295x285; eyes y41, nose y89, mouth y155, clothing y135. PickFaceParts consumes RNG even for explicit features. Lua derives faceDescription from character.seed and passes descriptor and seed to PiGui.Modules.Face. Editor regenerates texture on feature changes. Do not change existing descriptor semantics or asset counts.

## Decision
Add optional full-image NPC portraits, deterministic selection by seed and gender/armour constraints, preserve classic editor and fallback for missing assets. Use original fictional subjects, consistent neutral framing, industrial clothing, no logos. Prototype 512x512 source cropped to 295:285 aspect, mobile 296x286 or 512-class texture, desktop 1024-class optional. Animation: aligned neutral/blink frames, timed display, no per-frame disk loading, bounded texture cache. Lip sync deferred until dialogue/audio integration. No generated portraits committed yet.

## Build audit
COMPILING.txt confirms Linux CMake, Windows MSVC or MSYS2, portable data directory, modelcompiler build-data target. Baseline must precede engine changes. Stable tag and exact workflow path still unverified; attempted .github/workflows/build.yml and src/pigui/PiGuiFace.cpp returned 404. No build or runtime tests performed.
