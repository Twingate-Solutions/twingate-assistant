"""Shared URL safety primitives (SSRF allowlist, request headers, safe_get)."""

from __future__ import annotations

from urllib.parse import urljoin, urlparse

import requests

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
    parsed = urlparse(url)
    if parsed.scheme not in _ALLOWED_SCHEMES:
        return False
    for hostname, path_prefix in _ALLOWED_ORIGINS:
        if parsed.hostname == hostname:
            if not path_prefix or parsed.path.startswith(path_prefix):
                return True
    return False


# ---------------------------------------------------------------------------
# safe_get — redirect-revalidating, size-capped GET.
# ---------------------------------------------------------------------------

# Status codes requests treats as a redirect when allow_redirects=True; we
# handle them manually so every hop can be re-validated.
_REDIRECT_STATUS_CODES: frozenset[int] = frozenset({301, 302, 303, 307, 308})

# Bytes read per chunk while streaming a response body under the size cap.
_STREAM_CHUNK_SIZE = 65536


class TooManyRedirectsError(Exception):
    """Raised when a request exceeds the configured redirect hop limit."""


class ResponseTooLargeError(Exception):
    """Raised when a response body exceeds the configured byte cap."""


def safe_get(
    url: str,
    *,
    timeout: float,
    headers: dict[str, str] | None = None,
    max_bytes: int,
    max_redirects: int = 5,
    params: dict[str, str] | None = None,
) -> requests.Response:
    """Perform a GET request with SSRF-safe redirect handling and a size cap.

    The initial URL and every redirect target are validated with
    :func:`_is_safe_url` before being fetched — a redirect to a disallowed
    origin raises rather than being followed silently. Redirects are
    followed manually (``allow_redirects=False``) so each hop can be
    checked; a relative ``Location`` is resolved against the current URL.
    If a redirect changes hostname, any ``Authorization`` header is stripped
    before the next hop, so credentials meant for the original host are
    never sent to a redirect target on a different host.

    The final (non-redirect) response's body is read via ``iter_content``
    — note this yields decompressed bytes for a gzip-encoded response — and
    reading aborts with :class:`ResponseTooLargeError` as soon as
    ``max_bytes`` is exceeded, so an oversized or malicious body is never
    fully buffered in memory. On success the response's ``.content`` /
    ``.text`` / ``.json()`` behave normally, reflecting exactly the bytes
    read.

    Status-code handling (e.g. ``raise_for_status()``, custom 403/404
    branching) is left to the caller, matching prior per-call-site behavior.

    Args:
        url: The URL to fetch.
        timeout: Per-request timeout in seconds.
        headers: Optional request headers.
        max_bytes: Maximum allowed (decompressed) response body size.
        max_redirects: Maximum number of redirect hops to follow.
        params: Optional query parameters, sent only on the first hop (a
            redirect's ``Location`` already carries its own query string).

    Returns:
        The final ``requests.Response``.

    Raises:
        ValueError: If the initial URL or any redirect target fails
            :func:`_is_safe_url`, or a redirect response has no
            ``Location`` header.
        TooManyRedirectsError: If more than ``max_redirects`` hops occur.
        ResponseTooLargeError: If the response body exceeds ``max_bytes``.
        requests.RequestException: Propagated from the underlying transport.
    """
    current_url = url
    current_headers = dict(headers or {})

    for hop in range(max_redirects + 1):
        if not _is_safe_url(current_url):
            raise ValueError(f"Refusing to fetch disallowed URL: {current_url}")

        response = requests.get(
            current_url,
            params=params if hop == 0 else None,
            timeout=timeout,
            headers=current_headers,
            allow_redirects=False,
            stream=True,
        )

        if response.status_code in _REDIRECT_STATUS_CODES:
            location = response.headers.get("Location")
            response.close()
            if not location:
                raise ValueError(
                    f"Redirect response ({response.status_code}) from {current_url} "
                    "has no Location header"
                )
            next_url = urljoin(current_url, location)
            if urlparse(next_url).hostname != urlparse(current_url).hostname:
                for key in [k for k in current_headers if k.lower() == "authorization"]:
                    current_headers.pop(key, None)
            current_url = next_url
            continue

        body = bytearray()
        try:
            for chunk in response.iter_content(chunk_size=_STREAM_CHUNK_SIZE):
                if not chunk:
                    continue
                body.extend(chunk)
                if len(body) > max_bytes:
                    raise ResponseTooLargeError(
                        f"Response from {current_url} exceeded {max_bytes}-byte cap"
                    )
            response._content = bytes(body)  # noqa: SLF001 - populate for .content/.text/.json()
        finally:
            response.close()
        return response

    raise TooManyRedirectsError(f"Exceeded {max_redirects} redirect(s) fetching {url}")
