"""Shared URL safety primitives (SSRF allowlist and request headers)."""

# Each entry is (hostname, path_prefix). An empty path_prefix matches any path
# on that host; a non-empty prefix restricts to that subtree only.
_ALLOWED_SCHEMES: frozenset[str] = frozenset({"https"})
_ALLOWED_ORIGINS: list[tuple[str, str]] = [
    ("www.twingate.com", ""),                              # Twingate documentation site
    ("help.twingate.com", ""),                             # Twingate help center (Docsie)
    ("github.com", "/Twingate/"),                          # Twingate GitHub org
    ("github.com", "/Twingate-Solutions/"),                # Twingate-Solutions GitHub org
    ("github.com", "/Twingate-Labs/"),                     # Twingate-Labs GitHub org
    ("github.com", "/Twingate-Community/"),                # Twingate-Community GitHub org
    ("raw.githubusercontent.com", "/Twingate/"),           # Raw files from Twingate repos
    ("raw.githubusercontent.com", "/Twingate-Solutions/"), # Raw files from Twingate-Solutions repos
    ("raw.githubusercontent.com", "/Twingate-Labs/"),      # Raw files from Twingate-Labs repos
    ("raw.githubusercontent.com", "/Twingate-Community/"), # Raw files from Twingate-Community repos
    ("api.github.com", ""),                                # GitHub REST API (repo discovery, compare diffs)
]

REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": (
        "twingate-assistant-pipeline/1.0 "
        "(github.com/Twingate-Solutions/twingate-assistant)"
    )
}


def _is_safe_url(url: str) -> bool:
    """Return True if the URL is an HTTPS origin in the fetch allowlist.

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
