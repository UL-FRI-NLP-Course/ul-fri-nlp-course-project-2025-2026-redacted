from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass(slots=True)
class SiteRef:
    title: str
    url: str
    language: str
    organization: str
    categories: list[str] = field(default_factory=list)
    standard_description: str = ""


@dataclass(slots=True)
class TopicMeta:
    topic_id: str
    title: str
    url: str
    language: str
    date_created: str
    also_called: list[str] = field(default_factory=list)
    groups: list[str] = field(default_factory=list)
    mesh_headings: list[str] = field(default_factory=list)
    see_references: list[str] = field(default_factory=list)
    full_summary_text: str = ""
    sites: list[SiteRef] = field(default_factory=list)
    primary_institute: str = ""


@dataclass(slots=True)
class Chunk:
    chunk_id: str
    topic_id: str
    topic_title: str
    topic_url: str
    groups: list[str]
    also_called: list[str]
    mesh_headings: list[str]
    source_url: str
    source_title: str
    organization: str
    information_categories: list[str]
    text: str
    chunk_index: int
    total_chunks: int

    def to_dict(self) -> dict:
        return asdict(self)
