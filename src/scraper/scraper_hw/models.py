from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass(slots=True)
class ProductRecord:
    vendor: str
    url: str
    name: str | None = None
    model: str | None = None
    category: str | None = None
    specs: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)
