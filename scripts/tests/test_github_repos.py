"""Unit tests for github_repos module (the zero-LLM-call half of the pipeline)."""

import sys
import time

import pytest
import requests
from unittest.mock import MagicMock, patch

import github_repos
from github_repos import (
    DEFAULT_ORGS,
    DiffSizing,
    FilteredDiff,
    GITHUB_API_BASE,
    OrgDiscovery,
    WikiSnapshot,
    _wiki_clone_url,
    build_filtered_diff,
    build_wiki_diff,
    clone_wiki,
    compute_doc_diff_size,
    discover_org_repos,
    dry_run,
    fetch_latest_release_notes,
    fetch_org_repos_raw,
    fetch_repo_readme,
    get_default_branch_head_sha,
    is_changed_since_last_run,
    is_doc_relevant_path,
    load_repo_state,
    parse_repo,
    save_repo_state,
)


# ── Fixture raw repo payloads ──────────────────────────────────────────────


def _raw_repo(**overrides) -> dict:
    """Build a raw GitHub org-repos API repo dict with sane defaults."""
    base = {
        "name": "example-repo",
        "full_name": "Twingate/example-repo",
        "html_url": "https://github.com/Twingate/example-repo",
        "default_branch": "main",
        "pushed_at": "2024-06-01T00:00:00Z",
        "fork": False,
        "archived": False,
        "disabled": False,
        "size": 1200,
        "description": "An example Twingate repo",
        "topics": ["ztna"],
        "language": "Go",
        "has_wiki": False,
    }
    base.update(overrides)
    return base


# A fork that must be hard-excluded even though it is public and non-archived.
QUICLY_FORK_RAW = _raw_repo(
    name="quicly",
    full_name="Twingate/quicly",
    html_url="https://github.com/Twingate/quicly",
    fork=True,
    size=5000,
    language="C",
    description="QUIC transport implementation (upstream fork)",
)


# ── HTTP mock helpers ───────────────────────────────────────────────────────


def _mock_response(
    json_data=None,
    status_code: int = 200,
    headers: dict | None = None,
    links: dict | None = None,
) -> MagicMock:
    """Build a mock requests.Response for the GitHub API."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.headers = headers or {}
    mock_resp.json = MagicMock(return_value=json_data)
    mock_resp.links = links if links is not None else {}
    mock_resp.raise_for_status = MagicMock()
    return mock_resp


# ── parse_repo / discover_org_repos: fork exclusion & stub classification ──


@patch("github_repos.requests.get")
def test_discover_org_repos_excludes_forks(mock_get: MagicMock) -> None:
    """A fork (modeled on Twingate/quicly) is excluded from kept repos."""
    kept_raw = _raw_repo(name="edge-relay", full_name="Twingate/edge-relay")
    mock_get.return_value = _mock_response(json_data=[QUICLY_FORK_RAW, kept_raw])

    result = discover_org_repos("Twingate")

    assert isinstance(result, OrgDiscovery)
    assert result.total_repos == 2
    assert result.forks_excluded == 1
    kept_full_names = [r.full_name for r in result.kept]
    assert "Twingate/quicly" not in kept_full_names
    assert "Twingate/edge-relay" in kept_full_names
    assert len(result.kept) == 1


@patch("github_repos.requests.get")
def test_discover_org_repos_keeps_non_fork_sibling(mock_get: MagicMock) -> None:
    """A non-fork sibling repo alongside a fork is kept, not excluded."""
    sibling_raw = _raw_repo(name="twingate-client", full_name="Twingate/twingate-client")
    mock_get.return_value = _mock_response(json_data=[QUICLY_FORK_RAW, sibling_raw])

    result = discover_org_repos("Twingate")

    kept = {r.full_name: r for r in result.kept}
    assert "Twingate/twingate-client" in kept
    assert kept["Twingate/twingate-client"].fork is False


def test_parse_repo_archived_non_fork_is_stub() -> None:
    """A non-fork repo that is archived is retained and flagged is_stub."""
    repo = parse_repo(_raw_repo(archived=True))
    assert repo.fork is False
    assert repo.is_stub is True


def test_parse_repo_disabled_non_fork_is_stub() -> None:
    """A non-fork repo that is disabled is retained and flagged is_stub."""
    repo = parse_repo(_raw_repo(disabled=True))
    assert repo.is_stub is True


def test_parse_repo_empty_non_fork_is_stub() -> None:
    """A non-fork repo with size == 0 is retained and flagged is_stub."""
    repo = parse_repo(_raw_repo(size=0))
    assert repo.is_stub is True


def test_parse_repo_normal_non_fork_is_not_stub() -> None:
    """A normal (non-archived, non-disabled, non-empty) non-fork repo is not a stub."""
    repo = parse_repo(_raw_repo())
    assert repo.is_stub is False


def test_parse_repo_fork_is_never_marked_stub_even_if_archived() -> None:
    """A fork is excluded upstream by discover_org_repos, but parse_repo itself
    never marks a fork as a stub (is_stub requires `not fork`)."""
    repo = parse_repo(_raw_repo(fork=True, archived=True))
    assert repo.fork is True
    assert repo.is_stub is False


@patch("github_repos.requests.get")
def test_discover_org_repos_stub_count_reflects_kept_stubs_only(mock_get: MagicMock) -> None:
    """stub_count counts only kept (non-fork) stub repos, ignoring forks."""
    normal_raw = _raw_repo(name="normal-repo", full_name="Twingate/normal-repo")
    archived_raw = _raw_repo(name="old-repo", full_name="Twingate/old-repo", archived=True)
    mock_get.return_value = _mock_response(
        json_data=[QUICLY_FORK_RAW, normal_raw, archived_raw]
    )

    result = discover_org_repos("Twingate")

    assert result.total_repos == 3
    assert result.forks_excluded == 1
    assert len(result.kept) == 2
    assert result.stub_count == 1


# ── fetch_org_repos_raw: pagination ─────────────────────────────────────────


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_follows_link_header_pagination(mock_get: MagicMock) -> None:
    """Both pages of a paginated org-repos response are fully consumed."""
    page1_repo = _raw_repo(name="repo-page1", full_name="Twingate/repo-page1")
    page2_repo = _raw_repo(name="repo-page2", full_name="Twingate/repo-page2")
    next_url = f"{GITHUB_API_BASE}/organizations/12345/repos?type=public&per_page=100&page=2"

    page1_response = _mock_response(
        json_data=[page1_repo], links={"next": {"url": next_url}}
    )
    page2_response = _mock_response(json_data=[page2_repo], links={})
    mock_get.side_effect = [page1_response, page2_response]

    result = fetch_org_repos_raw("Twingate")

    assert result == [page1_repo, page2_repo]
    assert mock_get.call_count == 2


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_second_request_omits_page_params(mock_get: MagicMock) -> None:
    """The paginated follow-up request does not re-send type/per_page params
    (the Link-header URL already carries its own query string)."""
    next_url = f"{GITHUB_API_BASE}/organizations/999/repos?page=2"
    page1_response = _mock_response(json_data=[], links={"next": {"url": next_url}})
    page2_response = _mock_response(json_data=[], links={})
    mock_get.side_effect = [page1_response, page2_response]

    fetch_org_repos_raw("Twingate")

    first_call, second_call = mock_get.call_args_list
    assert first_call.kwargs["params"] == {"type": "public", "per_page": "100"}
    assert second_call.kwargs["params"] is None
    assert second_call.args[0] == next_url


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_no_link_header_is_single_page(mock_get: MagicMock) -> None:
    """An empty Link header (no rel=next) stops pagination after one page."""
    mock_get.return_value = _mock_response(json_data=[_raw_repo()], links={})

    result = fetch_org_repos_raw("Twingate")

    assert len(result) == 1
    mock_get.assert_called_once()


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_sends_bearer_token_when_provided(mock_get: MagicMock) -> None:
    """A provided token is sent as an Authorization: Bearer header."""
    mock_get.return_value = _mock_response(json_data=[], links={})

    fetch_org_repos_raw("Twingate", token="ghs_testtoken123")

    sent_headers = mock_get.call_args.kwargs["headers"]
    assert sent_headers["Authorization"] == "Bearer ghs_testtoken123"


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_no_token_omits_authorization_header(mock_get: MagicMock) -> None:
    """Without a token, no Authorization header is sent (unauthenticated request)."""
    mock_get.return_value = _mock_response(json_data=[], links={})

    fetch_org_repos_raw("Twingate", token=None)

    sent_headers = mock_get.call_args.kwargs["headers"]
    assert "Authorization" not in sent_headers


# ── _github_get funnel: rate limit / 404 / network failure ────────────────


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_403_rate_limit_returns_empty_list(mock_get: MagicMock) -> None:
    """A 403 rate-limit response is handled gracefully: empty list, no raise."""
    mock_get.return_value = _mock_response(
        status_code=403, headers={"Retry-After": "60"}
    )

    result = fetch_org_repos_raw("Twingate")

    assert result == []


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_404_org_returns_empty_list(mock_get: MagicMock) -> None:
    """A 404 (org does not exist / not public) is handled gracefully."""
    mock_get.return_value = _mock_response(status_code=404)

    result = fetch_org_repos_raw("Nonexistent-Org")

    assert result == []


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_network_exception_returns_empty_list(mock_get: MagicMock) -> None:
    """A requests.RequestException (network failure) does not propagate; it is
    caught by _github_get and results in an empty (not crashed) discovery."""
    mock_get.side_effect = requests.RequestException("Connection timed out")

    result = fetch_org_repos_raw("Twingate")

    assert result == []


@patch("github_repos.requests.get")
def test_fetch_org_repos_raw_server_error_returns_empty_list(mock_get: MagicMock) -> None:
    """A non-2xx, non-403/404 status (e.g. 500) is handled via raise_for_status
    and does not propagate past _github_get."""
    error_response = _mock_response(status_code=500)
    error_response.raise_for_status.side_effect = requests.HTTPError("500 Server Error")
    mock_get.return_value = error_response

    result = fetch_org_repos_raw("Twingate")

    assert result == []


# ── Adaptive rate-limit throttle (set_rate_limit_wait / rate_limit_wait) ───


@pytest.fixture(autouse=True)
def _reset_rate_limit_wait_toggle():
    """Guarantee the module-level throttle toggle never leaks between tests."""
    yield
    github_repos.set_rate_limit_wait(False)


@patch("github_repos.time.sleep")
@patch("github_repos.requests.get")
def test_github_get_403_disabled_by_default_returns_none_no_sleep(
    mock_get: MagicMock, mock_sleep: MagicMock
) -> None:
    """With the throttle at its default (disabled), a 403 still returns None
    immediately with no sleep — the dry-run/main path is unchanged."""
    mock_get.return_value = _mock_response(
        status_code=403, headers={"X-RateLimit-Reset": str(int(time.time()) + 60)}
    )

    result = github_repos._github_get(f"{GITHUB_API_BASE}/orgs/Twingate/repos", token=None)

    assert result is None
    mock_sleep.assert_not_called()
    assert mock_get.call_count == 1


@patch("github_repos.time.sleep")
@patch("github_repos.requests.get")
def test_github_get_403_with_wait_enabled_sleeps_then_retries_and_succeeds(
    mock_get: MagicMock, mock_sleep: MagicMock
) -> None:
    """With the throttle enabled, a 403 reporting X-RateLimit-Reset causes a
    sleep-then-retry that ultimately returns the retried, successful response."""
    rate_limited = _mock_response(
        status_code=403, headers={"X-RateLimit-Reset": str(int(time.time()) + 30)}
    )
    success = _mock_response(json_data={"ok": True}, status_code=200)
    mock_get.side_effect = [rate_limited, success]

    with github_repos.rate_limit_wait():
        result = github_repos._github_get(f"{GITHUB_API_BASE}/orgs/Twingate/repos", token=None)

    assert result is success
    assert result.json() == {"ok": True}
    mock_sleep.assert_called_once()
    assert mock_get.call_count == 2


@patch("github_repos.time.sleep")
@patch("github_repos.requests.get")
def test_github_get_403_retry_after_header_honored_when_enabled(
    mock_get: MagicMock, mock_sleep: MagicMock
) -> None:
    """Retry-After (relative seconds) is honored the same way as
    X-RateLimit-Reset, and the sleep duration reflects it (plus margin/jitter)."""
    rate_limited = _mock_response(status_code=403, headers={"Retry-After": "5"})
    success = _mock_response(json_data={"ok": True}, status_code=200)
    mock_get.side_effect = [rate_limited, success]

    with github_repos.rate_limit_wait():
        result = github_repos._github_get(f"{GITHUB_API_BASE}/orgs/Twingate/repos", token=None)

    assert result is success
    mock_sleep.assert_called_once()
    slept_seconds = mock_sleep.call_args.args[0]
    assert slept_seconds >= 5.0


@patch("github_repos.time.sleep")
@patch("github_repos.requests.get")
def test_github_get_proactive_pacing_sleeps_on_exhausted_2xx_when_enabled(
    mock_get: MagicMock, mock_sleep: MagicMock
) -> None:
    """A successful (2xx) response reporting X-RateLimit-Remaining: 0 triggers
    a proactive pacing sleep, before the next call, when the throttle is
    enabled."""
    exhausted_success = _mock_response(
        json_data={"ok": True},
        status_code=200,
        headers={
            "X-RateLimit-Remaining": "0",
            "X-RateLimit-Reset": str(int(time.time()) + 15),
        },
    )
    mock_get.return_value = exhausted_success

    with github_repos.rate_limit_wait():
        result = github_repos._github_get(f"{GITHUB_API_BASE}/orgs/Twingate/repos", token=None)

    assert result is exhausted_success
    mock_sleep.assert_called_once()


@patch("github_repos.time.sleep")
@patch("github_repos.requests.get")
def test_github_get_proactive_pacing_disabled_by_default(
    mock_get: MagicMock, mock_sleep: MagicMock
) -> None:
    """The same exhausted 2xx response does NOT sleep when the throttle is
    disabled (the default) — the dry-run/main path is unaffected."""
    exhausted_success = _mock_response(
        json_data={"ok": True},
        status_code=200,
        headers={
            "X-RateLimit-Remaining": "0",
            "X-RateLimit-Reset": str(int(time.time()) + 15),
        },
    )
    mock_get.return_value = exhausted_success

    result = github_repos._github_get(f"{GITHUB_API_BASE}/orgs/Twingate/repos", token=None)

    assert result is exhausted_success
    mock_sleep.assert_not_called()


@patch("github_repos.time.sleep")
@patch("github_repos.requests.get")
def test_github_get_bounded_wait_gives_up_after_cap(
    mock_get: MagicMock, mock_sleep: MagicMock
) -> None:
    """If the rate limit persists past _MAX_RATE_LIMIT_WAITS, _github_get
    returns None rather than looping forever."""
    always_limited = _mock_response(
        status_code=403, headers={"X-RateLimit-Reset": str(int(time.time()) + 5)}
    )
    mock_get.return_value = always_limited

    with github_repos.rate_limit_wait():
        result = github_repos._github_get(f"{GITHUB_API_BASE}/orgs/Twingate/repos", token=None)

    assert result is None
    # One initial request plus one retry per allowed wait.
    assert mock_get.call_count == 1 + github_repos._MAX_RATE_LIMIT_WAITS
    assert mock_sleep.call_count == github_repos._MAX_RATE_LIMIT_WAITS


def test_rate_limit_wait_context_manager_restores_previous_state() -> None:
    """rate_limit_wait() restores the toggle to whatever it was before the
    block on exit, including when the block raises."""
    assert github_repos._rate_limit_wait_enabled is False

    with github_repos.rate_limit_wait():
        assert github_repos._rate_limit_wait_enabled is True
    assert github_repos._rate_limit_wait_enabled is False

    github_repos.set_rate_limit_wait(True)
    with pytest.raises(ValueError):
        with github_repos.rate_limit_wait():
            raise ValueError("boom")
    assert github_repos._rate_limit_wait_enabled is True

    # Restore the module-global toggle before leaving this test.
    github_repos.set_rate_limit_wait(False)
    assert github_repos._rate_limit_wait_enabled is False


# ── is_changed_since_last_run: pushed_at gate ───────────────────────────────


def test_is_changed_since_last_run_new_repo_with_no_state_entry_is_changed() -> None:
    """A repo with no entry in state at all is treated as new/changed."""
    repo = parse_repo(_raw_repo(full_name="Twingate/brand-new", pushed_at="2024-06-01T00:00:00Z"))
    assert is_changed_since_last_run(repo, state={}) is True


def test_is_changed_since_last_run_newer_pushed_at_is_changed() -> None:
    """A repo whose pushed_at is newer than the recorded state is changed."""
    repo = parse_repo(_raw_repo(full_name="Twingate/advanced", pushed_at="2024-08-01T00:00:00Z"))
    state = {"Twingate/advanced": {"last_sha": "abc123", "pushed_at": "2024-06-01T00:00:00Z"}}

    assert is_changed_since_last_run(repo, state) is True


def test_is_changed_since_last_run_equal_pushed_at_is_not_changed() -> None:
    """A repo whose pushed_at exactly matches the recorded state is not changed."""
    repo = parse_repo(_raw_repo(full_name="Twingate/stable", pushed_at="2024-06-01T00:00:00Z"))
    state = {"Twingate/stable": {"last_sha": "abc123", "pushed_at": "2024-06-01T00:00:00Z"}}

    assert is_changed_since_last_run(repo, state) is False


def test_is_changed_since_last_run_older_pushed_at_is_not_changed() -> None:
    """A repo whose pushed_at is older than the recorded state is not changed."""
    repo = parse_repo(_raw_repo(full_name="Twingate/stale", pushed_at="2024-01-01T00:00:00Z"))
    state = {"Twingate/stale": {"last_sha": "abc123", "pushed_at": "2024-06-01T00:00:00Z"}}

    assert is_changed_since_last_run(repo, state) is False


def test_is_changed_since_last_run_missing_recorded_pushed_at_is_changed() -> None:
    """A state entry that exists but has no pushed_at recorded is treated as changed."""
    repo = parse_repo(_raw_repo(full_name="Twingate/legacy-entry"))
    state = {"Twingate/legacy-entry": {"last_sha": "abc123"}}

    assert is_changed_since_last_run(repo, state) is True


# ── load_repo_state / save_repo_state ───────────────────────────────────────


def test_load_repo_state_missing_file_returns_empty_dict(tmp_path) -> None:
    """Loading state from a path that does not exist returns {} rather than raising."""
    result = load_repo_state(path=tmp_path / ".repo_state.json")
    assert result == {}


def test_save_and_load_repo_state_round_trip(tmp_path) -> None:
    """State saved to disk can be loaded back unchanged."""
    path = tmp_path / ".repo_state.json"
    state = {"Twingate/example-repo": {"last_sha": "deadbeef", "pushed_at": "2024-06-01T00:00:00Z"}}

    save_repo_state(state, path=path)
    result = load_repo_state(path=path)

    assert result == state


# ── is_doc_relevant_path ────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "path,expected",
    [
        ("README.md", True),
        ("docs/x.rst", True),
        ("CHANGELOG.md", True),
        ("x.mdx", True),
        ("src/main.go", False),
        ("main.py", False),
    ],
)
def test_is_doc_relevant_path_matrix(path: str, expected: bool) -> None:
    """is_doc_relevant_path classifies each representative path correctly."""
    assert is_doc_relevant_path(path) is expected


def test_is_doc_relevant_path_nested_docs_directory_matches() -> None:
    """Any path with a docs/ directory segment (not just top-level) matches."""
    assert is_doc_relevant_path("packages/server/docs/guide.txt") is True


def test_is_doc_relevant_path_release_notes_style_filename_matches() -> None:
    """RELEASE*-style filenames count as doc-relevant (release notes)."""
    assert is_doc_relevant_path("RELEASE-NOTES.txt") is True


def test_is_doc_relevant_path_lowercase_readme_matches() -> None:
    """README matching is case-insensitive."""
    assert is_doc_relevant_path("readme.rst") is True


def test_is_doc_relevant_path_source_in_docs_named_directory_is_not_fooled() -> None:
    """A filename merely containing 'docs' as a substring (not a path segment)
    is not treated as doc-relevant."""
    assert is_doc_relevant_path("src/docstore.go") is False


# ── compute_doc_diff_size ───────────────────────────────────────────────────


@patch("github_repos.requests.get")
def test_compute_doc_diff_size_filters_to_doc_paths_only(mock_get: MagicMock) -> None:
    """A compare payload mixing source and doc files yields only doc paths."""
    compare_payload = {
        "files": [
            {"filename": "src/foo.go", "changes": 40, "patch": "x" * 100},
            {"filename": "docs/bar.md", "changes": 10, "patch": "y" * 50},
            {"filename": "README.md", "changes": 3, "patch": "z" * 20},
        ]
    }
    mock_get.return_value = _mock_response(json_data=compare_payload)

    result = compute_doc_diff_size("Twingate", "example-repo", "base123", "head456")

    assert isinstance(result, DiffSizing)
    assert set(result.filtered_files) == {"docs/bar.md", "README.md"}
    assert "src/foo.go" not in result.filtered_files
    assert result.filtered_file_count == 2
    assert result.filtered_line_changes == 13
    assert result.filtered_patch_bytes == 70
    assert result.is_first_run is False


@patch("github_repos.requests.get")
def test_compute_doc_diff_size_falls_back_to_additions_plus_deletions(
    mock_get: MagicMock,
) -> None:
    """When a file entry has no 'changes' key, additions + deletions is used."""
    compare_payload = {
        "files": [
            {"filename": "docs/new.md", "additions": 7, "deletions": 2, "patch": ""},
        ]
    }
    mock_get.return_value = _mock_response(json_data=compare_payload)

    result = compute_doc_diff_size("Twingate", "example-repo", "base123", "head456")

    assert result.filtered_line_changes == 9


@patch("github_repos.requests.get")
def test_compute_doc_diff_size_first_run_makes_no_compare_call(mock_get: MagicMock) -> None:
    """base_sha=None (new repo) short-circuits: is_first_run True, zero fields,
    and no compare HTTP request is ever made."""
    result = compute_doc_diff_size(
        "Twingate", "example-repo", base_sha=None, head_sha="head456"
    )

    assert result.is_first_run is True
    assert result.filtered_files == ()
    assert result.filtered_file_count == 0
    assert result.filtered_line_changes == 0
    assert result.filtered_patch_bytes == 0
    mock_get.assert_not_called()


@patch("github_repos.requests.get")
def test_compute_doc_diff_size_failed_compare_request_yields_empty_diff(
    mock_get: MagicMock,
) -> None:
    """A failed compare request (e.g. 404) yields an empty (not crashed) diff."""
    mock_get.return_value = _mock_response(status_code=404)

    result = compute_doc_diff_size("Twingate", "example-repo", "base123", "head456")

    assert result.is_first_run is False
    assert result.filtered_file_count == 0


# ── get_default_branch_head_sha: branches -> commits fallback ──────────────


@patch("github_repos.requests.get")
def test_get_default_branch_head_sha_uses_branches_endpoint(mock_get: MagicMock) -> None:
    """The branches endpoint's commit.sha is used when it succeeds."""
    mock_get.return_value = _mock_response(json_data={"commit": {"sha": "branchsha111"}})

    result = get_default_branch_head_sha("Twingate", "example-repo", "main")

    assert result == "branchsha111"
    mock_get.assert_called_once()


@patch("github_repos.requests.get")
def test_get_default_branch_head_sha_falls_back_to_commits_endpoint(
    mock_get: MagicMock,
) -> None:
    """When the branches endpoint fails, the commits endpoint is tried next."""
    branches_404 = _mock_response(status_code=404)
    commits_ok = _mock_response(json_data={"sha": "fallbacksha999"})
    mock_get.side_effect = [branches_404, commits_ok]

    result = get_default_branch_head_sha("Twingate", "example-repo", "main")

    assert result == "fallbacksha999"
    assert mock_get.call_count == 2


@patch("github_repos.requests.get")
def test_get_default_branch_head_sha_both_endpoints_fail_returns_none(
    mock_get: MagicMock,
) -> None:
    """When both the branches and commits endpoints fail, None is returned."""
    mock_get.return_value = _mock_response(status_code=404)

    result = get_default_branch_head_sha("Twingate", "example-repo", "main")

    assert result is None


# ── dry_run: zero LLM calls, end-to-end aggregation ─────────────────────────


def _dry_run_dispatch(url, params=None, timeout=None, headers=None):
    """Route a mocked requests.get call to a canned response by URL shape."""
    if "/orgs/" in url and url.endswith("/repos"):
        org = url.split("/orgs/")[1].split("/repos")[0]
        return _mock_response(json_data=_ORG_REPOS_FIXTURE[org], links={})
    if "/branches/" in url:
        return _mock_response(json_data={"commit": {"sha": "newsha000"}})
    if "/compare/" in url:
        return _mock_response(
            json_data={
                "files": [
                    {"filename": "docs/changed.md", "changes": 5, "patch": "abcde"},
                    {"filename": "src/main.go", "changes": 99, "patch": "z" * 500},
                ]
            }
        )
    raise AssertionError(f"Unexpected URL requested in dry_run: {url}")


_ORG_REPOS_FIXTURE = {
    "OrgA": [
        _raw_repo(
            name="repo-new",
            full_name="OrgA/repo-new",
            pushed_at="2024-07-01T00:00:00Z",
            has_wiki=True,
        ),
        _raw_repo(
            name="repo-unchanged",
            full_name="OrgA/repo-unchanged",
            pushed_at="2024-06-01T00:00:00Z",
        ),
    ],
    "OrgB": [
        _raw_repo(
            name="repo-updated",
            full_name="OrgB/repo-updated",
            pushed_at="2024-08-01T00:00:00Z",
        ),
    ],
}

_DRY_RUN_STATE = {
    "OrgA/repo-unchanged": {"last_sha": "somesha", "pushed_at": "2024-06-01T00:00:00Z"},
    "OrgB/repo-updated": {"last_sha": "oldsha111", "pushed_at": "2024-01-01T00:00:00Z"},
}


def _make_org_listing_only_dispatch(org_repos: dict):
    """Build a requests.get side_effect that permits ONLY /orgs/{org}/repos
    listing calls, failing the test on any /branches/, /commits/, or /compare/ request."""

    def _dispatch(url, params=None, timeout=None, headers=None):
        if "/orgs/" in url and url.endswith("/repos"):
            org = url.split("/orgs/")[1].split("/repos")[0]
            return _mock_response(json_data=org_repos[org], links={})
        raise AssertionError(
            f"Unexpected per-repo URL requested on a first-run dry_run "
            f"(branches/commits/compare must not be called): {url}"
        )

    return _dispatch


@patch("github_repos.requests.get")
def test_dry_run_aggregates_counts_across_orgs(mock_get: MagicMock) -> None:
    """dry_run aggregates per-org discovery, the pushed_at gate, and diff
    sizing into correct grand totals, across a small fake multi-org set."""
    mock_get.side_effect = _dry_run_dispatch

    result = dry_run(orgs=("OrgA", "OrgB"), token="tok", state=_DRY_RUN_STATE)

    assert result.total_public_repos == 3
    assert result.total_forks_excluded == 0
    assert result.total_kept == 3
    assert result.total_stub == 0
    # repo-new (no state) and repo-updated (newer pushed_at) changed; repo-unchanged did not.
    assert result.changed_count == 2
    assert result.wiki_count == 1

    sizings_by_repo = {d.full_name: d for d in result.diff_sizings}
    # repo-new is first run: no head SHA resolved, no compare call.
    assert sizings_by_repo["OrgA/repo-new"].is_first_run is True
    assert sizings_by_repo["OrgA/repo-new"].base_sha is None
    assert sizings_by_repo["OrgA/repo-new"].head_sha is None
    assert sizings_by_repo["OrgA/repo-new"].filtered_file_count == 0
    # repo-updated has a recorded last_sha: head SHA resolved and compare called.
    assert sizings_by_repo["OrgB/repo-updated"].is_first_run is False
    assert sizings_by_repo["OrgB/repo-updated"].base_sha == "oldsha111"
    assert sizings_by_repo["OrgB/repo-updated"].head_sha == "newsha000"
    assert sizings_by_repo["OrgB/repo-updated"].filtered_file_count == 1
    assert sizings_by_repo["OrgB/repo-updated"].filtered_files == ("docs/changed.md",)

    # 4 requests: 2 org-listing + 1 branches + 1 compare (repo-updated only).
    assert mock_get.call_count == 4


@patch("github_repos.requests.get")
def test_dry_run_makes_zero_anthropic_calls(mock_get: MagicMock, monkeypatch) -> None:
    """dry_run makes zero LLM calls: it succeeds even when importing 'anthropic' would fail."""
    mock_get.side_effect = _dry_run_dispatch
    # Poison the import: any `import anthropic` in the call path would raise here.
    monkeypatch.setitem(sys.modules, "anthropic", None)

    result = dry_run(orgs=("OrgA", "OrgB"), token="tok", state=_DRY_RUN_STATE)

    assert result.total_kept == 3
    assert result.changed_count == 2
    assert not hasattr(github_repos, "anthropic")


@patch("github_repos.requests.get")
def test_dry_run_unauthenticated_flag_reflects_missing_token(
    mock_get: MagicMock, monkeypatch
) -> None:
    """When no token is passed and GITHUB_TOKEN is unset, the result is
    flagged unauthenticated."""
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    mock_get.side_effect = _dry_run_dispatch

    result = dry_run(orgs=("OrgA", "OrgB"), token=None, state=_DRY_RUN_STATE)

    assert result.unauthenticated is True


@patch("github_repos.requests.get")
def test_dry_run_default_empty_state_treats_full_corpus_as_changed(
    mock_get: MagicMock,
) -> None:
    """With state=None, every kept repo is changed and first-run: only org-listing calls."""
    mock_get.side_effect = _make_org_listing_only_dispatch(_ORG_REPOS_FIXTURE)

    result = dry_run(orgs=("OrgA", "OrgB"), token="tok", state=None)

    assert result.changed_count == result.total_kept == 3
    assert len(result.diff_sizings) == 3
    assert all(d.is_first_run for d in result.diff_sizings)
    assert all(d.head_sha is None for d in result.diff_sizings)
    assert mock_get.call_count == 2


# ── dry_run: first-run/empty-baseline makes ONLY org-listing calls ─────────


_FIRST_RUN_ORG_REPOS = {
    "OrgC": [
        _raw_repo(name="repo-c1", full_name="OrgC/repo-c1", pushed_at="2024-07-01T00:00:00Z"),
    ],
    "OrgD": [
        _raw_repo(
            name="repo-d1",
            full_name="OrgD/repo-d1",
            pushed_at="2024-07-02T00:00:00Z",
            has_wiki=True,
        ),
    ],
}


@patch("github_repos.requests.get")
def test_dry_run_first_run_makes_no_per_repo_calls(mock_get: MagicMock) -> None:
    """On a first-run dry_run, only /orgs/{org}/repos listing endpoints are hit."""
    mock_get.side_effect = _make_org_listing_only_dispatch(_FIRST_RUN_ORG_REPOS)

    result = dry_run(orgs=("OrgC", "OrgD"), token="tok", state=None)

    assert result.total_kept == 2
    assert result.changed_count == result.total_kept == 2
    assert len(result.diff_sizings) == 2
    for sizing in result.diff_sizings:
        assert sizing.is_first_run is True
        assert sizing.base_sha is None
        assert sizing.head_sha is None
        assert sizing.filtered_file_count == 0
    # Exactly 2 requests: one org-listing call per org, nothing else.
    assert mock_get.call_count == 2


# ── FilteredDiff / WikiSnapshot dataclasses ─────────────────────────────────


def test_filtered_diff_is_frozen() -> None:
    diff = FilteredDiff(text="x", file_count=1, byte_len=1)
    with pytest.raises(Exception):
        diff.text = "y"  # type: ignore[misc]


def test_wiki_snapshot_carries_head_sha_and_files() -> None:
    snapshot = WikiSnapshot(head_sha="abc123", files={"Home.md": "content"})
    assert snapshot.head_sha == "abc123"
    assert snapshot.files == {"Home.md": "content"}


# ── build_filtered_diff ──────────────────────────────────────────────────────


@patch("github_repos.requests.get")
def test_build_filtered_diff_no_base_sha_returns_empty_and_skips_request(
    mock_get: MagicMock,
) -> None:
    """base_sha=None (cold start) short-circuits: empty FilteredDiff, and
    no compare HTTP request is ever made."""
    result = build_filtered_diff("Twingate", "example-repo", base_sha=None, head_sha="head456")

    assert result == FilteredDiff(text="", file_count=0, byte_len=0)
    mock_get.assert_not_called()


@patch("github_repos.requests.get")
def test_build_filtered_diff_filters_to_doc_relevant_patches_only(mock_get: MagicMock) -> None:
    """Only doc-relevant files' patches end up concatenated into .text, each
    preceded by a '--- {filename} ---' marker; non-doc files are excluded."""
    compare_payload = {
        "files": [
            {"filename": "src/foo.go", "patch": "source code patch, should be excluded"},
            {"filename": "docs/bar.md", "patch": "doc patch content"},
            {"filename": "README.md", "patch": "readme patch content"},
        ]
    }
    mock_get.return_value = _mock_response(json_data=compare_payload)

    result = build_filtered_diff("Twingate", "example-repo", "base123", "head456")

    assert isinstance(result, FilteredDiff)
    assert "source code patch, should be excluded" not in result.text
    assert "--- docs/bar.md ---\ndoc patch content" in result.text
    assert "--- README.md ---\nreadme patch content" in result.text
    assert result.file_count == 2
    assert result.byte_len == len(result.text.encode("utf-8"))


@patch("github_repos.requests.get")
def test_build_filtered_diff_failed_compare_returns_empty(mock_get: MagicMock) -> None:
    mock_get.return_value = _mock_response(status_code=404)

    result = build_filtered_diff("Twingate", "example-repo", "base123", "head456")

    assert result == FilteredDiff(text="", file_count=0, byte_len=0)


# ── fetch_repo_readme ────────────────────────────────────────────────────────


@patch("github_repos.requests.get")
def test_fetch_repo_readme_happy_path_returns_raw_text(mock_get: MagicMock) -> None:
    response = _mock_response(status_code=200)
    response.text = "# Example Repo\n\nSome README content."
    mock_get.return_value = response

    result = fetch_repo_readme("Twingate", "example-repo")

    assert result == "# Example Repo\n\nSome README content."
    sent_headers = mock_get.call_args.kwargs["headers"]
    assert sent_headers["Accept"] == "application/vnd.github.raw+json"


@patch("github_repos.requests.get")
def test_fetch_repo_readme_not_found_returns_none(mock_get: MagicMock) -> None:
    mock_get.return_value = _mock_response(status_code=404)

    result = fetch_repo_readme("Twingate", "no-readme-repo")

    assert result is None


# ── fetch_latest_release_notes ───────────────────────────────────────────────


@patch("github_repos.requests.get")
def test_fetch_latest_release_notes_happy_path_returns_body(mock_get: MagicMock) -> None:
    mock_get.return_value = _mock_response(json_data={"body": "## v1.2.3\n\nRelease notes here."})

    result = fetch_latest_release_notes("Twingate", "example-repo")

    assert result == "## v1.2.3\n\nRelease notes here."


@patch("github_repos.requests.get")
def test_fetch_latest_release_notes_404_returns_none(mock_get: MagicMock) -> None:
    mock_get.return_value = _mock_response(status_code=404)

    result = fetch_latest_release_notes("Twingate", "no-releases-repo")

    assert result is None


@patch("github_repos.requests.get")
def test_fetch_latest_release_notes_empty_body_returns_none(mock_get: MagicMock) -> None:
    mock_get.return_value = _mock_response(json_data={"body": ""})

    result = fetch_latest_release_notes("Twingate", "example-repo")

    assert result is None


@patch("github_repos.requests.get")
def test_fetch_latest_release_notes_missing_body_key_returns_none(mock_get: MagicMock) -> None:
    mock_get.return_value = _mock_response(json_data={})

    result = fetch_latest_release_notes("Twingate", "example-repo")

    assert result is None


# ── _wiki_clone_url ──────────────────────────────────────────────────────────


def test_wiki_clone_url_rejects_org_outside_default_orgs() -> None:
    with pytest.raises(ValueError, match="DEFAULT_ORGS"):
        _wiki_clone_url("Some-Random-Org", "example-repo")


def test_wiki_clone_url_builds_expected_url_for_known_org() -> None:
    assert "Twingate" in DEFAULT_ORGS  # sanity: this org is really in the allowlist
    url = _wiki_clone_url("Twingate", "example-repo")
    assert url == "https://github.com/Twingate/example-repo.wiki.git"


# ── clone_wiki ───────────────────────────────────────────────────────────────


def _mock_run(returncode: int = 0, stdout: str = "", stderr: str = "") -> MagicMock:
    """Build a mock subprocess.CompletedProcess-like result."""
    result = MagicMock()
    result.returncode = returncode
    result.stdout = stdout
    result.stderr = stderr
    return result


@patch("github_repos.subprocess.run")
def test_clone_wiki_clone_failure_returns_none(mock_run: MagicMock, tmp_path) -> None:
    """A nonzero exit from git clone is treated as an empty/disabled wiki,
    not an error."""
    mock_run.return_value = _mock_run(returncode=1, stderr="repository not found")

    result = clone_wiki("Twingate", "example-repo", tmp_path)

    assert result is None
    mock_run.assert_called_once()


@patch("github_repos.subprocess.run")
def test_clone_wiki_no_markdown_files_returns_none(mock_run: MagicMock, tmp_path) -> None:
    """Clone succeeds (mocked) but the destination has no *.md files."""
    mock_run.return_value = _mock_run(returncode=0)

    result = clone_wiki("Twingate", "example-repo", tmp_path)

    assert result is None
    # Only the clone call is made; rev-parse HEAD is never reached.
    mock_run.assert_called_once()


@patch("github_repos.subprocess.run")
def test_clone_wiki_with_markdown_files_returns_populated_snapshot(
    mock_run: MagicMock, tmp_path
) -> None:
    """Clone succeeds and the destination (pre-populated here in place of a
    real clone) has markdown files: a populated WikiSnapshot is returned
    with the resolved HEAD sha and every file's real content."""
    (tmp_path / "Home.md").write_text("# Home\n\nWelcome.", encoding="utf-8")
    (tmp_path / "Setup.md").write_text("# Setup\n\nInstructions.", encoding="utf-8")
    mock_run.side_effect = [
        _mock_run(returncode=0),  # git clone
        _mock_run(returncode=0, stdout="deadbeef1234\n"),  # git rev-parse HEAD
    ]

    result = clone_wiki("Twingate", "example-repo", tmp_path)

    assert isinstance(result, WikiSnapshot)
    assert result.head_sha == "deadbeef1234"
    assert result.files == {
        "Home.md": "# Home\n\nWelcome.",
        "Setup.md": "# Setup\n\nInstructions.",
    }
    assert mock_run.call_count == 2


@patch("github_repos.subprocess.run")
def test_clone_wiki_rev_parse_failure_returns_none(mock_run: MagicMock, tmp_path) -> None:
    """Markdown files exist, but resolving HEAD fails — treated as empty."""
    (tmp_path / "Home.md").write_text("content", encoding="utf-8")
    mock_run.side_effect = [
        _mock_run(returncode=0),  # git clone
        _mock_run(returncode=1, stderr="fatal: not a git repository"),  # rev-parse fails
    ]

    result = clone_wiki("Twingate", "example-repo", tmp_path)

    assert result is None


def test_clone_wiki_rejects_org_outside_default_orgs_before_any_subprocess_call(tmp_path) -> None:
    """The org allowlist check happens before subprocess ever runs."""
    with (
        patch("github_repos.subprocess.run") as mock_run,
        pytest.raises(ValueError, match="DEFAULT_ORGS"),
    ):
        clone_wiki("Some-Random-Org", "example-repo", tmp_path)
    mock_run.assert_not_called()


# ── build_wiki_diff ──────────────────────────────────────────────────────────


@patch("github_repos.subprocess.run")
def test_build_wiki_diff_no_base_sha_returns_empty_without_subprocess(
    mock_run: MagicMock, tmp_path
) -> None:
    result = build_wiki_diff(tmp_path, base_sha=None)

    assert result == FilteredDiff(text="", file_count=0, byte_len=0)
    mock_run.assert_not_called()


@patch("github_repos.subprocess.run")
def test_build_wiki_diff_base_sha_absent_from_clone_falls_back_to_empty(
    mock_run: MagicMock, tmp_path
) -> None:
    """cat-file -e reports the base sha is not present in this clone's
    history: falls back to an empty diff (caller does a full summarize)."""
    mock_run.return_value = _mock_run(returncode=1, stderr="fatal: Not a valid object name")

    result = build_wiki_diff(tmp_path, base_sha="missingsha123")

    assert result == FilteredDiff(text="", file_count=0, byte_len=0)
    mock_run.assert_called_once()


@patch("github_repos.subprocess.run")
def test_build_wiki_diff_success_returns_populated_diff(mock_run: MagicMock, tmp_path) -> None:
    diff_text = (
        "diff --git a/Home.md b/Home.md\n"
        "+added line\n"
        "diff --git a/Setup.md b/Setup.md\n"
        "+another added line\n"
    )
    mock_run.side_effect = [
        _mock_run(returncode=0),  # cat-file -e succeeds (base present)
        _mock_run(returncode=0, stdout=diff_text),  # git diff succeeds
    ]

    result = build_wiki_diff(tmp_path, base_sha="basesha000")

    assert isinstance(result, FilteredDiff)
    assert result.text == diff_text
    assert result.file_count == 2  # two "diff --git" occurrences
    assert result.byte_len == len(diff_text.encode("utf-8"))
    assert mock_run.call_count == 2


@patch("github_repos.subprocess.run")
def test_build_wiki_diff_diff_command_failure_returns_empty(mock_run: MagicMock, tmp_path) -> None:
    mock_run.side_effect = [
        _mock_run(returncode=0),  # cat-file -e succeeds
        _mock_run(returncode=1, stderr="fatal: bad revision"),  # git diff fails
    ]

    result = build_wiki_diff(tmp_path, base_sha="basesha000")

    assert result == FilteredDiff(text="", file_count=0, byte_len=0)
