from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class VendorConfig:
    name: str
    sitemaps: tuple[str, ...]
    include_keywords: tuple[str, ...]
    exclude_keywords: tuple[str, ...] = ()
    strip_locale_prefix: bool = True
    fallback_link_seeds: tuple[str, ...] = ()
    fallback_link_max_depth: int = 1
    minimum_path_segments: int = 0
    search_queries: tuple[str, ...] = ()
    search_result_pages: int = 1
    use_playwright: bool = False


VENDORS: dict[str, VendorConfig] = {
    "asus": VendorConfig(
        name="asus",
        sitemaps=("https://www.asus.com/sitemap.xml",),
        include_keywords=(
            "/motherboards-components/",
            "/motherboards/",
            "/graphics-cards/",
            "/laptops/",
            "/networking-iot-servers/",
        ),
        exclude_keywords=(
            "/review",
            "/review/",
            "/where-to-buy/",
            "/support/",
            "/accessories/",
            "/filter?"
        ),
    ),
    "asrock": VendorConfig(
        name="asrock",
        sitemaps=(
            "https://www.asrock.com/sitemap.xml",
            "http://www.asrock.com/sitemap.xml",
        ),
        include_keywords=(
            "/mb/",
            "/motherboard/",
            "/graphic-card/",
            "/graphics-card/",
            "/monitor/",
            "/networking/",
        ),
        exclude_keywords=(
            "/news/",
            "/support/",
            "/event",
            "/events/",
            "/general/",
            "/feature/",
            "/microsite/",
            "/graphics-card/index.asp",
            "/graphic-card/index.asp",
            "/networking/index.asp",
            "/monitor/index.asp",
            "/mb/index.asp",
            "/motherboard/index.asp",
        ),
        fallback_link_seeds=(
            "https://www.asrock.com/",
            "https://www.asrock.com/mb/index.asp",
            "https://www.asrock.com/graphics-card/index.asp",
            "https://www.asrock.com/monitor/index.asp",
            "https://www.asrock.com/nettop/index.asp",
            "https://www.asrock.com/CPU-Coolers/index.asp",
            "https://www.asrock.com/Power-Supply/index.asp",
        ),
        fallback_link_max_depth=2,
        minimum_path_segments=0,
        search_queries=(
            "site:asrock.com/mb/ index.asp",
            "site:asrock.com/motherboard/ index.asp",
            "site:asrock.com/graphics-card/ index.asp",
            "site:asrock.com/graphic-card/ index.asp",
            "site:asrock.com/monitor/ index.asp",
            "site:asrock.com/networking/ index.asp",
            "site:asrock.com/nettop/ index.asp",
            "site:pg.asrock.com/mb/ index.asp",
        ),
        search_result_pages=2,
    ),
    "msi": VendorConfig(
        name="msi",
        sitemaps=("https://www.msi.com/sitemap.xml",),
        include_keywords=(
            "/Motherboard/",
            "/Graphics-Card/",
            "/Laptop/",
            "/Monitor/",
            "/Desktop/",
        ),
        exclude_keywords=(
            "/Content-Creation/",
            "/Business-Productivity/",
            "/news/",
            "/blog/",
            "/support/",
        ),
        use_playwright=True,
    ),
    "gigabyte": VendorConfig(
        name="gigabyte",
        sitemaps=(
            "https://www.gigabyte.com/Sitemap.xml",
            "https://www.gigabyte.com/sitemap.xml",
        ),
        include_keywords=(
            "/Motherboard/",
            "/Graphics-Card/",
            "/Laptop/",
            "/Monitor/",
            "/Mini-PCBarebone/",
        ),
        exclude_keywords=(
            "/Support/",
            "/News/",
            "/Enterprise/",
            "?fid=",
            "/All-Series",
            "/AI-TOP-Capable",
        ),
        fallback_link_seeds=(
            "https://www.gigabyte.com/",
            "https://www.gigabyte.com/Motherboard",
            "https://www.gigabyte.com/Graphics-Card",
            "https://www.gigabyte.com/Laptop",
            "https://www.gigabyte.com/Monitor",
            "https://www.gigabyte.com/Mini-PCBarebone",
        ),
        fallback_link_max_depth=2,
    ),
    "biostar": VendorConfig(
        name="biostar",
        sitemaps=(
            "https://www.biostar.com.tw/sitemap.xml",
            "https://www.biostar.com.tw/app/en/sitemap.xml",
        ),
        include_keywords=(
            "/introduction.php?S_ID=",
        ),
        exclude_keywords=(
            "/index.php",
            "/solutions/",
            "/applications/",
            "/download/",
            "/support/",
        ),
    ),
    "evga": VendorConfig(
        name="evga",
        sitemaps=("https://www.evga.com/sitemap.xml",),
        include_keywords=(
            "/products/product.aspx",
        ),
        exclude_keywords=(
            "/support/",
            "/articles/",
            "/members/",
        ),
    ),
    "zotac": VendorConfig(
        name="zotac",
        sitemaps=(),
        include_keywords=(
            "/us/product/",
        ),
        exclude_keywords=(
            "/news/",
            "/support",
            "/download/",
            "/faq/",
            "/all",
            "/overview",
            "/compare/",
            "/page/",
            "_series",
            "-series",
            "?field_filter",
            "/discontinued/",
            "/enterprise/",
            "/accessories/",
            "/handheld/",
            "/mainboard/",
            "/pc-case/",
            "/pro_mini_pc/",
        ),
        fallback_link_seeds=(
            "https://www.zotac.com/us/product/graphics_card/all",
            "https://www.zotac.com/us/product/zotac_gaming/all",
            "https://www.zotac.com/us/product/mini_pcs/all",
        ),
        fallback_link_max_depth=2,
        strip_locale_prefix=False,
    ),
    "coolermaster": VendorConfig(
        name="coolermaster",
        sitemaps=("https://www.coolermaster.com/sitemap_index.xml",),
        include_keywords=(
            "/products/",
        ),
        exclude_keywords=(
            "/en-global/",
            "/zh-",
            "/ja-jp/",
            "/ko-kr/",
            "/news/",
            "/support/",
            "/where-to-buy/",
        ),
        use_playwright=True,
    ),
    "corsair": VendorConfig(
        name="corsair",
        sitemaps=("https://www.corsair.com/us-sitemap.xml",),
        include_keywords=(
            "/en/p/",
        ),
        exclude_keywords=(
            "/support/",
            "/blog/",
            "/newsroom/",
            "/revival-series/",
            "/headsets/",
            "/gaming-mice/",
            "/gaming-keyboards/",
            "/mousepads/",
            "/chairs/",
        ),
        strip_locale_prefix=False,
    ),
    "phanteks": VendorConfig(
        name="phanteks",
        sitemaps=("https://phanteks.com/wp-sitemap-posts-product-1.xml",),
        include_keywords=(
            "/product/",
        ),
        exclude_keywords=(
            "/category/",
            "/tag/",
            "/support/",
        ),
    ),
    "fractal-design": VendorConfig(
        name="fractal-design",
        sitemaps=("https://www.fractal-design.com/sitemap.xml",),
        include_keywords=(
            "/products/",
        ),
        exclude_keywords=(
            "/support/",
            "/downloads/",
            "/news/",
        ),
    ),
    "mushkin": VendorConfig(
        name="mushkin",
        sitemaps=("https://mushkin.com/wp-sitemap-posts-product-1.xml",),
        include_keywords=(
            "/product/",
        ),
        exclude_keywords=(
            "/product-category/",
            "/product-tag/",
            "/support/",
        ),
    ),
    "silverstone": VendorConfig(
        name="silverstone",
        sitemaps=("https://www.silverstonetek.com/sitemap.xml",),
        include_keywords=(
            "/product/info/",
        ),
        exclude_keywords=(
            "?filter=",
            "/support/",
            "/news/",
        ),
        strip_locale_prefix=False,
    ),
    "seasonic": VendorConfig(
        name="seasonic",
        sitemaps=("https://seasonic.com/product-sitemap.xml",),
        include_keywords=(
            "/",
        ),
        exclude_keywords=(
            "/shop/",
            "/support/",
            "/warranty/",
            "/news/",
        ),
    ),
    "lian-li": VendorConfig(
        name="lian-li",
        sitemaps=("https://lian-li.com/product-sitemap.xml",),
        include_keywords=(
            "/product/",
        ),
        exclude_keywords=(
            "/support/",
            "/category/",
            "/tag/",
        ),
    ),
    "thermalright": VendorConfig(
        name="thermalright",
        sitemaps=("https://www.thermalright.com/wp-sitemap-posts-product-1.xml",),
        include_keywords=(
            "/product/",
        ),
        exclude_keywords=(
            "/support/",
            "/faq/",
            "/category/",
            "/tag/",
        ),
    ),
    "noctua": VendorConfig(
        name="noctua",
        sitemaps=("https://noctua.at/sitemap.xml",),
        include_keywords=(
            "/en/products/",
        ),
        exclude_keywords=(
            "/buying-guides/",
            "/browse/",
            "/support/",
            "/news/",
            "/privacy-policy/",
        ),
        strip_locale_prefix=False,
    ),
    "xfx": VendorConfig(
        name="xfx",
        sitemaps=(),
        include_keywords=(
            "/shop/",
        ),
        exclude_keywords=(
            "/support/",
            "/news/",
            "/blog/",
            "/about/",
            "/contact/",
            "/careers/",
            "/terms/",
            "/privacy/",
            "/account/",
            "/cart/",
        ),
        fallback_link_seeds=(
            "https://www.xfxforce.com/",
        ),
        fallback_link_max_depth=2,
    ),
    "sapphire": VendorConfig(
        name="sapphire",
        sitemaps=("https://www.sapphiretech.com/sitemap.xml",),
        include_keywords=(
            "/en/consumer/",
        ),
        exclude_keywords=(
            "/zh-",
            "/ru-",
            "/de-",
            "/ko-",
            "/ja-",
            "/news/",
            "/support/",
            "/event/",
        ),
        strip_locale_prefix=False,
    ),
    "sparkle": VendorConfig(
        name="sparkle",
        sitemaps=("https://sparkle.com.tw/sitemap.xml",),
        include_keywords=(
            "/products/",
        ),
        exclude_keywords=(
            "/news",
            "/media-center",
            "/brand-story",
            "/support",
        ),
        strip_locale_prefix=False,
        use_playwright=True,
    ),
    "maxsun": VendorConfig(
        name="maxsun",
        sitemaps=("https://en.maxsun.com/sitemap.xml",),
        include_keywords=(
            "/products/",
        ),
        exclude_keywords=(
            "/blogs/",
            "/pages/",
            "/collections/",
            "/support/",
        ),
        strip_locale_prefix=False,
    ),
    "powercolor": VendorConfig(
        name="powercolor",
        sitemaps=("https://powercolor.com/sitemap.xml",),
        include_keywords=(
            "/product-detail",
        ),
        exclude_keywords=(
            "/news/",
            "/where-to-buy/",
            "/support/",
        ),
        strip_locale_prefix=False,
        use_playwright=True,
    ),
    "powercolour": VendorConfig(
        name="powercolour",
        sitemaps=("https://powercolor.com/sitemap.xml",),
        include_keywords=(
            "/product-detail",
        ),
        exclude_keywords=(
            "/news/",
            "/where-to-buy/",
            "/support/",
        ),
        strip_locale_prefix=False,
        use_playwright=True,
    ),
    "gunnir": VendorConfig(
        name="gunnir",
        sitemaps=("https://en.gunnir.com/sitemap.xml",),
        include_keywords=(
            "/product/",
        ),
        exclude_keywords=(
            "/support/",
            "/news/",
            "/blog/",
            "/product_category/",
            "/product.html",
        ),
        fallback_link_seeds=(
            "https://en.gunnir.com/product_category/PHOTON.html",
            "https://en.gunnir.com/product_category/FLUX.html",
            "https://en.gunnir.com/product_category/INDEX.htm",
        ),
        fallback_link_max_depth=1,
        strip_locale_prefix=False,
    ),
    "kingston": VendorConfig(
        name="kingston",
        sitemaps=(),
        include_keywords=(
            "/ssd/",
            "/memory/",
            "/usb-flash-drives/",
            "/flash-cards/",
            "/card-readers/",
        ),
        exclude_keywords=(
            "/support/",
            "/shop/",
            "/search",
            "/company/",
            "/category/",
            "/tag/",
            "/server-premier",
            "/gaming",
            "/system-specific",
            "/laptop",
            "/desktop",
            "/apple",
            "/all-memory",
            "/memory/client/",
            "/server-memory",
            "/servers-datacenters",
            "/external-portable",
            "/desktop-laptop-workstations",
        ),
        fallback_link_seeds=(
            "https://www.kingston.com/en/ssd",
            "https://www.kingston.com/en/memory",
            "https://www.kingston.com/en/usb-flash-drives",
            "https://www.kingston.com/en/flash-cards",
            "https://www.kingston.com/en/card-readers",
        ),
        fallback_link_max_depth=2,
        minimum_path_segments=3,
        strip_locale_prefix=False,
        use_playwright=True,
    ),
    "sandisk": VendorConfig(
        name="sandisk",
        sitemaps=(
            "https://www.sandisk.com/sitemap.xml",
        ),
        include_keywords=(
            "/products/",
        ),
        exclude_keywords=(
            "/support/",
            "/topics/",
            "/products/clearance/",
            "/company/newsroom/",
            "/legal/",
            "/account",
        ),
    ),
    "acer": VendorConfig(
        name="acer",
        sitemaps=("https://www.acer.com/sitemap.xml",),
        include_keywords=(
            "/products/",
            "/laptops/",
            "/desktops/",
            "/motherboards/",
            "/predator/",
        ),
        exclude_keywords=(
            "/support/",
            "/news/",
            "/press/",
            "/about/",
        ),
    ),
}
