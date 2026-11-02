#!/usr/bin/env python3
"""Rebuild Nintendo Neon.bbtheme from the public BloomBox catalog parts."""
from pathlib import Path
import hashlib
import json

directory = Path(__file__).resolve().parent
manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
assert manifest["format"] == "bbtheme-chunks" and manifest["version"] == 1
parts = manifest["parts"]
assert 1 <= len(parts) <= 50

output = directory / "Nintendo-Neon.bbtheme"
digest = hashlib.sha256()
size = 0
with output.open("wb") as dest:
    for index, filename in enumerate(parts):
        if filename != f"part-{index:03}.txt":
            raise ValueError("Unexpected chunk filename")
        data = (directory / filename).read_bytes()
        if not 0 < len(data) <= 900_000:
            raise ValueError("Invalid chunk size")
        dest.write(data)
        digest.update(data)
        size += len(data)

if size != manifest["totalBytes"] or digest.hexdigest() != manifest["sha256"]:
    output.unlink(missing_ok=True)
    raise ValueError("Theme checksum failed")
theme = json.loads(output.read_text(encoding="utf-8"))
assert theme["format"] == "bbtheme" and theme["version"] == 2
print(f"Verified {output.name}: {size:,} bytes")
