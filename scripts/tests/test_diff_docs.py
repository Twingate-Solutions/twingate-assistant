"""Unit tests for diff_docs module."""

import yaml

from diff_docs import auto_assign, diff_docs, load_mapping


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


def test_diff_docs_path_filter_scopes_to_one_source(tmp_path) -> None:
    """path_filter restricts the mapped set so other sources' URLs are not
    reported as removed. Regression: the help source once reported every mapped
    /docs/ URL as 'removed' because the whole mapping was diffed against one
    source's sitemap."""
    mapping_path = _write_mapping(tmp_path, docs=[
        {"url": "https://www.twingate.com/docs/architecture", "skill": "twingate-architect"},
        {"url": "https://www.twingate.com/docs/connectors", "skill": "twingate-connectors"},
        {"url": "https://help.twingate.com/articles/1-foo", "skill": "twingate-troubleshoot",
         "type": "help"},
    ])
    help_sitemap = ["https://help.twingate.com/articles/1-foo"]

    new_urls, removed_urls = diff_docs(help_sitemap, mapping_path, path_filter="/articles/")

    # The /docs/ URLs belong to the docs source and must not show as removed here.
    assert removed_urls == []
    assert new_urls == []

    # Without the filter, the old behavior reports both /docs/ URLs as removed.
    _, removed_unscoped = diff_docs(help_sitemap, mapping_path)
    assert len(removed_unscoped) == 2


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

    result = auto_assign("https://www.twingate.com/docs/connector-deployment", patterns)

    assert result == "twingate-connectors"


def test_auto_assign_empty_patterns_returns_none() -> None:
    """auto_assign returns None when the pattern list is empty."""
    result = auto_assign("https://www.twingate.com/docs/anything", [])

    assert result is None


# ── auto_assign with real doc_mapping.yaml patterns (help.twingate.com) ──────


def _real_patterns() -> list[dict]:
    """Load the auto_assign_patterns actually shipped in doc_mapping.yaml."""
    mapping = load_mapping()
    return mapping.get("auto_assign_patterns", [])


def test_auto_assign_help_connector_url_routes_to_connectors() -> None:
    url = "https://help.twingate.com/articles/1422554451-connector-offline-too-many-open-files-in-logs"
    result = auto_assign(url, _real_patterns())
    assert result == "twingate-connectors"


def test_auto_assign_help_dns_url_routes_to_dns_security() -> None:
    url = "https://help.twingate.com/articles/9988776655-twingate-dns-cisco-umbrella"
    result = auto_assign(url, _real_patterns())
    assert result == "twingate-dns-security"


def test_auto_assign_help_generic_article_falls_back_to_troubleshoot() -> None:
    """A help article slug matching no override falls back to troubleshoot."""
    url = "https://help.twingate.com/articles/1111111111-something-nobody-anticipated"
    result = auto_assign(url, _real_patterns())
    assert result == "twingate-troubleshoot"


# ── GitHub repos live under `repos:`, not `docs:` ───────────────────────────


def test_load_mapping_exposes_a_non_empty_repos_key() -> None:
    """The real doc_mapping.yaml carries a non-empty `repos:` list."""
    mapping = load_mapping()

    repos = mapping.get("repos")
    assert repos
    assert isinstance(repos, list)
    for entry in repos:
        assert entry.get("full_name")
        assert entry.get("skill")


def test_docs_list_has_no_github_com_urls() -> None:
    """No `docs:` entry points at a github.com URL."""
    mapping = load_mapping()

    docs = mapping.get("docs", [])
    github_doc_urls = [entry["url"] for entry in docs if "github.com" in entry.get("url", "")]

    assert github_doc_urls == []


def test_help_entries_are_well_formed() -> None:
    """Every help-type entry in docs: has a skill and a help-center article URL.

    Help articles are carried in the mapping (type: help) so the sitemap diff is
    accurate and they survive a hash-cache loss without being re-summarized.
    """
    mapping = load_mapping()
    helps = [d for d in mapping.get("docs", []) if d.get("type") == "help"]

    assert helps, "expected help-center articles carried in the mapping"
    for entry in helps:
        assert "/articles/" in entry.get("url", "")
        assert entry.get("skill")


def test_every_repos_entry_full_name_matches_org_slash_repo_shape() -> None:
    """Each `repos:` entry's full_name is a plain '{org}/{repo}' identifier."""
    mapping = load_mapping()

    for entry in mapping.get("repos", []):
        full_name = entry["full_name"]
        assert full_name.count("/") == 1
        assert not full_name.startswith("http")


def test_auto_assign_help_okta_url_routes_to_identity() -> None:
    url = "https://help.twingate.com/articles/2222222222-configuring-okta-scim"
    result = auto_assign(url, _real_patterns())
    assert result == "twingate-identity"


def test_auto_assign_help_client_url_routes_to_troubleshoot() -> None:
    """'-client' is an explicit troubleshoot override, not the bare catch-all."""
    url = "https://help.twingate.com/articles/3333333333-macos-client-crash"
    result = auto_assign(url, _real_patterns())
    assert result == "twingate-troubleshoot"


def test_auto_assign_real_docs_pattern_regression_guard() -> None:
    """A /docs/ URL still routes correctly alongside the help overrides."""
    url = "https://www.twingate.com/docs/connector-brand-new-page"
    result = auto_assign(url, _real_patterns())
    assert result == "twingate-connectors"
