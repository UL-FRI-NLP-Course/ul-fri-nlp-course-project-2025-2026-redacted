from __future__ import annotations

import re
import sys
import time
from urllib.parse import urlparse
from urllib.parse import urljoin
from xml.etree.ElementTree import ParseError

import requests
from bs4 import BeautifulSoup

from scraper_hw.crawler import discover_product_urls
from scraper_hw.http import HttpClient
from scraper_hw.models import ProductRecord
from scraper_hw.parsers import parse_product_html
from scraper_hw.vendors import VendorConfig


def _dedupe_preserve_order(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def _build_spec_candidate_urls(vendor: str, url: str) -> list[str]:
    base = url.rstrip("/")
    candidates: list[str] = [url]

    if vendor == "asus":
        candidates.append(f"{base}/techspec/")
    elif vendor == "gigabyte":
        candidates.append(f"{base}/sp")
    elif vendor == "msi":
        candidates.append(f"{base}/Specification")
    elif vendor == "noctua":
        candidates.append(f"{base}/specifications")
    elif vendor == "asrock":
        if re.search(r"index\.asp$", base, flags=re.IGNORECASE):
            spec_url = re.sub(r"index\.asp$", "index.us.asp", base, flags=re.IGNORECASE)
        else:
            spec_url = f"{base}/index.us.asp"
        candidates.append(f"{spec_url}#Specification")
        candidates.append(spec_url)
    return _dedupe_preserve_order(candidates)


def _merge_records(target: ProductRecord, source: ProductRecord) -> ProductRecord:
    if target.name is None and source.name is not None:
        target.name = source.name
    if target.model is None and source.model is not None:
        target.model = source.model
    if target.category is None and source.category is not None:
        target.category = source.category
    for key, value in source.specs.items():
        target.specs.setdefault(key, value)
    return target


def _needs_fallback_spec_fetch(record: ProductRecord | None) -> bool:
    if record is None:
        return True
    return len(record.specs) < 4


def _extract_biostar_spec_urls(page_url: str, html: str) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    spec_urls: list[str] = []
    for tab in soup.select('[data-option][route]'):
        option = " ".join((tab.get("data-option") or "").split()).lower()
        route = tab.get("route")
        if not route or "spec" not in option:
            continue
        spec_urls.append(urljoin(page_url, route.strip()))
    return _dedupe_preserve_order(spec_urls)


def scrape_vendor(
    config: VendorConfig,
    *,
    limit: int | None = None,
    delay_seconds: float = 0.5,
    timeout: float = 20.0,
) -> list[ProductRecord]:
    client = HttpClient(timeout=timeout)
    all_urls: list[str] = []

    for sitemap in config.sitemaps:
        try:
            urls = discover_product_urls(
                client,
                sitemap,
                config.include_keywords,
                exclude_keywords=config.exclude_keywords,
                max_urls=limit,
                strip_locale_prefix=config.strip_locale_prefix,
            )
            all_urls.extend(urls)
        except (requests.RequestException, ParseError, ValueError) as exc:
            print(f"[warn] could not parse sitemap {sitemap}: {exc}", file=sys.stderr)

    unique_urls = list(dict.fromkeys(all_urls))
    if limit is not None:
        unique_urls = unique_urls[:limit]

    products: list[ProductRecord] = []
    for idx, url in enumerate(unique_urls):
        parsed_url = urlparse(url)
        if config.name == "fractal-design" and parsed_url.path.rstrip("/") == "/products":
            continue

        combined_product: ProductRecord | None = None
        candidate_urls = _build_spec_candidate_urls(config.name, url)
        if not candidate_urls:
            continue

        # Fetch canonical URL first; try extra spec endpoints only when specs are sparse.
        primary_url = candidate_urls[0]
        try:
            primary_response = client.get(primary_url)
            parsed = parse_product_html(config.name, primary_url, primary_response.text)
            if parsed is not None:
                combined_product = parsed
                combined_product.url = url

            if config.name == "biostar" and "introduction.php" in primary_url.lower() and primary_response is not None:
                for spec_url in _extract_biostar_spec_urls(primary_url, primary_response.text):
                    try:
                        spec_response = client.get(spec_url, timeout=min(timeout, 12.0), retries=0)
                    except requests.RequestException:
                        continue
                    spec_record = parse_product_html(config.name, spec_url, spec_response.text)
                    if spec_record is None:
                        continue
                    if combined_product is None:
                        combined_product = spec_record
                        combined_product.url = url
                    else:
                        combined_product = _merge_records(combined_product, spec_record)
        except requests.RequestException:
            pass

        for candidate_url in candidate_urls[1:]:
            if not _needs_fallback_spec_fetch(combined_product):
                break
            try:
                response = client.get(candidate_url, timeout=min(timeout, 12.0), retries=0)
                parsed = parse_product_html(config.name, candidate_url, response.text)
                if parsed is None:
                    continue
                if combined_product is None:
                    combined_product = parsed
                    combined_product.url = url
                else:
                    combined_product = _merge_records(combined_product, parsed)
            except requests.RequestException:
                continue

        if combined_product is not None:
            products.append(combined_product)
        else:
            print(f"[warn] failed to fetch product content from {url}", file=sys.stderr)

        if idx < len(unique_urls) - 1 and delay_seconds > 0:
            time.sleep(delay_seconds)

    return products
