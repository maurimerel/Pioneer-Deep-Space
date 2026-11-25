# Deep Space hybrid faces
Approved 2026-11-25.

Preserve original procedural descriptors, editor, save compatibility and classic fallback. Full portraits remain optional for compatible NPCs; never override player customization. Current gender guard commit fa863a62 requires in-game verification.

## Prototype gates
1. Inventory actual facegen PNG dimensions, alpha, offsets, species/gender/race counts and compositing order in FaceParts.cpp. Do not alter counts or seed semantics.
2. Create one male and one female aligned photoreal base family, with neutral lighting and consistent camera. Separate compatible head, eyes, nose, mouth, hair, clothes and accessories. Preserve transparent edges and avoid seams. Long hair variants for women.
3. Test alternate asset root with classic fallback; preserve original files. Validate editor arrows, randomization, gender changes, saved player appearance and NPC identity.
4. Add compatible variants only after visual acceptance; then blink/expression frames using engine time, not os.clock. Keep runtime offline.
5. Add profession/age matching only where reliable character metadata exists. Do not infer from names.

## Constraints
Full photographs cannot be independently customized without aligned components. Do not claim the hybrid compositor is implemented until tested. Existing five full portraits remain NPC prototypes. Release Linux crash remains unresolved; ASan debug is current test environment.
