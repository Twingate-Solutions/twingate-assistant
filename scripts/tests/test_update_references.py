"""Unit tests for update_references.py — the pipeline orchestrator."""

import dataclasses
import json
from datetime import date
from unittest.mock import MagicMock, patch

import anthropic
import httpx
import pytest
import yaml

import update_references
from github_repos import OrgDiscovery, RepoInfo
from github_summarize import SummaryResult
from pipeline_metrics import GitHubRunMetrics, RunMetrics
from update_references import (
    MANUAL_REFERENCE_MARKER,
    check_api_health,
    choose_github_mode,
    github_repo_slug,
    github_wiki_slug,
    is_manual_reference,
    load_hash_cache,
    load_sources,
    main,
    process_doc,
    process_github_source,
    process_new_urls,
    save_hash_cache,
    seed_github,
    seed_norm_cache,
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
    written = output_file.read_text(encoding="utf-8")
    assert "## Summary\nContent" in written

    assert written.startswith("---\n")
    _, frontmatter_block, body = written.split("---\n", 2)
    parsed = yaml.safe_load(frontmatter_block)
    assert parsed["source"] == url
    assert parsed["type"] == "docs"
    assert parsed["fetched"] == date.today()
    assert parsed["source_version"] == "hash001"
    assert body == "\n## Summary\nContent"


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
        # Stub the GitHub step so no live API call is made.
        patch("update_references.process_github_source"),
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
        # Stub the GitHub step so no live API call is made.
        patch("update_references.process_github_source"),
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
        # Stub the GitHub step so no live API call is made.
        patch("update_references.process_github_source"),
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
    written = output_file.read_text(encoding="utf-8")
    assert "## New Summary" in written
    assert written.startswith("---\n")
    _, frontmatter_block, body = written.split("---\n", 2)
    parsed = yaml.safe_load(frontmatter_block)
    assert parsed["source"] == new_url
    assert parsed["type"] == "docs"
    assert parsed["fetched"] == date.today()
    assert parsed["source_version"] == "newhash"
    assert body == "\n## New Summary"


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
        # Stub the GitHub step so no live API call is made.
        patch("update_references.process_github_source"),
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
        # Stub the GitHub step so no live API call is made.
        patch("update_references.process_github_source"),
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.HASH_CACHE_PATH", hash_cache_path),
        patch("update_references.fetch_sitemap", return_value=["https://www.twingate.com/docs/broken"]),
        patch("update_references.diff_docs", return_value=([], [])),
        patch("update_references.load_mapping", return_value=fake_mapping),
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
        write_reference_file(
            "../../evil",
            "some-doc",
            "content",
            source="https://www.twingate.com/docs/some-doc",
            type_="docs",
            fetched="2026-08-05",
            source_version="deadbeef",
        )


# ---------------------------------------------------------------------------
# is_manual_reference — hand-authored reference protection
# ---------------------------------------------------------------------------


def _manual_content() -> str:
    return f"<!-- {MANUAL_REFERENCE_MARKER} -->\n\n# Hand-authored guide\n"


def test_is_manual_reference_missing_file(tmp_path):
    assert is_manual_reference(tmp_path / "nope.md") is False


def test_is_manual_reference_generated_file(tmp_path):
    path = tmp_path / "generated.md"
    path.write_text("## Summary\nAuto-generated content", encoding="utf-8")
    assert is_manual_reference(path) is False


def test_is_manual_reference_marked_file(tmp_path):
    path = tmp_path / "manual.md"
    path.write_text(_manual_content(), encoding="utf-8")
    assert is_manual_reference(path) is True


def test_is_manual_reference_marker_beyond_header_ignored(tmp_path):
    """Only the first 1024 chars are inspected — a marker buried deep doesn't count."""
    path = tmp_path / "deep.md"
    path.write_text("x" * 2000 + MANUAL_REFERENCE_MARKER, encoding="utf-8")
    assert is_manual_reference(path) is False


def test_process_doc_skips_manual_reference(tmp_path):
    """A mapped/auto-assigned URL whose slug collides with a hand-authored
    reference is skipped before any fetch or API call, and the file is untouched."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    url = "https://www.twingate.com/docs/gateway-troubleshooting"

    manual_file = skills_dir / "twingate-idfw" / "references" / "gateway-troubleshooting.md"
    manual_file.parent.mkdir(parents=True)
    manual_file.write_text(_manual_content(), encoding="utf-8")

    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html") as mock_fetch,
        patch("update_references.summarize_with_backoff") as mock_summarize,
    ):
        process_doc(url, "twingate-idfw", hash_cache, stats)

    assert stats == {"updated": 0, "skipped": 1, "failed": 0}
    mock_fetch.assert_not_called()
    mock_summarize.assert_not_called()
    assert manual_file.read_text(encoding="utf-8") == _manual_content()
    assert hash_cache == {}


def test_write_reference_file_rejects_manual_overwrite(tmp_path):
    """write_reference_file refuses to clobber a hand-authored reference."""
    skills_dir = tmp_path / "skills"
    manual_file = skills_dir / "twingate-idfw" / "references" / "gateway-troubleshooting.md"
    manual_file.parent.mkdir(parents=True)
    manual_file.write_text(_manual_content(), encoding="utf-8")

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        pytest.raises(ValueError, match="hand-authored"),
    ):
        write_reference_file(
            "twingate-idfw",
            "gateway-troubleshooting",
            "## Generated",
            source="https://www.twingate.com/docs/gateway-troubleshooting",
            type_="docs",
            fetched="2026-08-05",
            source_version="deadbeef",
        )

    assert manual_file.read_text(encoding="utf-8") == _manual_content()


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
    mock_sitemap.assert_not_called()


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
    mock_summarize.assert_called_once()
    mock_sleep.assert_not_called()


# ---------------------------------------------------------------------------
# load_sources — multi-source declaration
# ---------------------------------------------------------------------------


def test_load_sources_returns_declared_sources():
    """Both docs and help sources are returned, in declaration order."""
    mapping = {
        "sources": [
            {
                "name": "docs",
                "sitemap_url": "https://www.twingate.com/sitemap/sitemap-0.xml",
                "path_filter": "/docs/",
                "type": "docs",
            },
            {
                "name": "help",
                "sitemap_url": "https://help.twingate.com/sitemap.xml",
                "path_filter": "/articles/",
                "type": "help",
            },
        ],
    }

    sources = load_sources(mapping)

    assert len(sources) == 2
    assert sources[0]["name"] == "docs"
    assert sources[0]["type"] == "docs"
    assert sources[1]["name"] == "help"
    assert sources[1]["type"] == "help"


def test_load_sources_falls_back_to_single_docs_source_when_absent():
    """A mapping with no 'sources:' key synthesizes one docs source."""
    legacy_mapping = {"docs": [], "auto_assign_patterns": []}

    sources = load_sources(legacy_mapping)

    assert len(sources) == 1
    assert sources[0]["name"] == "docs"
    assert sources[0]["path_filter"] == "/docs/"
    assert sources[0]["type"] == "docs"
    assert sources[0]["sitemap_url"] == update_references.DEFAULT_SITEMAP_URL


def test_load_sources_falls_back_when_sources_key_is_empty_list():
    """An explicit but empty 'sources: []' is treated the same as absent."""
    mapping = {"sources": [], "docs": []}

    sources = load_sources(mapping)

    assert len(sources) == 1
    assert sources[0]["name"] == "docs"


# ---------------------------------------------------------------------------
# process_new_urls — auto-assign / triage routing with doc_type threaded through
# ---------------------------------------------------------------------------


@patch("update_references.process_doc")
def test_process_new_urls_routes_matched_url_with_doc_type(mock_process_doc):
    """A URL matching a pattern is routed to its skill, with doc_type/fetched passed through."""
    patterns = [{"pattern": "-connector", "skill": "twingate-connectors"}]
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    url = "https://help.twingate.com/articles/123-connector-offline"

    process_new_urls(
        [url], patterns, hash_cache, stats, fetched="2026-08-05", doc_type="help"
    )

    mock_process_doc.assert_called_once_with(
        url,
        "twingate-connectors",
        hash_cache,
        stats,
        fetched="2026-08-05",
        doc_type="help",
        source_name="docs",
        metrics=None,
        norm_cache=None,
    )


@patch("update_references.process_doc")
def test_process_new_urls_routes_unmatched_url_to_triage_with_doc_type(mock_process_doc):
    """A URL matching no pattern is routed to triage, still carrying doc_type."""
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    url = "https://help.twingate.com/articles/999-totally-unrecognized"

    process_new_urls([url], [], hash_cache, stats, fetched="2026-08-05", doc_type="help")

    mock_process_doc.assert_called_once_with(
        url,
        "",
        hash_cache,
        stats,
        triage=True,
        fetched="2026-08-05",
        doc_type="help",
        source_name="docs",
        metrics=None,
        norm_cache=None,
    )


def test_process_new_urls_docs_source_regression_guard(tmp_path):
    """A /docs/ URL through process_new_urls with doc_type='docs' writes docs-shaped frontmatter."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    patterns = [{"pattern": "/docs/connector", "skill": "twingate-connectors"}]
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    url = "https://www.twingate.com/docs/connector-new-feature"

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
        patch("update_references.content_hash", return_value="dochash"),
        patch("update_references.summarize_with_backoff", return_value="## Docs Summary"),
    ):
        process_new_urls(
            [url], patterns, hash_cache, stats, fetched="2026-08-05", doc_type="docs"
        )

    output_file = skills_dir / "twingate-connectors" / "references" / "connector-new-feature.md"
    written = output_file.read_text(encoding="utf-8")
    _, frontmatter_block, _ = written.split("---\n", 2)
    parsed = yaml.safe_load(frontmatter_block)
    assert parsed["type"] == "docs"
    assert parsed["source"] == url


# ---------------------------------------------------------------------------
# Help-source end-to-end: process_doc stamps type: help in the frontmatter
# ---------------------------------------------------------------------------


def test_process_doc_help_source_writes_type_help_frontmatter(tmp_path):
    """A help.twingate.com URL processed through process_doc writes a file
    whose frontmatter carries type: help and the help source URL."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    url = "https://help.twingate.com/articles/1422554451-connector-offline"

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="help text"),
        patch("update_references.content_hash", return_value="helphash"),
        patch("update_references.summarize_with_backoff", return_value="## Help Summary"),
    ):
        process_doc(
            url,
            "twingate-connectors",
            hash_cache,
            stats,
            fetched="2026-08-05",
            doc_type="help",
        )

    assert stats == {"updated": 1, "skipped": 0, "failed": 0}
    output_file = (
        skills_dir
        / "twingate-connectors"
        / "references"
        / "1422554451-connector-offline.md"
    )
    written = output_file.read_text(encoding="utf-8")
    _, frontmatter_block, body = written.split("---\n", 2)
    parsed = yaml.safe_load(frontmatter_block)

    assert parsed["type"] == "help"
    assert parsed["source"] == url
    assert "## Help Summary" in body


# ---------------------------------------------------------------------------
# main() — multi-source iteration (docs + help) with per-source type stamping
# ---------------------------------------------------------------------------


def test_main_iterates_both_sources_and_stamps_correct_type(tmp_path):
    """main() processes both a docs and a help source, each URL stamped with its source's type."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache_path = tmp_path / ".doc_hashes.json"

    new_docs_url = "https://www.twingate.com/docs/connector-new-feature"
    new_help_url = "https://help.twingate.com/articles/123-connector-offline"

    fake_mapping = {
        "sources": [
            {
                "name": "docs",
                "sitemap_url": "https://www.twingate.com/sitemap/sitemap-0.xml",
                "path_filter": "/docs/",
                "type": "docs",
            },
            {
                "name": "help",
                "sitemap_url": "https://help.twingate.com/sitemap.xml",
                "path_filter": "/articles/",
                "type": "help",
            },
        ],
        "docs": [],
        "auto_assign_patterns": [
            {"pattern": "/docs/connector", "skill": "twingate-connectors"},
            {"pattern": "-connector", "skill": "twingate-connectors"},
        ],
    }

    def fake_fetch_sitemap(sitemap_url, path_filter):
        if path_filter == "/docs/":
            return [new_docs_url]
        return [new_help_url]

    with (
        patch("update_references.check_api_health", return_value=True),
        # Stub the GitHub step so no live API call is made.
        patch("update_references.process_github_source"),
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.HASH_CACHE_PATH", hash_cache_path),
        patch("update_references.fetch_sitemap", side_effect=fake_fetch_sitemap),
        patch("update_references.diff_docs", side_effect=lambda urls: (urls, [])),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="content"),
        patch("update_references.content_hash", return_value="samehash"),
        patch("update_references.summarize_with_backoff", return_value="## Summary"),
    ):
        exit_code = main()

    assert exit_code == 0

    docs_file = skills_dir / "twingate-connectors" / "references" / "connector-new-feature.md"
    help_file = (
        skills_dir / "twingate-connectors" / "references" / "123-connector-offline.md"
    )
    assert docs_file.exists()
    assert help_file.exists()

    docs_written = docs_file.read_text(encoding="utf-8")
    _, docs_fm, _ = docs_written.split("---\n", 2)
    assert yaml.safe_load(docs_fm)["type"] == "docs"
    assert yaml.safe_load(docs_fm)["source"] == new_docs_url

    help_written = help_file.read_text(encoding="utf-8")
    _, help_fm, _ = help_written.split("---\n", 2)
    assert yaml.safe_load(help_fm)["type"] == "help"
    assert yaml.safe_load(help_fm)["source"] == new_help_url


# ---------------------------------------------------------------------------
# process_doc — churn-attribution metrics + shadow-hash cache
# ---------------------------------------------------------------------------


def test_process_doc_raw_hash_unchanged_seeds_norm_cache_without_summarizing(tmp_path):
    """Cache hit + existing file: no summarize, metrics records 'skipped', norm_cache seeded."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    url = "https://www.twingate.com/docs/connector-deployment"

    output_file = skills_dir / "twingate-connectors" / "references" / "connector-deployment.md"
    output_file.parent.mkdir(parents=True)
    output_file.write_text("old summary", encoding="utf-8")

    hash_cache = {url: "hash001"}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    metrics = RunMetrics()
    norm_cache: dict[str, str] = {}

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="same content"),
        patch("update_references.content_hash", return_value="hash001"),
        patch("update_references.summarize_with_backoff") as mock_summarize,
    ):
        process_doc(
            url, "twingate-connectors", hash_cache, stats, metrics=metrics, norm_cache=norm_cache
        )

    assert stats == {"updated": 0, "skipped": 1, "failed": 0}
    mock_summarize.assert_not_called()
    assert metrics.sources["docs"]["skipped"] == 1
    assert metrics.sources["docs"]["resummarized"] == 0
    assert norm_cache[url] == "hash001"


def test_process_doc_raw_change_with_matching_norm_hash_classifies_noise_only(tmp_path):
    """Raw hash changed but normalized hash matches baseline: classified noise_only."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    url = "https://www.twingate.com/docs/connector-deployment"

    hash_cache = {url: "old-raw-hash"}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    metrics = RunMetrics()
    norm_cache = {url: "stable-norm-hash"}

    def fake_content_hash(t):
        return {"raw-text-v2": "new-raw-hash", "stable-normalized-text": "stable-norm-hash"}[t]

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="raw-text-v2"),
        patch("update_references.normalize_for_hash", return_value="stable-normalized-text"),
        patch("update_references.content_hash", side_effect=fake_content_hash),
        patch("update_references.summarize_with_backoff", return_value="## Summary"),
    ):
        process_doc(
            url, "twingate-connectors", hash_cache, stats, metrics=metrics, norm_cache=norm_cache
        )

    assert stats == {"updated": 1, "skipped": 0, "failed": 0}
    assert metrics.sources["docs"]["resummarized"] == 1
    assert metrics.sources["docs"]["noise_only"] == 1
    assert metrics.sources["docs"]["real_change"] == 0
    assert norm_cache[url] == "stable-norm-hash"


def test_process_doc_raw_change_with_differing_norm_hash_classifies_real_change(tmp_path):
    """Raw hash changed AND normalized hash differs from baseline: classified real_change."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    url = "https://www.twingate.com/docs/connector-deployment"

    hash_cache = {url: "old-raw-hash"}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    metrics = RunMetrics()
    norm_cache = {url: "old-norm-hash"}

    def fake_content_hash(t):
        return {"raw-text-v3": "new-raw-hash", "changed-normalized-text": "new-norm-hash"}[t]

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="raw-text-v3"),
        patch("update_references.normalize_for_hash", return_value="changed-normalized-text"),
        patch("update_references.content_hash", side_effect=fake_content_hash),
        patch("update_references.summarize_with_backoff", return_value="## Summary"),
    ):
        process_doc(
            url, "twingate-connectors", hash_cache, stats, metrics=metrics, norm_cache=norm_cache
        )

    assert stats == {"updated": 1, "skipped": 0, "failed": 0}
    assert metrics.sources["docs"]["resummarized"] == 1
    assert metrics.sources["docs"]["real_change"] == 1
    assert metrics.sources["docs"]["noise_only"] == 0


def test_process_doc_raw_change_with_unseeded_norm_cache_classifies_real_change(tmp_path):
    """An unseeded URL (no prior baseline) counts as real_change, not noise_only."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    url = "https://www.twingate.com/docs/connector-deployment"

    hash_cache = {url: "old-raw-hash"}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    metrics = RunMetrics()
    norm_cache: dict[str, str] = {}

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
        patch("update_references.content_hash", return_value="new-raw-hash"),
        patch("update_references.summarize_with_backoff", return_value="## Summary"),
    ):
        process_doc(
            url, "twingate-connectors", hash_cache, stats, metrics=metrics, norm_cache=norm_cache
        )

    assert metrics.sources["docs"]["resummarized"] == 1
    assert metrics.sources["docs"]["real_change"] == 1
    assert metrics.sources["docs"]["noise_only"] == 0


def test_process_doc_fetch_failure_records_metrics_fetch_fail(tmp_path):
    """A failed fetch records fetch_fail and never reaches the summarizer."""
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    metrics = RunMetrics()

    with (
        patch("update_references.fetch_doc_html", return_value=None),
        patch("update_references.summarize_with_backoff") as mock_summarize,
    ):
        process_doc(
            "https://www.twingate.com/docs/missing",
            "twingate-connectors",
            hash_cache,
            stats,
            metrics=metrics,
        )

    assert stats == {"updated": 0, "skipped": 0, "failed": 1}
    assert metrics.sources["docs"]["fetch_fail"] == 1
    assert metrics.sources["docs"]["fetched_ok"] == 0
    mock_summarize.assert_not_called()


def test_process_doc_manual_reference_records_metrics_manual_skipped(tmp_path):
    """A slug-collision with a hand-authored reference records
    manual_skipped and never fetches or summarizes."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    url = "https://www.twingate.com/docs/gateway-troubleshooting"

    manual_file = skills_dir / "twingate-idfw" / "references" / "gateway-troubleshooting.md"
    manual_file.parent.mkdir(parents=True)
    manual_file.write_text(_manual_content(), encoding="utf-8")

    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    metrics = RunMetrics()

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html") as mock_fetch,
        patch("update_references.summarize_with_backoff") as mock_summarize,
    ):
        process_doc(url, "twingate-idfw", hash_cache, stats, metrics=metrics)

    assert stats == {"updated": 0, "skipped": 1, "failed": 0}
    assert metrics.sources["docs"]["manual_skipped"] == 1
    mock_fetch.assert_not_called()
    mock_summarize.assert_not_called()


def test_process_doc_triage_records_metrics_triaged(tmp_path):
    """A doc written to _triage/ records the triaged counter."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    hash_cache: dict[str, str] = {}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    metrics = RunMetrics()
    url = "https://www.twingate.com/docs/some-new-doc"

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
        patch("update_references.content_hash", return_value="hashXXX"),
        patch("update_references.summarize_with_backoff", return_value="## Triage Summary"),
    ):
        process_doc(url, "", hash_cache, stats, triage=True, metrics=metrics)

    assert stats == {"updated": 1, "skipped": 0, "failed": 0}
    assert metrics.sources["docs"]["triaged"] == 1


def test_process_doc_norm_hash_never_gates_the_resummarize_decision(tmp_path):
    """norm_hash never gates the summarize decision; only the raw hash does.

    Case A: raw hash changed, norm_hash identical to baseline -> summarizer called.
    Case B: raw hash unchanged, norm baseline stale -> summarizer not called.
    """
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    url = "https://www.twingate.com/docs/connector-deployment"

    # --- Case A: raw changed, norm_hash unchanged from baseline ------------
    hash_cache_a = {url: "old-raw-hash"}
    stats_a = {"updated": 0, "skipped": 0, "failed": 0}
    norm_cache_a = {url: "same-norm-hash"}

    def fake_content_hash_a(t):
        return {"raw-text": "new-raw-hash", "normalized-text": "same-norm-hash"}[t]

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="raw-text"),
        patch("update_references.normalize_for_hash", return_value="normalized-text"),
        patch("update_references.content_hash", side_effect=fake_content_hash_a),
        patch(
            "update_references.summarize_with_backoff", return_value="## Summary"
        ) as mock_summarize_a,
    ):
        process_doc(url, "twingate-connectors", hash_cache_a, stats_a, norm_cache=norm_cache_a)

    mock_summarize_a.assert_called_once()
    assert stats_a["updated"] == 1

    # --- Case B: raw unchanged (skip), norm baseline stale/mismatched ------
    output_file = skills_dir / "twingate-connectors" / "references" / "connector-deployment.md"
    assert output_file.exists()  # written by Case A above
    hash_cache_b = {url: "same-raw-hash"}
    stats_b = {"updated": 0, "skipped": 0, "failed": 0}
    norm_cache_b = {url: "stale-mismatched-norm-hash"}

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="raw-text-2"),
        patch(
            "update_references.normalize_for_hash", return_value="a-totally-different-norm-text"
        ),
        patch("update_references.content_hash", return_value="same-raw-hash"),
        patch("update_references.summarize_with_backoff") as mock_summarize_b,
    ):
        process_doc(url, "twingate-connectors", hash_cache_b, stats_b, norm_cache=norm_cache_b)

    mock_summarize_b.assert_not_called()
    assert stats_b == {"updated": 0, "skipped": 1, "failed": 0}


# ---------------------------------------------------------------------------
# seed_norm_cache — populate the shadow-hash cache without touching the API
# ---------------------------------------------------------------------------


def test_seed_norm_cache_populates_norm_cache_for_all_hash_cache_urls(tmp_path):
    """Every URL in the raw hash cache gets a normalized-hash entry."""
    hash_path = tmp_path / ".doc_hashes.json"
    norm_path = tmp_path / ".doc_norm_hashes.json"
    urls = [
        "https://www.twingate.com/docs/connector-deployment",
        "https://www.twingate.com/docs/how-twingate-works",
    ]
    hash_path.write_text(json.dumps({u: "irrelevant-raw-hash" for u in urls}), encoding="utf-8")

    with (
        patch(
            "update_references.fetch_doc_html", return_value="<html><body>content</body></html>"
        ),
        patch("update_references.extract_text_from_html", return_value="content text"),
    ):
        exit_code = seed_norm_cache(norm_path, hash_path)

    assert exit_code == 0
    saved = json.loads(norm_path.read_text(encoding="utf-8"))
    assert set(saved) == set(urls)
    expected = update_references.content_hash(
        update_references.normalize_for_hash("content text")
    )
    for u in urls:
        assert saved[u] == expected


def test_seed_norm_cache_makes_no_summarizer_or_api_calls(tmp_path):
    """seed_norm_cache never calls the summarizer."""
    hash_path = tmp_path / ".doc_hashes.json"
    norm_path = tmp_path / ".doc_norm_hashes.json"
    hash_path.write_text(
        json.dumps({"https://www.twingate.com/docs/connector-deployment": "h"}),
        encoding="utf-8",
    )

    with (
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
        patch("update_references.summarize_with_backoff") as mock_summarize,
        patch("update_references.summarize_doc") as mock_summarize_doc,
    ):
        seed_norm_cache(norm_path, hash_path)

    mock_summarize.assert_not_called()
    mock_summarize_doc.assert_not_called()


def test_seed_norm_cache_writes_nothing_to_references_directory(tmp_path):
    """seed_norm_cache never creates or writes into skills/*/references/."""
    hash_path = tmp_path / ".doc_hashes.json"
    norm_path = tmp_path / ".doc_norm_hashes.json"
    skills_dir = tmp_path / "skills"
    hash_path.write_text(
        json.dumps({"https://www.twingate.com/docs/connector-deployment": "h"}),
        encoding="utf-8",
    )

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.fetch_doc_html", return_value="<html></html>"),
        patch("update_references.extract_text_from_html", return_value="text"),
    ):
        seed_norm_cache(norm_path, hash_path)

    assert not skills_dir.exists()


def test_seed_norm_cache_skips_fetch_failures_without_crashing(tmp_path):
    """A fetch failure is skipped without raising; the failed URL gets no entry."""
    hash_path = tmp_path / ".doc_hashes.json"
    norm_path = tmp_path / ".doc_norm_hashes.json"
    good_url = "https://www.twingate.com/docs/connector-deployment"
    bad_url = "https://www.twingate.com/docs/unreachable-page"
    hash_path.write_text(json.dumps({good_url: "h1", bad_url: "h2"}), encoding="utf-8")

    def fake_fetch(url):
        return None if url == bad_url else "<html></html>"

    with (
        patch("update_references.fetch_doc_html", side_effect=fake_fetch),
        patch("update_references.extract_text_from_html", return_value="text"),
    ):
        exit_code = seed_norm_cache(norm_path, hash_path)

    assert exit_code == 0
    saved = json.loads(norm_path.read_text(encoding="utf-8"))
    assert good_url in saved
    assert bad_url not in saved


# ---------------------------------------------------------------------------
# call_with_backoff — generic retry wrapper
# ---------------------------------------------------------------------------


def test_call_with_backoff_success_returns_value():
    fn = MagicMock(return_value="ok")

    result = update_references.call_with_backoff(fn, label="test")

    assert result == "ok"
    fn.assert_called_once()


@patch("update_references.time.sleep")
def test_call_with_backoff_retries_on_rate_limit_then_succeeds(mock_sleep):
    rate_limit_err = _make_rate_limit_error()
    fn = MagicMock(side_effect=[rate_limit_err, "ok"])

    result = update_references.call_with_backoff(fn, label="test")

    assert result == "ok"
    assert fn.call_count == 2
    mock_sleep.assert_called_once()


@patch("update_references.time.sleep")
def test_call_with_backoff_exhausts_retries_returns_none(mock_sleep):
    rate_limit_err = _make_rate_limit_error()
    fn = MagicMock(side_effect=rate_limit_err)

    result = update_references.call_with_backoff(fn, label="test")

    assert result is None
    assert fn.call_count == update_references.BACKOFF_MAX_RETRIES + 1


def test_call_with_backoff_api_error_returns_none_no_retry():
    api_err = _make_api_connection_error()
    fn = MagicMock(side_effect=api_err)

    result = update_references.call_with_backoff(fn, label="test")

    assert result is None
    fn.assert_called_once()


def test_call_with_backoff_unexpected_exception_returns_none():
    fn = MagicMock(side_effect=ValueError("boom"))

    result = update_references.call_with_backoff(fn, label="test")

    assert result is None
    fn.assert_called_once()


# ---------------------------------------------------------------------------
# github_repo_slug / github_wiki_slug
# ---------------------------------------------------------------------------


def test_github_repo_slug_lowercases_org_and_repo():
    assert github_repo_slug("Twingate", "Terraform-Provider-Twingate") == (
        "gh-twingate-terraform-provider-twingate"
    )


def test_github_wiki_slug_lowercases_and_appends_wiki_suffix():
    assert github_wiki_slug("Twingate", "Kubernetes-Operator") == (
        "gh-twingate-kubernetes-operator-wiki"
    )


def test_github_repo_slug_strips_path_separators():
    # A hostile repo name cannot introduce a path separator into the slug.
    slug = github_repo_slug("Twingate", "../../other-skill/references/evil")
    assert "/" not in slug
    assert ".." not in slug


def test_github_repo_slug_replaces_dots():
    assert github_repo_slug("Twingate", "docs.twingate.com") == "gh-twingate-docs-twingate-com"


# ---------------------------------------------------------------------------
# choose_github_mode
# ---------------------------------------------------------------------------


def test_choose_github_mode_small_diff_with_prior_doc_is_delta():
    assert choose_github_mode(has_prior_doc=True, filtered_byte_len=100, filtered_file_count=2) == "delta"


def test_choose_github_mode_no_prior_doc_is_full_regardless_of_diff_size():
    assert choose_github_mode(has_prior_doc=False, filtered_byte_len=0, filtered_file_count=0) == "full"


def test_choose_github_mode_oversized_bytes_is_full():
    mode = choose_github_mode(
        has_prior_doc=True,
        filtered_byte_len=update_references.MAX_TEXT_LENGTH + 1,
        filtered_file_count=1,
    )
    assert mode == "full"


def test_choose_github_mode_too_many_files_is_full():
    mode = choose_github_mode(
        has_prior_doc=True,
        filtered_byte_len=10,
        filtered_file_count=update_references.MAX_DELTA_FILES + 1,
    )
    assert mode == "full"


def test_choose_github_mode_exact_threshold_boundary_stays_delta():
    """Exactly at both thresholds (not over) stays delta."""
    mode = choose_github_mode(
        has_prior_doc=True,
        filtered_byte_len=update_references.MAX_TEXT_LENGTH,
        filtered_file_count=update_references.MAX_DELTA_FILES,
    )
    assert mode == "delta"


# ---------------------------------------------------------------------------
# _strip_frontmatter / _read_prior_doc_body
# ---------------------------------------------------------------------------


def test_strip_frontmatter_removes_leading_block():
    content = "---\nsource: x\ntype: github\n---\n\nBody text here"
    assert update_references._strip_frontmatter(content) == "Body text here"


def test_strip_frontmatter_no_frontmatter_returns_content_unchanged():
    content = "Just a body, no frontmatter block"
    assert update_references._strip_frontmatter(content) == content


def test_read_prior_doc_body_missing_file_returns_none(tmp_path):
    assert update_references._read_prior_doc_body(tmp_path / "nope.md") is None


def test_read_prior_doc_body_reads_and_strips_frontmatter(tmp_path):
    path = tmp_path / "doc.md"
    path.write_text("---\nsource: x\n---\n\nActual body\n", encoding="utf-8")

    assert update_references._read_prior_doc_body(path) == "Actual body\n"


# ---------------------------------------------------------------------------
# process_github_source / _process_github_repo
# ---------------------------------------------------------------------------


def _repo_info(**overrides) -> RepoInfo:
    """Build a RepoInfo with sane defaults for the GitHub pipeline tests."""
    base = RepoInfo(
        name="example-repo",
        full_name="Twingate/example-repo",
        html_url="https://github.com/Twingate/example-repo",
        default_branch="main",
        pushed_at="2024-06-01T00:00:00Z",
        fork=False,
        archived=False,
        disabled=False,
        size=1200,
        description="An example Twingate repo",
        topics=(),
        language="Go",
        has_wiki=False,
        is_stub=False,
    )
    return dataclasses.replace(base, **overrides)


def _discover_dispatch(repo: RepoInfo, org_name: str = "Twingate"):
    """Build a discover_org_repos side_effect returning `repo` only for
    `org_name`; every other org (of the four DEFAULT_ORGS) is empty."""

    def _dispatch(org, token):
        if org == org_name:
            return OrgDiscovery(org=org, total_repos=1, forks_excluded=0, kept=(repo,), stub_count=0)
        return OrgDiscovery(org=org, total_repos=0, forks_excluded=0, kept=(), stub_count=0)

    return _dispatch


def test_process_github_source_mapped_repo_writes_github_type_frontmatter(tmp_path):
    """A mapped, changed, cold-start repo is summarized and written with type: github."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    repo = _repo_info()
    fake_mapping = {"repos": [{"full_name": "Twingate/example-repo", "skill": "twingate-terraform"}]}
    result = SummaryResult(text="## Fresh Summary\nBody content", input_tokens=10, output_tokens=5, model="m")
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    github_metrics = GitHubRunMetrics()

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.load_repo_state", return_value={}),
        patch("update_references.save_repo_state") as mock_save_state,
        patch("update_references.discover_org_repos", side_effect=_discover_dispatch(repo)),
        patch("update_references.get_default_branch_head_sha", return_value="headsha123"),
        patch("update_references.fetch_repo_readme", return_value="# README content"),
        patch("update_references.fetch_latest_release_notes", return_value=None),
        patch("update_references.summarize_repo_full", return_value=result) as mock_full,
        patch("update_references.summarize_repo_delta") as mock_delta,
    ):
        process_github_source("2026-08-06", stats, github_metrics)

    output_file = skills_dir / "twingate-terraform" / "references" / "gh-twingate-example-repo.md"
    assert output_file.exists()
    written = output_file.read_text(encoding="utf-8")
    _, frontmatter_block, body = written.split("---\n", 2)
    parsed = yaml.safe_load(frontmatter_block)
    assert parsed["type"] == "github"
    assert "## Fresh Summary" in body

    mock_full.assert_called_once()
    mock_delta.assert_not_called()
    assert stats["updated"] == 1
    mock_save_state.assert_called_once()
    assert github_metrics.records[0]["mode"] == "full"


def test_process_github_source_unmapped_repo_routes_to_triage(tmp_path):
    """A discovered repo with no `repos:` mapping entry routes to _triage/."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    repo = _repo_info(name="unmapped-repo", full_name="Twingate/unmapped-repo")
    fake_mapping = {"repos": []}
    result = SummaryResult(text="## Unmapped Summary", input_tokens=1, output_tokens=1, model="m")
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    github_metrics = GitHubRunMetrics()

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.load_repo_state", return_value={}),
        patch("update_references.save_repo_state"),
        patch("update_references.discover_org_repos", side_effect=_discover_dispatch(repo)),
        patch("update_references.get_default_branch_head_sha", return_value="headsha456"),
        patch("update_references.fetch_repo_readme", return_value="# README"),
        patch("update_references.fetch_latest_release_notes", return_value=None),
        patch("update_references.summarize_repo_full", return_value=result),
    ):
        process_github_source("2026-08-06", stats, github_metrics)

    triage_file = triage_dir / "gh-twingate-unmapped-repo.md"
    assert triage_file.exists()
    assert "triage: unassigned" in triage_file.read_text(encoding="utf-8")


def test_process_github_source_manual_reference_collision_is_untouched(tmp_path):
    """A hand-authored reference file colliding with the computed slug is
    never overwritten, and Claude is never called for that repo."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    repo = _repo_info()
    fake_mapping = {"repos": [{"full_name": "Twingate/example-repo", "skill": "twingate-terraform"}]}

    manual_file = skills_dir / "twingate-terraform" / "references" / "gh-twingate-example-repo.md"
    manual_file.parent.mkdir(parents=True)
    manual_content = f"<!-- {MANUAL_REFERENCE_MARKER} -->\n\n# Hand-authored\n"
    manual_file.write_text(manual_content, encoding="utf-8")

    stats = {"updated": 0, "skipped": 0, "failed": 0}
    github_metrics = GitHubRunMetrics()

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.load_repo_state", return_value={}),
        patch("update_references.save_repo_state"),
        patch("update_references.discover_org_repos", side_effect=_discover_dispatch(repo)),
        patch("update_references.get_default_branch_head_sha") as mock_head_sha,
        patch("update_references.summarize_repo_full") as mock_full,
        patch("update_references.summarize_repo_delta") as mock_delta,
    ):
        process_github_source("2026-08-06", stats, github_metrics)

    assert manual_file.read_text(encoding="utf-8") == manual_content
    assert stats["skipped"] == 1
    mock_full.assert_not_called()
    mock_delta.assert_not_called()
    mock_head_sha.assert_not_called()


def test_process_github_source_skips_when_head_sha_unchanged_and_doc_exists(tmp_path):
    """Idempotency: recorded last_sha equals the freshly-resolved head sha
    AND the doc file already exists -> skipped, Claude never called."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    repo = _repo_info(pushed_at="2024-07-01T00:00:00Z")
    fake_mapping = {"repos": [{"full_name": "Twingate/example-repo", "skill": "twingate-terraform"}]}

    doc_path = skills_dir / "twingate-terraform" / "references" / "gh-twingate-example-repo.md"
    doc_path.parent.mkdir(parents=True)
    doc_path.write_text("---\nsource: x\n---\n\nExisting body", encoding="utf-8")

    # pushed_at newer than recorded so the repo reaches the head-sha comparison.
    state = {
        "Twingate/example-repo": {
            "last_sha": "samesha000",
            "pushed_at": "2024-01-01T00:00:00Z",
        }
    }
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    github_metrics = GitHubRunMetrics()

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.load_repo_state", return_value=state),
        patch("update_references.save_repo_state"),
        patch("update_references.discover_org_repos", side_effect=_discover_dispatch(repo)),
        patch("update_references.get_default_branch_head_sha", return_value="samesha000"),
        patch("update_references.summarize_repo_full") as mock_full,
        patch("update_references.summarize_repo_delta") as mock_delta,
    ):
        process_github_source("2026-08-06", stats, github_metrics)

    assert stats["skipped"] == 1
    mock_full.assert_not_called()
    mock_delta.assert_not_called()
    assert doc_path.read_text(encoding="utf-8") == "---\nsource: x\n---\n\nExisting body"


def test_process_github_source_stub_repo_writes_one_liner_without_claude_call(tmp_path):
    """Stub repos (archived/disabled/empty) get a one-line summary with mode
    'stub'; Claude is never called for them."""
    skills_dir = tmp_path / "skills"
    triage_dir = skills_dir / "_triage"
    repo = _repo_info(name="stub-repo", full_name="Twingate/stub-repo", archived=True, is_stub=True)
    fake_mapping = {"repos": [{"full_name": "Twingate/stub-repo", "skill": "twingate-terraform"}]}
    stats = {"updated": 0, "skipped": 0, "failed": 0}
    github_metrics = GitHubRunMetrics()

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        patch("update_references.TRIAGE_DIR", triage_dir),
        patch("update_references.load_mapping", return_value=fake_mapping),
        patch("update_references.load_repo_state", return_value={}),
        patch("update_references.save_repo_state"),
        patch("update_references.discover_org_repos", side_effect=_discover_dispatch(repo)),
        patch("update_references.get_default_branch_head_sha") as mock_head_sha,
        patch("update_references.summarize_repo_full") as mock_full,
        patch("update_references.summarize_repo_delta") as mock_delta,
    ):
        process_github_source("2026-08-06", stats, github_metrics)

    output_file = skills_dir / "twingate-terraform" / "references" / "gh-twingate-stub-repo.md"
    assert output_file.exists()
    assert "stub" in output_file.read_text(encoding="utf-8").lower()
    mock_full.assert_not_called()
    mock_delta.assert_not_called()
    mock_head_sha.assert_not_called()
    assert stats["updated"] == 1
    assert github_metrics.records[-1]["mode"] == "stub"
    assert github_metrics.records[-1]["input_tokens"] == 0


# ---------------------------------------------------------------------------
# seed_github — one-time cold-start entrypoint
# ---------------------------------------------------------------------------


def test_seed_github_missing_anthropic_key_returns_1(monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "ghs_test")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

    assert seed_github() == 1


@patch("update_references.emit_github")
@patch("update_references.process_github_source")
def test_seed_github_no_github_token_is_no_longer_fatal(
    mock_process, mock_emit, monkeypatch
):
    """GITHUB_TOKEN is optional: with it unset, seed_github still returns 0."""
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

    exit_code = seed_github(fetched="2026-08-06")

    assert exit_code == 0
    mock_process.assert_called_once()
    mock_emit.assert_called_once()


@patch("update_references.emit_github")
@patch("update_references.process_github_source")
def test_seed_github_still_requires_anthropic_key(mock_process, mock_emit, monkeypatch):
    """ANTHROPIC_API_KEY is still required; missing it returns 1 with no work done."""
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)

    assert seed_github() == 1
    mock_process.assert_not_called()
    mock_emit.assert_not_called()


@patch("update_references.emit_github")
@patch("update_references.process_github_source")
def test_seed_github_smoke_returns_int_and_touches_no_real_paths(
    mock_process, mock_emit, monkeypatch
):
    """With both credentials present, seed_github returns an int exit code of 0."""
    monkeypatch.setenv("GITHUB_TOKEN", "ghs_test")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

    exit_code = seed_github(fetched="2026-08-06")

    assert isinstance(exit_code, int)
    assert exit_code == 0
    mock_process.assert_called_once()
    called_fetched = mock_process.call_args.args[0]
    assert called_fetched == "2026-08-06"
    mock_emit.assert_called_once()
