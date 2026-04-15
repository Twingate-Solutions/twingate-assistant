"""Unit tests for diff_docs module.

Tests use tmp_path to write real YAML files on disk rather than mocking
file I/O, ensuring the YAML parsing path is exercised end-to-end.
The conftest.py at scripts/tests/ adds scripts/ to sys.path.
"""

import yaml

from diff_docs import auto_assign, diff_docs


# ── Helpers ──────────────────────────────────────────────────────────────────


def _write_mapping(tmp_path, docs: list[dict], patterns: list[dict] | None = None) -> str:
    """Write a minimal doc_mapping.yaml and return its path as a string."""
    data: dict = {"docs": docs}
    if patterns is not None:
        data["auto_assign_patterns"] = patterns
    path = tmp_path / "doc_mapping.yaml"
    path.write_text(yaml.dump(data, default_flow_style=False), encoding="utf-8")
    return str(path)


# ── diff_docs tests ──────────────────────────────────────────────────────────


def test_new_url_detected(tmp_path) -> None:
    """A URL in the sitemap but not in the mapping appears in new_urls."""
    mapping_path = _write_mapping(tmp_path, docs=[
        {"url": "https://www.twingate.com/docs/architecture", "skill": "twingate-architect"},
    ])
    sitemap = [
        "https://www.twingate.com/docs/architecture",
        "https://www.twingate.com/docs/brand-new-page",
    ]

    new_urls, removed_urls = diff_docs(sitemap, mapping_path)

    assert "https://www.twingate.com/docs/brand-new-page" in new_urls
    assert "https://www.twingate.com/docs/architecture" not in new_urls
    assert removed_urls == []


def test_removed_url_detected(tmp_path) -> None:
    """A URL in the mapping but not in the sitemap appears in removed_urls."""
    mapping_path = _write_mapping(tmp_path, docs=[
        {"url": "https://www.twingate.com/docs/architecture", "skill": "twingate-architect"},
        {"url": "https://www.twingate.com/docs/old-page", "skill": "twingate-architect"},
    ])
    sitemap = [
        "https://www.twingate.com/docs/architecture",
    ]

    new_urls, removed_urls = diff_docs(sitemap, mapping_path)

    assert "https://www.twingate.com/docs/old-page" in removed_urls
    assert "https://www.twingate.com/docs/architecture" not in removed_urls
    assert new_urls == []


def test_url_in_both_not_in_either_list(tmp_path) -> None:
    """A URL present in both the sitemap and mapping appears in neither list."""
    mapping_path = _write_mapping(tmp_path, docs=[
        {"url": "https://www.twingate.com/docs/architecture", "skill": "twingate-architect"},
    ])
    sitemap = [
        "https://www.twingate.com/docs/architecture",
    ]

    new_urls, removed_urls = diff_docs(sitemap, mapping_path)

    assert new_urls == []
    assert removed_urls == []


def test_empty_sitemap_all_mapped_are_removed(tmp_path) -> None:
    """When the sitemap is empty, every mapped URL is reported as removed."""
    mapping_path = _write_mapping(tmp_path, docs=[
        {"url": "https://www.twingate.com/docs/architecture", "skill": "twingate-architect"},
        {"url": "https://www.twingate.com/docs/connectors", "skill": "twingate-connectors"},
    ])

    new_urls, removed_urls = diff_docs([], mapping_path)

    assert new_urls == []
    assert len(removed_urls) == 2
    assert "https://www.twingate.com/docs/architecture" in removed_urls
    assert "https://www.twingate.com/docs/connectors" in removed_urls


def test_diff_docs_returns_sorted_lists(tmp_path) -> None:
    """Both new_urls and removed_urls are returned in sorted order."""
    mapping_path = _write_mapping(tmp_path, docs=[
        {"url": "https://www.twingate.com/docs/zzz-removed", "skill": "twingate-architect"},
        {"url": "https://www.twingate.com/docs/aaa-removed", "skill": "twingate-architect"},
        {"url": "https://www.twingate.com/docs/kept", "skill": "twingate-architect"},
    ])
    sitemap = [
        "https://www.twingate.com/docs/kept",
        "https://www.twingate.com/docs/zzz-new",
        "https://www.twingate.com/docs/aaa-new",
    ]

    new_urls, removed_urls = diff_docs(sitemap, mapping_path)

    assert new_urls == [
        "https://www.twingate.com/docs/aaa-new",
        "https://www.twingate.com/docs/zzz-new",
    ]
    assert removed_urls == [
        "https://www.twingate.com/docs/aaa-removed",
        "https://www.twingate.com/docs/zzz-removed",
    ]


# ── auto_assign tests ───────────────────────────────────────────────────────


def test_auto_assign_matches_first_pattern() -> None:
    """auto_assign returns the skill from the first matching pattern."""
    patterns = [
        {"pattern": "/docs/connector", "skill": "twingate-connectors"},
        {"pattern": "/docs/terraform", "skill": "twingate-terraform"},
    ]

    result = auto_assign("https://www.twingate.com/docs/connector-deployment", patterns)

    assert result == "twingate-connectors"


def test_auto_assign_no_match_returns_none() -> None:
    """auto_assign returns None when no pattern matches the URL."""
    patterns = [
        {"pattern": "/docs/connector", "skill": "twingate-connectors"},
        {"pattern": "/docs/terraform", "skill": "twingate-terraform"},
    ]

    result = auto_assign("https://www.twingate.com/docs/architecture", patterns)

    assert result is None


def test_auto_assign_first_match_wins() -> None:
    """When multiple patterns match, the first one in the list wins."""
    patterns = [
        {"pattern": "/docs/connector", "skill": "twingate-connectors"},
        {"pattern": "/docs/connector-deployment", "skill": "twingate-terraform"},
    ]

    # Both patterns match this URL; first-match semantics should pick connectors
    result = auto_assign("https://www.twingate.com/docs/connector-deployment", patterns)

    assert result == "twingate-connectors"


def test_auto_assign_empty_patterns_returns_none() -> None:
    """auto_assign returns None when the pattern list is empty."""
    result = auto_assign("https://www.twingate.com/docs/anything", [])

    assert result is None
