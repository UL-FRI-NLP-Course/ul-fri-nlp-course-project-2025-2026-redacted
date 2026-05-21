from __future__ import annotations

import json
from json import JSONDecodeError
import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from scraper_hw.models import ProductRecord


TECHNICAL_KEY_HINTS = (
    "model",
    "part number",
    "sku",
    "chipset",
    "socket",
    "memory",
    "capacity",
    "interface",
    "dimensions",
    "dimension",
    "weight",
    "power",
    "voltage",
    "frequency",
    "clock",
    "cores",
    "threads",
    "resolution",
    "ports",
    "lan",
    "wifi",
    "bluetooth",
    "pcie",
    "sata",
    "usb",
    "warranty",
)


def _is_in_non_content_area(node) -> bool:
    return bool(node.find_parent(["header", "nav", "footer", "aside"]))


def _looks_technical_key(key: str) -> bool:
    lowered = key.lower()
    return any(hint in lowered for hint in TECHNICAL_KEY_HINTS)


def _extract_category(soup: BeautifulSoup) -> str | None:
    crumb_nodes = soup.select(
        '[itemprop="itemListElement"] [itemprop="name"], nav[aria-label*="breadcrumb" i] a, .breadcrumb a'
    )
    values = [" ".join(node.get_text(" ", strip=True).split()) for node in crumb_nodes]
    values = [value for value in values if value]
    if len(values) >= 2:
        return values[-2]
    if values:
        return values[-1]
    return None


def _extract_category_from_url(url: str) -> str | None:
    segments = [segment for segment in urlparse(url).path.split("/") if segment]
    skip = {"en", "fr", "de", "it", "es", "pt", "ru", "cn", "tw", "jp", "kr", "africa-fr"}
    for segment in segments:
        if segment.lower() in skip:
            continue
        if segment.lower() in {"www", "home"}:
            continue
        return segment.replace("-", " ").strip() or None
    return None


def _extract_jsonld_blocks(soup: BeautifulSoup) -> list[dict]:
    blocks: list[dict] = []
    for script in soup.select('script[type="application/ld+json"]'):
        raw = script.string or script.get_text(strip=True)
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
        except JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            blocks.append(parsed)
        elif isinstance(parsed, list):
            blocks.extend(item for item in parsed if isinstance(item, dict))
    return blocks


def _find_jsonld_product(blocks: list[dict]) -> dict | None:
    for block in blocks:
        block_type = block.get("@type")
        if isinstance(block_type, list):
            type_values = [str(item).lower() for item in block_type]
            if "product" in type_values:
                return block
        elif isinstance(block_type, str) and block_type.lower() == "product":
            return block
    return None


def _extract_specs_from_table(soup: BeautifulSoup) -> dict[str, str]:
    specs: dict[str, str] = {}
    for table in soup.select("table"):
        if _is_in_non_content_area(table):
            continue

        table_specs: dict[str, str] = {}
        technical_key_found = False
        for row in table.select("tr"):
            key_cell = row.find("th")
            value_cell = row.find("td")
            if key_cell is None or value_cell is None:
                cells = row.find_all("td")
                if len(cells) == 2:
                    key_cell, value_cell = cells
                else:
                    continue
            key = " ".join(key_cell.get_text(" ", strip=True).split())
            value = " ".join(value_cell.get_text(" ", strip=True).split())
            if not key or not value:
                continue
            if _looks_technical_key(key):
                technical_key_found = True
            table_specs[key] = value

        if technical_key_found or len(table_specs) >= 4:
            specs.update(table_specs)
    return specs


def _extract_specs_from_dl(soup: BeautifulSoup) -> dict[str, str]:
    specs: dict[str, str] = {}
    for dl in soup.select("dl"):
        if _is_in_non_content_area(dl):
            continue
        terms = dl.find_all("dt")
        dl_specs: dict[str, str] = {}
        technical_key_found = False
        for term in terms:
            value = term.find_next_sibling("dd")
            if value is None:
                continue
            key = " ".join(term.get_text(" ", strip=True).split())
            val = " ".join(value.get_text(" ", strip=True).split())
            if key and val:
                if _looks_technical_key(key):
                    technical_key_found = True
                dl_specs[key] = val
        if technical_key_found or len(dl_specs) >= 4:
            specs.update(dl_specs)
    return specs


def _extract_specs_from_structured_divs(soup: BeautifulSoup) -> dict[str, str]:
    specs: dict[str, str] = {}
    row_nodes = soup.select(
        'div[class*="rowtable" i], div[class*="spec-row" i], div[class*="specrow" i], div[class*="spec_item" i]'
    )
    for row in row_nodes:
        if _is_in_non_content_area(row):
            continue
        key_node = row.select_one(
            '[class*="title" i], [class*="name" i], [class*="label" i], strong, b'
        )
        value_node = row.select_one(
            '[class*="item" i], [class*="value" i], [class*="content" i], [class*="desc" i], p'
        )
        if key_node is None or value_node is None:
            continue
        key = " ".join(key_node.get_text(" ", strip=True).split())
        value = " ".join(value_node.get_text(" ", strip=True).split())
        if not key or not value or key == value:
            continue
        specs[key] = value
    return specs


def _extract_specs_from_spec_lists(soup: BeautifulSoup) -> dict[str, str]:
    specs: dict[str, str] = {}
    for container in soup.select('[class*="spec" i], [id*="spec" i], [class*="techspec" i], [id*="techspec" i]'):
        if _is_in_non_content_area(container):
            continue
        for item in container.select("li, p"):
            text = " ".join(item.get_text(" ", strip=True).split())
            if ":" not in text:
                continue
            key, value = text.split(":", 1)
            key = key.strip()
            value = value.strip()
            if not key or not value:
                continue
            if len(key) > 80 or len(value) > 1000:
                continue
            if not re.search(r"[A-Za-z]", key):
                continue
            specs[key] = value
    return specs


def _extract_specs_from_colon_lines(text: str) -> dict[str, str]:
    specs: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = " ".join(raw_line.split())
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            continue
        if len(key) > 80 or len(value) > 1200:
            continue
        specs[key] = value
    return specs


def _extract_specs_from_container_lists(soup: BeautifulSoup) -> dict[str, str]:
    specs: dict[str, str] = {}
    for container in soup.select(".container-lists"):
        if _is_in_non_content_area(container):
            continue

        for block in container.select("div, section, article"):
            heading_node = block.select_one(
                "h2, h3, h4, h5, strong, b, [class*='title' i], [class*='headline' i], [class*='label' i]"
            )
            heading = None
            if heading_node is not None:
                heading_text = " ".join(heading_node.get_text(" ", strip=True).split())
                if heading_text and len(heading_text) <= 120:
                    heading = heading_text

            for ul in block.select("ul"):
                items = [" ".join(li.get_text(" ", strip=True).split()) for li in ul.select("li")]
                items = [item for item in items if item]
                if not items:
                    continue

                parsed_any_pairs = False
                for item in items:
                    if ":" not in item:
                        continue
                    key, value = item.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key and value:
                        specs[key] = value
                        parsed_any_pairs = True
                if parsed_any_pairs:
                    continue

                if heading:
                    specs[heading] = " | ".join(items)
    return specs


def _extract_maxsun_grid_specs(soup: BeautifulSoup) -> dict[str, str]:
    specs: dict[str, str] = {}
    for grid in soup.select(".ztcanshugrid"):
        if _is_in_non_content_area(grid):
            continue
        for group in grid.select("ul"):
            values = [" ".join(node.get_text(" ", strip=True).split()) for node in group.select("li")]
            values = [value for value in values if value]
            if len(values) < 2:
                continue
            key = values[0].strip()
            value = " ".join(values[1:]).strip()
            if not key or not value:
                continue
            if len(key) > 120 or len(value) > 1200:
                continue
            specs[key] = value
    return specs


def _extract_sparkle_pdf_specs(soup: BeautifulSoup, base_url: str) -> dict[str, str]:
    specs: dict[str, str] = {}
    seen_urls: set[str] = set()
    link_index = 1

    for node in soup.select("a[href], button[data-href], [data-pdf], [data-file], [data-download], [data-url]"):
        text = " ".join(node.get_text(" ", strip=True).split())
        lowered_text = text.lower()
        candidates = [
            node.get("href"),
            node.get("data-href"),
            node.get("data-pdf"),
            node.get("data-file"),
            node.get("data-download"),
            node.get("data-url"),
        ]
        for raw_candidate in candidates:
            if not isinstance(raw_candidate, str):
                continue
            candidate = raw_candidate.strip()
            if not candidate:
                continue
            resolved = urljoin(base_url, candidate)
            lowered_url = resolved.lower()
            if ".pdf" not in lowered_url and "spec sheet" not in lowered_text:
                continue
            if resolved in seen_urls:
                continue
            seen_urls.add(resolved)

            if "spec sheet" in lowered_text:
                key = "Spec Sheet PDF"
            elif text:
                key = f"{text} PDF"
            else:
                key = f"PDF {link_index}"
            link_index += 1
            specs[key] = resolved
    return specs


def _extract_corsair_next_data_specs(soup: BeautifulSoup) -> dict[str, str]:
    specs: dict[str, str] = {}
    next_data = soup.find("script", id="__NEXT_DATA__")
    if next_data is None or not next_data.string:
        return specs

    try:
        payload = json.loads(next_data.string)
    except JSONDecodeError:
        return specs

    try:
        items = payload["props"]["pageProps"]["productData"]["productDetail"]["items"]
    except (KeyError, TypeError):
        return specs
    if not isinstance(items, list) or not items:
        return specs
    first_item = items[0]
    if not isinstance(first_item, dict):
        return specs

    for row in first_item.get("tech_specs", []):
        if not isinstance(row, dict):
            continue
        key = row.get("code")
        value = row.get("value")
        if isinstance(key, str) and isinstance(value, str) and key.strip() and value.strip():
            specs[key.strip()] = value.strip()
    return specs


def _extract_vendor_specific_specs(vendor: str, soup: BeautifulSoup, base_url: str) -> dict[str, str]:
    specs: dict[str, str] = {}

    if vendor == "thermalright":
        description_panel = soup.select_one("#tab-description")
        if description_panel is not None:
            specs.update(_extract_specs_from_colon_lines(description_panel.get_text("\n", strip=True)))

    if vendor == "coolermaster":
        for item in soup.select(".repeater-container.container .repeater-item"):
            key_node = item.select_one(".repeater-item__label")
            value_node = item.select_one(".repeater-item__value")
            if key_node is None or value_node is None:
                continue
            key = " ".join(key_node.get_text(" ", strip=True).split())
            value = " ".join(value_node.get_text(" ", strip=True).split())
            if key and value:
                specs[key] = value

    if vendor == "fractal-design":
        for item in soup.select(".c-product-spec .c-product-spec__item"):
            key_node = item.select_one(".c-product-spec__label")
            value_node = item.select_one(".c-product-spec__value")
            if key_node is None or value_node is None:
                continue
            key = " ".join(key_node.get_text(" ", strip=True).split())
            value = " ".join(value_node.get_text(" ", strip=True).split())
            if key and value:
                specs[key] = value

    if vendor == "sandisk":
        for item in soup.select("#specifications .column-two"):
            key_node = item.select_one(".font-bold")
            value_node = item.select_one(".text-grey-4")
            if key_node is None or value_node is None:
                continue
            key = " ".join(key_node.get_text(" ", strip=True).split())
            value = " ".join(value_node.get_text(" ", strip=True).split())
            if key and value:
                specs[key] = value

    if vendor in {"phanteks", "sapphire", "noctua"}:
        for container in soup.select(".tab-content, .container-lists"):
            specs.update(_extract_specs_from_colon_lines(container.get_text("\n", strip=True)))

    if vendor == "noctua":
        specs.update(_extract_specs_from_container_lists(soup))

    if vendor == "phanteks":
        tab_cells = [
            " ".join(node.get_text(" ", strip=True).split())
            for node in soup.select(".tab-content .container_tabs")
            if node.get_text(" ", strip=True)
        ]
        for index in range(0, len(tab_cells) - 1, 2):
            key = tab_cells[index].strip()
            value = tab_cells[index + 1].strip()
            if not key or not value:
                continue
            if len(key) > 80 or len(value) > 500:
                continue
            specs[key] = value

    if vendor == "msi":
        # JS-rendered spec page: section.specWrapper > div.pdtb > div.tr > div.td
        # Each div.td has a <ul> child (the key) and a NavigableString sibling (the value).
        for row in soup.select("section.specWrapper div.pdtb div.tr"):
            td = row.select_one("div.td")
            if td is None:
                continue
            key_node = td.select_one("ul")
            if key_node is None:
                continue
            key = " ".join(key_node.get_text(" ", strip=True).split())
            value_parts = [
                str(child).strip()
                for child in td.children
                if not getattr(child, "name", None) and str(child).strip()
            ]
            value = " ".join(value_parts)
            if key and value:
                specs[key] = value

    if vendor == "corsair":
        specs.update(_extract_corsair_next_data_specs(soup))

    if vendor in {"powercolor", "powercolour"}:
        for row in soup.select(".dataTable__tr"):
            key_node = row.select_one(".th")
            value_node = row.select_one(".td")
            if key_node is None or value_node is None:
                continue
            key = " ".join(key_node.get_text(" ", strip=True).split())
            value = " ".join(value_node.get_text(" ", strip=True).split())
            if key and value:
                specs[key] = value

    if vendor == "maxsun":
        specs.update(_extract_maxsun_grid_specs(soup))

    if vendor == "sparkle":
        specs.update(_extract_sparkle_pdf_specs(soup, base_url))

    return specs


def _extract_name_fallback(soup: BeautifulSoup) -> str | None:
    blocked_markers = ("access denied", "just a moment", "error", "security checkpoint", "bad gateway")

    og_title = soup.select_one('meta[property="og:title"]')
    if og_title and og_title.get("content"):
        value = " ".join(og_title.get("content", "").split()).strip()
        if value and not any(marker in value.lower() for marker in blocked_markers):
            return value

    if soup.title:
        value = " ".join(soup.title.get_text(" ", strip=True).split())
        if value and not any(marker in value.lower() for marker in blocked_markers):
            return value
    return None


def _contains_template_token(value: str) -> bool:
    lowered = value.lower()
    return "{{" in lowered or "}}" in lowered or "{%" in lowered or "%}" in lowered


def _infer_name_from_url(url: str) -> str | None:
    segments = [segment for segment in urlparse(url).path.split("/") if segment]
    if not segments:
        return None
    for segment in reversed(segments):
        lowered = segment.lower()
        if lowered in {"products", "product", "en", "us", "shop"}:
            continue
        value = segment.replace("-", " ").strip()
        return value if value else None
    return None


def parse_product_html(vendor: str, url: str, html: str) -> ProductRecord | None:
    soup = BeautifulSoup(html, "lxml")
    product = ProductRecord(vendor=vendor, url=url)
    product.category = _extract_category(soup)
    if product.category is None:
        product.category = _extract_category_from_url(url)

    title = soup.find("h1")
    if title:
        product.name = " ".join(title.get_text(" ", strip=True).split())
    if not product.name:
        product.name = _extract_name_fallback(soup)

    blocks = _extract_jsonld_blocks(soup)
    product_block = _find_jsonld_product(blocks)
    if product_block:
        if not product.name and isinstance(product_block.get("name"), str):
            product.name = product_block["name"].strip()
        model_value = product_block.get("model")
        if isinstance(model_value, str):
            product.model = model_value.strip()
        additional = product_block.get("additionalProperty")
        if isinstance(additional, list):
            for item in additional:
                if not isinstance(item, dict):
                    continue
                key = item.get("name")
                value = item.get("value")
                if isinstance(key, str) and isinstance(value, str):
                    product.specs[key.strip()] = value.strip()

    table_specs = _extract_specs_from_table(soup)
    dl_specs = _extract_specs_from_dl(soup)
    structured_div_specs = _extract_specs_from_structured_divs(soup)
    list_specs = _extract_specs_from_spec_lists(soup)
    vendor_specs = _extract_vendor_specific_specs(vendor, soup, url)
    product.specs.update(table_specs)
    product.specs.update(dl_specs)
    product.specs.update(structured_div_specs)
    product.specs.update(list_specs)
    product.specs.update(vendor_specs)

    if product.model is None:
        for key, value in product.specs.items():
            lowered = key.lower()
            if "model" in lowered or "part number" in lowered or "sku" in lowered:
                product.model = value
                break

    if product.name and _contains_template_token(product.name):
        product.name = None
    if product.model and _contains_template_token(product.model):
        product.model = None

    product.specs = {
        key: value
        for key, value in product.specs.items()
        if not _contains_template_token(key) and not _contains_template_token(value)
    }

    if product.model is None:
        for key, value in product.specs.items():
            lowered = key.lower()
            if "model" in lowered or "part number" in lowered or "sku" in lowered:
                product.model = value
                break

    if product.name is None:
        product.name = _infer_name_from_url(url)

    if not product.name and not product.specs:
        return None
    return product
