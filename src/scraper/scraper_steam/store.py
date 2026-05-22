from __future__ import annotations

import sys
import time
from dataclasses import asdict, dataclass, field

import requests
from bs4 import BeautifulSoup


@dataclass(slots=True)
class GameRequirements:
    rank: int
    app_id: int
    name: str
    pc_minimum: dict[str, str] = field(default_factory=dict)
    pc_recommended: dict[str, str] = field(default_factory=dict)
    mac_minimum: dict[str, str] = field(default_factory=dict)
    mac_recommended: dict[str, str] = field(default_factory=dict)
    linux_minimum: dict[str, str] = field(default_factory=dict)
    linux_recommended: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


def _parse_requirements_html(html: str) -> dict[str, str]:
    if not html:
        return {}
    soup = BeautifulSoup(html, "lxml")
    specs: dict[str, str] = {}
    for li in soup.select("li"):
        text = " ".join(li.get_text(" ", strip=True).split())
        if ":" not in text:
            continue
        key, _, value = text.partition(":")
        key = key.strip()
        value = value.strip()
        if key and value:
            specs[key] = value
    return specs


def _fetch_app_data(session: requests.Session, app_id: int, retries: int = 3) -> dict | None:
    for attempt in range(retries):
        try:
            response = session.get(
                "https://store.steampowered.com/api/appdetails",
                params={"appids": app_id},
                timeout=15.0,
            )

            if response.status_code == 429:
                wait = 60.0 * (attempt + 1)
                print(f"  [rate limited] 429 on app {app_id}, waiting {wait:.0f}s …", file=sys.stderr, flush=True)
                time.sleep(wait)
                continue

            response.raise_for_status()

            try:
                payload = response.json()
            except ValueError:
                print(f"  [warn] non-JSON response for app {app_id} (status {response.status_code}): {response.text[:120]}", file=sys.stderr, flush=True)
                return None

            app_payload = payload.get(str(app_id), {})
            if not app_payload.get("success"):
                return None

            data = app_payload.get("data")
            return data if isinstance(data, dict) else None

        except requests.RequestException as exc:
            print(f"  [warn] request error for app {app_id} (attempt {attempt+1}): {exc}", file=sys.stderr, flush=True)
            if attempt < retries - 1:
                time.sleep(2.0 ** attempt)

    return None


def fetch_requirements(
    entries: list[tuple[int, int, str]],  # (rank, app_id, name)
    delay_seconds: float = 1.5,
    verbose: bool = True,
) -> list[GameRequirements]:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "application/json, text/javascript, */*; q=0.01",
    })

    results: list[GameRequirements] = []

    for idx, (rank, app_id, name) in enumerate(entries):
        if verbose and idx % 50 == 0:
            print(f"  {idx}/{len(entries)} …", file=sys.stderr, flush=True)

        data = _fetch_app_data(session, app_id)
        if data is None:
            continue

        req = GameRequirements(rank=rank, app_id=app_id, name=data.get("name", name))

        for platform_key, min_field, rec_field in [
            ("pc_requirements", "pc_minimum", "pc_recommended"),
            ("mac_requirements", "mac_minimum", "mac_recommended"),
            ("linux_requirements", "linux_minimum", "linux_recommended"),
        ]:
            platform = data.get(platform_key, {})
            if isinstance(platform, dict):
                setattr(req, min_field, _parse_requirements_html(platform.get("minimum", "")))
                setattr(req, rec_field, _parse_requirements_html(platform.get("recommended", "")))

        results.append(req)

        if idx < len(entries) - 1 and delay_seconds > 0:
            time.sleep(delay_seconds)

    return results
