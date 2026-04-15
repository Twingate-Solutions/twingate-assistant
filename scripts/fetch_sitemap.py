"""Fetch and parse the Twingate sitemap to extract /docs/ URLs.

This module downloads the Twingate sitemap XML, parses it with
xml.etree.ElementTree, and returns all URLs that contain /docs/
in their path. Used by the auto-update pipeline to discover which
documentation pages exist.
"""

import logging
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

import requests

logger = logging.getLogger(__name__)

SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
DEFAULT_SITEMAP_URL = "https://www.twingate.com/sitemap/sitemap-0.xml"
REQUEST_TIMEOUT_SECONDS = 30
MAX_SITEMAP_BYTES = 10 * 1024 * 1024  # 10 MB guard against XML bombs

# Allowed URL origins for the auto-update pipeline.
# Each entry is (hostname, path_prefix). An empty path_prefix matches any path
# on that host; a non-empty prefix restricts to that subtree only.
_ALLOWED_SCHEMES = {"https"}
_ALLOWED_ORIGINS: list[tuple[str, str]] = [
    ("www.twingate.com", ""),              # Twingate documentation site
    ("github.com", "/Twingate/"),          # Twingate GitHub org (operator, Helm, tf provider, etc.)
    ("raw.githubusercontent.com", "/Twingate/"),  # Raw file content from Twingate repos
]

REQUEST_HEADERS = {
    "User-Agent": "twingate-assistant-pipeline/1.0 (github.com/Twingate-Solutions/twingate-assistant)"
}


def _is_safe_url(url: str) -> bool:
    """Return True if the URL is in the pipeline's fetch allowlist.

    Allows HTTPS URLs from Twingate's documentation site and from the
    Twingate GitHub org (github.com/Twingate/ and raw.githubusercontent.com/Twingate/).
    Rejects all other origins to prevent SSRF via a compromised sitemap or
    mapping file.

    Args:
        url: The URL string to validate.

    Returns:
        True if the URL is safe to fetch; False otherwise.
    """
    parsed = urlparse(url)
    if parsed.scheme not in _ALLOWED_SCHEMES:
        return False
    for hostname, path_prefix in _ALLOWED_ORIGINS:
        if parsed.hostname == hostname:
            if not path_prefix or parsed.path.startswith(path_prefix):
                return True
    return False


def fetch_sitemap(url: str = DEFAULT_SITEMAP_URL) -> list[str]:
    """Fetch sitemap XML and return all /docs/ URLs.

    Downloads the sitemap from the given URL, parses the XML to extract
    all ``<loc>`` elements, and filters to URLs containing ``/docs/``
    that originate from ``www.twingate.com`` over HTTPS.

    Handles both namespaced (standard sitemap xmlns) and non-namespaced
    ``<loc>`` tags.

    Args:
        url: The sitemap URL to fetch. Defaults to the Twingate
            production sitemap.

    Returns:
        A sorted, deduplicated list of documentation URLs found in
        the sitemap.

    Raises:
        requests.RequestException: If the HTTP request fails (timeout,
            connection error, non-2xx status).
        ValueError: If the sitemap response exceeds MAX_SITEMAP_BYTES.
        xml.etree.ElementTree.ParseError: If the response body is not
            valid XML.
    """
    logger.info("Fetching sitemap from %s", url)
    response = requests.get(url, timeout=REQUEST_TIMEOUT_SECONDS, headers=REQUEST_HEADERS)
    response.raise_for_status()
    logger.info(
        "Sitemap fetched successfully, status=%d, length=%d bytes",
        response.status_code,
        len(response.content),
    )

    if len(response.content) > MAX_SITEMAP_BYTES:
        raise ValueError(
            f"Sitemap response too large ({len(response.content)} bytes); "
            f"refusing to parse (limit: {MAX_SITEMAP_BYTES} bytes)"
        )

    root = ET.fromstring(response.content)

    urls: set[str] = set()

    # Try namespaced <loc> elements (standard sitemap format)
    namespaced_locs = root.findall(f".//{{{SITEMAP_NAMESPACE}}}loc")
    for loc in namespaced_locs:
        if loc.text:
            urls.add(loc.text.strip())

    # Also try non-namespaced <loc> elements (fallback for atypical sitemaps)
    plain_locs = root.findall(".//loc")
    for loc in plain_locs:
        if loc.text:
            urls.add(loc.text.strip())

    all_urls = sorted(urls)
    docs_urls = [u for u in all_urls if "/docs/" in u and _is_safe_url(u)]

    logger.info(
        "Parsed %d total URLs, %d are /docs/ URLs",
        len(all_urls),
        len(docs_urls),
    )

    return docs_urls


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
