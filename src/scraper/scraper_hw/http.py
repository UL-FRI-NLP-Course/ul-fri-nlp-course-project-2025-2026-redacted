from __future__ import annotations

import time

import requests


class HttpClient:
    def __init__(self, timeout: float = 20.0, retries: int = 2) -> None:
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (X11; Linux x86_64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36 hw-scraper/0.1"
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
