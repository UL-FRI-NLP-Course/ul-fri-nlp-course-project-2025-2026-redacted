from __future__ import annotations

import json
from pathlib import Path

import typer

from scraper_steam.charts import fetch_charts, parse_charts_from_file
from scraper_steam.store import fetch_requirements

app = typer.Typer(help="Scrape SteamDB top charts and fetch system requirements from the Steam store API.")


@app.command()
def scrape(
    limit: int = typer.Option(10000, min=1, help="Number of top games to collect."),
    delay: float = typer.Option(1.5, min=0.0, help="Delay between Steam store API calls (seconds)."),
    timeout: float = typer.Option(60.0, min=5.0, help="Playwright page-load timeout (seconds)."),
    charts_only: bool = typer.Option(False, help="Only dump the chart list; skip system requirements."),
    headless: bool = typer.Option(True, help="Run browser headless. Use --no-headless to see the browser (helps debug Cloudflare)."),
    from_html: Path = typer.Option(None, help="Parse chart entries from a locally saved SteamDB HTML file instead of using Playwright."),
    output: Path = typer.Option(Path("output/steamdb_requirements.json"), help="Output file."),
) -> None:
    if from_html is not None:
        typer.echo(f"[1/2] Parsing chart entries from {from_html} …", err=True)
        charts = parse_charts_from_file(from_html, limit=limit)
    else:
        typer.echo(f"[1/2] Fetching top {limit} games from SteamDB charts …", err=True)
        charts = fetch_charts(limit=limit, timeout=timeout, headless=headless)
    typer.echo(f"      Got {len(charts)} games.", err=True)

    if charts_only:
        output.parent.mkdir(parents=True, exist_ok=True)
        rows = [{"rank": e.rank, "name": e.name, "app_id": e.app_id,
                 "current_players": e.current_players, "peak_today": e.peak_today,
                 "peak_all_time": e.peak_all_time} for e in charts]
        output.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
        typer.echo(f"wrote {len(rows)} chart entries to {output}")
        return

    typer.echo(f"[2/2] Fetching system requirements from Steam store API …", err=True)
    entries = [(e.rank, e.app_id, e.name) for e in charts]
    requirements = fetch_requirements(entries, delay_seconds=delay, verbose=True)
    typer.echo(f"      Got requirements for {len(requirements)}/{len(charts)} games.", err=True)

    output.parent.mkdir(parents=True, exist_ok=True)
    rows = [r.to_dict() for r in requirements]
    output.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    typer.echo(f"wrote {len(rows)} records to {output}")


if __name__ == "__main__":
    app()
