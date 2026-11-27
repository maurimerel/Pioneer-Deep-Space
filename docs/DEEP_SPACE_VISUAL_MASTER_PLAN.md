# Pioneer: Deep Space — Visual master plan

Approved direction, 2026-11-25.

## Mission
Comprehensively remaster Pioneer using generative AI as an offline artistic production tool. Replace all original visual textures with improved assets, preserving the simulation, economy, procedural universe and gameplay. No runtime AI service or paid generation dependency. Independent fork; respect upstream and individual asset licenses.

## Art direction
Photorealistic, cinematic industrial hard science fiction, coherent materials, lighting, scale and visual language. Attractive, diverse characters and functional futuristic equipment. Avoid arbitrary stylistic changes between assets.

## Roadmap
1. FaceGen: remaster all original heads, eyes, noses, mouths, hair, clothing, accessories, armour and backgrounds. Preserve filenames, selectors, counts and compatibility; validate layer alignment and jaw clipping. Animation later.
2. Ships: diffuse, normal, specular and emissive textures, preserve UV mapping; cockpit and materials.
3. Buildings, stations, hangars and cities.
4. Planetary terrain, surfaces, vegetation, water and atmosphere.
5. Space backgrounds, stars, rings, propulsion and lighting.
6. UI: menus, icons, HUD, maps, navigation and communications.
7. Immersion: animation, effects, lighting and ambience.
8. Optimization and testing on Linux, Windows/Winlator, and eventual native Android.

## Workflow
Inventory original assets; use each as geometry/UV/alpha reference; generate improved art; calibrate and validate offline; test in engine; commit in small reversible batches. Preserve originals in Git. Track each asset as pending, generated, calibrated, integrated or verified. Use original dimensions initially; evaluate HD upgrades after compatibility and performance tests. Preserve gameplay and saved-character semantics.

## Current checkpoint
Native layered editor restored (6085e4553bbc5397e2bab1deb19fd894a53c787e). Offline compositor added (bcf13377867e2bc2021ac1f18355aeecdd73a805), not yet validated locally. User confirmed prototype layers appear in game, but female jaw clipping remains. Next: inspect original head variants, diagnose clipping, calibrate replacement heads, then other facial parts. Full visual remaster not yet implemented.

## Checkpoint — 2026-11-27
Local Linux Release O2 startup verified by user and build log (372/372 tasks, 11.08 s reported). AMD Vega 3, Mesa 25.2.8, OpenGL 4.6 hardware rendering. Build directory `build-release-o2`; configure Release with `-DCMAKE_C_FLAGS_RELEASE="-O2 -g -DNDEBUG" -DCMAKE_CXX_FLAGS_RELEASE="-O2 -g -DNDEBUG" -DUSE_SSE42=OFF`. O3 crashes during DDS upload; O2 is a workaround, not a root-cause fix. Clean shutdown and extended gameplay remain unverified. Local asset packs and source changes must be reconciled before editing the same files remotely. Next: inventory current terrain shaders and materials, improve orbit-to-surface transitions, preserve building textures and measure VRAM/FPS before increasing resolution.

## Asset storage policy
User explicitly requests keeping remastered binary assets outside GitHub. Retain upstream tracked assets; do not stage modified textures, portraits, models or asset packs. GitHub stores source, scripts, manifests and documentation only for new work. User confirms local backup completed. Preserve local modifications; never reset or clean the working tree. Planetary V3 must be applied against current local shaders, not blindly against upstream versions.
