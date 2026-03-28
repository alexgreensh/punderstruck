#!/usr/bin/env python3
"""Build a clean distributable zip for the Punderstruck skill.

Excludes local/dev artifacts that should not ship to end users:
- git metadata
- eval fixtures
- nested zip artifacts
- macOS metadata
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path


EXCLUDED_NAMES = {
    ".DS_Store",
    ".gitignore",
    "punderstruck.zip",
}

EXCLUDED_PARTS = {
    ".git",
    "__pycache__",
    "evals",
}


def should_include(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return False
    if path.name in EXCLUDED_NAMES:
        return False
    return path.is_file()


def build_package(root: Path, output_path: Path) -> None:
    files = sorted(path for path in root.rglob("*") if should_include(path, root))
    output_path.unlink(missing_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(root.parent))
            print(f"Added: {path.relative_to(root.parent)}")


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    output_path = root / "punderstruck.zip"
    build_package(root, output_path)
    print(f"\nCreated clean package: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
