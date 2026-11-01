# BloomBox Catalog

Remote catalog for the BloomBox App Store, Tweak Store and localized News.

## Feeds

- [Apps](catalog/apps.json) — migrated from [BloomBox PR #22](https://github.com/adri23rep-stack/BloomBox/pull/22), including DolphiniOS.
- [Tweaks v1](catalog/tweaks.json) — legacy compatible feed.
- [Tweaks v2](catalog/tweaks-v2.json) — expanded community listings.
- [News locale index](news/index.json) — resolves Spanish and English feeds.
- [Noticias en español](news/es.json)
- [News in English](news/en.json)

The news feeds intentionally start empty. Publish verified news items with locale-specific content instead of invented announcements.

## URLs after merging into main

- https://raw.githubusercontent.com/adri23rep-stack/BloomBox-Catalog/main/catalog/apps.json
- https://raw.githubusercontent.com/adri23rep-stack/BloomBox-Catalog/main/catalog/tweaks.json
- https://raw.githubusercontent.com/adri23rep-stack/BloomBox-Catalog/main/catalog/tweaks-v2.json
- https://raw.githubusercontent.com/adri23rep-stack/BloomBox-Catalog/main/news/index.json

Keep application binaries on their original publisher's release pages. Do not upload guest app data, credentials or private files to this repository.

## Compatibility and rollout

These feeds are **staged on a feature branch** until approved. The BloomBox client still needs its feed URLs migrated and a system / Español / English app-language override implemented and tested. Do not remove the original catalog until the new feed has been tested on-device. An app-language override should affect BloomBox-owned UI and news locale only; it must not change the iPhone system language.
