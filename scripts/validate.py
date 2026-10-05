"""Validate mirror metadata without downloading proprietary installers."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "catalog.json").read_text())
assert catalog["schema_version"] == 1
seen = set()
assets = set()
for item in catalog["artifacts"]:
    assert item["id"] not in seen
    seen.add(item["id"])
    assert item["os"] in {"linux", "windows", "macos"}
    for field in ("arch", "version", "format", "variant", "license", "verification"):
        assert isinstance(item[field], str) and item[field]
    for field in ("asset", "release_tag"):
        assert re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]*", item[field])
    key = (item["release_tag"], item["asset"])
    assert key not in assets
    assets.add(key)
    assert re.fullmatch(r"[0-9a-f]{64}", item["sha256"])
    assert isinstance(item["size_bytes"], int) and item["size_bytes"] > 0
    assert item["source_url"].startswith("https://")
    for field in ("source_acquired_on", "mirrored_on"):
        from datetime import date
        date.fromisoformat(item[field])
    expected = ("https://github.com/rwv/cajviewer-binaries/releases/download/"
                + item["release_tag"] + "/" + item["asset"])
    assert item["download_url"] == expected
print(f"Validated {len(seen)} artifact(s)")
