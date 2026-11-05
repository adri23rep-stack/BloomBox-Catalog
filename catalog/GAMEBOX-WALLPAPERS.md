# GameBox v2 — curated wallpaper rules

The `gamebox-wallpaper-rules.json` registry maps **installed app identities**
to an explicitly selected image or a specific background search topic. This is separate from
`game-profiles.json`, which controls guest compatibility and JIT.

## Priority

1. Exact installed **CFBundleIdentifier** in `bundleIDs`.
2. Exact normalized name from `keywords` (accents/case ignored), optionally followed by a version or a safe label like `beta`/`iOS`/`emulator`. Arbitrary fragments and unrelated suffixes never match.
3. If a rule has a vetted direct image URL, download it **first**.
4. If unavailable, use the rule's precise console/game search topic.
5. Otherwise, preserve the existing app icon and gradient.

**Manual wallpapers and covers always outrank every automatic download.**

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
- `imageURL` *(optional)*: a vetted **HTTPS direct image** hosted on `upload.wikimedia.org/wikipedia/commons/`. No arbitrary hosts or redirects outside the approved image CDN.
- `sourceURL` *(required with imageURL)*: the matching Commons `https://commons.wikimedia.org/wiki/File:...` attribution/license page.
- `imageLicense` *(required with imageURL)*: currently only `Public domain`, verified manually on the image file page.

Use `bundleIDs: []` when the real bundle ID is not verified, then add it
after inspection. Each alias must be unique across the entire file after
normalizing accents, punctuation and case.

**Never add** unverified images, arbitrary HTTP/image-host URLs, scripts,
commands, executable code, tokens, guest paths, permissions or app settings.
BloomBox rejects unsafe URLs, mismatched Commons filenames, missing attribution,
unverified license labels, ambiguous aliases and unsafe provider/topic combinations.

## Pinned artwork (seven emulators)

| Emulator | Chosen hardware photograph | Attribution |
|---|---|---|
| MeloNX / MelonNX | Nintendo Switch | [Evan-Amos, public domain](https://commons.wikimedia.org/wiki/File:Nintendo-Switch-Console-Flat-Top.jpg) |
| LemoNX | Nintendo Switch | [Same public-domain image](https://commons.wikimedia.org/wiki/File:Nintendo-Switch-Console-Flat-Top.jpg) |
| DolphiniOS | GameCube | [Evan-Amos, public domain](https://commons.wikimedia.org/wiki/File:Nintendo-GameCube-Console-FL.jpg) |
| MeloCafe | Wii U | [Evan-Amos, public domain](https://commons.wikimedia.org/wiki/File:Nintendo-Wii-U-Console-FL.jpg) |
| Vita3KiOS | PlayStation Vita | [Evan-Amos, public domain](https://commons.wikimedia.org/wiki/File:PlayStation-Vita-2001-FL.jpg) |
| PPSSPP | PSP | [Evan-Amos, public domain](https://commons.wikimedia.org/wiki/File:Sony-PSP-1000-Body.jpg) |
| Husk | Android gaming device (Xperia Play; representative hardware, not a Husk logo) | [Evan-Amos, public domain](https://commons.wikimedia.org/wiki/File:Sony-Xperia-Play-Open-FL.jpg) |

These are console photographs, not screenshots or guessed box art. They are
downloaded only on demand, decoded at screen size, and cached for offline use.
No third-party artwork binaries are bundled into BloomBox.

**Husk is an Android app/emulation environment**, not Minecraft Dungeons.
The previous inaccurate Husk → Minecraft Dungeons rule was removed. It now
uses a verified public-domain image of Android gaming hardware, never a random
Steam game cover. Users can still set their preferred Husk wallpaper from
Photos or Files.

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
