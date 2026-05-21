from __future__ import annotations

import time
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from playwright.sync_api import Browser, Playwright, SyncPlaywrightContextManager


class HttpClient:
    def __init__(self, timeout: float = 20.0, retries: int = 2) -> None:
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0"
                )
            }
        )

    def get(self, url: str, *, timeout: float | None = None, retries: int | None = None) -> requests.Response:
        effective_timeout = self.timeout if timeout is None else timeout
        effective_retries = self.retries if retries is None else retries
        last_error: requests.RequestException | None = None
        for attempt in range(effective_retries + 1):
            try:
                response = self.session.get(url, timeout=effective_timeout)
                response.raise_for_status()
                return response
            except requests.RequestException as exc:
                last_error = exc
                if attempt < effective_retries:
                    time.sleep(0.5 * (attempt + 1))
        assert last_error is not None
        raise last_error


class BrowserPage:
    """Minimal response-like wrapper around Playwright-rendered HTML."""
    def __init__(self, text: str) -> None:
        self.text = text


class PlaywrightClient:
    """Headless-browser fetcher for JS-rendered or bot-protected pages.

    Use as a context manager so the browser process is shared across requests:

        with PlaywrightClient() as pw:
            page = pw.get(url)
            html = page.text
    """

    _UA = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    )

    def __init__(self, timeout: float = 30.0) -> None:
        self._timeout_ms = int(timeout * 1000)
        self._pw_cm: SyncPlaywrightContextManager | None = None
        self._pw: Playwright | None = None
        self._browser: Browser | None = None

    def __enter__(self) -> PlaywrightClient:
        from playwright.sync_api import sync_playwright
        self._pw_cm = sync_playwright()
        self._pw = self._pw_cm.__enter__()
        # Firefox avoids Chromium-specific headless fingerprints caught by Akamai/Cloudflare
        self._browser = self._pw.firefox.launch(headless=True)
        return self

    def __exit__(self, *args: object) -> None:
        if self._browser:
            self._browser.close()
        if self._pw_cm:
            self._pw_cm.__exit__(*args)

    _CONSENT_SELECTORS = (
        "#onetrust-accept-btn-handler",
        'button:has-text("Accept All Cookies")',
        'button:has-text("Accept All")',
        'button:has-text("Accept all")',
        'button:has-text("Agree to all")',
        'button:has-text("Agree")',
        '[id*="accept"][role="button"]',
        '[id*="accept-all"]',
        '[class*="accept-all"]',
        '[class*="acceptAll"]',
    )

    def _dismiss_cookie_consent(self, page: object) -> None:
        for selector in self._CONSENT_SELECTORS:
            try:
                btn = page.locator(selector).first  # type: ignore[attr-defined]
                if btn.is_visible(timeout=1200):
                    btn.click()
                    page.wait_for_timeout(1200)  # type: ignore[attr-defined]
                    return
            except Exception:
                pass

    def get(self, url: str) -> BrowserPage:
        assert self._browser is not None, "PlaywrightClient must be used as a context manager"
        context = self._browser.new_context(
            user_agent=self._UA,
            viewport={"width": 1280, "height": 900},
            java_script_enabled=True,
            ignore_https_errors=True,
        )
        page = context.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=self._timeout_ms)
            self._dismiss_cookie_consent(page)
            # Let JS populate spec tables/components before capturing
            page.wait_for_timeout(2500)
            return BrowserPage(page.content())
        finally:
            page.close()
            context.close()
