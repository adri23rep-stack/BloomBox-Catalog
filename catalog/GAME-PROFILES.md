# Game & compatibility profiles

`catalog/game-profiles.json` is **data**, not executable code. BloomBox loads it over HTTPS at startup and keeps the most recent validated copy offline. If the new file is unavailable, BloomBox retains its last validated cache and has a local Husk fallback.

## Format (schemaVersion 1)

```json
{
  "schemaVersion": 1,
  "catalogID": "bloombox.game-compatibility",
  "updatedAt": "2026-11-02",
  "profiles": [
    {
      "bundleID": "com.example.game",
      "name": "Example game",
      "revision": 1,
      "gameMode": true,
      "requiresRAMPlus": true,
      "requiresJIT": true,
      "compatibility": {
        "orientation": "landscape",
        "jitNeeded": true,
        "classicMode": false,
        "spoofSDKVersion": false,
        "hideLiveContainer": false,
        "dontInjectTweakLoader": false,
        "fixFilePicker": true,
        "fixLocalNotification": false
      },
      "notes": "Explanation, evidence, version tested."
    }
  ]
}
```

Fields inside `compatibility` are **optional** and must be based on a reproducible test. An absent field is never changed. Only `orientation` values `landscape`, `portrait`, or `auto` are valid. Bundle IDs are exact, never wildcards or name guesses. Revision increases only when settings need to be proposed again.

BloomBox asks once before applying a compatibility profile and saves per-bundle consent + profile revision. A subsequent update requires renewed consent. Manual changes made after acceptance are not repeatedly overwritten. Users can decline without preventing ordinary apps from opening. RAM+, JIT, privacy access, signing, executable scripts, and installation never get enabled from a remote file.

Do not add `Red Dead Redemption` until its **installed, unmodified bundle ID**, app version, and precise tested LiveContainer compatibility flags are confirmed. A game title alone is not reliable evidence. Avoid copyrighted game binaries or user account data.

Security: protect the main branch through review, do not use URL overrides or scripts in a profile, do not add executable code or privileged toggles, and validate size, schema version and duplicates before publishing.
