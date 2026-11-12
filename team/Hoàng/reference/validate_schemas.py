"""Validate local JSON Schema files and their internal $refs using stdlib only."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1] / "schemas"
SCHEMA_FILES = sorted(ROOT.glob("*.schema.json"))

def local_ref_exists(schema: dict[str, Any], ref: str) -> bool:
    if not ref.startswith("#/"):
        return True  # External references are not part of this local check.
    node: Any = schema
    for raw_part in ref[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if not isinstance(node, dict) or part not in node:
            return False
        node = node[part]
    return True

def collect_refs(value: Any) -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        ref = value.get("$ref")
        if isinstance(ref, str):
            found.append(ref)
        for child in value.values():
            found.extend(collect_refs(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(collect_refs(child))
    return found

def main() -> int:
    if not SCHEMA_FILES:
        raise SystemExit(f"No JSON Schema files found in {ROOT}")
    errors: list[str] = []
    for path in SCHEMA_FILES:
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: cannot parse JSON: {exc}")
            continue
        if not isinstance(schema, dict) or "$schema" not in schema or "$defs" not in schema:
            errors.append(f"{path.name}: missing $schema or $defs")
            continue
        for ref in collect_refs(schema):
            if not local_ref_exists(schema, ref):
                errors.append(f"{path.name}: unresolved local reference {ref}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated JSON syntax and local $refs in {len(SCHEMA_FILES)} schema files.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
