from __future__ import annotations

import requests
from bs4 import BeautifulSoup, Tag

from scraper_med.http import HttpClient

_REMOVE_TAGS = {"script", "style", "noscript", "nav", "header", "footer", "aside", "form", "button"}
_MAIN_SELECTORS = [
    "main",
    "article",
    '[role="main"]',
    "#content",
    ".content",
    "#main-content",
    ".main-content",
    "#article-body",
    ".article-body",
]


def _strip_noise(soup: BeautifulSoup) -> None:
    for tag in soup.find_all(_REMOVE_TAGS):
        tag.decompose()
    for tag in soup.find_all(attrs={"aria-hidden": "true"}):
        tag.decompose()


def _find_main_content(soup: BeautifulSoup) -> Tag | None:
    for selector in _MAIN_SELECTORS:
        node = soup.select_one(selector)
        if node:
            return node
    return soup.find("body")


def _clean_text(raw: str) -> str:
    lines = [" ".join(line.split()) for line in raw.splitlines()]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def extract_page_text(client: HttpClient, url: str, timeout: float = 20.0) -> str | None:
    try:
        response = client.get(url, timeout=timeout, retries=1)
    except requests.RequestException:
        return None

    content_type = response.headers.get("Content-Type", "")
    if "text/html" not in content_type and "application/xhtml" not in content_type:
        return None

    soup = BeautifulSoup(response.text, "lxml")
    _strip_noise(soup)

    content_node = _find_main_content(soup)
    if content_node is None:
        return None

    text = _clean_text(content_node.get_text("\n", strip=True))
    return text if len(text) >= 100 else None
