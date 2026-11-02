# Game Mode & LiveContainer compatibility profiles

This registry is declarative data used by experimental BloomBox Game Mode.
BloomBox fetches `catalog/game-profiles.json` over HTTPS at startup and retains
the last schema-validated version for offline use. Only **exact bundle IDs**
match; no names, wildcards, partial IDs or automatic app discovery.

## Adding a profile

1. Confirm the guest's **actual CFBundleIdentifier** from the installed app.
2. Test the exact guest build inside BloomBox on the target iOS version.
3. Record only supported settings and explain which issue each setting fixes.
4. Raise `revision` whenever compatibility settings change so users see a new
   prompt before any updated settings are applied.
5. Submit a PR with device/iOS version, screenshots or logs, and reproduction
   steps for the pre-fix issue.

A profile can set `gameMode`, `requiresRAMPlus`, and `requiresJIT`, and may
**recommend** these limited per-guest LiveContainer settings: `orientation`
(`landscape`, `portrait`, `auto`), `jitNeeded`, `classicMode`,
`spoofSDKVersion`, `hideLiveContainer`, `dontInjectTweakLoader`,
`fixFilePicker`, and `fixLocalNotification`. BloomBox shows users the
recommendations on first launch and applies them **only after permission**;
the same accepted revision is not reapplied over later manual changes.

**Forbidden:** code, executable scripts, arbitrary URLs, entitlements, private
data permission, signing changes, Apple developer portal actions, arbitrary
files, network restrictions, or edits to a different installed LiveContainer's
private storage. Unknown fields, wildcards, oversized responses, and invalid
schema versions are rejected.

## Known compatibility

- **Husk** (`com.husk.app`): user-tested on iPhone 14 Pro / iOS 27 with
  BloomBox RAM+, built-in JIT and Husk-specific local JIT script. The profile
  recommends a landscape window and non-Classic guest compatibility mode.
- **Red Dead**: needs an identified app/port version, exact bundle ID, and
  confirmed settings. No automatic profile should be published based on the
  title alone.

When this experimental branch is reviewed and merged, BloomBox's registry URL
must be switched from the preview branch to
`BloomBox-Catalog/main/catalog/game-profiles.json` before release.
