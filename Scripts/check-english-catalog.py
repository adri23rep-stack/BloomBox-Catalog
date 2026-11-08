#!/usr/bin/env python3
"""Check English and Spanish catalog payloads without touching release metadata."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
apps = json.loads((root / "catalog/apps.json").read_text(encoding="utf-8"))
tweaks = json.loads((root / "catalog/tweaks-v2.json").read_text(encoding="utf-8"))
for name, entries in (
    ("apps", apps["apps"]),
    ("tweakEntries", tweaks["tweakEntries"]),
):
    ids = [entry["id"] for entry in entries]
    assert len(ids) == len(set(ids)), "Duplicate catalog ids"
    for entry in entries:
        for field in ("description", "notes", "descriptionEn", "notesEn"):
            assert isinstance(entry.get(field), str) and entry[field].strip(), (
                f"{name}/{entry['id']} missing {field}"
            )
        assert entry["descriptionEn"] != entry["description"], f"{entry['id']} untranslated"
assert len(apps["apps"]) >= 32
assert len(tweaks["tweakEntries"]) >= 6
es = json.loads((root / "news/es.json").read_text(encoding="utf-8"))
en = json.loads((root / "news/en.json").read_text(encoding="utf-8"))
assert es["locale"] == "es" and en["locale"] == "en"
assert {p["id"] for p in es["posts"]} == {p["id"] for p in en["posts"]}
print(f"Catalog English ready: {len(apps['apps'])} apps, {len(tweaks['tweakEntries'])} tweaks, news aligned.")
