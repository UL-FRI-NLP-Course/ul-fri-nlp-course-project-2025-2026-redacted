from __future__ import annotations

from collections import deque
from html import unescape
import re
from urllib.parse import parse_qs, unquote, urlencode, urljoin, urlparse, urlunparse
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
    patterns = (
        r"""(?i)(?<![\w-])href=["']([^"']+)["']""",
        r"""(?i)(?<![\w-])href=([^\s"'<>]+)""",
        r"""(?i)data-href=["']([^"']+)["']""",
        r"""(?i)data-url=["']([^"']+)["']""",
        r"""(?i)data-link=["']([^"']+)["']""",
    )
    links: list[str] = []
    for pattern in patterns:
        for match in re.findall(pattern, text):
            href = unescape(match).strip()
            if not href:
                continue
            lowered = href.lower()
            if lowered.startswith(("#", "javascript:", "mailto:", "tel:", "data:")):
                continue
            # Reject JS template expressions and invalid characters in hrefs
            if any(c in href for c in ("(", ")", "{", "}", "<", ">", "\\")):
                continue
            if " " in href:
                continue
            links.append(urljoin(base_url, href))
    return links


def _looks_like_asset_url(url: str) -> bool:
    path = urlparse(url).path.lower()
    return path.endswith(
        (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".ico", ".css", ".js", ".pdf", ".zip", ".xml.gz")
    )


def _looks_like_js_template_url(url: str) -> bool:
    path = urlparse(url).path
    return any(c in path for c in ("(", ")", "{", "}", "\\"))


def _is_same_host(url: str, allowed_hosts: set[str]) -> bool:
    host = urlparse(url).netloc.lower()
    if not host:
        return False
    return host in allowed_hosts


def _matches_path_depth(url: str, minimum_path_segments: int) -> bool:
    if minimum_path_segments <= 0:
        return True
    segments = [segment for segment in urlparse(url).path.split("/") if segment]
    return len(segments) >= minimum_path_segments


def _decode_uddg_url(value: str) -> str:
    decoded = value
    for _ in range(2):
        next_value = unquote(decoded)
        if next_value == decoded:
            break
        decoded = next_value
    return decoded


def discover_product_urls(
    client: HttpClient,
    sitemap_url: str,
    include_keywords: tuple[str, ...],
    exclude_keywords: tuple[str, ...] = (),
    max_urls: int | None = None,
    strip_locale_prefix: bool = True,
    minimum_path_segments: int = 0,
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
                    if _looks_like_js_template_url(raw_url):
                        continue
                    url = _strip_locale_segment(raw_url) if strip_locale_prefix else raw_url
                    if _matches_exclude_keywords(url, exclude_keywords):
                        continue
                    if _matches_keywords(url, include_keywords) and _matches_path_depth(url, minimum_path_segments):
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
                    if _matches_keywords(url, include_keywords) and _matches_path_depth(url, minimum_path_segments):
                        results.append(url)
                        if max_urls is not None and len(results) >= max_urls:
                            return results

                current_url = _normalize_known_hosts(current)
                current_url = _strip_locale_segment(current_url) if strip_locale_prefix else current_url
                if (
                    not _matches_exclude_keywords(current_url, exclude_keywords)
                    and _matches_keywords(current_url, include_keywords)
                    and _matches_path_depth(current_url, minimum_path_segments)
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
                if _looks_like_js_template_url(raw_url):
                    continue
                url = _strip_locale_segment(raw_url) if strip_locale_prefix else raw_url
                if _matches_exclude_keywords(url, exclude_keywords):
                    continue
                if _matches_keywords(url, include_keywords) and _matches_path_depth(url, minimum_path_segments):
                    results.append(url)
                    if max_urls is not None and len(results) >= max_urls:
                        return results

    return results


def discover_product_urls_from_links(
    client: HttpClient,
    seed_urls: tuple[str, ...],
    include_keywords: tuple[str, ...],
    exclude_keywords: tuple[str, ...] = (),
    max_urls: int | None = None,
    strip_locale_prefix: bool = True,
    max_depth: int = 1,
    minimum_path_segments: int = 0,
) -> list[str]:
    queue: deque[tuple[str, int]] = deque((seed, 0) for seed in seed_urls)
    seen: set[str] = set()
    results: list[str] = []
    allowed_hosts = {urlparse(seed).netloc.lower() for seed in seed_urls if urlparse(seed).netloc}

    while queue:
        current, depth = queue.popleft()
        normalized_current = _normalize_known_hosts(current)
        if normalized_current in seen:
            continue
        seen.add(normalized_current)

        url_for_match = _strip_locale_segment(normalized_current) if strip_locale_prefix else normalized_current
        if not _matches_exclude_keywords(url_for_match, exclude_keywords) and _matches_keywords(
            url_for_match, include_keywords
        ) and _matches_path_depth(url_for_match, minimum_path_segments):
            results.append(url_for_match)
            if max_urls is not None and len(results) >= max_urls:
                return results

        if depth >= max_depth:
            continue

        try:
            response = client.get(normalized_current)
        except Exception:
            continue

        for href in _extract_href_links_relaxed(response.text, normalized_current):
            normalized_href = _normalize_known_hosts(href)
            parsed = urlparse(normalized_href)
            if parsed.scheme not in {"http", "https"}:
                continue
            if not _is_same_host(normalized_href, allowed_hosts):
                continue
            if _looks_like_asset_url(normalized_href):
                continue
            if parsed.fragment:
                normalized_href = urlunparse(
                    (parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, "")
                )
            if normalized_href in seen:
                continue
            queue.append((normalized_href, depth + 1))

    return results


def discover_product_urls_via_search(
    client: HttpClient,
    search_queries: tuple[str, ...],
    include_keywords: tuple[str, ...],
    exclude_keywords: tuple[str, ...] = (),
    max_urls: int | None = None,
    strip_locale_prefix: bool = True,
    minimum_path_segments: int = 0,
    pages_per_query: int = 1,
) -> list[str]:
    results: list[str] = []
    seen: set[str] = set()
    page_count = max(1, pages_per_query)

    for query in search_queries:
        for page in range(page_count):
            if max_urls is not None and len(results) >= max_urls:
                return results

            params = {"q": query}
            if page > 0:
                params["s"] = str(page * 30)
            search_url = f"https://duckduckgo.com/html/?{urlencode(params)}"

            try:
                response = client.get(search_url, timeout=min(client.timeout, 12.0), retries=0)
            except requests.RequestException:
                continue

            for href in _extract_href_links_relaxed(response.text, search_url):
                parsed = urlparse(href)
                candidate = href
                if parsed.netloc.endswith("duckduckgo.com") and parsed.path.startswith("/l/"):
                    uddg = parse_qs(parsed.query).get("uddg")
                    if not uddg:
                        continue
                    candidate = _decode_uddg_url(uddg[0])

                normalized = _normalize_known_hosts(candidate)
                parsed_candidate = urlparse(normalized)
                if parsed_candidate.scheme not in {"http", "https"}:
                    continue
                if "asrock.com" not in parsed_candidate.netloc.lower():
                    continue

                url_for_match = _strip_locale_segment(normalized) if strip_locale_prefix else normalized
                if url_for_match in seen:
                    continue
                seen.add(url_for_match)

                if _matches_exclude_keywords(url_for_match, exclude_keywords):
                    continue
                if not _matches_keywords(url_for_match, include_keywords):
                    continue
                if not _matches_path_depth(url_for_match, minimum_path_segments):
                    continue
                results.append(url_for_match)
                if max_urls is not None and len(results) >= max_urls:
                    return results

    return results
