from __future__ import annotations

import sys
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ChartEntry:
    rank: int
    name: str
    app_id: int
    current_players: int | None = None
    peak_today: int | None = None
    peak_all_time: int | None = None


def _parse_player_count(text: str) -> int | None:
    cleaned = text.strip().replace(",", "").replace("\xa0", "").split()[0] if text.strip() else ""
    try:
        return int(cleaned)
    except ValueError:
        return None


def _stealth_init_script() -> str:
    return """
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
    Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
    window.chrome = { runtime: {} };
    """


def _wait_through_cloudflare(page, table_selector: str, total_wait: float = 30.0) -> bool:
    """Return True once the table is visible; False if Cloudflare never clears."""
    deadline = time.monotonic() + total_wait
    while time.monotonic() < deadline:
        title = page.title().lower()
        if "just a moment" in title or "checking" in title or "attention required" in title:
            print("  [cloudflare] challenge detected, waiting …", file=sys.stderr)
            time.sleep(3.0)
            continue
        el = page.query_selector(table_selector)
        if el is not None:
            return True
        time.sleep(2.0)
    return False


def parse_charts_from_file(path: str | Path, limit: int = 1000) -> list[ChartEntry]:
    from bs4 import BeautifulSoup

    html = Path(path).read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "lxml")
    entries: list[ChartEntry] = []

    for row in soup.select("table#table-apps tbody tr[data-appid]"):
        if len(entries) >= limit:
            break
        try:
            app_id = int(row["data-appid"])
        except (KeyError, ValueError):
            continue

        name_el = row.select_one(".b") or row.select_one("a[href*='/app/']")
        name = name_el.get_text(strip=True) if name_el else None
        if not name:
            continue

        cells = row.select("td")
        current_players = _parse_player_count(cells[3].get_text()) if len(cells) > 3 else None
        peak_today      = _parse_player_count(cells[4].get_text()) if len(cells) > 4 else None
        peak_all_time   = _parse_player_count(cells[5].get_text()) if len(cells) > 5 else None

        entries.append(ChartEntry(
            rank=len(entries) + 1,
            name=name,
            app_id=app_id,
            current_players=current_players,
            peak_today=peak_today,
            peak_all_time=peak_all_time,
        ))

    return entries


def fetch_charts(limit: int = 1000, timeout: float = 60.0, headless: bool = True) -> list[ChartEntry]:
    from playwright.sync_api import sync_playwright

    entries: list[ChartEntry] = []
    seen_ids: set[int] = set()
    table_selector = "table#table-apps tbody tr[data-appid]"

    def _extract_rows(page) -> None:
        rows = page.query_selector_all(table_selector)
        for row in rows:
            if len(entries) >= limit:
                break

            app_id_str = row.get_attribute("data-appid")
            if not app_id_str:
                continue
            try:
                app_id = int(app_id_str)
            except ValueError:
                continue
            if app_id in seen_ids:
                continue

            name_el = row.query_selector(".b") or row.query_selector("a[href*='/app/']")
            name = name_el.inner_text().strip() if name_el else None
            if not name:
                continue

            # Columns: rank | icon | name | current | peak-today | peak-alltime | trend
            cells = row.query_selector_all("td")
            current_players = _parse_player_count(cells[3].inner_text()) if len(cells) > 3 else None
            peak_today      = _parse_player_count(cells[4].inner_text()) if len(cells) > 4 else None
            peak_all_time   = _parse_player_count(cells[5].inner_text()) if len(cells) > 5 else None

            seen_ids.add(app_id)
            entries.append(ChartEntry(
                rank=len(entries) + 1,
                name=name,
                app_id=app_id,
                current_players=current_players,
                peak_today=peak_today,
                peak_all_time=peak_all_time,
            ))

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"],
        )
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.7727.56 Safari/537.36"
            ),
            locale="en-US",
            viewport={"width": 1280, "height": 900},
        )
        context.add_init_script(_stealth_init_script())
        page = context.new_page()

        page.goto("https://steamdb.info/charts/", wait_until="load", timeout=int(timeout * 1000))

        print(f"  [page title] {page.title()!r}", file=sys.stderr)

        found = _wait_through_cloudflare(page, table_selector, total_wait=max(timeout, 30.0))
        if not found:
            screenshot_path = Path("output/debug_screenshot.png")
            screenshot_path.parent.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(screenshot_path), full_page=True)
            browser.close()
            raise RuntimeError(
                f"Table '{table_selector}' never appeared. "
                f"Page title was {page.title()!r}. "
                f"Screenshot saved to {screenshot_path} — check if Cloudflare blocked the request."
            )

        # Try to expand DataTables to show all rows at once
        try:
            page.select_option("select[name='table-apps_length']", value="-1")
            time.sleep(2.0)
        except Exception:
            pass

        _extract_rows(page)

        # Page through DataTables if it's server-side paginated
        while len(entries) < limit:
            next_btn = page.query_selector("#table-apps_next:not(.disabled)")
            if next_btn is None:
                break
            next_btn.click()
            time.sleep(2.0)
            _extract_rows(page)

        browser.close()

    return entries[:limit]
