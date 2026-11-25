# Pioneer: Deep Space

Checkpoint 2026-11-24 — independent fork; preserve upstream master.

## Mandate
Photorealistic industrial hard science fiction, original fictional characters, animated portraits, HD ship materials, cockpit and station art. Preserve simulation and offline operation. Generate art during development with ChatGPT, not runtime APIs. Windows/Winlator first, native Android ARM64 later. Artistic decisions delegated to assistant.

## Verified initial audit
Upstream CMake: C++17, SDL2, SDL2_image, Assimp >=5, Lua, GLEW, desktop OpenGL, FreeType, sigc++, Vorbis, optional OpenAL, ImGui, unit tests, host modelcompiler for cross builds. ARM64 Raspberry Pi option reduces desktop GL requirements to 3.1; not GLES compatibility. Upstream master reports 20260907-dev; stable release tag still to pin. GPLv3 engine; audit individual asset licenses and preserve attribution. Do not submit AI-generated changes upstream.

## Ordered gates
- [x] Fork access and isolated develop branch
- [ ] Pin stable release and inventory source/assets
- [ ] Reproduce Windows/Linux build and unit tests
- [ ] Locate portrait compositor and deterministic identity mapping
- [ ] Prototype photoreal portrait and blink animation, fallback to classic portraits
- [ ] Inventory ship UVs/materials and prototype one ship without altering geometry
- [ ] Add optional asset packs, provenance and mobile texture budgets
- [ ] Validate Winlator visual quality and performance
- [ ] Audit Android NDK dependencies, GLES shaders, storage and touch
- [ ] Build and test native APK

## Constraints
No claims of successful compilation or runtime until tested. Keep original assets and saves compatible where practical. No destructive changes to upstream master. Minimize Actions artifact retention (1 day for temporary builds); no large generated binaries in Git. Record commits, tests, failures and next action here. User wants minimal interruptions, only essential blockers or test requests. No background execution implied.
