import json
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.lttlabs.com/products"
LIST_URL = "https://www.lttlabs.com/products/archives/1"
PER_PAGE = 250
OUTPUT_FILE = Path(__file__).parent.parent.parent.parent / "data" / "lttlabs.jsonl"


def extract_specs(model: dict) -> dict:
    skip = {
        "__hydratedModel", "affiliateLinks", "authors", "documents",
        "featuresAndSoftwareNotes", "featuresAndSoftwareSoftwareAssets",
        "hardwareNotes", "hardwareAssets", "performanceNotes",
        "performanceSoftwareAssets", "highlights", "productImages",
        "testConfigurationNotes", "testConfigurationAssets",
        "createdAt", "updatedAt", "labsWebAvailableAt", "deck",
        "brand", "model", "category", "categorySlug", "assetTag", "slug",
    }
    return {k: v for k, v in model.items() if k not in skip and not isinstance(v, (list, dict))}


def extract_text(model: dict) -> str:
    parts = []
    if model.get("deck"):
        parts.append(model["deck"])
    for field in ("hardwareNotes", "featuresAndSoftwareNotes", "performanceNotes", "testConfigurationNotes"):
        for block in model.get(field) or []:
            if isinstance(block, dict) and block.get("insert"):
                text = block["insert"].strip()
                if text:
                    parts.append(text)
    for h in model.get("highlights") or []:
        if isinstance(h, dict):
            for key in ("title", "body"):
                if h.get(key):
                    parts.append(h[key].strip())
    return "\n\n".join(parts)


def process_result(data: dict, out):
    for result in data.get("results", []):
        for hit in result.get("hits", []):
            doc = hit["document"]
            model = doc.get("__hydratedModel", doc)
            slug = model.get("slug") or doc.get("slug", "")
            category = model.get("categorySlug") or model.get("category", "")
            url = f"{BASE_URL}/{category}/{slug}" if slug else ""
            record = {
                "vendor": "lttlabs",
                "url": url,
                "name": f"{model.get('brand', '')} {model.get('model', '')}".strip(),
                "brand": model.get("brand"),
                "category": category,
                "specs": extract_specs(model),
                "text": extract_text(model),
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")


def scrape():
    with sync_playwright() as p, OUTPUT_FILE.open("w", encoding="utf-8") as out:
        browser = p.chromium.launch()
        page = browser.new_page()

        captured = []

        def handle_response(response):
            if "typesense/multi_search" in response.url and "x-typesense-api-key=" in response.url:
                try:
                    captured.append(response.json())
                except Exception:
                    pass

        page.on("response", handle_response)

        # Load the first archives page — this triggers the initial search API call
        page.goto(LIST_URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(5000)

        if not captured:
            print("No API responses captured", file=sys.stderr)
            browser.close()
            return

        # Use JS fetch for all pages so we control per_page
        api_url = "https://www.lttlabs.com/api/typesense/multi_search?x-typesense-api-key="
        fetched = 0
        total = None
        pg = 1
        while True:
            body = json.dumps({
                "searches": [{
                    "collection": "generic_text_search",
                    "highlight_full_fields": "model",
                    "page": pg,
                    "per_page": PER_PAGE,
                    "q": "*",
                    "query_by": "model,brand,assetTag",
                    "sort_by": "labsWebAvailableAt:desc",
                }]
            })
            resp = page.evaluate(f"""
                fetch("{api_url}", {{
                    method: "POST",
                    headers: {{"Content-Type": "application/json"}},
                    body: {repr(body)}
                }}).then(r => r.json())
            """)
            if total is None:
                total = resp["results"][0].get("found", 0)
                print(f"Total products: {total}", file=sys.stderr)
            process_result(resp, out)
            hits = len(resp["results"][0].get("hits", []))
            if hits == 0:
                break
            fetched += hits
            print(f"Fetched {fetched}/{total}", file=sys.stderr)
            if fetched >= total:
                break
            time.sleep(1)
            pg += 1

        page.remove_listener("response", handle_response)
        browser.close()


if __name__ == "__main__":
    scrape()
