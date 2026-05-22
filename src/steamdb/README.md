# SteamDB Scraper (`steamdb_scraper`)

Fetches the top games list from SteamDB and collects their minimum and recommended system requirements from the Steam Store API.

## Install

```bash
cd src/steamdb
python -m venv .venv
. .venv/bin/activate
pip install -e .
playwright install chromium
```

## Usage

Full scrape — top 10,000 games with system requirements:

```bash
steamdb-scraper scrape
```

Only dump the chart list, skip requirements:

```bash
steamdb-scraper scrape --charts-only
```

Parse from a locally saved SteamDB HTML file (avoids Playwright/Cloudflare):

```bash
steamdb-scraper scrape --from-html steamdb_charts.html
```

## Options

| Option | Default | Description |
| --- | --- | --- |
| `--limit` | `10000` | Number of top games to collect |
| `--delay` | `1.5` | Seconds between Steam store API calls |
| `--timeout` | `60.0` | Playwright page-load timeout (seconds) |
| `--charts-only` | false | Skip system requirements, dump chart list only |
| `--headless` / `--no-headless` | headless | Show/hide the browser (helps debug Cloudflare) |
| `--from-html` | — | Parse chart entries from a local HTML file |
| `--output` | `output/steamdb_requirements.json` | Output file path |

## Output schema

```json
[
  {
    "rank": 1,
    "app_id": 730,
    "name": "Counter-Strike 2",
    "minimum": { "os": "Windows 10", "processor": "...", "memory": "8 GB RAM", ... },
    "recommended": { "os": "Windows 10", "processor": "...", "memory": "16 GB RAM", ... }
  }
]
```

## Notes

- SteamDB uses Cloudflare protection; Playwright is required to load the charts page. If scraping fails, save the page HTML manually and use `--from-html`.
- The Steam Store API is public and does not require authentication.
