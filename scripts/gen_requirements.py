#!/usr/bin/env python3
"""Generate requirements.txt from pyproject.toml dependencies."""

import tomllib
from pathlib import Path

root = Path(__file__).parent.parent
pyproject = root / "pyproject.toml"
requirements = root / "requirements.txt"

with open(pyproject, "rb") as f:
    data = tomllib.load(f)

deps = data.get("project", {}).get("dependencies", [])

with open(requirements, "w") as f:
    f.write("\n".join(deps) + "\n")

print(f"Generated {requirements} with {len(deps)} dependencies")
