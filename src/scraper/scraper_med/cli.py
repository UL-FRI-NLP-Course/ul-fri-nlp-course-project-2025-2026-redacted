from __future__ import annotations

import json
from pathlib import Path

import typer

from scraper_med.pipeline import _DEFAULT_XML_URL, scrape_topics

app = typer.Typer(help="MedlinePlus health topic scraper for RAG pipelines.")


@app.command("scrape")
def scrape(
    xml_url: str = typer.Option(_DEFAULT_XML_URL, help="URL of the MedlinePlus XML topic file."),
    xml_file: Path | None = typer.Option(None, help="Local XML file path (overrides --xml-url)."),
    limit: int | None = typer.Option(None, help="Maximum number of topics to process."),
    max_sites: int | None = typer.Option(None, help="Maximum linked sites to scrape per topic."),
    no_summaries: bool = typer.Option(False, help="Skip MedlinePlus summary chunks."),
    no_site_scraping: bool = typer.Option(False, help="Skip scraping linked sites (XML summaries only)."),
    language: str = typer.Option("English", help="Topic language to include (default: English)."),
    categories: str | None = typer.Option(
        None,
        help="Comma-separated information categories to include, e.g. 'Overview,Diagnosis,Treatments'.",
    ),
    delay: float = typer.Option(0.5, min=0.0, help="Delay between HTTP requests in seconds."),
    timeout: float = typer.Option(20.0, min=1.0, help="HTTP request timeout in seconds."),
    output: Path = typer.Option(Path("output/chunks.jsonl"), help="Output JSONL file path."),
) -> None:
    xml_text: str | None = None
    if xml_file is not None:
        xml_text = xml_file.read_text(encoding="utf-8")

    category_filter: set[str] | None = None
    if categories:
        category_filter = {c.strip() for c in categories.split(",") if c.strip()}

    chunks = scrape_topics(
        xml_url=xml_url,
        xml_text=xml_text,
        limit=limit,
        max_sites_per_topic=max_sites,
        include_summaries=not no_summaries,
        skip_site_scraping=no_site_scraping,
        language_filter=language or None,
        category_filter=category_filter,
        delay_seconds=delay,
        timeout=timeout,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk.to_dict(), ensure_ascii=False))
            f.write("\n")

    typer.echo(f"wrote {len(chunks)} chunks to {output}")


if __name__ == "__main__":
    app()
