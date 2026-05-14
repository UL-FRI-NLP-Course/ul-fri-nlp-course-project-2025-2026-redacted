from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _normalize(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return " ".join(value.split())
    return " ".join(str(value).split())


def _format_specs(specs: Any) -> str:
    if not isinstance(specs, dict):
        return ""
    items: list[str] = []
    for key, value in specs.items():
        k = _normalize(key)
        v = _normalize(value)
        if k and v:
            items.append(f"{k}: {v}")
    return "; ".join(items)


def _is_valid_entry(entry: Any) -> bool:
    if not isinstance(entry, dict):
        return False
    keys = ("vendor", "name", "model", "category", "url")
    has_core = any(_normalize(entry.get(key)) for key in keys)
    has_specs = bool(_format_specs(entry.get("specs")))
    return has_core or has_specs


def _entry_to_text(entry: dict[str, Any]) -> str:
    parts: list[str] = []
    vendor = _normalize(entry.get("vendor"))
    name = _normalize(entry.get("name"))
    model = _normalize(entry.get("model"))
    category = _normalize(entry.get("category"))
    url = _normalize(entry.get("url"))
    specs = _format_specs(entry.get("specs"))

    if vendor:
        parts.append(f"Vendor: {vendor}")
    if name:
        parts.append(f"Name: {name}")
    if model:
        parts.append(f"Model: {model}")
    if category:
        parts.append(f"Category: {category}")
    if url:
        parts.append(f"URL: {url}")
    if specs:
        parts.append(f"Specs: {specs}")
    return " | ".join(parts)


def _parse_json_file(path: Path) -> tuple[list[dict[str, Any]], int]:
    text = path.read_text(encoding="utf-8")
    valid_rows: list[dict[str, Any]] = []
    skipped = 0

    try:
        loaded = json.loads(text)
        items = loaded if isinstance(loaded, list) else [loaded]
        for item in items:
            if _is_valid_entry(item):
                valid_rows.append(item)
            else:
                skipped += 1
        return valid_rows, skipped
    except json.JSONDecodeError:
        pass

    for line in text.splitlines():
        row = line.strip()
        if not row:
            continue
        try:
            item = json.loads(row)
        except json.JSONDecodeError:
            skipped += 1
            continue

        if _is_valid_entry(item):
            valid_rows.append(item)
        else:
            skipped += 1
    return valid_rows, skipped


def convert_json_to_text(input_dir: Path, output_dir: Path) -> tuple[int, int, int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(input_dir.glob("*.json"))
    converted_files = 0
    total_written = 0
    total_skipped = 0

    for path in files:
        rows, skipped = _parse_json_file(path)
        total_skipped += skipped
        lines = [_entry_to_text(row) for row in rows]
        lines = [line for line in lines if line]
        total_written += len(lines)

        output_path = output_dir / f"{path.stem}.txt"
        output_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        converted_files += 1

    return converted_files, total_written, total_skipped


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert JSON/JSONL product records into plain-text entries."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("data"),
        help="Directory containing .json files (default: data)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/text"),
        help="Directory for generated .txt files (default: data/text)",
    )
    args = parser.parse_args()

    converted_files, written_rows, skipped_rows = convert_json_to_text(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
    )
    print(
        f"Converted {converted_files} files. "
        f"Wrote {written_rows} text entries. "
        f"Skipped {skipped_rows} invalid entries."
    )


if __name__ == "__main__":
    main()
