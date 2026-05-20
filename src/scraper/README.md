# MedlinePlus Scraper

A Python scraper that reads the [MedlinePlus health topics XML feed](https://medlineplus.gov/xml.html) and produces RAG-ready JSONL chunks by:

- parsing every English health topic from the XML (Spanish and other languages are excluded)
- scraping the full text from each linked external resource (NIH, CDC, Mayo Clinic, etc.)
- splitting content into overlapping chunks (~1500 chars with ~150-char overlap at sentence boundaries)
- writing one chunk per line to JSONL, each carrying full topic metadata for retrieval context

## Install

```bash
cd src/scraper
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

## Usage

Full scrape — all English topics, all linked sites:

```bash
med-scraper scrape
```

Quick test — 10 topics, summaries only (no outbound HTTP):

```bash
med-scraper scrape --limit 10 --no-site-scraping
```

Only include Overview and Diagnosis pages from linked sites:

```bash
med-scraper scrape --categories "Overview,Diagnosis and Tests"
```

Use a locally downloaded XML file instead of fetching from the web:

```bash
med-scraper scrape --xml-file mplus_topics_2026-05-16.xml
```

Custom output path:

```bash
med-scraper scrape --output ../../data/chunks.jsonl --delay 0.7
```

All options:

| Option | Default | Description |
| --- | --- | --- |
| `--xml-url` | MedlinePlus XML URL | URL of the XML topic feed |
| `--xml-file` | — | Local XML file (overrides `--xml-url`) |
| `--limit` | — | Max topics to process |
| `--max-sites` | — | Max linked sites to scrape per topic |
| `--no-summaries` | false | Skip MedlinePlus summary chunks |
| `--no-site-scraping` | false | Skip scraping linked sites entirely |
| `--language` | `English` | Topic language filter |
| `--categories` | — | Comma-separated site categories to include |
| `--delay` | `0.5` | Seconds between HTTP requests |
| `--timeout` | `20.0` | HTTP timeout in seconds |
| `--output` | `output/chunks.jsonl` | Output file path |

## Output schema

Each line of the JSONL file is one chunk:

```json
{
  "chunk_id": "a3f1c2e4b8d09f1e",
  "topic_id": "8002",
  "topic_title": "Diabetes",
  "topic_url": "https://medlineplus.gov/diabetes.html",
  "groups": ["Metabolic Problems"],
  "also_called": ["Diabetes Mellitus"],
  "mesh_headings": ["Diabetes Mellitus"],
  "source_url": "https://www.niddk.nih.gov/health-information/diabetes",
  "source_title": "Diabetes | NIDDK",
  "organization": "National Institute of Diabetes and Digestive and Kidney Diseases",
  "information_categories": ["Overview"],
  "text": "Diabetes is a disease that occurs when your blood glucose...",
  "chunk_index": 0,
  "total_chunks": 4
}
```

`text` is the field to embed. All other fields are metadata for filtering and context injection at retrieval time.

## Notes

- The XML URL is dated (e.g. `mplus_topics_2026-05-16.xml`). Update `--xml-url` or `_DEFAULT_XML_URL` in `pipeline.py` when a newer file is published.
- Some external sites block scrapers (403, 429). These are silently skipped with a `[warn]` message.
- Scrape responsibly — use `--delay` and respect site terms of service.
