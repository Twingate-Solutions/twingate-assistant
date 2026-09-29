"""Fetch and parse a Twingate sitemap to extract documentation URLs."""

import logging
import xml.etree.ElementTree as ET

from url_safety import REQUEST_HEADERS, _is_safe_url, safe_get

logger = logging.getLogger(__name__)

SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
DEFAULT_SITEMAP_URL = "https://www.twingate.com/sitemap/sitemap-0.xml"
REQUEST_TIMEOUT_SECONDS = 30
MAX_SITEMAP_BYTES = 10 * 1024 * 1024  # 10 MB size cap


def fetch_sitemap(
    url: str = DEFAULT_SITEMAP_URL,
    path_filter: str = "/docs/",
) -> list[str]:
    """Fetch sitemap XML and return URLs matching a path filter.

    Extracts all ``<loc>`` elements (namespaced or not) and keeps URLs whose
    path contains ``path_filter`` and that pass the ``_is_safe_url`` allowlist.

    Args:
        url: The sitemap URL to fetch. Defaults to the Twingate docs sitemap.
        path_filter: Substring a URL's path must contain to be kept. Defaults
            to ``/docs/``; pass ``/articles/`` for the help source.

    Returns:
        A sorted, deduplicated list of URLs matching ``path_filter``.

    Raises:
        ValueError: If ``url`` fails the fetch allowlist, or the sitemap
            response exceeds ``MAX_SITEMAP_BYTES``.
        requests.RequestException: If the HTTP request fails.
        url_safety.TooManyRedirectsError: If the request redirects more than
            ``safe_get``'s default hop limit.
        xml.etree.ElementTree.ParseError: If the response body is not valid XML.
    """
    if not _is_safe_url(url):
        raise ValueError(f"Refusing to fetch disallowed sitemap URL: {url}")

    logger.info("Fetching sitemap from %s", url)
    response = safe_get(
        url,
        timeout=REQUEST_TIMEOUT_SECONDS,
        headers=REQUEST_HEADERS,
        max_bytes=MAX_SITEMAP_BYTES,
    )
    response.raise_for_status()
    logger.info(
        "Sitemap fetched successfully, status=%d, length=%d bytes",
        response.status_code,
        len(response.content),
    )

    root = ET.fromstring(response.content)

    urls: set[str] = set()

    namespaced_locs = root.findall(f".//{{{SITEMAP_NAMESPACE}}}loc")
    for loc in namespaced_locs:
        if loc.text:
            urls.add(loc.text.strip())

    plain_locs = root.findall(".//loc")
    for loc in plain_locs:
        if loc.text:
            urls.add(loc.text.strip())

    all_urls = sorted(urls)
    matched_urls = [u for u in all_urls if path_filter in u and _is_safe_url(u)]

    logger.info(
        "Parsed %d total URLs, %d match path filter %r",
        len(all_urls),
        len(matched_urls),
        path_filter,
    )

    return matched_urls


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    results = fetch_sitemap()
    print(f"Found {len(results)} /docs/ URLs")
    for url in results[:10]:
        print(f"  {url}")
    if len(results) > 10:
        print(f"  ... and {len(results) - 10} more")
