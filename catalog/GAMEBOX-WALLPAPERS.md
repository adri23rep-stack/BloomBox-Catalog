# GameBox v2 — curated wallpaper rules

The `gamebox-wallpaper-rules.json` registry maps **installed app identities**
to a specific background search topic. This is separate from
`game-profiles.json`, which controls guest compatibility and JIT.

## Priority

1. Exact installed **CFBundleIdentifier** in `bundleIDs`.
2. Exact normalized name from `keywords` (accents/case ignored, **not** a substring).
3. BloomBox's existing conservative artwork fallback.
4. Existing app icon and gradient, if no usable image exists.

Example: `MeloNX` or `MelonNX` → Wikipedia article `Nintendo Switch`.
No game image is guessed for an emulator: it gets a platform illustration.
Game ports like RDR and GTA V use a verified Steam title, never vague
search-result similarities.

## Adding an app

Add a new entry in `catalog/gamebox-wallpaper-rules.json` with:

- `id`: stable identifier, such as `another-emulator-console`.
- `bundleIDs`: exact bundle IDs verified from an actual installed IPA. **Do not guess.**
- `keywords`: explicit alternative *whole* app names, used only when no bundle ID matches. No arbitrary fragments such as `nx` or `game`.
- `provider`: `wikipedia` (known console topic) or `steam` (verified title).
- `query`: precise article title or exact Steam game name.
- `note`: why this is an appropriate mapping.

Use `bundleIDs: []` when the real bundle ID is not verified, then add it
after inspection. Each alias must be unique across the entire file after
normalizing accents, punctuation and case.

**Never add** direct image URLs, scripts, commands, executable code, tokens,
guest paths, permissions or app settings. BloomBox rejects unexpected fields,
ambiguous aliases and unsafe provider/topic combinations.

## Testing and rollout

The BloomBox client validates the entire JSON and caches only the last known
good version. An invalid remote update cannot change active mappings.
Existing manual wallpapers remain untouched. Cached automatic wallpapers can
be replaced by a changed, newly validated rule.

Current development flow: catalog PR on this branch and BloomBox v2 PR #40.
While testing, BloomBox points to this preview branch; **switch its catalog
URL to `main` after this PR merges**. Check a fresh iPhone install offline,
renamed apps, exact-bundle matching, incorrect alias handling (e.g. Delta Force
is not Delta), and source attribution.

An app's bundle ID is a local matching key. BloomBox does not transmit bundle
IDs, signing data, saved game content or guest paths to image services. Only
the curated console/game topic is requested.
