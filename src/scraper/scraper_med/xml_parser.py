from __future__ import annotations

from xml.etree import ElementTree

from scraper_med.models import SiteRef, TopicMeta


def _inner_text(el: ElementTree.Element) -> str:
    return " ".join("".join(el.itertext()).split())


def parse_topics_xml(xml_text: str, language_filter: str | None = "English") -> list[TopicMeta]:
    root = ElementTree.fromstring(xml_text)
    topics: list[TopicMeta] = []

    for topic_el in root.findall(".//health-topic"):
        lang = topic_el.get("language", "English")
        if language_filter and lang != language_filter:
            continue

        topic = TopicMeta(
            topic_id=topic_el.get("id", ""),
            title=topic_el.get("title", ""),
            url=topic_el.get("url", ""),
            language=lang,
            date_created=topic_el.get("date-created", ""),
        )

        for el in topic_el.findall("also-called"):
            text = _inner_text(el)
            if text:
                topic.also_called.append(text)

        for el in topic_el.findall("group"):
            text = _inner_text(el)
            if text:
                topic.groups.append(text)

        for el in topic_el.findall(".//mesh-heading/descriptor"):
            text = _inner_text(el)
            if text:
                topic.mesh_headings.append(text)

        for el in topic_el.findall("see-reference"):
            text = _inner_text(el)
            if text:
                topic.see_references.append(text)

        summary_el = topic_el.find("full-summary")
        if summary_el is not None:
            topic.full_summary_text = _inner_text(summary_el)

        pi_el = topic_el.find("primary-institute")
        if pi_el is not None:
            topic.primary_institute = _inner_text(pi_el)

        for site_el in topic_el.findall("site"):
            site = SiteRef(
                title=site_el.get("title", ""),
                url=site_el.get("url", ""),
                language=site_el.get("language", ""),
                organization=site_el.get("organization", ""),
            )
            for cat_el in site_el.findall("information-category"):
                text = _inner_text(cat_el)
                if text:
                    site.categories.append(text)
            desc_el = site_el.find("standard-description")
            if desc_el is not None:
                site.standard_description = _inner_text(desc_el)
            topic.sites.append(site)

        topics.append(topic)

    return topics
