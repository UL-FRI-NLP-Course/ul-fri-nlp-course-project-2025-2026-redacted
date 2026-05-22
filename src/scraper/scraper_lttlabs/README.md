# LTT Labs Scraper (`scraper_lttlabs`)

Scrapes product specs from [LTT Labs](https://www.lttlabs.com/products) by intercepting the Typesense search API the site uses internally. Outputs one record per product to `data/lttlabs.jsonl`.

## Install

```bash
pip install playwright
playwright install chromium
```

## Usage

```bash
python scraper_lttlabs/lttlabs_scraper.py
```

Output is written to `data/lttlabs.jsonl` relative to the repo root.

## Output schema

```json
{
  "vendor": "lttlabs",
  "url": "https://www.lttlabs.com/products/keyboards/...",
  "name": "Brand Model",
  "brand": "Attack Shark",
  "category": "keyboards",
  "specs": { "bluetooth": false, "boardSize": "75%", ... },
  "text": "Deck and highlight text combined into a single string."
}
```

## Notes

- Requires Playwright because the site uses client-side rendering.
- The scraper captures the Typesense API key from the first page load, then paginates via `fetch()` inside the browser context — no key needs to be hard-coded.
