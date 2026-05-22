# YouTube Transcript Scraper (`scraper_yt`)

Downloads transcripts from YouTube playlists and saves each video as a plain `.txt` file.

## Install

```bash
pip install yt-dlp youtube-transcript-api
```

## Usage

1. Add playlist URLs to `input.txt`, one per line (lines starting with `#` are ignored).
2. Run:

```bash
python scraper_yt/yt_scraper.py
```

Transcripts are saved to `output/<playlist_title>/<video_title>.txt`.

If the site blocks requests by IP, pass a Netscape-format cookies file as the first argument:

```bash
python scraper_yt/yt_scraper.py cookies.txt
```

## Notes

- Videos without a transcript (no captions available) are skipped with a warning.
- A random delay of 1–9 seconds is added between requests to avoid rate limiting.
