#!/usr/bin/env python3
"""Validate every product folder under products/ and print the catalog.

Checks each products/PRD-###-slug/ folder has the required files (plus
tech-pack.md, size-chart.md, and samples.md for `type: apparel`) and that product.md
front matter has the required fields with valid values.
Exit code 1 if any product is invalid. Standard library only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRODUCTS = ROOT / "products"
REQUIRED_FILES = ["product.md", "specs.md", "sourcing.md", "costing.md", "content.md"]
APPAREL_FILES = ["tech-pack.md", "size-chart.md", "samples.md"]
REQUIRED_FIELDS = ["id", "name", "category", "status", "price", "currency"]
STATUSES = {"concept", "development", "sampling", "approved", "launched", "retired"}
FOLDER_RE = re.compile(r"^(PRD-\d{3})-[a-z0-9-]+$")


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "#")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.split("#", 1)[0].strip().strip('"')
    return fields


def validate(folder):
    errors = []
    match = FOLDER_RE.match(folder.name)
    if not match:
        return ["folder name must look like PRD-001-short-name"], None
    for name in REQUIRED_FILES:
        if not (folder / name).is_file():
            errors.append(f"missing {name}")
    product = folder / "product.md"
    fields = front_matter(product) if product.is_file() else None
    if product.is_file() and fields is None:
        errors.append("product.md has no front matter")
    if fields:
        for key in REQUIRED_FIELDS:
            if not fields.get(key):
                errors.append(f"product.md: '{key}' is empty")
        if fields.get("id") and fields["id"] != match.group(1):
            errors.append(f"product.md: id {fields['id']} does not match folder {match.group(1)}")
        if fields.get("type") == "apparel":
            for name in APPAREL_FILES:
                if not (folder / name).is_file():
                    errors.append(f"apparel product missing {name}")
        if fields.get("status") and fields["status"] not in STATUSES:
            errors.append(f"product.md: status '{fields['status']}' not in {sorted(STATUSES)}")
        try:
            if float(fields.get("price") or 0) <= 0 and fields.get("status") in {"approved", "launched"}:
                errors.append("product.md: approved/launched product needs a price > 0")
        except ValueError:
            errors.append("product.md: price must be a number")
    return errors, fields


def main():
    skip = {"collections"}
    folders = sorted(p for p in PRODUCTS.iterdir() if p.is_dir() and not p.name.startswith("_") and p.name not in skip)
    failed = False
    ids = {}
    rows = []
    for folder in folders:
        errors, fields = validate(folder)
        if fields and fields.get("id"):
            if fields["id"] in ids:
                errors.append(f"duplicate id, also used by {ids[fields['id']]}")
            ids[fields["id"]] = folder.name
        if errors:
            failed = True
            for err in errors:
                print(f"ERROR {folder.name}: {err}")
        if fields:
            rows.append(fields)

    print(f"\n{len(folders)} product(s)")
    if rows:
        print("| ID | Name | Category | Status | Price |")
        print("| --- | --- | --- | --- | --- |")
        for f in rows:
            print(f"| {f.get('id')} | {f.get('name')} | {f.get('category')} | {f.get('status')} | {f.get('price')} {f.get('currency')} |")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
