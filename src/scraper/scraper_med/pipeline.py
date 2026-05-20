from __future__ import annotations

import hashlib
import sys
import time

import requests

from scraper_med.http import HttpClient
from scraper_med.models import Chunk, TopicMeta
from scraper_med.page_scraper import extract_page_text
from scraper_med.xml_parser import parse_topics_xml

_DEFAULT_XML_URL = "https://medlineplus.gov/xml/mplus_topics_2026-05-16.xml"
_MAX_CHUNK_CHARS = 1500
_OVERLAP_CHARS = 150


def _chunk_text(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    if len(text) <= _MAX_CHUNK_CHARS:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + _MAX_CHUNK_CHARS
        if end >= len(text):
            chunk = text[start:].strip()
            if chunk:
                chunks.append(chunk)
            break

        midpoint = start + _MAX_CHUNK_CHARS // 2
        break_at = text.rfind(". ", midpoint, end)
        if break_at != -1:
            end = break_at + 2
        else:
            break_at = text.rfind(" ", midpoint, end)
            if break_at != -1:
                end = break_at + 1

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = max(end - _OVERLAP_CHARS, start + 1)

    return chunks


def _make_chunk_id(topic_id: str, source_url: str, index: int) -> str:
    key = f"{topic_id}:{source_url}:{index}"
    return hashlib.sha1(key.encode()).hexdigest()[:16]


def _build_chunks(
    text: str,
    topic: TopicMeta,
    source_url: str,
    source_title: str,
    organization: str,
    categories: list[str],
) -> list[Chunk]:
    parts = _chunk_text(text)
    total = len(parts)
    return [
        Chunk(
            chunk_id=_make_chunk_id(topic.topic_id, source_url, idx),
            topic_id=topic.topic_id,
            topic_title=topic.title,
            topic_url=topic.url,
            groups=list(topic.groups),
            also_called=list(topic.also_called),
            mesh_headings=list(topic.mesh_headings),
            source_url=source_url,
            source_title=source_title,
            organization=organization,
            information_categories=categories,
            text=part,
            chunk_index=idx,
            total_chunks=total,
        )
        for idx, part in enumerate(parts)
    ]


def scrape_topics(
    xml_url: str = _DEFAULT_XML_URL,
    xml_text: str | None = None,
    *,
    limit: int | None = None,
    max_sites_per_topic: int | None = None,
    include_summaries: bool = True,
    skip_site_scraping: bool = False,
    language_filter: str | None = "English",
    category_filter: set[str] | None = None,
    delay_seconds: float = 0.5,
    timeout: float = 20.0,
) -> list[Chunk]:
    client = HttpClient(timeout=timeout)

    if xml_text is None:
        print(f"[info] fetching {xml_url}", file=sys.stderr)
        try:
            response = client.get(xml_url)
            xml_text = response.text
        except requests.RequestException as exc:
            raise RuntimeError(f"Failed to fetch XML: {exc}") from exc

    topics = parse_topics_xml(xml_text, language_filter=language_filter)
    print(f"[info] parsed {len(topics)} topics", file=sys.stderr)

    if limit is not None:
        topics = topics[:limit]

    all_chunks: list[Chunk] = []

    for topic_idx, topic in enumerate(topics):
        if include_summaries and topic.full_summary_text:
            all_chunks.extend(
                _build_chunks(
                    topic.full_summary_text,
                    topic,
                    source_url=topic.url,
                    source_title=f"{topic.title} - MedlinePlus",
                    organization="National Library of Medicine",
                    categories=["Overview"],
                )
            )

        if skip_site_scraping:
            continue

        sites_to_scrape = topic.sites
        if category_filter:
            sites_to_scrape = [
                s for s in sites_to_scrape
                if any(cat in category_filter for cat in s.categories)
            ]
        if max_sites_per_topic is not None:
            sites_to_scrape = sites_to_scrape[:max_sites_per_topic]

        for site_idx, site in enumerate(sites_to_scrape):
            if not site.url:
                continue

            print(
                f"[info] topic {topic_idx + 1}/{len(topics)}"
                f" site {site_idx + 1}/{len(sites_to_scrape)}: {site.url}",
                file=sys.stderr,
            )

            text = extract_page_text(client, site.url, timeout=timeout)
            if text:
                all_chunks.extend(
                    _build_chunks(
                        text,
                        topic,
                        source_url=site.url,
                        source_title=site.title,
                        organization=site.organization,
                        categories=site.categories,
                    )
                )
            else:
                print(f"[warn] no text extracted from {site.url}", file=sys.stderr)

            if delay_seconds > 0:
                time.sleep(delay_seconds)

    return all_chunks
