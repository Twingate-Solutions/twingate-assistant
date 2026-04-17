"""Unit tests for summarize_docs module.

All HTTP requests and Claude API calls are mocked so tests run
without network access or an API key. The conftest.py at
scripts/tests/ adds scripts/ to sys.path.
"""

from unittest.mock import MagicMock, patch

import requests

from summarize_docs import (
    REQUEST_HEADERS,
    _is_safe_url,
    content_hash,
    extract_text_from_html,
    fetch_doc_html,
    summarize_doc,
)


# ── Fixture HTML payloads ────────────────────────────────────────────────────

SIMPLE_HTML = """\
<!DOCTYPE html>
<html>
<head><title>Test Page</title></head>
<body>
  <header><nav>Navigation links</nav></header>
  <main>
    <h1>Connector Deployment</h1>
    <p>Deploy connectors on Docker or Kubernetes.</p>
  </main>
  <footer>Footer content</footer>
</body>
</html>
"""

HTML_WITH_SCRIPTS = """\
<!DOCTYPE html>
<html>
<head>
  <style>body { color: red; }</style>
  <script>console.log("track");</script>
</head>
<body>
  <script>alert("nope");</script>
  <p>Visible content here.</p>
  <style>.hidden { display: none; }</style>
</body>
</html>
"""

HTML_WITH_ARTICLE = """\
<!DOCTYPE html>
<html>
<body>
  <div id="sidebar">Sidebar stuff</div>
  <article>
    <h1>Article Title</h1>
    <p>Article body text.</p>
  </article>
  <div id="other">Other stuff</div>
</body>
</html>
"""

MINIMAL_HTML = """\
<html><body><p>Hello world</p></body></html>
"""


# ── Helpers ──────────────────────────────────────────────────────────────────


def _mock_response(text: str, status_code: int = 200) -> MagicMock:
    """Build a mock requests.Response with the given text body."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.text = text
    mock_resp.content = text.encode("utf-8")
    mock_resp.raise_for_status = MagicMock()
    return mock_resp


def _mock_claude_message(summary_text: str) -> MagicMock:
    """Build a mock anthropic Message with a single text content block."""
    content_block = MagicMock()
    content_block.text = summary_text
    message = MagicMock()
    message.content = [content_block]
    return message


# ── fetch_doc_html tests ────────────────────────────────────────────────────


@patch("summarize_docs.requests.get")
def test_fetch_doc_html_returns_html_on_success(mock_get: MagicMock) -> None:
    """Successful fetch returns the HTML string."""
    mock_get.return_value = _mock_response("<html><body>OK</body></html>")

    result = fetch_doc_html("https://www.twingate.com/docs/test")

    assert result == "<html><body>OK</body></html>"
    mock_get.assert_called_once_with(
        "https://www.twingate.com/docs/test", timeout=30, headers=REQUEST_HEADERS
    )


@patch("summarize_docs.requests.get")
def test_fetch_doc_html_returns_none_on_request_exception(
    mock_get: MagicMock,
) -> None:
    """Returns None (does NOT raise) on requests.RequestException."""
    mock_get.side_effect = requests.RequestException("Connection refused")

    result = fetch_doc_html("https://www.twingate.com/docs/broken")

    assert result is None


@patch("summarize_docs.requests.get")
def test_fetch_doc_html_returns_none_on_http_error(mock_get: MagicMock) -> None:
    """Returns None (does NOT raise) on HTTP error status."""
    mock_resp = _mock_response("", status_code=404)
    mock_resp.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
    mock_get.return_value = mock_resp

    result = fetch_doc_html("https://www.twingate.com/docs/missing")

    assert result is None


# ── extract_text_from_html tests ────────────────────────────────────────────


def test_extract_strips_script_and_style_tags() -> None:
    """Script and style tags are removed; only visible text remains."""
    text = extract_text_from_html(HTML_WITH_SCRIPTS)

    assert "console.log" not in text
    assert "alert" not in text
    assert "color: red" not in text
    assert "display: none" not in text
    assert "Visible content here." in text


def test_extract_finds_main_content() -> None:
    """When a <main> tag is present, text is extracted from it."""
    text = extract_text_from_html(SIMPLE_HTML)

    assert "Connector Deployment" in text
    assert "Deploy connectors" in text
    # Header/footer should be stripped by tag removal.
    assert "Navigation links" not in text
    assert "Footer content" not in text


def test_extract_finds_article_content() -> None:
    """When an <article> tag is present and no <main>, article is used."""
    text = extract_text_from_html(HTML_WITH_ARTICLE)

    assert "Article Title" in text
    assert "Article body text." in text


def test_extract_handles_minimal_html() -> None:
    """Minimal HTML without main/article still returns body text."""
    text = extract_text_from_html(MINIMAL_HTML)

    assert "Hello world" in text


# ── content_hash tests ──────────────────────────────────────────────────────


def test_content_hash_returns_consistent_hash() -> None:
    """Same input always produces the same 64-char SHA-256 hex string."""
    h1 = content_hash("test content")
    h2 = content_hash("test content")

    assert h1 == h2
    assert len(h1) == 64
    assert all(c in "0123456789abcdef" for c in h1)


def test_content_hash_different_for_different_input() -> None:
    """Different inputs produce different hashes."""
    h1 = content_hash("content A")
    h2 = content_hash("content B")

    assert h1 != h2


# ── summarize_doc tests ─────────────────────────────────────────────────────


@patch("summarize_docs.anthropic.Anthropic")
def test_summarize_doc_calls_api_with_correct_params(
    mock_anthropic_cls: MagicMock,
) -> None:
    """summarize_doc calls Claude API with the right model, system prompt, and message."""
    mock_client = MagicMock()
    mock_anthropic_cls.return_value = mock_client
    mock_client.messages.create.return_value = _mock_claude_message(
        "# Summary\nTest summary."
    )

    result = summarize_doc(
        "https://www.twingate.com/docs/test",
        MINIMAL_HTML,
    )

    assert result == "# Summary\nTest summary."

    # Verify the API was called with the expected parameters.
    call_kwargs = mock_client.messages.create.call_args.kwargs
    assert call_kwargs["model"] == "claude-sonnet-4-6"
    assert call_kwargs["max_tokens"] == 1024
    assert "summarizing a Twingate documentation page" in call_kwargs["system"]
    assert call_kwargs["messages"][0]["role"] == "user"
    assert call_kwargs["messages"][0]["content"].startswith(
        "URL: https://www.twingate.com/docs/test\n\n"
    )


@patch("summarize_docs.anthropic.Anthropic")
def test_summarize_doc_truncates_long_text(
    mock_anthropic_cls: MagicMock,
) -> None:
    """Text exceeding 60000 chars is truncated with a notice appended."""
    mock_client = MagicMock()
    mock_anthropic_cls.return_value = mock_client
    mock_client.messages.create.return_value = _mock_claude_message(
        "# Truncated Summary"
    )

    # Build HTML with a body exceeding 60000 chars of text.
    long_text = "word " * 15000  # ~75000 chars
    long_html = f"<html><body><p>{long_text}</p></body></html>"

    summarize_doc("https://www.twingate.com/docs/long", long_html)

    user_content = mock_client.messages.create.call_args.kwargs["messages"][0][
        "content"
    ]
    assert "[Content truncated for length]" in user_content


@patch("summarize_docs.anthropic.Anthropic")
def test_summarize_doc_long_html_still_calls_api(
    mock_anthropic_cls: MagicMock,
) -> None:
    """Even with very long HTML, the API is still called (truncation doesn't prevent it)."""
    mock_client = MagicMock()
    mock_anthropic_cls.return_value = mock_client
    mock_client.messages.create.return_value = _mock_claude_message(
        "# Long Page Summary"
    )

    long_text = "paragraph " * 7000
    long_html = (
        f"<html><body><main><h1>Big Doc</h1><p>{long_text}</p></main></body></html>"
    )

    result = summarize_doc("https://www.twingate.com/docs/big", long_html)

    assert result == "# Long Page Summary"
    mock_client.messages.create.assert_called_once()

    # Verify the text was extracted from <main> and truncated.
    user_content = mock_client.messages.create.call_args.kwargs["messages"][0][
        "content"
    ]
    assert "Big Doc" in user_content
    assert "[Content truncated for length]" in user_content


# ── _is_safe_url tests ──────────────────────────────────────────────────────


def test_is_safe_url_allows_twingate_docs() -> None:
    assert _is_safe_url("https://www.twingate.com/docs/connector-deployment")


def test_is_safe_url_allows_github_twingate_org() -> None:
    assert _is_safe_url("https://github.com/Twingate/kubernetes-operator")


def test_is_safe_url_allows_github_twingate_org_subpath() -> None:
    assert _is_safe_url("https://github.com/Twingate/kubernetes-operator/blob/main/README.md")


def test_is_safe_url_allows_raw_githubusercontent_twingate() -> None:
    assert _is_safe_url("https://raw.githubusercontent.com/Twingate/kubernetes-operator/main/README.md")


def test_is_safe_url_rejects_github_other_org() -> None:
    assert not _is_safe_url("https://github.com/SomeOtherOrg/repo")


def test_is_safe_url_rejects_raw_githubusercontent_other_org() -> None:
    assert not _is_safe_url("https://raw.githubusercontent.com/SomeOtherOrg/repo/main/file.md")


def test_is_safe_url_rejects_http_scheme() -> None:
    assert not _is_safe_url("http://www.twingate.com/docs/connector-deployment")


def test_is_safe_url_rejects_arbitrary_host() -> None:
    assert not _is_safe_url("https://evil.com/docs/something")


def test_is_safe_url_rejects_metadata_endpoint() -> None:
    assert not _is_safe_url("https://169.254.169.254/docs/latest/meta-data/")


@patch("summarize_docs.requests.get")
def test_fetch_doc_html_rejects_non_twingate_url(mock_get: MagicMock) -> None:
    """fetch_doc_html returns None without making a request for disallowed URLs."""
    result = fetch_doc_html("https://github.com/SomeOtherOrg/repo")

    assert result is None
    mock_get.assert_not_called()


@patch("summarize_docs.requests.get")
def test_fetch_doc_html_allows_github_twingate_url(mock_get: MagicMock) -> None:
    """fetch_doc_html fetches github.com/Twingate/ URLs."""
    mock_get.return_value = MagicMock(
        status_code=200,
        text="<html><body>Operator README</body></html>",
        content=b"<html><body>Operator README</body></html>",
        raise_for_status=MagicMock(),
    )

    result = fetch_doc_html("https://github.com/Twingate/kubernetes-operator")

    assert result is not None
    mock_get.assert_called_once()
