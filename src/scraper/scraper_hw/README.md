# Hardware Spec Scraper (`scraper_hw`)

Crawls vendor product pages for consumer PC hardware and writes product specifications to JSONL or JSON.

## Supported vendors

| Key | Site |
| --- | --- |
| `asus` | asus.com |
| `asrock` | asrock.com |
| `msi` | msi.com |
| `gigabyte` | gigabyte.com |
| `biostar` | biostar.com.tw |
| `evga` | evga.com |
| `zotac` | zotac.com |
| `coolermaster` | coolermaster.com |
| `corsair` | corsair.com |
| `phanteks` | phanteks.com |
| `fractal-design` | fractal-design.com |
| `mushkin` | mushkin.com |
| `silverstone` | silverstonetek.com |
| `seasonic` | seasonic.com |
| `lian-li` | lian-li.com |
| `thermalright` | thermalright.com |
| `noctua` | noctua.at |
| `xfx` | xfxforce.com |
| `sapphire` | sapphiretech.com |
| `sparkle` | sparkle.com.tw |
| `maxsun` | en.maxsun.com |
| `powercolor` | powercolor.com |
| `gunnir` | en.gunnir.com |
| `kingston` | kingston.com |
| `sandisk` | sandisk.com |
| `acer` | acer.com |

## Install

```bash
cd src/scraper
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

## Usage

List available vendor keys:

```bash
hw-scraper vendors
```

Scrape a single vendor (up to 100 products by default):

```bash
hw-scraper scrape --vendor asus
```

Scrape all vendors:

```bash
hw-scraper scrape --vendor all
```

Custom output path and limit:

```bash
hw-scraper scrape --vendor msi --limit 500 --output output/msi.jsonl
```

## Options

| Option | Default | Description |
| --- | --- | --- |
| `--vendor` | *(required)* | Vendor key, or `all` |
| `--limit` | `100` | Max product pages per vendor |
| `--delay` | `0.5` | Seconds between requests |
| `--timeout` | `20.0` | HTTP timeout in seconds |
| `--output` | `output/products.jsonl` | Output file path |
| `--output-format` | `jsonl` | `jsonl` or `json` |

## Output schema

Each record is one product:

```json
{
  "vendor": "asus",
  "url": "https://www.asus.com/...",
  "name": "ROG STRIX B650E-F GAMING WIFI",
  "model": "B650E-F",
  "category": "motherboards",
  "specs": {
    "Socket": "AM5",
    "Chipset": "AMD B650E",
    "Memory": "DDR5"
  }
}
```

## Notes

- Vendors marked `use_playwright=True` in `vendors.py` need a Playwright browser: `playwright install chromium`.
- Sites returning 403/429 are silently skipped.
