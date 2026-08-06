"""Discover Twingate GitHub repos and size the doc-relevant diff since last run."""

from __future__ import annotations

import argparse
import json
import logging
import os
import random
import statistics
import subprocess
import sys
import time
from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, cast

import requests

from url_safety import REQUEST_HEADERS, _is_safe_url

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
METRICS_DIR = PROJECT_ROOT / "docs" / "metrics"
DRY_RUN_REPORT_PATH = METRICS_DIR / "github-dry-run.md"
REPO_STATE_PATH = SCRIPTS_DIR / ".repo_state.json"

GITHUB_API_BASE = "https://api.github.com"
GITHUB_API_VERSION = "2022-11-28"
REQUEST_TIMEOUT_SECONDS = 30

# GitHub-specific headers merged on top of the shared pipeline User-Agent.
GITHUB_API_HEADERS: dict[str, str] = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": GITHUB_API_VERSION,
}

# The four Twingate orgs this pipeline source covers.
DEFAULT_ORGS: tuple[str, ...] = (
    "Twingate",
    "Twingate-Solutions",
    "Twingate-Labs",
    "Twingate-Community",
)

# Filename extensions treated as doc-relevant for compare-diff sizing.
_DOC_EXTENSIONS: tuple[str, ...] = (".md", ".mdx", ".rst")


@dataclass(frozen=True)
class RepoInfo:
    """A single public repo as discovered from the GitHub org repos endpoint.

    ``is_stub`` marks a non-fork repo that is archived, disabled, or empty
    (``size == 0``).
    """

    name: str
    full_name: str
    html_url: str
    default_branch: str
    pushed_at: str
    fork: bool
    archived: bool
    disabled: bool
    size: int
    description: str | None
    topics: tuple[str, ...]
    language: str | None
    has_wiki: bool
    is_stub: bool


@dataclass(frozen=True)
class OrgDiscovery:
    """Discovery result for one org: raw counts plus the kept (non-fork) repos."""

    org: str
    total_repos: int
    forks_excluded: int
    kept: tuple[RepoInfo, ...]
    stub_count: int


@dataclass(frozen=True)
class DiffSizing:
    """Doc-relevant compare-diff size for one repo since its recorded state.

    ``is_first_run`` is True when there was no recorded ``last_sha`` to diff
    against; the ``filtered_*`` fields are then left at zero.
    """

    full_name: str
    base_sha: str | None
    head_sha: str | None
    filtered_files: tuple[str, ...]
    filtered_file_count: int
    filtered_line_changes: int
    filtered_patch_bytes: int
    is_first_run: bool
    has_wiki: bool


@dataclass(frozen=True)
class DryRunResult:
    """Structured output of :func:`dry_run`."""

    generated_at: str
    unauthenticated: bool
    org_results: tuple[OrgDiscovery, ...]
    total_public_repos: int
    total_forks_excluded: int
    total_kept: int
    total_stub: int
    changed_count: int
    diff_sizings: tuple[DiffSizing, ...]
    wiki_count: int


def _build_headers(token: str | None) -> dict[str, str]:
    """Merge the shared pipeline User-Agent with GitHub API headers and auth.

    Args:
        token: A GitHub token (``GITHUB_TOKEN``), or ``None`` for an
            unauthenticated request.

    Returns:
        A header dict ready to pass to ``requests.get``.
    """
    headers = {**REQUEST_HEADERS, **GITHUB_API_HEADERS}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


# Adaptive rate-limit throttle (opt-in, module-level toggle).
_rate_limit_wait_enabled = False

_MAX_RATE_LIMIT_WAITS = 3
_MAX_SINGLE_SLEEP_SECONDS = 3600.0  # 1 hour
_RATE_LIMIT_MARGIN_SECONDS = 2.0
_RATE_LIMIT_JITTER_SECONDS = 5.0


def set_rate_limit_wait(enabled: bool) -> None:
    """Enable or disable the adaptive rate-limit throttle in ``_github_get``.

    Args:
        enabled: ``True`` to make ``_github_get`` block-and-retry on rate
            limits (bounded); ``False`` to log and give up.
    """
    global _rate_limit_wait_enabled
    _rate_limit_wait_enabled = enabled


@contextmanager
def rate_limit_wait() -> Iterator[None]:
    """Enable the adaptive rate-limit throttle for the duration of a ``with`` block.

    Restores the previous toggle value on exit.
    """
    previous = _rate_limit_wait_enabled
    set_rate_limit_wait(True)
    try:
        yield
    finally:
        set_rate_limit_wait(previous)


def _response_now_epoch(response: requests.Response) -> float:
    """Resolve "now" (epoch seconds), preferring the response's ``Date`` header.

    Args:
        response: The ``requests.Response`` to read the ``Date`` header from.

    Returns:
        An epoch-seconds float, falling back to ``time.time()``.
    """
    date_header = response.headers.get("Date")
    if date_header:
        try:
            parsed = parsedate_to_datetime(date_header)
        except (TypeError, ValueError, IndexError):
            parsed = None
        if parsed is not None:
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.timestamp()
    return time.time()


def _resolve_wait_seconds(response: requests.Response) -> float:
    """Compute how long to wait for a rate-limit window to reset, from response headers.

    Prefers ``Retry-After``; falls back to ``X-RateLimit-Reset``.

    Args:
        response: The rate-limited (403) or exhausted (2xx with
            ``X-RateLimit-Remaining: 0``) response.

    Returns:
        Seconds to wait (uncapped, no jitter/margin), or ``0.0`` if neither
        header is present or parseable.
    """
    retry_after = response.headers.get("Retry-After")
    if retry_after is not None:
        try:
            return max(float(retry_after), 0.0)
        except ValueError:
            logger.debug("Could not parse Retry-After header: %r", retry_after)

    reset_epoch = response.headers.get("X-RateLimit-Reset")
    if reset_epoch is not None:
        try:
            reset_ts = float(reset_epoch)
        except ValueError:
            logger.debug("Could not parse X-RateLimit-Reset header: %r", reset_epoch)
            return 0.0
        return max(reset_ts - _response_now_epoch(response), 0.0)

    return 0.0


def _sleep_for_rate_limit(url: str, response: requests.Response, *, reason: str) -> None:
    """Sleep until a rate-limit window resets (capped), with jitter/margin.

    Args:
        url: The URL that was rate-limited/exhausted (for the log message).
        response: The response carrying the rate-limit headers.
        reason: Short label for the log message (``"rate-limited"`` or
            ``"proactive pacing"``).
    """
    wait_seconds = min(_resolve_wait_seconds(response), _MAX_SINGLE_SLEEP_SECONDS)
    wait_seconds += _RATE_LIMIT_MARGIN_SECONDS + random.uniform(0, _RATE_LIMIT_JITTER_SECONDS)
    logger.info(
        "GitHub API %s for %s; sleeping %.1fs for the rate-limit window to reset "
        "(adaptive throttle enabled).",
        reason,
        url,
        wait_seconds,
    )
    time.sleep(wait_seconds)


def _handle_rate_limit(url: str, response: requests.Response) -> None:
    """Log a 403 rate-limit response without blocking the caller.

    Args:
        url: The URL that was rate-limited (for the log message).
        response: The 403 response from ``requests``.
    """
    retry_after = response.headers.get("Retry-After")
    reset_epoch = response.headers.get("X-RateLimit-Reset")
    if retry_after is not None:
        logger.warning(
            "GitHub API rate-limited for %s (Retry-After=%ss); giving up on this "
            "request for this sizing pass rather than blocking.",
            url,
            retry_after,
        )
    elif reset_epoch is not None:
        logger.warning(
            "GitHub API rate-limited for %s (X-RateLimit-Reset=%s epoch); giving "
            "up on this request for this sizing pass rather than blocking.",
            url,
            reset_epoch,
        )
    else:
        logger.warning(
            "GitHub API rate-limited (403) for %s with no Retry-After/"
            "X-RateLimit-Reset header.",
            url,
        )


def _github_get(
    url: str,
    token: str | None,
    *,
    params: dict[str, str] | None = None,
    extra_headers: dict[str, str] | None = None,
) -> requests.Response | None:
    """Perform a validated GET against the GitHub API.

    Validates ``url`` against ``url_safety._is_safe_url`` before fetching.
    All failure paths log and return ``None`` rather than raising.

    Args:
        url: Full URL to request.
        token: A GitHub token, or ``None`` for an unauthenticated request.
        params: Optional query parameters (ignored when ``url`` already
            carries its own query string).
        extra_headers: Optional headers merged on top of the default
            GitHub API headers (e.g. overriding ``Accept`` for raw content).

    Returns:
        The ``requests.Response`` on a 2xx result, or ``None`` on any
        disallowed URL, network failure, 404, other non-2xx status, or a
        403 that persists past the throttle's wait cap.
    """
    if not _is_safe_url(url):
        logger.warning("Refusing to fetch disallowed URL: %s", url)
        return None

    headers = _build_headers(token)
    if extra_headers:
        headers.update(extra_headers)

    waits_used = 0
    while True:
        try:
            response = requests.get(
                url, params=params, timeout=REQUEST_TIMEOUT_SECONDS, headers=headers
            )
        except requests.RequestException as exc:
            logger.warning("GitHub API request failed for %s: %s", url, exc)
            return None

        if response.status_code == 403:
            if _rate_limit_wait_enabled and waits_used < _MAX_RATE_LIMIT_WAITS:
                waits_used += 1
                _sleep_for_rate_limit(url, response, reason="rate-limited (403)")
                continue
            _handle_rate_limit(url, response)
            return None
        if response.status_code == 404:
            logger.warning("GitHub API 404 for %s", url)
            return None

        try:
            response.raise_for_status()
        except requests.RequestException as exc:
            logger.warning("GitHub API error for %s: %s", url, exc)
            return None

        if _rate_limit_wait_enabled:
            remaining = response.headers.get("X-RateLimit-Remaining")
            if remaining is not None:
                try:
                    remaining_exhausted = int(remaining) <= 0
                except ValueError:
                    remaining_exhausted = False
                if remaining_exhausted:
                    _sleep_for_rate_limit(url, response, reason="rate limit exhausted")

        return response


def fetch_org_repos_raw(org: str, token: str | None = None) -> list[dict[str, Any]]:
    """Fetch every public repo for an org, following ``Link``-header pagination.

    Args:
        org: GitHub organization login (e.g. ``"Twingate"``).
        token: A GitHub token from ``GITHUB_TOKEN``, or ``None`` for an
            unauthenticated request.

    Returns:
        A list of raw repo JSON dicts. Empty if the org 404s or every page
        request fails.
    """
    url = f"{GITHUB_API_BASE}/orgs/{org}/repos"
    params: dict[str, str] | None = {"type": "public", "per_page": "100"}
    results: list[dict[str, Any]] = []
    page_count = 0

    while url:
        response = _github_get(url, token, params=params)
        if response is None:
            logger.warning(
                "Stopping pagination for org %s after a failed request (page %d)",
                org,
                page_count + 1,
            )
            break
        page = cast(list[dict[str, Any]], response.json())
        results.extend(page)
        page_count += 1
        # The "next" URL carries its own query string; do not reapply params.
        url = response.links.get("next", {}).get("url", "")
        params = None

    logger.info(
        "Fetched %d repo(s) for org %s across %d page(s)", len(results), org, page_count
    )
    return results


def parse_repo(raw: dict[str, Any]) -> RepoInfo:
    """Convert a raw GitHub repo JSON dict into a :class:`RepoInfo`.

    Args:
        raw: A single repo object from the GitHub org repos API response.

    Returns:
        The parsed :class:`RepoInfo`, with ``is_stub`` computed as
        ``not fork and (archived or disabled or size == 0)``.
    """
    fork = bool(raw.get("fork", False))
    archived = bool(raw.get("archived", False))
    disabled = bool(raw.get("disabled", False))
    size = int(raw.get("size", 0) or 0)
    is_stub = (not fork) and (archived or disabled or size == 0)

    return RepoInfo(
        name=raw["name"],
        full_name=raw["full_name"],
        html_url=raw["html_url"],
        default_branch=raw.get("default_branch") or "main",
        pushed_at=raw.get("pushed_at") or "",
        fork=fork,
        archived=archived,
        disabled=disabled,
        size=size,
        description=raw.get("description"),
        topics=tuple(raw.get("topics", []) or []),
        language=raw.get("language"),
        has_wiki=bool(raw.get("has_wiki", False)),
        is_stub=is_stub,
    )


def discover_org_repos(org: str, token: str | None = None) -> OrgDiscovery:
    """Discover, filter, and classify all public repos for one org.

    Excludes forks and marks archived/disabled/empty repos as stub candidates
    without dropping them.

    Args:
        org: GitHub organization login (e.g. ``"Twingate"``).
        token: A GitHub token from ``GITHUB_TOKEN``, or ``None``.

    Returns:
        An :class:`OrgDiscovery` with the raw total, fork-exclusion count,
        the kept (non-fork) repos, and how many of those are stubs.
    """
    raw_repos = fetch_org_repos_raw(org, token)
    total = len(raw_repos)
    kept: list[RepoInfo] = []
    forks_excluded = 0

    for raw in raw_repos:
        repo = parse_repo(raw)
        if repo.fork:
            forks_excluded += 1
            logger.info(
                "Skipping fork: %s (excluded — not a Twingate release)", repo.full_name
            )
            continue
        kept.append(repo)
        if repo.is_stub:
            reasons = []
            if repo.archived:
                reasons.append("archived")
            if repo.disabled:
                reasons.append("disabled")
            if repo.size == 0:
                reasons.append("empty")
            logger.info(
                "Marking %s as a stub candidate (%s)", repo.full_name, ", ".join(reasons)
            )

    stub_count = sum(1 for r in kept if r.is_stub)
    logger.info(
        "Org %s: %d total public, %d forks excluded, %d kept, %d stub candidate(s)",
        org,
        total,
        forks_excluded,
        len(kept),
        stub_count,
    )
    return OrgDiscovery(
        org=org,
        total_repos=total,
        forks_excluded=forks_excluded,
        kept=tuple(kept),
        stub_count=stub_count,
    )


def load_repo_state(path: Path = REPO_STATE_PATH) -> dict[str, dict[str, Any]]:
    """Load the persisted per-repo state cache from disk.

    Maps a repo's ``full_name`` to a dict carrying (at least) ``last_sha``,
    ``doc_path``, ``wiki_last_sha``, and ``pushed_at``.

    Args:
        path: Filesystem path to the JSON state file.

    Returns:
        A dict mapping ``full_name`` to its state dict. Returns an empty
        dict if the file does not exist.
    """
    if not path.exists():
        logger.debug("Repo state not found at %s, starting fresh", path)
        return {}
    logger.debug("Loading repo state from %s", path)
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)  # type: ignore[no-any-return]


def save_repo_state(state: dict[str, dict[str, Any]], path: Path = REPO_STATE_PATH) -> None:
    """Persist the per-repo state cache to disk.

    Args:
        state: Dict mapping repo ``full_name`` to its state dict.
        path: Filesystem path to write the JSON file.
    """
    logger.debug("Saving repo state to %s (%d entries)", path, len(state))
    with path.open("w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True)


def is_changed_since_last_run(repo: RepoInfo, state: dict[str, dict[str, Any]]) -> bool:
    """Return True if a repo looks changed since the last recorded run.

    A repo is "changed" if it has no state entry (new repo) or its
    ``pushed_at`` is newer than the ``pushed_at`` recorded in its state entry.

    Args:
        repo: The repo to check.
        state: The loaded per-repo state cache (``full_name`` -> state dict).

    Returns:
        True if the repo is new or has a newer ``pushed_at`` than recorded.
    """
    entry = state.get(repo.full_name)
    if entry is None:
        return True
    recorded_pushed_at = entry.get("pushed_at")
    if not recorded_pushed_at:
        return True
    # ISO-8601 UTC timestamps compare correctly as plain strings.
    return repo.pushed_at > recorded_pushed_at


def get_default_branch_head_sha(
    org: str,
    repo: str,
    default_branch: str,
    token: str | None = None,
) -> str | None:
    """Resolve the current head commit SHA of a repo's default branch.

    Tries the branches endpoint first, falling back to the commits endpoint.

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).
        default_branch: The repo's default branch name.
        token: A GitHub token, or ``None``.

    Returns:
        The head commit SHA string, or ``None`` if both endpoints fail.
    """
    branches_url = f"{GITHUB_API_BASE}/repos/{org}/{repo}/branches/{default_branch}"
    response = _github_get(branches_url, token)
    if response is not None:
        data = cast(dict[str, Any], response.json())
        sha = data.get("commit", {}).get("sha")
        if sha:
            return cast(str, sha)

    commits_url = f"{GITHUB_API_BASE}/repos/{org}/{repo}/commits/{default_branch}"
    response = _github_get(commits_url, token)
    if response is None:
        return None
    data = cast(dict[str, Any], response.json())
    sha = data.get("sha")
    return cast(str, sha) if sha else None


def is_doc_relevant_path(path: str) -> bool:
    """Return True if a changed file path is doc-relevant for diff sizing.

    Matches ``README*``, ``.md``/``.mdx``/``.rst`` extensions, any path with a
    ``docs/`` segment, or ``CHANGELOG*``/``RELEASE*`` filenames (all
    case-insensitive).

    Args:
        path: A file path from a GitHub compare-diff ``files[].filename``.

    Returns:
        True if the path should count toward the filtered doc-diff size.
    """
    segments = path.split("/")
    filename_lower = segments[-1].lower()

    if filename_lower.startswith("readme"):
        return True
    if any(filename_lower.endswith(ext) for ext in _DOC_EXTENSIONS):
        return True
    if filename_lower.startswith("changelog") or filename_lower.startswith("release"):
        return True
    if any(segment.lower() == "docs" for segment in segments[:-1]):
        return True
    return False


def compute_doc_diff_size(
    org: str,
    repo: str,
    base_sha: str | None,
    head_sha: str,
    *,
    has_wiki: bool = False,
    token: str | None = None,
) -> DiffSizing:
    """Size the doc-relevant portion of the diff between two commits.

    Filters the compare ``files[]`` to doc-relevant paths and sums line
    ``changes`` and ``patch`` byte length. When ``base_sha`` is ``None`` no
    compare call is made and a first-run sizing is returned.

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).
        base_sha: The previously-recorded default-branch head SHA, or
            ``None`` if there is no prior state for this repo.
        head_sha: The current default-branch head SHA.
        has_wiki: Whether the repo has a wiki enabled.
        token: A GitHub token, or ``None``.

    Returns:
        A :class:`DiffSizing` describing the filtered file list and sizes.
        On a failed or first-run compare, the filtered fields are all zero.
    """
    full_name = f"{org}/{repo}"

    if base_sha is None:
        logger.info(
            "%s: no recorded last_sha, treating as new (no compare call made)",
            full_name,
        )
        return DiffSizing(
            full_name=full_name,
            base_sha=None,
            head_sha=head_sha,
            filtered_files=(),
            filtered_file_count=0,
            filtered_line_changes=0,
            filtered_patch_bytes=0,
            is_first_run=True,
            has_wiki=has_wiki,
        )

    compare_url = f"{GITHUB_API_BASE}/repos/{org}/{repo}/compare/{base_sha}...{head_sha}"
    response = _github_get(compare_url, token)
    if response is None:
        logger.warning("%s: compare request failed; treating doc-diff as empty", full_name)
        return DiffSizing(
            full_name=full_name,
            base_sha=base_sha,
            head_sha=head_sha,
            filtered_files=(),
            filtered_file_count=0,
            filtered_line_changes=0,
            filtered_patch_bytes=0,
            is_first_run=False,
            has_wiki=has_wiki,
        )

    data = cast(dict[str, Any], response.json())
    files = cast(list[dict[str, Any]], data.get("files", []) or [])
    filtered = _filter_compare_files(files)

    filtered_files: list[str] = []
    line_changes = 0
    patch_bytes = 0
    for file_entry in filtered:
        filename = cast(str, file_entry.get("filename", ""))
        filtered_files.append(filename)
        changes = file_entry.get("changes")
        if changes is None:
            changes = int(file_entry.get("additions", 0)) + int(file_entry.get("deletions", 0))
        line_changes += int(changes)
        patch_bytes += len(file_entry.get("patch", "") or "")

    logger.info(
        "%s: compare %s...%s -> %d doc-relevant file(s), %d line change(s), %d patch byte(s)",
        full_name,
        base_sha[:8],
        head_sha[:8],
        len(filtered_files),
        line_changes,
        patch_bytes,
    )
    return DiffSizing(
        full_name=full_name,
        base_sha=base_sha,
        head_sha=head_sha,
        filtered_files=tuple(filtered_files),
        filtered_file_count=len(filtered_files),
        filtered_line_changes=line_changes,
        filtered_patch_bytes=patch_bytes,
        is_first_run=False,
        has_wiki=has_wiki,
    )


@dataclass(frozen=True)
class FilteredDiff:
    """Concatenated doc-relevant patch TEXT for one repo/wiki compare.

    ``text`` is empty when there is nothing to diff against (no prior SHA, a
    failed compare, or a wiki base SHA absent from the clone).
    """

    text: str
    file_count: int
    byte_len: int


@dataclass(frozen=True)
class WikiSnapshot:
    """A freshly-cloned wiki's markdown corpus at a point in time.

    ``files`` maps each ``*.md`` file's path (relative to the clone root) to
    its text content.
    """

    head_sha: str
    files: dict[str, str]


def _filter_compare_files(files: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return only the doc-relevant entries from a compare-diff ``files[]`` list.

    Args:
        files: The raw ``files[]`` array from a GitHub compare-diff response.

    Returns:
        The subset of ``files`` whose ``filename`` is doc-relevant per
        :func:`is_doc_relevant_path`.
    """
    return [
        file_entry
        for file_entry in files
        if file_entry.get("filename") and is_doc_relevant_path(cast(str, file_entry["filename"]))
    ]


def build_filtered_diff(
    org: str,
    repo: str,
    base_sha: str | None,
    head_sha: str,
    *,
    token: str | None = None,
) -> FilteredDiff:
    """Build the concatenated doc-relevant patch TEXT for a repo compare.

    When ``base_sha`` is ``None`` no compare call is made and an empty
    :class:`FilteredDiff` is returned.

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).
        base_sha: Previously-recorded default-branch head SHA, or ``None``.
        head_sha: Current default-branch head SHA.
        token: A GitHub token, or ``None``.

    Returns:
        A :class:`FilteredDiff` with the concatenated patch text (each file
        preceded by a ``--- {filename} ---`` marker), the doc-relevant file
        count, and the UTF-8 byte length of ``text``. Empty (all zero/blank)
        if ``base_sha`` is ``None`` or the compare request fails.
    """
    full_name = f"{org}/{repo}"

    if base_sha is None:
        logger.info(
            "%s: no recorded last_sha, cannot build a delta diff (full summarize instead)",
            full_name,
        )
        return FilteredDiff(text="", file_count=0, byte_len=0)

    compare_url = f"{GITHUB_API_BASE}/repos/{org}/{repo}/compare/{base_sha}...{head_sha}"
    response = _github_get(compare_url, token)
    if response is None:
        logger.warning("%s: compare request failed; filtered diff is empty", full_name)
        return FilteredDiff(text="", file_count=0, byte_len=0)

    data = cast(dict[str, Any], response.json())
    files = cast(list[dict[str, Any]], data.get("files", []) or [])
    filtered = _filter_compare_files(files)

    chunks: list[str] = []
    for file_entry in filtered:
        filename = cast(str, file_entry.get("filename", ""))
        patch = cast(str, file_entry.get("patch", "") or "")
        chunks.append(f"--- {filename} ---\n{patch}")

    text = "\n\n".join(chunks)
    logger.info(
        "%s: built filtered diff %s...%s -> %d doc-relevant file(s), %d byte(s)",
        full_name,
        base_sha[:8],
        head_sha[:8],
        len(filtered),
        len(text.encode("utf-8")),
    )
    return FilteredDiff(text=text, file_count=len(filtered), byte_len=len(text.encode("utf-8")))


def fetch_repo_readme(org: str, repo: str, token: str | None = None) -> str | None:
    """Fetch a repo's README as raw markdown text.

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).
        token: A GitHub token, or ``None``.

    Returns:
        The README's raw text content, or ``None`` if the repo has no
        README (404) or the request otherwise fails.
    """
    url = f"{GITHUB_API_BASE}/repos/{org}/{repo}/readme"
    response = _github_get(
        url, token, extra_headers={"Accept": "application/vnd.github.raw+json"}
    )
    if response is None:
        return None
    return response.text


def fetch_latest_release_notes(org: str, repo: str, token: str | None = None) -> str | None:
    """Fetch the notes body of a repo's latest release, if any.

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).
        token: A GitHub token, or ``None``.

    Returns:
        The release body markdown, or ``None`` if the repo has no releases
        (404), the body is empty, or the request fails.
    """
    url = f"{GITHUB_API_BASE}/repos/{org}/{repo}/releases/latest"
    response = _github_get(url, token)
    if response is None:
        return None
    data = cast(dict[str, Any], response.json())
    body = data.get("body")
    return cast(str, body) if body else None


def _wiki_clone_url(org: str, repo: str) -> str:
    """Build a repo's wiki git-clone URL, constraining ``org`` to :data:`DEFAULT_ORGS`.

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).

    Returns:
        The ``https://github.com/{org}/{repo}.wiki.git`` clone URL.

    Raises:
        ValueError: If ``org`` is not one of :data:`DEFAULT_ORGS`.
    """
    if org not in DEFAULT_ORGS:
        raise ValueError(f"Refusing to clone a wiki for org outside DEFAULT_ORGS: {org}")
    return f"https://github.com/{org}/{repo}.wiki.git"


def clone_wiki(org: str, repo: str, dest: Path) -> WikiSnapshot | None:
    """Clone a repo's wiki and read its markdown files.

    Does a full clone so a later ``git diff`` against a recorded base SHA
    stays reliable. Returns ``None`` when the wiki is empty or unreachable.

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).
        dest: An existing, empty directory to clone into; the caller owns
            its lifecycle.

    Returns:
        A :class:`WikiSnapshot` with the resolved HEAD SHA and every
        ``*.md`` file's content, or ``None`` if the wiki is empty, disabled,
        or unreachable.
    """
    clone_url = _wiki_clone_url(org, repo)
    full_name = f"{org}/{repo}"

    try:
        clone_result = subprocess.run(
            ["git", "clone", "--quiet", clone_url, str(dest)],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        logger.info(
            "%s: wiki clone could not be started (%s); treating as empty/disabled",
            full_name,
            exc,
        )
        return None

    if clone_result.returncode != 0:
        logger.info(
            "%s: wiki clone failed (exit %d) — likely an empty or disabled wiki, "
            "not an error: %s",
            full_name,
            clone_result.returncode,
            clone_result.stderr.strip(),
        )
        return None

    md_files = sorted(dest.rglob("*.md"))
    if not md_files:
        logger.info("%s: wiki cloned but contains no .md files; treating as empty", full_name)
        return None

    head_result = subprocess.run(
        ["git", "-C", str(dest), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if head_result.returncode != 0:
        logger.warning(
            "%s: could not resolve wiki HEAD sha (exit %d); treating as empty",
            full_name,
            head_result.returncode,
        )
        return None
    head_sha = head_result.stdout.strip()

    files: dict[str, str] = {}
    for path in md_files:
        rel = str(path.relative_to(dest))
        try:
            files[rel] = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            logger.warning("%s: could not read wiki file %s: %s", full_name, rel, exc)

    logger.info(
        "%s: wiki cloned at %s, %d markdown file(s)", full_name, head_sha[:8], len(files)
    )
    return WikiSnapshot(head_sha=head_sha, files=files)


def build_wiki_diff(dest: Path, base_sha: str | None) -> FilteredDiff:
    """Build the ``*.md`` diff text for an already-cloned wiki, base..HEAD.

    Returns an empty :class:`FilteredDiff` when ``base_sha`` is ``None`` or is
    not present in the clone's history.

    Args:
        dest: Path to an already-cloned wiki working tree.
        base_sha: Previously-recorded wiki HEAD SHA, or ``None``.

    Returns:
        A :class:`FilteredDiff` over the wiki's markdown changes, or an
        empty one signaling "fall back to full summarize".
    """
    if base_sha is None:
        return FilteredDiff(text="", file_count=0, byte_len=0)

    verify_result = subprocess.run(
        ["git", "-C", str(dest), "cat-file", "-e", base_sha],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if verify_result.returncode != 0:
        logger.info(
            "Wiki base sha %s not present in this clone; falling back to full summarize",
            base_sha[:8],
        )
        return FilteredDiff(text="", file_count=0, byte_len=0)

    diff_result = subprocess.run(
        ["git", "-C", str(dest), "diff", f"{base_sha}..HEAD", "--", "*.md"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if diff_result.returncode != 0:
        logger.warning(
            "Wiki git diff failed (exit %d): %s",
            diff_result.returncode,
            diff_result.stderr.strip(),
        )
        return FilteredDiff(text="", file_count=0, byte_len=0)

    text = diff_result.stdout
    file_count = text.count("diff --git")
    return FilteredDiff(text=text, file_count=file_count, byte_len=len(text.encode("utf-8")))


def dry_run(
    orgs: Sequence[str] = DEFAULT_ORGS,
    token: str | None = None,
    state: dict[str, dict[str, Any]] | None = None,
) -> DryRunResult:
    """Run discovery, the pushed_at gate, and compare-diff sizing.

    For each kept repo flagged as changed: if it has a recorded base SHA in
    ``state``, resolve the head SHA and size the doc-relevant diff; otherwise
    record a first-run sizing directly with no per-repo API call.

    Args:
        orgs: Org logins to scan. Defaults to :data:`DEFAULT_ORGS`.
        token: A GitHub token, or ``None`` to read ``GITHUB_TOKEN`` from the
            environment (falling back to unauthenticated if unset).
        state: Per-repo state to gate against. ``None`` means an empty
            baseline (first-run semantics); pass :func:`load_repo_state`'s
            result to gate against the real persisted state instead.

    Returns:
        A :class:`DryRunResult` with per-org and grand-total counts, the
        changed-repo count, per-repo diff sizings, and the wiki count.
    """
    if token is None:
        token = os.environ.get("GITHUB_TOKEN")
    if not token:
        logger.info(
            "GITHUB_TOKEN not set; using unauthenticated public GitHub API "
            "requests (60 req/hr limit). A first-run dry-run stays within this "
            "budget because it makes only org-listing calls — no per-repo "
            "head-SHA or diff calls (see the first-run branch below)."
        )

    effective_state = state if state is not None else {}

    org_results: list[OrgDiscovery] = []
    diff_sizings: list[DiffSizing] = []
    changed_count = 0
    wiki_count = 0

    for org in orgs:
        org_result = discover_org_repos(org, token)
        org_results.append(org_result)

        for repo in org_result.kept:
            if repo.has_wiki:
                wiki_count += 1

            if not is_changed_since_last_run(repo, effective_state):
                logger.info("%s: unchanged since last run, skipping diff sizing", repo.full_name)
                continue

            changed_count += 1
            base_sha = effective_state.get(repo.full_name, {}).get("last_sha")

            if base_sha is None:
                # No base to diff against: record a first-run sizing without
                # a per-repo API call.
                diff_sizings.append(
                    DiffSizing(
                        full_name=repo.full_name,
                        base_sha=None,
                        head_sha=None,
                        filtered_files=(),
                        filtered_file_count=0,
                        filtered_line_changes=0,
                        filtered_patch_bytes=0,
                        is_first_run=True,
                        has_wiki=repo.has_wiki,
                    )
                )
                continue

            head_sha = get_default_branch_head_sha(
                org, repo.name, repo.default_branch, token
            )
            if head_sha is None:
                logger.warning(
                    "%s: could not resolve default-branch head SHA; skipping diff sizing",
                    repo.full_name,
                )
                continue

            sizing = compute_doc_diff_size(
                org, repo.name, base_sha, head_sha, has_wiki=repo.has_wiki, token=token
            )
            diff_sizings.append(sizing)

    total_public_repos = sum(r.total_repos for r in org_results)
    total_forks_excluded = sum(r.forks_excluded for r in org_results)
    total_kept = sum(len(r.kept) for r in org_results)
    total_stub = sum(r.stub_count for r in org_results)

    logger.info(
        "Dry-run complete: %d total public repos, %d forks excluded, %d kept, "
        "%d stub, %d changed since baseline, %d with a wiki",
        total_public_repos,
        total_forks_excluded,
        total_kept,
        total_stub,
        changed_count,
        wiki_count,
    )

    return DryRunResult(
        generated_at=datetime.now(timezone.utc).isoformat(),
        unauthenticated=not bool(token),
        org_results=tuple(org_results),
        total_public_repos=total_public_repos,
        total_forks_excluded=total_forks_excluded,
        total_kept=total_kept,
        total_stub=total_stub,
        changed_count=changed_count,
        diff_sizings=tuple(diff_sizings),
        wiki_count=wiki_count,
    )


def _size_bucket_label(patch_bytes: int) -> str:
    """Classify a filtered patch-byte size into a display bucket label.

    Args:
        patch_bytes: ``filtered_patch_bytes`` for one repo's diff sizing.

    Returns:
        A human-readable bucket label.
    """
    if patch_bytes == 0:
        return "0 bytes (empty)"
    if patch_bytes < 1_000:
        return "1 B - 1 KB"
    if patch_bytes < 10_000:
        return "1 KB - 10 KB"
    if patch_bytes < 100_000:
        return "10 KB - 100 KB"
    return "> 100 KB"


def render_dry_run_report(result: DryRunResult) -> str:
    """Render a :class:`DryRunResult` as the ``docs/metrics/github-dry-run.md`` report.

    Args:
        result: The structured dry-run output from :func:`dry_run`.

    Returns:
        A markdown document as a string.
    """
    lines: list[str] = []
    lines.append("# GitHub Discovery Dry-Run — Cost/Time Sizing Report")
    lines.append("")
    lines.append(f"Generated at: {result.generated_at}")
    if result.unauthenticated:
        lines.append("")
        lines.append(
            "> **Unauthenticated run** — no `GITHUB_TOKEN`. This source is token-free "
            "by design: all repos and pages here are public, so a token is never "
            "required. A first-run sizing pass makes only the four org-listing "
            "calls (no per-repo diff calls), which stays well within the 60 req/hr "
            "unauthenticated limit — this is the supported way to run it, and this "
            "dry-run/sizing pass deliberately does not enable the adaptive "
            "rate-limit throttle (it stays fast and log-and-give-up on a 403). If a "
            "future run does diff against recorded state and 403s more than "
            "expected, that throttle is available (see `rate_limit_wait()`), and a "
            "present `GITHUB_TOKEN` is still picked up automatically as an optional "
            "speed-up; check the run log for any 403 WARNING lines if counts look short."
        )
    lines.append("")

    lines.append("## Per-Org Discovery")
    lines.append("")
    lines.append("| Org | Total Public Repos | Forks Excluded | Non-Fork Kept | Stub Candidates |")
    lines.append("|---|---:|---:|---:|---:|")
    for org_result in result.org_results:
        lines.append(
            f"| {org_result.org} | {org_result.total_repos} | {org_result.forks_excluded} "
            f"| {len(org_result.kept)} | {org_result.stub_count} |"
        )
    lines.append(
        f"| **Total** | **{result.total_public_repos}** | **{result.total_forks_excluded}** "
        f"| **{result.total_kept}** | **{result.total_stub}** |"
    )
    lines.append("")

    lines.append("## Change Detection")
    lines.append("")
    lines.append(
        f"- Repos changed since baseline (this run's baseline is {'empty — first run' if not result.diff_sizings or all(d.is_first_run for d in result.diff_sizings) else 'the persisted state'}): "
        f"**{result.changed_count}** of {result.total_kept} kept repos"
    )
    lines.append(f"- Repos with a wiki enabled (`has_wiki`): **{result.wiki_count}**")
    lines.append("")

    first_run_sizings = [d for d in result.diff_sizings if d.is_first_run]
    diffed_sizings = [d for d in result.diff_sizings if not d.is_first_run]

    lines.append("## Filtered Doc-Diff Size Distribution")
    lines.append("")
    if first_run_sizings:
        lines.append(
            f"- **{len(first_run_sizings)}** repo(s) had no recorded `last_sha` "
            "(new repo / first observed run) — no compare call was made for these; "
            "they are sized by presence, not diff. Their filtered size shows as 0."
        )
    if not diffed_sizings:
        lines.append(
            "- No repos had a prior recorded state to diff against, so there is no "
            "real diff-size distribution yet. Run again after `.repo_state.json` has "
            "been populated by a real run to get meaningful sizing."
        )
    else:
        sizes = [d.filtered_patch_bytes for d in diffed_sizings]
        lines.append(f"- Repos actually diffed against a prior SHA: **{len(diffed_sizings)}**")
        lines.append(f"- Filtered patch bytes — min: {min(sizes)}, median: {int(statistics.median(sizes))}, max: {max(sizes)}")
        lines.append("")
        lines.append("| Size Bucket | Repo Count |")
        lines.append("|---|---:|")
        bucket_counts: dict[str, int] = {}
        for size in sizes:
            label = _size_bucket_label(size)
            bucket_counts[label] = bucket_counts.get(label, 0) + 1
        for label in (
            "0 bytes (empty)",
            "1 B - 1 KB",
            "1 KB - 10 KB",
            "10 KB - 100 KB",
            "> 100 KB",
        ):
            if label in bucket_counts:
                lines.append(f"| {label} | {bucket_counts[label]} |")
    lines.append("")

    if result.diff_sizings:
        lines.append("## Per-Repo Detail")
        lines.append("")
        lines.append("| Repo | First Run | Doc Files Changed | Line Changes | Patch Bytes | Has Wiki |")
        lines.append("|---|---|---:|---:|---:|---|")
        for sizing in sorted(result.diff_sizings, key=lambda d: d.full_name):
            lines.append(
                f"| {sizing.full_name} | {'yes' if sizing.is_first_run else 'no'} "
                f"| {sizing.filtered_file_count} | {sizing.filtered_line_changes} "
                f"| {sizing.filtered_patch_bytes} | {'yes' if sizing.has_wiki else 'no'} |"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    """Run the dry-run sizing pass and write the markdown report to disk.

    Returns:
        Exit code ``0`` (individual repo or org failures are logged but
        never fatal).
    """
    result = dry_run()
    report = render_dry_run_report(result)
    METRICS_DIR.mkdir(parents=True, exist_ok=True)
    DRY_RUN_REPORT_PATH.write_text(report, encoding="utf-8")
    logger.info("Dry-run report written to %s", DRY_RUN_REPORT_PATH)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "GitHub repo discovery for the Twingate docs pipeline "
            "(zero-LLM-call sizing pass)."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Run discovery, the pushed_at gate, and compare-diff sizing across "
            "all four orgs against an empty baseline, and write a markdown "
            "metrics report to docs/metrics/github-dry-run.md. Makes zero "
            "LLM calls."
        ),
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    if args.dry_run:
        sys.exit(main())
    parser.print_help()
    sys.exit(0)
