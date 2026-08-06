"""Unit tests for fetch_sitemap module."""

from unittest.mock import MagicMock, patch
import xml.etree.ElementTree as ET

import pytest
import requests

from fetch_sitemap import REQUEST_HEADERS, fetch_sitemap


# ── Fixture XML payloads ──────────────────────────────────────────────────────

SITEMAP_XML_NAMESPACED = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.twingate.com/docs/architecture</loc></url>
  <url><loc>https://www.twingate.com/docs/how-it-works</loc></url>
  <url><loc>https://www.twingate.com/blog/some-post</loc></url>
</urlset>
"""

SITEMAP_XML_NO_NAMESPACE = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset>
  <url><loc>https://www.twingate.com/docs/connectors</loc></url>
  <url><loc>https://www.twingate.com/docs/terraform</loc></url>
  <url><loc>https://www.twingate.com/pricing</loc></url>
</urlset>
"""

SITEMAP_XML_EMPTY = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
</urlset>
"""

SITEMAP_XML_MALFORMED = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.twingate.com/docs/broken
"""

SITEMAP_XML_DUPLICATES = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.twingate.com/docs/architecture</loc></url>
  <url><loc>https://www.twingate.com/docs/architecture</loc></url>
  <url><loc>https://www.twingate.com/docs/connectors</loc></url>
</urlset>
"""

# help.twingate.com's flat urlset: no xmlns, mixes /articles/ with other paths.
SITEMAP_XML_HELP_ARTICLES = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset>
  <url><loc>https://help.twingate.com/articles/1422554451-connector-offline</loc></url>
  <url><loc>https://help.twingate.com/articles/8458642629-twingate-client-logs</loc></url>
  <url><loc>https://help.twingate.com/</loc></url>
  <url><loc>https://help.twingate.com/categories/general</loc></url>
</urlset>
"""

# A mixed sitemap containing both /docs/ and /articles/ URLs on the same host.
SITEMAP_XML_MIXED_DOCS_AND_ARTICLES = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset>
  <url><loc>https://www.twingate.com/docs/architecture</loc></url>
  <url><loc>https://www.twingate.com/articles/not-a-real-docs-path</loc></url>
</urlset>
"""


# ── Helpers ───────────────────────────────────────────────────────────────────


def _mock_response(content: str, status_code: int = 200) -> MagicMock:
    """Build a mock requests.Response with the given XML content."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.content = content.encode("utf-8")
    mock_resp.raise_for_status = MagicMock()
    return mock_resp


# ── Tests ─────────────────────────────────────────────────────────────────────


@patch("fetch_sitemap.requests.get")
def test_fetch_sitemap_returns_docs_urls(mock_get: MagicMock) -> None:
    """Successful fetch returns only /docs/ URLs, sorted."""
    mock_get.return_value = _mock_response(SITEMAP_XML_NAMESPACED)

    result = fetch_sitemap("https://example.com/sitemap.xml")

    assert result == [
        "https://www.twingate.com/docs/architecture",
        "https://www.twingate.com/docs/how-it-works",
    ]
    mock_get.assert_called_once_with(
        "https://example.com/sitemap.xml", timeout=30, headers=REQUEST_HEADERS
    )


@patch("fetch_sitemap.requests.get")
def test_non_docs_urls_are_filtered_out(mock_get: MagicMock) -> None:
    """URLs that do not contain /docs/ are excluded from the result."""
    mock_get.return_value = _mock_response(SITEMAP_XML_NAMESPACED)

    result = fetch_sitemap()

    assert "https://www.twingate.com/blog/some-post" not in result
    assert len(result) == 2


@patch("fetch_sitemap.requests.get")
def test_request_exception_propagates(mock_get: MagicMock) -> None:
    """requests.RequestException is not caught — it propagates to the caller."""
    mock_get.side_effect = requests.RequestException("Connection timed out")

    with pytest.raises(requests.RequestException, match="Connection timed out"):
        fetch_sitemap()


@patch("fetch_sitemap.requests.get")
def test_malformed_xml_raises_parse_error(mock_get: MagicMock) -> None:
    """Malformed XML raises ElementTree.ParseError."""
    mock_get.return_value = _mock_response(SITEMAP_XML_MALFORMED)

    with pytest.raises(ET.ParseError):
        fetch_sitemap()


@patch("fetch_sitemap.requests.get")
def test_empty_sitemap_returns_empty_list(mock_get: MagicMock) -> None:
    """A sitemap with no <url> entries returns an empty list."""
    mock_get.return_value = _mock_response(SITEMAP_XML_EMPTY)

    result = fetch_sitemap()

    assert result == []


@patch("fetch_sitemap.requests.get")
def test_non_namespaced_loc_tags_are_parsed(mock_get: MagicMock) -> None:
    """Sitemaps without the standard xmlns still have their <loc> tags parsed."""
    mock_get.return_value = _mock_response(SITEMAP_XML_NO_NAMESPACE)

    result = fetch_sitemap()

    assert result == [
        "https://www.twingate.com/docs/connectors",
        "https://www.twingate.com/docs/terraform",
    ]
    assert "https://www.twingate.com/pricing" not in result


@patch("fetch_sitemap.requests.get")
def test_duplicate_urls_are_deduplicated(mock_get: MagicMock) -> None:
    """Duplicate URLs in the sitemap are collapsed to a single entry."""
    mock_get.return_value = _mock_response(SITEMAP_XML_DUPLICATES)

    result = fetch_sitemap()

    assert result == [
        "https://www.twingate.com/docs/architecture",
        "https://www.twingate.com/docs/connectors",
    ]


@patch("fetch_sitemap.requests.get")
def test_http_error_status_propagates(mock_get: MagicMock) -> None:
    """Non-2xx HTTP status codes propagate via raise_for_status."""
    mock_resp = _mock_response("", status_code=500)
    mock_resp.raise_for_status.side_effect = requests.HTTPError(
        "500 Server Error"
    )
    mock_get.return_value = mock_resp

    with pytest.raises(requests.HTTPError, match="500 Server Error"):
        fetch_sitemap()


@patch("fetch_sitemap.requests.get")
def test_result_is_sorted(mock_get: MagicMock) -> None:
    """Returned URLs are in alphabetical order."""
    xml = """\
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.twingate.com/docs/zzz-last</loc></url>
  <url><loc>https://www.twingate.com/docs/aaa-first</loc></url>
  <url><loc>https://www.twingate.com/docs/mmm-middle</loc></url>
</urlset>
"""
    mock_get.return_value = _mock_response(xml)

    result = fetch_sitemap()

    assert result == [
        "https://www.twingate.com/docs/aaa-first",
        "https://www.twingate.com/docs/mmm-middle",
        "https://www.twingate.com/docs/zzz-last",
    ]


# ── Multi-source: path_filter="/articles/" (help.twingate.com) ────────────────


@patch("fetch_sitemap.requests.get")
def test_fetch_sitemap_articles_filter_keeps_only_articles_urls(mock_get: MagicMock) -> None:
    """path_filter='/articles/' keeps only /articles/ URLs, dropping others."""
    mock_get.return_value = _mock_response(SITEMAP_XML_HELP_ARTICLES)

    result = fetch_sitemap("https://help.twingate.com/sitemap.xml", path_filter="/articles/")

    assert result == [
        "https://help.twingate.com/articles/1422554451-connector-offline",
        "https://help.twingate.com/articles/8458642629-twingate-client-logs",
    ]
    assert "https://help.twingate.com/" not in result
    assert "https://help.twingate.com/categories/general" not in result


@patch("fetch_sitemap.requests.get")
def test_fetch_sitemap_articles_filter_ignores_docs_urls(mock_get: MagicMock) -> None:
    """path_filter='/articles/' does not accidentally match /docs/ URLs."""
    mock_get.return_value = _mock_response(SITEMAP_XML_MIXED_DOCS_AND_ARTICLES)

    result = fetch_sitemap("https://www.twingate.com/sitemap.xml", path_filter="/articles/")

    assert result == ["https://www.twingate.com/articles/not-a-real-docs-path"]
    assert "https://www.twingate.com/docs/architecture" not in result


@patch("fetch_sitemap.requests.get")
def test_fetch_sitemap_default_path_filter_still_keeps_docs_and_drops_articles(
    mock_get: MagicMock,
) -> None:
    """With no path_filter override, fetch_sitemap selects /docs/ and drops /articles/."""
    mock_get.return_value = _mock_response(SITEMAP_XML_MIXED_DOCS_AND_ARTICLES)

    result = fetch_sitemap("https://www.twingate.com/sitemap.xml")

    assert result == ["https://www.twingate.com/docs/architecture"]
    assert "https://www.twingate.com/articles/not-a-real-docs-path" not in result
