"""Shared URL safety primitives for the auto-update pipeline.

Centralises the SSRF allowlist and the request User-Agent header so that
``fetch_sitemap`` and ``summarize_docs`` stay in sync without duplication.
"""

# Allowed URL origins for the auto-update pipeline.
# Each entry is (hostname, path_prefix). An empty path_prefix matches any path
# on that host; a non-empty prefix restricts to that subtree only.
_ALLOWED_SCHEMES: frozenset[str] = frozenset({"https"})
_ALLOWED_ORIGINS: list[tuple[str, str]] = [
    ("www.twingate.com", ""),                              # Twingate documentation site
    ("github.com", "/Twingate/"),                          # Twingate GitHub org
    ("github.com", "/Twingate-Solutions/"),                # Twingate-Solutions GitHub org
    ("raw.githubusercontent.com", "/Twingate/"),           # Raw files from Twingate repos
    ("raw.githubusercontent.com", "/Twingate-Solutions/"), # Raw files from Twingate-Solutions repos
]

REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": (
        "twingate-assistant-pipeline/1.0 "
        "(github.com/Twingate-Solutions/twingate-assistant)"
    )
}


def _is_safe_url(url: str) -> bool:
    """Return True if the URL is in the pipeline's fetch allowlist.

    Allows HTTPS URLs from Twingate's documentation site and from the
    Twingate and Twingate-Solutions GitHub orgs (both github.com/<org>/
    and raw.githubusercontent.com/<org>/). Rejects all other origins to
    prevent SSRF via a compromised sitemap or mapping file.

    Args:
        url: The URL string to validate.

    Returns:
        True if the URL is safe to fetch; False otherwise.
    """
    from urllib.parse import urlparse

    parsed = urlparse(url)
    if parsed.scheme not in _ALLOWED_SCHEMES:
        return False
    for hostname, path_prefix in _ALLOWED_ORIGINS:
        if parsed.hostname == hostname:
            if not path_prefix or parsed.path.startswith(path_prefix):
                return True
    return False
