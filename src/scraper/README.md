# Hardware Scraper

A simple, extensible Python scraper for hardware vendors (ASUS, ASRock, MSI, Gigabyte, BIOSTAR, EVGA, Zotac, AMD, Intel, Cooler Master, Corsair, Phanteks, Fractal Design, Mushkin, SilverStone, Seasonic, Lian Li, Thermalright, Noctua, XFX, Sapphire, Sparkle, Maxsun, PowerColor/PowerColour, Gunnir, Kingston, SanDisk, Acer) that:

- discovers product pages from sitemap XML files
- tries vendor-specific spec endpoints (ASUS `/techspec/`, Gigabyte `/sp`, MSI `/Specification`, ASRock `/index.us.asp#Specification`)
- extracts model/name/specs from JSON-LD, tables, dl lists, and spec-like row/list blocks
- writes normalized output to JSONL or JSON

## Install

```bash
cd src/scraper
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

## Usage

List supported vendors:

```bash
hw-scraper vendors
```

Scrape one vendor:

```bash
hw-scraper scrape --vendor asus --limit 50 --output ../../data/asus.jsonl --output-format jsonl
```

Scrape all vendors:

```bash
hw-scraper scrape --vendor all --limit 100 --delay 0.7 --output ../../data/all.json
```

## Output schema

Each record has:

- `vendor`
- `url`
- `name`
- `model`
- `category`
- `specs` (key/value dictionary)

## Notes

- Website structures change often, so keep `scraper_hw/vendors.py` include keywords updated.
- Scrape responsibly (rate limits, robots.txt, and site terms).
- Locale prefixes in sitemap URLs (for example `/africa-fr/`) are stripped so output URLs stay locale-free.
