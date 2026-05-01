from __future__ import annotations

from collections import deque
from html import unescape
import re
from urllib.parse import urljoin, urlparse, urlunparse
from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

import requests

from scraper_hw.http import HttpClient


def _matches_keywords(url: str, include_keywords: tuple[str, ...]) -> bool:
    lowered = url.lower()
    return any(keyword.lower() in lowered for keyword in include_keywords)


def _matches_exclude_keywords(url: str, exclude_keywords: tuple[str, ...]) -> bool:
    lowered = url.lower()
    if any(keyword.lower() in lowered for keyword in exclude_keywords):
        return True

    parsed = urlparse(url)
    path = parsed.path.lower().rstrip("/")
    # Treat filter endpoints with query params as listing pages, not products.
    if path.endswith("/filter") and bool(parsed.query):
        return True
    return False


LOCALE_SEGMENT_PATTERN = re.compile(r"^(?:[a-z]{2}(?:-[a-z]{2})?|[a-z]+-[a-z]{2}|[a-z]{2}-[a-z0-9]+)$")


def _normalize_known_hosts(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    if host == "www.sparkle.com.tw":
        return urlunparse(
            (parsed.scheme, "sparkle.com.tw", parsed.path, parsed.params, parsed.query, parsed.fragment)
        )
    if host == "silverstonetek.com":
        return urlunparse(
            (parsed.scheme, "www.silverstonetek.com", parsed.path, parsed.params, parsed.query, parsed.fragment)
        )
    return url


def _strip_locale_segment(url: str) -> str:
    parsed = urlparse(url)
    segments = [segment for segment in parsed.path.split("/") if segment]
    if not segments:
        return url

    first = segments[0].lower()
    if not LOCALE_SEGMENT_PATTERN.match(first):
        return url

    new_segments = segments[1:]
    new_path = "/" + "/".join(new_segments) if new_segments else "/"
    return urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            new_path,
            parsed.params,
            parsed.query,
            parsed.fragment,
        )
    )


def _extract_loc_tags_relaxed(xml_text: str) -> list[str]:
    matches = re.findall(r"<loc>\s*(.*?)\s*</loc>", xml_text, flags=re.IGNORECASE | re.DOTALL)
    locs: list[str] = []
    for match in matches:
        value = unescape(match).strip()
        if value:
            locs.append(value)
    return locs


def _extract_sitemap_hints_robots(text: str) -> list[str]:
    matches = re.findall(r"(?im)^\s*sitemap:\s*(\S+)\s*$", text)
    return [match.strip() for match in matches if match.strip()]


def _extract_href_links_relaxed(text: str, base_url: str) -> list[str]:
    matches = re.findall(r"""(?i)href=["']([^"']+)["']""", text)
    links: list[str] = []
    for match in matches:
        href = unescape(match).strip()
        if not href or href.startswith("#") or href.startswith("javascript:"):
            continue
        links.append(urljoin(base_url, href))
    return links


def _looks_like_asset_url(url: str) -> bool:
    path = urlparse(url).path.lower()
    return path.endswith(
        (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".ico", ".css", ".js", ".pdf", ".zip", ".xml.gz")
    )


def discover_product_urls(
    client: HttpClient,
    sitemap_url: str,
    include_keywords: tuple[str, ...],
    exclude_keywords: tuple[str, ...] = (),
    max_urls: int | None = None,
    strip_locale_prefix: bool = True,
) -> list[str]:
    queue = deque([sitemap_url])
    seen: set[str] = set()
    results: list[str] = []

    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)

        try:
            response = client.get(current)
        except requests.RequestException:
            continue
        xml_text = response.text

        try:
            root = ElementTree.fromstring(xml_text)
            root_tag = root.tag.lower()

            if root_tag.endswith("sitemapindex"):
                for node in root.findall(".//{*}sitemap/{*}loc"):
                    if node.text:
                        queue.append(node.text.strip())
                continue

            if root_tag.endswith("urlset"):
                for node in root.findall(".//{*}url/{*}loc"):
                    if not node.text:
                        continue
                    raw_url = _normalize_known_hosts(node.text.strip())
                    url = _strip_locale_segment(raw_url) if strip_locale_prefix else raw_url
                    if _matches_exclude_keywords(url, exclude_keywords):
                        continue
                    if _matches_keywords(url, include_keywords):
                        results.append(url)
                        if max_urls is not None and len(results) >= max_urls:
                            return results
                continue

            raise ValueError(f"Unsupported sitemap type at {current}: {root.tag}")
        except ParseError:
            locs = _extract_loc_tags_relaxed(xml_text)
            if not locs:
                sitemap_hints = _extract_sitemap_hints_robots(xml_text)
                for hinted in sitemap_hints:
                    queue.append(hinted)

                hrefs = _extract_href_links_relaxed(xml_text, current)
                for href in hrefs:
                    normalized_href = _normalize_known_hosts(href)
                    if _looks_like_asset_url(normalized_href):
                        continue
                    if normalized_href.lower().endswith(".xml"):
                        queue.append(normalized_href)
                        continue

                    url = _strip_locale_segment(normalized_href) if strip_locale_prefix else normalized_href
                    if _matches_exclude_keywords(url, exclude_keywords):
                        continue
                    if _matches_keywords(url, include_keywords):
                        results.append(url)
                        if max_urls is not None and len(results) >= max_urls:
                            return results

                current_url = _normalize_known_hosts(current)
                current_url = _strip_locale_segment(current_url) if strip_locale_prefix else current_url
                if not _matches_exclude_keywords(current_url, exclude_keywords) and _matches_keywords(
                    current_url, include_keywords
                ):
                    results.append(current_url)
                    if max_urls is not None and len(results) >= max_urls:
                        return results
                continue

            for loc in locs:
                if loc.lower().endswith(".xml"):
                    queue.append(loc)
                    continue
                raw_url = _normalize_known_hosts(loc)
                url = _strip_locale_segment(raw_url) if strip_locale_prefix else raw_url
                if _matches_exclude_keywords(url, exclude_keywords):
                    continue
                if _matches_keywords(url, include_keywords):
                    results.append(url)
                    if max_urls is not None and len(results) >= max_urls:
                        return results

    return results
