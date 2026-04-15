"""Unit tests for update_references.py — the pipeline orchestrator."""

import json
from unittest.mock import patch

import anthropic
import httpx
import pytest

import update_references
from update_references import (
    check_api_health,
    load_hash_cache,
    main,
    process_doc,
    save_hash_cache,
    summarize_with_backoff,
    url_to_slug,
    write_reference_file,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_rate_limit_error() -> anthropic.RateLimitError:
    """Construct a minimal anthropic.RateLimitError for testing."""
    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    response = httpx.Response(429, request=request)
    return anthropic.RateLimitError("rate limited", response=response, body=None)


def _make_api_connection_error() -> anthropic.APIConnectionError:
    """Construct a minimal anthropic.APIConnectionError for testing."""
    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    return anthropic.APIConnectionError(message="network error", request=request)


# ---------------------------------------------------------------------------
# url_to_slug
# ---------------------------------------------------------------------------


def test_url_to_slug_standard_path():
    url = "https://www.twingate.com/docs/connector-deployment"
    assert url_to_slug(url) == "connector-deployment"


def test_url_to_slug_trailing_slash():
    url = "https://www.twingate.com/docs/connector-deployment/"
    assert url_to_slug(url) == "connector-deployment"


def test_url_to_slug_dot_in_segment():
    url = "https://www.twingate.com/docs/some.page"
    assert url_to_slug(url) == "some-page"


def test_url_to_slug_bare_domain():
    # Last non-empty segment of "https://www.twingate.com/" is "www.twingate.com"
    assert url_to_slug("https://www.twingate.com/") == "www-twingate-com"


def test_url_to_slug_empty_string():
    assert url_to_slug("") == "index"


def test_url_to_slug_double_dot_becomes_index():
    """A segment of '..' is sanitized to empty and falls back to 'index'."""
    url = "https://www.twingate.com/docs/.."
    assert url_to_slug(url) == "index"


def test_url_to_slug_strips_special_chars():
    """Characters outside [a-zA-Z0-9-_] are replaced with hyphens."""
    url = "https://www.twingate.com/docs/page%20name"
    slug = url_to_slug(url)
    assert slug == "page-20name"


# ---------------------------------------------------------------------------
# load_hash_cache / save_hash_cache
# ---------------------------------------------------------------------------


def test_load_hash_cache_missing_file(tmp_path):
    result = load_hash_cache(tmp_path / "nonexistent.json")
    assert result == {}


def test_load_hash_cache_reads_existing_file(tmp_path):
    cache_file = tmp_path / "hashes.json"
    data = {"https://example.com/docs/foo": "abc123"}
    cache_file.write_text(json.dumps(data), encoding="utf-8")
    result = load_hash_cache(cache_file)
    assert result == data


def test_save_hash_cache_writes_json(tmp_path):
    cache_file = tmp_path / "hashes.json"
    data = {"https://example.com/docs/foo": "abc123", "https://example.com/docs/bar": "def456"}
    save_hash_cache(data, cache_file)
    written = json.loads(cache_file.read_text(encoding="utf-8"))
    assert written == data


def test_save_then_load_roundtrip(tmp_path):
    cache_file = tmp_path / "hashes.json"
    data = {"https://example.com/docs/a": "111", "https://example.com/docs/b": "222"}
    save_hash_cache(data, cache_file)
    loaded = load_hash_cache(cache_file)
    assert loaded == data


# ---------------------------------------------------------------------------
# summarize_with_backoff
# ---------------------------------------------------------------------------


@patch("update_references.summarize_doc", return_value="## Summary\nContent here.")
def test_summarize_with_backoff_success(mock_summarize):
    result = summarize_with_backoff("https://example.com/docs/foo", "<html></html>")
    assert result == "## Summary\nContent here."
    mock_summarize.assert_called_once()


@patch("update_references.time.sleep")
@patch("update_references.summarize_doc")
def test_summarize_with_backoff_retries_on_rate_limit(mock_summarize, mock_sleep):
    """Should retry after RateLimitError and return the eventual success."""
    rate_limit_err = _make_rate_limit_error()
    mock_summarize.side_effect = [rate_limit_err, "## Summary\nOK"]

    result = summarize_with_backoff("https://example.com/docs/foo", "<html></html>")

    assert result == "## Summary\nOK"
    assert mock_summarize.call_count == 2
    mock_sleep.assert_called_once()


@patch("update_references.time.sleep")
@patch("update_references.summarize_doc")
def test_summarize_with_backoff_exhausts_retries(mock_summarize, mock_sleep):
    """Should return None after BACKOFF_MAX_RETRIES+1 failures."""
    rate_limit_err = _make_rate_limit_error()
    mock_summarize.side_effect = rate_limit_err

    result = summarize_with_backoff("https://example.com/docs/foo", "<html></html>")

    assert result is None
    expected_calls = update_references.BACKOFF_MAX_RETRIES + 1
    assert mock_summarize.call_count == expected_calls
    # sleep is called between each attempt except the last
    assert mock_sleep.call_count == update_references.BACKOFF_MAX_RETRIES


@patch("update_references.time.sleep")
@patch("update_references.summarize_doc")
def test_summarize_with_backoff_api_error_no_retry(mock_summarize, mock_sleep):
    """Non-rate-limit APIConnectionError should return None immediately, no retries."""
    api_err = _make_api_connection_error()
    mock_summarize.side_effect = api_err

    result = summarize_with_backoff("https://example.com/docs/foo", "<html></html>")

    assert result is None
    mock_summarize.assert_called_once()
    mock_sleep.assert_not_called()


# ---------------------------------------------------------------------------
# process_doc
# ---------------------------------------------------------------------------


def test_process_doc_happy_path(tmp_path):
    """Successfully fetched doc is summarized and written to skill references/."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    url = "https://www.twingate.com/docs/connector-deployment"

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html><body>Hello</body></html>"),
        patch("update_references.extract_text_from_html", return_value="Hello"),
        patch("update_references.content_hash", return_value="hash001"),
        patch("update_references.summarize_with_backoff", return_value="## Summary\nContent"),
    ):
        process_doc(url, "twingate-connectors", hash_cache, stats)

    assert stats == {"updated": 1, "skipped": 0, "failed": 0}
    assert hash_cache[url] == "hash001"
    output_file = skills_dir / "twingate-connectors" / "references" / "connector-deployment.md"
    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8") == "## Summary\nContent"


def test_process_doc_fetch_fail(tmp_path):
    """Failed HTML fetch increments stats['failed'] and writes nothing."""
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}

    with patch("update_references.fetch_doc_html", return_value=None):
        process_doc(
            "https://www.twingate.com/docs/missing",
            "twingate-connectors",
            hash_cache,
            stats,
        )

    assert stats == {"updated": 0, "skipped": 0, "failed": 1}
    assert hash_cache == {}


def test_process_doc_hash_skip(tmp_path):
    """Unchanged content (hash match + file exists) increments stats['skipped']."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    url = "https://www.twingate.com/docs/connector-deployment"

    # Pre-create the output file so the existence check passes.
    output_file = skills_dir / "twingate-connectors" / "references" / "connector-deployment.md"
    output_file.parent.mkdir(parents=True)
    output_file.write_text("old summary", encoding="utf-8")

    hash_cache = {url: "hash001"}
    stats = {"updated": 0, "skipped": 0, "failed": 0}

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="same content"),
        patch("update_references.content_hash", return_value="hash001"),
        patch("update_references.summarize_with_backoff") as mock_summarize,
    ):
        process_doc(url, "twingate-connectors", hash_cache, stats)

    assert stats == {"updated": 0, "skipped": 1, "failed": 0}
    mock_summarize.assert_not_called()
    # File unchanged
    assert output_file.read_text(encoding="utf-8") == "old summary"


def test_process_doc_summary_fail(tmp_path):
    """When summarize_with_backoff returns None, stats['failed'] increments."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
        patch("update_references.content_hash", return_value="hash999"),
        patch("update_references.summarize_with_backoff", return_value=None),
    ):
        process_doc(
            "https://www.twingate.com/docs/failing-doc",
            "twingate-connectors",
            hash_cache,
            stats,
        )

    assert stats == {"updated": 0, "skipped": 0, "failed": 1}
    assert hash_cache == {}


def test_process_doc_triage(tmp_path):
    """Unassigned new docs (triage=True) are written to _triage/ with a header comment."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    url = "https://www.twingate.com/docs/some-new-doc"

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
        patch("update_references.content_hash", return_value="hashXXX"),
        patch("update_references.summarize_with_backoff", return_value="## Triage Summary"),
    ):
        process_doc(url, "", hash_cache, stats, triage=True)

    assert stats == {"updated": 1, "skipped": 0, "failed": 0}
    triage_file = triage_dir / "some-new-doc.md"
    assert triage_file.exists()
    content = triage_file.read_text(encoding="utf-8")
    assert url in content
    assert "## Triage Summary" in content
    assert "triage" in content


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------


@patch("update_references.check_api_health", return_value=True)
@patch("update_references.fetch_sitemap", side_effect=Exception("network down"))
def test_main_sitemap_fail(mock_sitemap, mock_health, tmp_path, capsys):
    """Fatal sitemap failure returns exit code 1."""
    exit_code = main()
    assert exit_code == 1


def test_main_happy_path(tmp_path):
    """Full happy-path run: one mapped doc, no new/removed, exits 0."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache_path = tmp_path / ".doc_hashes.json"

    fake_mapping = {
        "docs": [{"url": "https://www.twingate.com/docs/connectors", "skill": "twingate-connectors"}],
        "auto_assign_patterns": [],
    }

    with (
        patch("update_references.check_api_health", return_value=True),
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.HASH_CACHE_PATH", hash_cache_path),
        patch("update_references.fetch_sitemap", return_value=["https://www.twingate.com/docs/connectors"]),
        patch("update_references.diff_docs", return_value=([], [])),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.fetch_doc_html", return_value="<html><body>content</body></html>"),
        patch("update_references.extract_text_from_html", return_value="content"),
        patch("update_references.content_hash", return_value="abc123"),
        patch("update_references.summarize_with_backoff", return_value="## Summary\nDone"),
    ):
        exit_code = main()

    assert exit_code == 0
    output_file = skills_dir / "twingate-connectors" / "references" / "connectors.md"
    assert output_file.exists()
    assert hash_cache_path.exists()
    saved_cache = json.loads(hash_cache_path.read_text())
    assert saved_cache["https://www.twingate.com/docs/connectors"] == "abc123"


def test_main_hash_skip(tmp_path):
    """Docs whose content hash matches are skipped; exit code 0."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache_path = tmp_path / ".doc_hashes.json"
    url = "https://www.twingate.com/docs/connectors"

    # Pre-create reference file and hash cache entry so skip logic triggers.
    refs_dir = skills_dir / "twingate-connectors" / "references"
    refs_dir.mkdir(parents=True)
    (refs_dir / "connectors.md").write_text("old summary", encoding="utf-8")
    hash_cache_path.write_text(json.dumps({url: "unchanged-hash"}), encoding="utf-8")

    fake_mapping = {
        "docs": [{"url": url, "skill": "twingate-connectors"}],
        "auto_assign_patterns": [],
    }

    with (
        patch("update_references.check_api_health", return_value=True),
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.HASH_CACHE_PATH", hash_cache_path),
        patch("update_references.fetch_sitemap", return_value=[url]),
        patch("update_references.diff_docs", return_value=([], [])),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="same"),
        patch("update_references.content_hash", return_value="unchanged-hash"),
        patch("update_references.summarize_with_backoff") as mock_summarize,
    ):
        exit_code = main()

    assert exit_code == 0
    mock_summarize.assert_not_called()
    # Original file is untouched
    assert (refs_dir / "connectors.md").read_text(encoding="utf-8") == "old summary"


def test_main_new_doc_auto_assigned(tmp_path):
    """New doc that matches an auto-assign pattern is written to the assigned skill."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache_path = tmp_path / ".doc_hashes.json"
    new_url = "https://www.twingate.com/docs/connector-new-feature"

    fake_mapping = {
        "docs": [],
        "auto_assign_patterns": [{"pattern": "/docs/connector", "skill": "twingate-connectors"}],
    }

    with (
        patch("update_references.check_api_health", return_value=True),
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.HASH_CACHE_PATH", hash_cache_path),
        patch("update_references.fetch_sitemap", return_value=[new_url]),
        patch("update_references.diff_docs", return_value=([new_url], [])),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
        patch("update_references.content_hash", return_value="newhash"),
        patch("update_references.summarize_with_backoff", return_value="## New Summary"),
    ):
        exit_code = main()

    assert exit_code == 0
    output_file = skills_dir / "twingate-connectors" / "references" / "connector-new-feature.md"
    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8") == "## New Summary"


def test_main_new_doc_triage(tmp_path):
    """New doc with no pattern match is written to _triage/."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache_path = tmp_path / ".doc_hashes.json"
    new_url = "https://www.twingate.com/docs/brand-new-mystery-page"

    fake_mapping = {
        "docs": [],
        "auto_assign_patterns": [],
    }

    with (
        patch("update_references.check_api_health", return_value=True),
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.HASH_CACHE_PATH", hash_cache_path),
        patch("update_references.fetch_sitemap", return_value=[new_url]),
        patch("update_references.diff_docs", return_value=([new_url], [])),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
        patch("update_references.content_hash", return_value="triageh"),
        patch("update_references.summarize_with_backoff", return_value="## Triage Content"),
    ):
        exit_code = main()

    assert exit_code == 0
    triage_file = triage_dir / "brand-new-mystery-page.md"
    assert triage_file.exists()
    content = triage_file.read_text(encoding="utf-8")
    assert new_url in content
    assert "## Triage Content" in content


def test_main_exits_nonzero_on_doc_failure(tmp_path):
    """Pipeline exits with code 1 when any doc fails processing."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache_path = tmp_path / ".doc_hashes.json"

    fake_mapping = {
        "docs": [{"url": "https://www.twingate.com/docs/broken", "skill": "twingate-connectors"}],
        "auto_assign_patterns": [],
    }

    with (
        patch("update_references.check_api_health", return_value=True),
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.HASH_CACHE_PATH", hash_cache_path),
        patch("update_references.fetch_sitemap", return_value=["https://www.twingate.com/docs/broken"]),
        patch("update_references.diff_docs", return_value=([], [])),
        patch("update_references.load_mapping", return_value=fake_mapping),
        # fetch_doc_html returns None → failure
        patch("update_references.fetch_doc_html", return_value=None),
    ):
        exit_code = main()

    assert exit_code == 1


# ---------------------------------------------------------------------------
# write_reference_file — path traversal guard
# ---------------------------------------------------------------------------


def test_write_reference_file_rejects_traversal_in_skill(tmp_path):
    """write_reference_file raises ValueError if skill name tries to escape SKILLS_DIR."""
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir(parents=True)

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        pytest.raises(ValueError, match="escapes skills directory"),
    ):
        write_reference_file("../../evil", "some-doc", "content")


# ---------------------------------------------------------------------------
# check_api_health
# ---------------------------------------------------------------------------


def test_check_api_health_missing_key():
    """Returns False immediately when ANTHROPIC_API_KEY is not set."""
    with patch.dict("os.environ", {}, clear=True):
        # Ensure the key is absent even if present in the test environment.
        import os
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        with patch.dict("os.environ", env, clear=True):
            result = check_api_health()
    assert result is False


@patch("update_references.anthropic.Anthropic")
def test_check_api_health_success(mock_anthropic_cls):
    """Returns True when the API responds successfully."""
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.return_value = object()  # any non-exception response

    with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "sk-test"}):
        result = check_api_health()

    assert result is True
    mock_client.messages.create.assert_called_once()


@patch("update_references.anthropic.Anthropic")
def test_check_api_health_auth_error(mock_anthropic_cls):
    """Returns False on AuthenticationError (bad or missing key)."""
    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    response = httpx.Response(401, request=request)
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.side_effect = anthropic.AuthenticationError(
        message="invalid key", response=response, body=None
    )

    with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "sk-bad"}):
        result = check_api_health()

    assert result is False


@patch("update_references.anthropic.Anthropic")
def test_check_api_health_connection_error(mock_anthropic_cls):
    """Returns False on APIConnectionError (API unreachable)."""
    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.side_effect = anthropic.APIConnectionError(
        message="connection refused", request=request
    )

    with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "sk-test"}):
        result = check_api_health()

    assert result is False


@patch("update_references.anthropic.Anthropic")
def test_check_api_health_server_error(mock_anthropic_cls):
    """Returns False on APIStatusError (e.g. 529 overloaded, 500 internal)."""
    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    response = httpx.Response(529, request=request)
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.side_effect = anthropic.InternalServerError(
        message="overloaded", response=response, body=None
    )

    with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "sk-test"}):
        result = check_api_health()

    assert result is False


@patch("update_references.check_api_health", return_value=False)
def test_main_exits_early_if_api_unhealthy(mock_health):
    """Pipeline exits with code 1 immediately when health check fails, touching no files."""
    with patch("update_references.fetch_sitemap") as mock_sitemap:
        exit_code = main()

    assert exit_code == 1
    mock_sitemap.assert_not_called()  # no work done before the health check fails


# ---------------------------------------------------------------------------
# summarize_with_backoff — unexpected exception handling
# ---------------------------------------------------------------------------


@patch("update_references.time.sleep")
@patch("update_references.summarize_doc")
def test_summarize_with_backoff_catches_unexpected_exception(mock_summarize, mock_sleep):
    """An unexpected exception (e.g. ValueError) is caught and returns None."""
    mock_summarize.side_effect = ValueError("unexpected content block type")

    result = summarize_with_backoff("https://www.twingate.com/docs/foo", "<html></html>")

    assert result is None
    mock_summarize.assert_called_once()  # no retries for non-API errors
    mock_sleep.assert_not_called()
