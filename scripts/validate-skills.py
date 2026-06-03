#!/usr/bin/env python3
"""
Simple validator for SKILL.md frontmatter in Grok Build Arsenal.

Sole author: Cobus Greyling
"""

import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml not installed, skipping deep validation")
    sys.exit(0)

REQUIRED_FIELDS = {"name", "description", "version", "author"}

def validate_skill(path: Path) -> list[str]:
    errors = []
    try:
        content = path.read_text()
        if not content.startswith("---"):
            errors.append("Missing YAML frontmatter")
            return errors
        # crude parse
        frontmatter_end = content.find("---", 3)
        if frontmatter_end == -1:
            errors.append("Malformed frontmatter")
            return errors
        fm_text = content[3:frontmatter_end]
        data = yaml.safe_load(fm_text) or {}
        for field in REQUIRED_FIELDS:
            if field not in data or not data[field]:
                errors.append(f"Missing or empty required field: {field}")
        if data.get("author") != "Cobus Greyling":
            errors.append("Author must be 'Cobus Greyling' (sole author policy)")
    except Exception as e:
        errors.append(f"Parse error: {e}")
    return errors

def main():
    root = Path(__file__).parent.parent
    skill_files = list(root.glob("skills/**/SKILL.md")) + list(root.glob(".grok/skills/*.md"))
    failures = 0
    for sf in skill_files:
        errs = validate_skill(sf)
        if errs:
            print(f"❌ {sf.relative_to(root)}")
            for e in errs:
                print(f"   - {e}")
            failures += 1
        else:
            print(f"✅ {sf.relative_to(root)}")
    if failures:
        print(f"\n{failures} skill(s) failed validation.")
        sys.exit(1)
    print("\nAll skills validated successfully.")

if __name__ == "__main__":
    main()
