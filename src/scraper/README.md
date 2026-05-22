# Scrapers

Data collection tools for the project. Each subdirectory is a self-contained scraper.

| Directory | What it does                                                                                                                                                                          |
| --- |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`scraper_hw/`](scraper_hw/README.md) | Crawls manufacturer websites (ASUS, MSI, Gigabyte, etc.) for product spec pages                                                                                                       |
| [`scraper_lttlabs/`](scraper_lttlabs/README.md) | Scrapes product specs from LTT Labs via their internal Typesense API                                                                                                                  |
| [`scraper_yt/`](scraper_yt/README.md) | Downloads transcripts from YouTube playlists                                                                                                                                            |
| [`scraper_steam/`](scraper_steam/README.md) | Fetches top games from SteamDB and collects system requirements from the Steam Store API                                                                                               |
| [`cpu-spec-dataset-main/`](cpu-spec-dataset-main/README.md) | Third-party Java-based CPU spec scraper ([felixsteinke/cpu-spec-dataset](https://github.com/felixsteinke/cpu-spec-dataset)) — required modifications to work with the current webpages |

## Shared setup

All Python scrapers share the same `pyproject.toml` and virtual environment in this directory:

```bash
cd src/scraper
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

Scrapers that use Playwright also need:

```bash
playwright install chromium
```
