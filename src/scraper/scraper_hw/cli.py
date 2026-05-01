from __future__ import annotations

import json
from pathlib import Path
from typing import TextIO

import typer

from scraper_hw.pipeline import scrape_vendor
from scraper_hw.vendors import VENDORS

app = typer.Typer(help="Hardware model/spec scraper for vendor websites.")


def _write_rows(stream: TextIO, rows: list[dict], output_format: str, first_json_row: bool) -> bool:
    if output_format == "jsonl":
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False))
            stream.write("\n")
        return first_json_row

    if output_format == "json":
        for row in rows:
            if not first_json_row:
                stream.write(",\n")
            stream.write(json.dumps(row, ensure_ascii=False))
            first_json_row = False
        return first_json_row

    raise ValueError(f"Unsupported format: {output_format}")


@app.command("vendors")
def list_vendors() -> None:
    typer.echo(", ".join(sorted(VENDORS.keys())))


@app.command("scrape")
def scrape(
    vendor: str = typer.Option(
        ...,
        help="Vendor key (use `hw-scraper vendors` to list keys, or all).",
    ),
    limit: int = typer.Option(100, min=1, help="Maximum product pages per vendor."),
    delay: float = typer.Option(0.5, min=0.0, help="Delay between page requests in seconds."),
    timeout: float = typer.Option(20.0, min=1.0, help="HTTP timeout in seconds."),
    output: Path = typer.Option(Path("output/products.jsonl"), help="Output file path."),
    output_format: str = typer.Option("jsonl", help="Output format: jsonl or json."),
) -> None:
    if output_format not in {"jsonl", "json"}:
        raise typer.BadParameter("output-format must be one of: jsonl, json")

    target_names = sorted(VENDORS.keys()) if vendor == "all" else [vendor]
    missing = [name for name in target_names if name not in VENDORS]
    if missing:
        raise typer.BadParameter(f"Unknown vendor(s): {', '.join(missing)}")

    output.parent.mkdir(parents=True, exist_ok=True)
    total_rows = 0
    first_json_row = True
    with output.open("w", encoding="utf-8") as stream:
        if output_format == "json":
            stream.write("[\n")

        for name in target_names:
            records = scrape_vendor(VENDORS[name], limit=limit, delay_seconds=delay, timeout=timeout)
            rows = [record.to_dict() for record in records]
            total_rows += len(rows)
            first_json_row = _write_rows(stream, rows, output_format, first_json_row)

        if output_format == "json":
            if not first_json_row:
                stream.write("\n")
            stream.write("]\n")

    typer.echo(f"wrote {total_rows} records to {output}")


if __name__ == "__main__":
    app()
