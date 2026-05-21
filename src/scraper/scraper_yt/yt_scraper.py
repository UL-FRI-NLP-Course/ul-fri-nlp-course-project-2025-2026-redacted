import random
import re
import sys
import time
from pathlib import Path

import requests
from yt_dlp import YoutubeDL as ytdl
from youtube_transcript_api import YouTubeTranscriptApi


def load_cookies(path: str) -> requests.Session:
    # Use yt-dlp's loader so Netscape format (leading dots, flags) is handled correctly
    with ytdl({"quiet": True, "no_warnings": True, "cookiefile": path}) as ydl:
        jar = ydl.cookiejar
    session = requests.Session()
    session.cookies = jar
    return session


def _sanitize(name: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", name).strip() or "untitled"


playlist_file = "input.txt"
playlists = []
with open(playlist_file, "r") as f:
    for line in f:
        if line.startswith("#"):
            continue
        url = line.strip()
        if url:
            playlists.append(url)

output_root = Path("output")

# Optional: pass cookies.txt as first arg to work around IP blocks
#   python yt_scraper.py cookies.txt
http_client = load_cookies(sys.argv[1]) if len(sys.argv) > 1 else None
api = YouTubeTranscriptApi(http_client=http_client)

for playlist_url in playlists:
    with ytdl({"quiet": True, "no_warnings": True}) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
    playlist_title = _sanitize(info.get("title") or info.get("id") or "unknown")
    for entry in info["entries"]:
        if not entry:
            continue
        vid_id = entry["id"]
        title = _sanitize(entry.get("title") or vid_id)
        out_dir = output_root / playlist_title
        out_dir.mkdir(parents=True, exist_ok=True)
        try:
            transcript = api.fetch(vid_id)
            text = " ".join([t.text for t in transcript])
            (out_dir / f"{title}.txt").write_text(text, encoding="utf-8")
            print(f"Saved: {playlist_title}/{title}.txt")
        except Exception as e:
            print(f"Skipping {vid_id} ({title}): {e}")
        time.sleep(1 + random.uniform(0, 8))