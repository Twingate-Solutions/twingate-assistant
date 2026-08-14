"""Entry point that fetches, summarizes, and writes Twingate doc/repo references."""

import json
import logging
import os
import random
import re
import sys
import tempfile
import time
from collections.abc import Callable
from datetime import date, datetime, timezone
from pathlib import Path
from typing import TypeVar

# Put scripts/ on the path so sibling modules import regardless of cwd.
sys.path.insert(0, str(Path(__file__).parent))

import anthropic

from diff_docs import auto_assign, diff_docs, load_mapping
from fetch_sitemap import DEFAULT_SITEMAP_URL, fetch_sitemap
from github_repos import (
    DEFAULT_ORGS,
    FilteredDiff,
    RepoInfo,
    build_filtered_diff,
    build_wiki_diff,
    clone_wiki,
    discover_org_repos,
    fetch_latest_release_notes,
    fetch_repo_readme,
    get_default_branch_head_sha,
    is_changed_since_last_run,
    load_repo_state,
    rate_limit_wait,
    save_repo_state,
)
from github_summarize import (
    MAX_DELTA_FILES,
    SummaryResult,
    build_metrics_record,
    summarize_repo_delta,
    summarize_repo_full,
)
from pipeline_metrics import (
    NORM_HASH_CACHE_PATH,
    GitHubRunMetrics,
    RunMetrics,
    emit,
    emit_github,
    load_norm_cache,
    save_norm_cache,
)
from summarize_docs import (
    CLAUDE_MODEL,
    MAX_TEXT_LENGTH,
    build_frontmatter,
    content_hash,
    extract_text_from_html,
    fetch_doc_html,
    normalize_for_hash,
    summarize_doc,
)

T = TypeVar("T")

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
TRIAGE_DIR = SKILLS_DIR / "_triage"
HASH_CACHE_PATH = SCRIPTS_DIR / ".doc_hashes.json"

# Exponential backoff for rate-limit retries.
BACKOFF_BASE_SECONDS = 1.0
BACKOFF_MAX_SECONDS = 60.0
BACKOFF_MAX_RETRIES = 4

# Marker identifying hand-authored references the pipeline must never overwrite.
MANUAL_REFERENCE_MARKER = "manual-reference: do-not-overwrite"

DEFAULT_SOURCE_TYPE = "docs"


def is_manual_reference(path: Path) -> bool:
    """Return True if ``path`` is a hand-authored reference file.

    The marker must appear within the first 1024 characters. Read errors are
    treated as manual (True) to fail safe against overwriting.

    Args:
        path: Candidate output path in a skill's ``references/`` directory.

    Returns:
        True if the file exists and contains the marker; False otherwise.
    """
    if not path.exists():
        return False
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:1024]
    except OSError as exc:
        logger.warning("Could not read %s to check manual marker (%s); treating as manual", path, exc)
        return True
    return MANUAL_REFERENCE_MARKER in head


def check_api_health() -> bool:
    """Verify the Claude API is reachable via a minimal (max_tokens=1) call.

    Returns:
        True if the API responded successfully; False otherwise.
    """
    if not os.environ.get("ANTHROPIC_API_KEY"):
        logger.error("ANTHROPIC_API_KEY environment variable is not set")
        return False

    try:
        client = anthropic.Anthropic()
        client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=1,
            messages=[{"role": "user", "content": "ping"}],
        )
        logger.info("API health check passed")
        return True
    except anthropic.AuthenticationError as exc:
        logger.error("API authentication failed — check ANTHROPIC_API_KEY: %s", exc)
    except anthropic.APIConnectionError as exc:
        logger.error("API is unreachable (connection error): %s", exc)
    except anthropic.APIStatusError as exc:
        logger.error("API returned error status %d: %s", exc.status_code, exc)
    except Exception as exc:
        logger.error("Unexpected error during API health check: %s", exc)
    return False


def load_hash_cache(path: Path = HASH_CACHE_PATH) -> dict[str, str]:
    """Load the persisted URL-to-content-hash cache from disk.

    Args:
        path: Filesystem path to the JSON cache file.

    Returns:
        URL-to-SHA-256-hex-digest mapping; empty dict if the file is absent.
    """
    if not path.exists():
        logger.debug("Hash cache not found at %s, starting fresh", path)
        return {}
    logger.debug("Loading hash cache from %s", path)
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)  # type: ignore[no-any-return]


def save_hash_cache(cache: dict[str, str], path: Path = HASH_CACHE_PATH) -> None:
    """Persist the URL-to-content-hash cache to disk.

    Args:
        cache: Dictionary mapping URL strings to SHA-256 hex-digests.
        path: Filesystem path to write the JSON file.
    """
    logger.debug("Saving hash cache to %s (%d entries)", path, len(cache))
    with path.open("w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=2, sort_keys=True)


def url_to_slug(url: str) -> str:
    """Convert a documentation URL to a filesystem-safe filename slug.

    Uses the last non-empty path segment, restricted to ``[a-zA-Z0-9\\-_]``.
    Falls back to ``"index"`` for root-only or fully-stripped URLs.

    Args:
        url: A full documentation page URL.

    Returns:
        A filename-safe string suitable for use as a ``.md`` file stem.
    """
    parts = [p for p in url.rstrip("/").split("/") if p]
    if not parts:
        return "index"
    raw = parts[-1].replace(".", "-")
    slug = re.sub(r"[^a-zA-Z0-9\-_]", "-", raw)
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "index"


def references_dir_for_skill(skill: str) -> Path:
    """Return the ``references/`` directory path for the given skill.

    Args:
        skill: Skill directory name (e.g. ``"twingate-connectors"``).

    Returns:
        Absolute path to ``skills/{skill}/references/``.
    """
    return SKILLS_DIR / skill / "references"


def state_doc_path(doc_path: Path) -> str:
    """Return the project-relative POSIX form of a reference path for state storage.

    The stored ``doc_path`` is informational only; keeping it relative avoids
    leaking absolute local filesystem paths into the committed ``.repo_state.json``.

    Args:
        doc_path: The reference file path (absolute in normal runs).

    Returns:
        The path relative to ``PROJECT_ROOT`` with forward slashes, or the
        path's own POSIX form if it lies outside the project (e.g. under a
        test tmp dir).
    """
    try:
        return doc_path.resolve().relative_to(PROJECT_ROOT.resolve()).as_posix()
    except ValueError:
        return doc_path.as_posix()


def call_with_backoff(fn: Callable[[], T], *, label: str) -> T | None:
    """Call ``fn()`` with exponential backoff on Claude API rate-limit errors.

    Retries up to ``BACKOFF_MAX_RETRIES`` times on ``anthropic.RateLimitError``;
    other errors are logged and treated as non-retryable.

    Args:
        fn: A zero-argument callable to invoke.
        label: Identifier for the call, used only in log messages.

    Returns:
        ``fn()``'s return value, or ``None`` if retries are exhausted or a
        non-retryable error occurs.
    """
    for attempt in range(BACKOFF_MAX_RETRIES + 1):
        try:
            return fn()
        except anthropic.RateLimitError as exc:
            if attempt == BACKOFF_MAX_RETRIES:
                logger.error(
                    "Rate limit exceeded after %d retries for %s: %s",
                    BACKOFF_MAX_RETRIES,
                    label,
                    exc,
                )
                return None
            delay = min(
                BACKOFF_BASE_SECONDS * (2**attempt) + random.uniform(0, 1),
                BACKOFF_MAX_SECONDS,
            )
            logger.warning(
                "Rate limited on %s, retrying in %.1fs (attempt %d/%d)",
                label,
                delay,
                attempt + 1,
                BACKOFF_MAX_RETRIES,
            )
            time.sleep(delay)
        except anthropic.APIError as exc:
            logger.error("Claude API error for %s: %s", label, exc)
            return None
        except Exception as exc:
            logger.error("Unexpected error for %s: %s", label, exc)
            return None
    return None


def summarize_with_backoff(url: str, html: str) -> str | None:
    """Call ``summarize_doc`` with exponential backoff on rate-limit errors.

    Args:
        url: URL of the documentation page.
        html: Raw HTML content of the page.

    Returns:
        The generated markdown summary, or ``None`` if retries are exhausted
        or a non-retryable error occurs.
    """
    return call_with_backoff(lambda: summarize_doc(url, html), label=url)


def write_reference_file(
    skill: str,
    slug: str,
    content: str,
    *,
    source: str,
    type_: str,
    fetched: str,
    source_version: str,
) -> Path:
    """Write a summary to the skill's ``references/`` directory.

    Creates the directory tree if needed and prepends a provenance
    frontmatter block (see :func:`build_frontmatter`).

    Args:
        skill: Skill name (e.g. ``"twingate-connectors"``).
        slug: File stem to use (without the ``.md`` extension).
        content: Markdown summary body to write (frontmatter is prepended).
        source: Provenance URL of the source page.
        type_: Source category — ``"docs"``, ``"help"``, or ``"github"``.
        fetched: Fetch date as an ISO ``YYYY-MM-DD`` string.
        source_version: Version identifier of the source content.

    Returns:
        The absolute path of the file that was written.

    Raises:
        ValueError: If the resolved path escapes ``SKILLS_DIR``, would
            overwrite a hand-authored reference, or the frontmatter would
            contain ``MANUAL_REFERENCE_MARKER``.
    """
    refs_dir = references_dir_for_skill(skill)
    refs_dir.mkdir(parents=True, exist_ok=True)
    output_path = refs_dir / f"{slug}.md"

    # Guard against path traversal via crafted skill or slug values.
    resolved = output_path.resolve()
    if not resolved.is_relative_to(SKILLS_DIR.resolve()):
        raise ValueError(f"Output path escapes skills directory: {resolved}")

    if is_manual_reference(output_path):
        raise ValueError(f"Refusing to overwrite hand-authored reference: {resolved}")

    frontmatter = build_frontmatter(source, type_, fetched, source_version)
    if MANUAL_REFERENCE_MARKER in frontmatter:
        raise ValueError(
            f"Refusing to write frontmatter containing the manual-reference marker: {resolved}"
        )

    output_path.write_text(f"{frontmatter}\n{content}", encoding="utf-8")
    logger.info("Wrote reference file: %s", output_path)
    return output_path


def process_doc(
    url: str,
    skill: str,
    hash_cache: dict[str, str],
    stats: dict[str, int],
    triage: bool = False,
    fetched: str | None = None,
    doc_type: str = "docs",
    *,
    source_name: str = "docs",
    metrics: RunMetrics | None = None,
    norm_cache: dict[str, str] | None = None,
) -> None:
    """Fetch, hash-check, summarize, and write one documentation page.

    Modifies ``hash_cache``, ``norm_cache``, and ``stats`` in-place. Never
    raises; failures are logged and counted in ``stats["failed"]``. ``metrics``
    is observation-only; ``norm_cache`` gates the skip decision (a normalized-hash
    match means only the volatile footer changed, so the page is skipped).

    Args:
        url: Documentation page URL to process.
        skill: Target skill directory name. Ignored when ``triage=True``.
        hash_cache: Mutable URL-to-hash dictionary; updated on success.
        stats: Mutable counters (``updated`` / ``skipped`` / ``failed``).
        triage: When ``True``, write to ``_triage/`` instead of the skill's
            ``references/`` directory.
        fetched: ISO ``YYYY-MM-DD`` fetch date for the frontmatter; defaults
            to today when ``None``.
        doc_type: Frontmatter ``type`` field — ``"docs"``, ``"help"``, or
            ``"github"``.
        source_name: Source name used to tag recorded metrics.
        metrics: Optional churn-attribution accumulator (observation only).
        norm_cache: URL-to-normalized-hash cache; gates the skip decision so
            footer-only ("Last updated … ago") changes don't force a re-summarize.
    """
    resolved_fetched = fetched if fetched is not None else date.today().isoformat()
    slug = url_to_slug(url)

    if triage or not skill:
        output_path = TRIAGE_DIR / f"{slug}.md"
    else:
        output_path = references_dir_for_skill(skill) / f"{slug}.md"

    if is_manual_reference(output_path):
        logger.warning(
            "Skipping %s: output %s is a hand-authored reference (slug collision?)",
            url,
            output_path,
        )
        stats["skipped"] += 1
        if metrics is not None:
            metrics.record(source_name, "manual_skipped")
        return

    html = fetch_doc_html(url)
    if html is None:
        logger.warning("Skipping %s: fetch failed", url)
        stats["failed"] += 1
        if metrics is not None:
            metrics.record(source_name, "fetch_fail")
        return
    if metrics is not None:
        metrics.record(source_name, "fetched_ok")

    # Skip if the page is unchanged and the file exists. Two independent signals
    # each count as "unchanged":
    #   * raw hash matches       -> the extracted text is byte-for-byte identical.
    #   * normalized hash matches -> only the volatile "Last updated … ago" footer
    #     moved (see normalize_for_hash); the substantive content is unchanged.
    # The normalized signal is the important one: without it the entire corpus
    # re-summarizes every run as the relative-age footer ticks over between runs.
    # On a skip we deliberately do NOT rewrite hash_cache[url] to the new raw hash
    # — doing so would make .doc_hashes.json churn every run (the footer always
    # differs) and defeat idempotency. norm_cache is refreshed (a no-op when the
    # normalized hash already matched).
    text = extract_text_from_html(html)
    current_hash = content_hash(text)
    norm_hash = content_hash(normalize_for_hash(text))
    prev_norm = norm_cache.get(url) if norm_cache is not None else None
    raw_unchanged = hash_cache.get(url) == current_hash
    norm_unchanged = prev_norm is not None and prev_norm == norm_hash
    if (raw_unchanged or norm_unchanged) and output_path.exists():
        logger.info("Content unchanged for %s, skipping", url)
        stats["skipped"] += 1
        if metrics is not None:
            metrics.record(source_name, "skipped")
        if norm_cache is not None:
            norm_cache[url] = norm_hash
        return

    # Re-summarizing. Classify footer-noise vs real edit for metrics. Post-fix this
    # should be real_change for ~everything reaching here; a nonzero noise_only now
    # means a footer-only change slipped the skip (e.g. the file was missing).
    is_noise_only = prev_norm is not None and prev_norm == norm_hash
    if metrics is not None:
        metrics.record(source_name, "resummarized")
        metrics.record(source_name, "noise_only" if is_noise_only else "real_change")

    summary = summarize_with_backoff(url, html)
    if summary is None:
        stats["failed"] += 1
        return

    source_version = current_hash
    if triage or not skill:
        TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
        resolved = output_path.resolve()
        if not resolved.is_relative_to(TRIAGE_DIR.resolve()):
            raise ValueError(f"Triage output path escapes triage directory: {resolved}")
        frontmatter = build_frontmatter(url, doc_type, resolved_fetched, source_version)
        if MANUAL_REFERENCE_MARKER in frontmatter:
            raise ValueError(
                f"Refusing to write triage frontmatter containing the manual-reference marker: {resolved}"
            )
        triage_content = f"{frontmatter}\n<!-- triage: unassigned -->\n\n{summary}"
        output_path.write_text(triage_content, encoding="utf-8")
        logger.info("Wrote triage file: %s", output_path)
        if metrics is not None:
            metrics.record(source_name, "triaged")
    else:
        write_reference_file(
            skill,
            slug,
            summary,
            source=url,
            type_=doc_type,
            fetched=resolved_fetched,
            source_version=source_version,
        )

    hash_cache[url] = current_hash
    if norm_cache is not None:
        norm_cache[url] = norm_hash
    stats["updated"] += 1


def load_sources(mapping: dict) -> list[dict]:
    """Return the list of doc sources declared in the mapping.

    Each source is a dict with ``name``, ``sitemap_url``, ``path_filter``,
    and ``type`` keys. When no ``sources:`` key is present, synthesises a
    single docs source from :data:`DEFAULT_SITEMAP_URL`.

    Args:
        mapping: The parsed ``doc_mapping.yaml`` document.

    Returns:
        A non-empty list of source descriptor dicts.
    """
    sources = mapping.get("sources")
    if not sources:
        logger.info("No 'sources' key in mapping; falling back to single docs source")
        return [
            {
                "name": "docs",
                "sitemap_url": DEFAULT_SITEMAP_URL,
                "path_filter": "/docs/",
                "type": DEFAULT_SOURCE_TYPE,
            }
        ]
    return sources


def process_new_urls(
    new_urls: list[str],
    patterns: list[dict],
    hash_cache: dict[str, str],
    stats: dict[str, int],
    *,
    fetched: str,
    doc_type: str,
    source_name: str = "docs",
    metrics: RunMetrics | None = None,
    norm_cache: dict[str, str] | None = None,
) -> None:
    """Auto-assign and process newly discovered URLs for one source.

    Each URL is routed to a skill via :func:`auto_assign`, or to ``_triage/``
    if no pattern matches.

    Args:
        new_urls: URLs present in the source's sitemap but not yet mapped.
        patterns: Auto-assign patterns (substring → skill), first match wins.
        hash_cache: Mutable URL-to-hash dictionary; updated in-place.
        stats: Mutable counters (``updated`` / ``skipped`` / ``failed``).
        fetched: ISO ``YYYY-MM-DD`` fetch date for the frontmatter.
        doc_type: The source's ``type`` tag (``docs`` / ``help`` / ...).
        source_name: Source name used to tag observation metrics.
        metrics: Optional churn-attribution accumulator (observation only).
        norm_cache: Optional shadow-hash cache (observation only).
    """
    for url in new_urls:
        assigned_skill = auto_assign(url, patterns) or ""
        if assigned_skill:
            logger.info("Auto-assigned new doc %s -> %s", url, assigned_skill)
            process_doc(
                url,
                assigned_skill,
                hash_cache,
                stats,
                fetched=fetched,
                doc_type=doc_type,
                source_name=source_name,
                metrics=metrics,
                norm_cache=norm_cache,
            )
        else:
            logger.warning("No auto-assign match for %s, routing to triage", url)
            process_doc(
                url,
                "",
                hash_cache,
                stats,
                triage=True,
                fetched=fetched,
                doc_type=doc_type,
                source_name=source_name,
                metrics=metrics,
                norm_cache=norm_cache,
            )


def _safe_slug_component(value: str) -> str:
    """Sanitize one slug component, stripping anything outside ``[a-zA-Z0-9\\-_]``.

    Args:
        value: A single component (e.g. an org or repo name).

    Returns:
        The sanitized component.
    """
    slug = re.sub(r"[^a-zA-Z0-9\-_]", "-", value.replace(".", "-"))
    return re.sub(r"-{2,}", "-", slug).strip("-")


def github_repo_slug(org: str, repo: str) -> str:
    """Build the ``gh-{org}-{repo}`` reference-file slug (lowercased, sanitized).

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).

    Returns:
        The slug, e.g. ``"gh-twingate-terraform-provider-twingate"``.
    """
    return f"gh-{_safe_slug_component(org.lower())}-{_safe_slug_component(repo.lower())}"


def github_wiki_slug(org: str, repo: str) -> str:
    """Build the ``gh-{org}-{repo}-wiki`` reference-file slug (lowercased, sanitized).

    Args:
        org: GitHub organization login.
        repo: Repo name (not ``full_name``).

    Returns:
        The slug, e.g. ``"gh-twingate-kubernetes-operator-wiki"``.
    """
    return f"{github_repo_slug(org, repo)}-wiki"


def choose_github_mode(
    *,
    has_prior_doc: bool,
    filtered_byte_len: int,
    filtered_file_count: int,
) -> str:
    """Pick ``"full"`` or ``"delta"`` summarization mode for a repo or wiki.

    Returns ``"full"`` when there is no prior doc, or when the diff exceeds
    ``MAX_TEXT_LENGTH`` bytes or :data:`github_summarize.MAX_DELTA_FILES`
    files; otherwise ``"delta"``.

    Args:
        has_prior_doc: Whether an existing reference file body was found.
        filtered_byte_len: UTF-8 byte length of the filtered diff text.
        filtered_file_count: Number of doc-relevant files in the diff.

    Returns:
        ``"full"`` or ``"delta"``.
    """
    if not has_prior_doc:
        return "full"
    if filtered_byte_len > MAX_TEXT_LENGTH or filtered_file_count > MAX_DELTA_FILES:
        return "full"
    return "delta"


def _strip_frontmatter(content: str) -> str:
    """Strip a leading ``---\\n...\\n---\\n`` frontmatter block, if present.

    Args:
        content: The full text of a generated reference file.

    Returns:
        ``content`` with its frontmatter block removed, or unchanged if it
        does not open with one.
    """
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end != -1:
            return content[end + 5 :].lstrip("\n")
    return content


def _read_prior_doc_body(path: Path) -> str | None:
    """Read an existing ``gh-*.md`` reference file's body, minus frontmatter.

    Args:
        path: Path to the expected reference file.

    Returns:
        The file's body text, or ``None`` if the file does not exist or
        cannot be read.
    """
    if not path.exists():
        return None
    try:
        return _strip_frontmatter(path.read_text(encoding="utf-8"))
    except OSError as exc:
        logger.warning("Could not read prior doc %s: %s", path, exc)
        return None


def write_github_reference(
    skill: str,
    slug: str,
    content: str,
    *,
    source: str,
    fetched: str,
    source_version: str,
) -> Path:
    """Write a GitHub-sourced reference file, routing unmapped repos to triage.

    A mapped repo (non-empty ``skill``) goes through
    :func:`write_reference_file`; an unmapped repo (``skill == ""``) is routed
    to ``_triage/`` with a ``<!-- triage: unassigned -->`` marker.

    Args:
        skill: Target skill directory name, or ``""`` to route to triage.
        slug: File stem (without ``.md``).
        content: The summary markdown body (frontmatter is prepended).
        source: Provenance URL — the repo's ``html_url`` or its ``/wiki`` page.
        fetched: ISO ``YYYY-MM-DD`` fetch date for the frontmatter.
        source_version: Git commit SHA this summary was generated from.

    Returns:
        The absolute path of the file that was written.

    Raises:
        ValueError: If the resolved triage path escapes ``TRIAGE_DIR`` or the
            frontmatter would contain the manual-reference marker.
    """
    if skill:
        return write_reference_file(
            skill,
            slug,
            content,
            source=source,
            type_="github",
            fetched=fetched,
            source_version=source_version,
        )

    TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
    output_path = TRIAGE_DIR / f"{slug}.md"
    resolved = output_path.resolve()
    if not resolved.is_relative_to(TRIAGE_DIR.resolve()):
        raise ValueError(f"Triage output path escapes triage directory: {resolved}")

    frontmatter = build_frontmatter(source, "github", fetched, source_version)
    if MANUAL_REFERENCE_MARKER in frontmatter:
        raise ValueError(
            f"Refusing to write triage frontmatter containing the manual-reference marker: {resolved}"
        )
    output_path.write_text(
        f"{frontmatter}\n<!-- triage: unassigned -->\n\n{content}", encoding="utf-8"
    )
    logger.info("Wrote GitHub triage file: %s", output_path)
    return output_path


def _stub_summary(repo: RepoInfo) -> str:
    """Build a one-line summary body for a stub repo — no LLM call made.

    Args:
        repo: The stub repo's discovery info.

    Returns:
        A short markdown body describing the repo and its stub status.
    """
    reasons = []
    if repo.archived:
        reasons.append("archived")
    if repo.disabled:
        reasons.append("disabled")
    if repo.size == 0:
        reasons.append("empty")
    reason_str = ", ".join(reasons) or "stub"
    description = repo.description or "No description."
    return (
        f"# {repo.name}\n\n"
        f"{description}\n\n"
        f"This repository is a stub ({reason_str}) and has not been fully "
        "summarized.\n"
    )


def _summarize_delta_or_full(
    *,
    prior_doc_body: str | None,
    filtered: FilteredDiff | None,
    readme_provider: Callable[[], str],
    metadata: dict,
    label: str,
) -> tuple[SummaryResult | None, str, int]:
    """Run ``summarize_repo_full`` or ``summarize_repo_delta``, choosing the mode.

    Deltas against ``prior_doc_body`` when one exists and the diff is small
    enough (see :func:`choose_github_mode`), otherwise full. An empty
    ``filtered.text`` is treated like ``None`` — fall back to full. Every call
    goes through :func:`call_with_backoff`.

    Args:
        prior_doc_body: The existing reference file's body, or ``None``.
        filtered: The filtered diff to delta against, or ``None``.
        readme_provider: Zero-argument callable returning the README (or, for
            a wiki, the concatenated markdown); called lazily only for a full.
        metadata: Repo metadata dict passed through to the summarize calls.
        label: Identifier for backoff log messages.

    Returns:
        A ``(result, llm_mode, diff_bytes)`` tuple; ``diff_bytes`` is ``0`` for
        a full summarize.
    """
    if prior_doc_body is None or filtered is None or not filtered.text:
        result = call_with_backoff(
            lambda: summarize_repo_full(readme_provider(), [], metadata), label=label
        )
        return result, "full", 0

    llm_mode = choose_github_mode(
        has_prior_doc=True,
        filtered_byte_len=filtered.byte_len,
        filtered_file_count=filtered.file_count,
    )
    if llm_mode == "full":
        result = call_with_backoff(
            lambda: summarize_repo_full(readme_provider(), [], metadata), label=label
        )
        return result, "full", filtered.byte_len

    result = call_with_backoff(
        lambda: summarize_repo_delta(prior_doc_body, filtered.text, metadata), label=label
    )
    return result, "delta", filtered.byte_len


def _process_github_repo(
    repo: RepoInfo,
    org: str,
    config_entry: dict | None,
    state: dict[str, dict],
    fetched: str,
    token: str | None,
    stats: dict[str, int],
    github_metrics: GitHubRunMetrics,
) -> None:
    """Process one discovered GitHub repo: gate, summarize, write, then its wiki.

    Mutates ``state`` and ``stats`` in place. Individual repo failures are
    logged and counted in ``stats["failed"]`` rather than raised.

    Args:
        repo: The repo's discovery info.
        org: GitHub organization login.
        config_entry: This repo's ``repos:`` mapping entry (``skill`` and
            ``track_releases``), or ``None`` if unmapped (routes to triage).
        state: The mutable per-repo state cache (``full_name`` -> state dict).
        fetched: ISO ``YYYY-MM-DD`` fetch date for the frontmatter.
        token: A GitHub token, or ``None``.
        stats: Mutable counters (``updated`` / ``skipped`` / ``failed``).
        github_metrics: Mutable per-repo LLM usage accumulator.
    """
    full_name = repo.full_name
    skill = (config_entry or {}).get("skill", "")
    track_releases = bool((config_entry or {}).get("track_releases", False))

    if not is_changed_since_last_run(repo, state):
        logger.info("%s: unchanged since last run, skipping", full_name)
        stats["skipped"] += 1
        return

    slug = github_repo_slug(org, repo.name)
    doc_path = (
        references_dir_for_skill(skill) / f"{slug}.md" if skill else TRIAGE_DIR / f"{slug}.md"
    )
    entry_state = state.get(full_name, {})

    if is_manual_reference(doc_path):
        logger.warning(
            "%s: output %s is a hand-authored reference, skipping", full_name, doc_path
        )
        stats["skipped"] += 1
    elif repo.is_stub:
        summary_text = _stub_summary(repo)
        write_github_reference(
            skill,
            slug,
            summary_text,
            source=repo.html_url,
            fetched=fetched,
            source_version=entry_state.get("last_sha") or "unknown",
        )
        state[full_name] = {
            **entry_state,
            "doc_path": state_doc_path(doc_path),
            "pushed_at": repo.pushed_at,
        }
        github_metrics.append(
            build_metrics_record(
                full_name=full_name, mode="stub", result=None, wall_clock_s=0.0, diff_bytes=0
            )
        )
        stats["updated"] += 1
    else:
        head_sha = get_default_branch_head_sha(org, repo.name, repo.default_branch, token)
        if head_sha is None:
            logger.warning("%s: could not resolve default-branch head sha, skipping", full_name)
            stats["failed"] += 1
        else:
            prior_sha = entry_state.get("last_sha")
            if head_sha == prior_sha and doc_path.exists():
                logger.info(
                    "%s: head sha unchanged (%s) and doc exists, skipping",
                    full_name,
                    head_sha[:8],
                )
                stats["skipped"] += 1
                state[full_name] = {**entry_state, "pushed_at": repo.pushed_at}
            else:
                release_notes = (
                    fetch_latest_release_notes(org, repo.name, token) if track_releases else None
                )
                metadata = {
                    "full_name": full_name,
                    "description": repo.description,
                    "default_branch": repo.default_branch,
                    "latest_release_notes": release_notes,
                }

                prior_doc_body = _read_prior_doc_body(doc_path)
                start = time.perf_counter()
                filtered: FilteredDiff | None = None
                if prior_doc_body is not None:
                    filtered = build_filtered_diff(org, repo.name, prior_sha, head_sha, token=token)

                result, llm_mode, diff_bytes = _summarize_delta_or_full(
                    prior_doc_body=prior_doc_body,
                    filtered=filtered,
                    readme_provider=lambda: fetch_repo_readme(org, repo.name, token) or "",
                    metadata=metadata,
                    label=full_name,
                )
                wall_clock = time.perf_counter() - start
                github_metrics.append(
                    build_metrics_record(
                        full_name=full_name,
                        mode=llm_mode,
                        result=result,
                        wall_clock_s=wall_clock,
                        diff_bytes=diff_bytes,
                    )
                )

                if result is None:
                    stats["failed"] += 1
                else:
                    write_github_reference(
                        skill,
                        slug,
                        result.text,
                        source=repo.html_url,
                        fetched=fetched,
                        source_version=head_sha,
                    )
                    state[full_name] = {
                        **entry_state,
                        "last_sha": head_sha,
                        "doc_path": state_doc_path(doc_path),
                        "pushed_at": repo.pushed_at,
                    }
                    stats["updated"] += 1

    if repo.has_wiki:
        _process_github_wiki(repo, org, skill, state, fetched, stats, github_metrics)


def _process_github_wiki(
    repo: RepoInfo,
    org: str,
    skill: str,
    state: dict[str, dict],
    fetched: str,
    stats: dict[str, int],
    github_metrics: GitHubRunMetrics,
) -> None:
    """Process one repo's wiki as an independent source.

    Clones the wiki into a temporary directory and summarizes it the same way
    as the main repo (delta against ``wiki_last_sha`` when possible, full
    otherwise). A clone that fails or yields no markdown returns cleanly.

    Args:
        repo: The parent repo's discovery info.
        org: GitHub organization login.
        skill: The parent repo's mapped skill (``""`` routes to triage).
        state: The mutable per-repo state cache.
        fetched: ISO ``YYYY-MM-DD`` fetch date for the frontmatter.
        stats: Mutable counters.
        github_metrics: Mutable per-repo LLM usage accumulator.
    """
    full_name = repo.full_name
    slug = github_wiki_slug(org, repo.name)
    doc_path = (
        references_dir_for_skill(skill) / f"{slug}.md" if skill else TRIAGE_DIR / f"{slug}.md"
    )

    if is_manual_reference(doc_path):
        logger.warning(
            "%s wiki: output %s is a hand-authored reference, skipping", full_name, doc_path
        )
        stats["skipped"] += 1
        return

    with tempfile.TemporaryDirectory(prefix="tg-wiki-") as tmp_dir:
        dest = Path(tmp_dir) / "wiki"
        snapshot = clone_wiki(org, repo.name, dest)
        if snapshot is None:
            logger.info("%s: wiki unavailable/empty, skipping wiki source", full_name)
            return

        entry_state = state.get(full_name, {})
        prior_wiki_sha = entry_state.get("wiki_last_sha")
        if snapshot.head_sha == prior_wiki_sha and doc_path.exists():
            logger.info("%s wiki: head sha unchanged, skipping", full_name)
            stats["skipped"] += 1
            state[full_name] = {**entry_state, "wiki_last_sha": snapshot.head_sha}
            return

        metadata = {
            "full_name": f"{full_name} (wiki)",
            "description": repo.description,
            "default_branch": "wiki",
            "latest_release_notes": None,
        }
        prior_doc_body = _read_prior_doc_body(doc_path)

        start = time.perf_counter()
        filtered: FilteredDiff | None = None
        if prior_doc_body is not None:
            filtered = build_wiki_diff(dest, prior_wiki_sha)

        result, _llm_mode, diff_bytes = _summarize_delta_or_full(
            prior_doc_body=prior_doc_body,
            filtered=filtered,
            readme_provider=lambda: "\n\n---\n\n".join(snapshot.files.values()),
            metadata=metadata,
            label=f"{full_name} wiki",
        )
        wall_clock = time.perf_counter() - start
        github_metrics.append(
            build_metrics_record(
                full_name=f"{full_name} (wiki)",
                mode="wiki",
                result=result,
                wall_clock_s=wall_clock,
                diff_bytes=diff_bytes,
            )
        )

        if result is None:
            stats["failed"] += 1
            return

        write_github_reference(
            skill,
            slug,
            result.text,
            source=f"{repo.html_url}/wiki",
            fetched=fetched,
            source_version=snapshot.head_sha,
        )
        state[full_name] = {**entry_state, "wiki_last_sha": snapshot.head_sha}
        stats["updated"] += 1


def process_github_source(
    fetched: str,
    stats: dict[str, int],
    github_metrics: GitHubRunMetrics,
) -> None:
    """Discover, diff, and LLM-summarize Twingate GitHub repos and wikis.

    Runs the whole pass inside :func:`github_repos.rate_limit_wait` so an
    unauthenticated run throttles rather than 403-ing. ``GITHUB_TOKEN`` is
    optional; when present it is used for a higher rate limit. Discovers every
    kept repo across :data:`github_repos.DEFAULT_ORGS`, processes each via
    :func:`_process_github_repo`, and persists per-repo state at the end. A
    single repo's failure is caught and counted, never fatal.

    Args:
        fetched: ISO ``YYYY-MM-DD`` fetch date for the frontmatter.
        stats: Mutable counters (``updated`` / ``skipped`` / ``failed``).
        github_metrics: Mutable per-repo LLM usage accumulator for this run.
    """
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        logger.info(
            "GITHUB_TOKEN present; GitHub API requests for this run will be "
            "authenticated (higher rate limit). This is an optional speed-up "
            "only — this source is token-free by design and does not require it."
        )
    else:
        logger.info(
            "GITHUB_TOKEN not set; running unauthenticated (60 req/hr) with the "
            "adaptive rate-limit throttle enabled so this pass completes rather "
            "than 403-ing partway. This is the supported, token-free default."
        )

    mapping = load_mapping()
    repo_config = {
        entry["full_name"]: entry for entry in mapping.get("repos", []) if entry.get("full_name")
    }
    state = load_repo_state()

    with rate_limit_wait():
        for org in DEFAULT_ORGS:
            org_discovery = discover_org_repos(org, token)
            for repo in org_discovery.kept:
                try:
                    _process_github_repo(
                        repo, org, repo_config.get(repo.full_name), state, fetched, token, stats, github_metrics
                    )
                except Exception as exc:
                    logger.error("Unexpected error processing %s: %s", repo.full_name, exc)
                    stats["failed"] += 1

    save_repo_state(state)


def main() -> int:
    """Orchestrate the full documentation update pipeline.

    Returns:
        Exit code ``0`` on full success, ``1`` if the API health check fails,
        any source's sitemap fetch fails, or nothing could be processed.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    # Step 0: Verify the Claude API is reachable before doing any work.
    logger.info("Step 0: Checking Claude API availability")
    if not check_api_health():
        logger.error(
            "Fatal: Claude API is unavailable. "
            "No files have been modified. Retry when the API is operational."
        )
        return 1

    run_start = time.perf_counter()

    # Step 1: Load mapping, hash cache, patterns, and the declared sources.
    mapping = load_mapping()
    hash_cache = load_hash_cache(HASH_CACHE_PATH)
    norm_cache = load_norm_cache(NORM_HASH_CACHE_PATH)
    metrics = RunMetrics()
    patterns = mapping.get("auto_assign_patterns", [])
    exclude_urls: set[str] = set(mapping.get("exclude", []))
    stats: dict[str, int] = {"updated": 0, "skipped": 0, "failed": 0}
    sources = load_sources(mapping)
    logger.info(
        "Step 1: %d source(s) declared: %s",
        len(sources),
        [s.get("name", "?") for s in sources],
    )

    # Compute the fetch date once so every file this run shares one value.
    fetched = date.today().isoformat()

    # Step 2: Fetch and diff every source's sitemap up front; a fetch failure
    # is fatal and must occur before any doc is written.
    logger.info("Step 2: Fetching and diffing %d source(s)", len(sources))
    discovered: list[tuple[dict, list[str]]] = []  # (source, new_urls)
    total_new = 0
    total_removed = 0
    for source in sources:
        name = source.get("name", "?")
        sitemap_url = source.get("sitemap_url") or DEFAULT_SITEMAP_URL
        path_filter = source.get("path_filter", "/docs/")
        try:
            sitemap_urls = fetch_sitemap(sitemap_url, path_filter)
        except Exception as exc:
            logger.error(
                "Fatal: sitemap fetch failed for source %r (%s): %s",
                name,
                sitemap_url,
                exc,
            )
            return 1
        logger.info(
            "Source %r returned %d URLs matching %r", name, len(sitemap_urls), path_filter
        )
        # Drop excluded URLs (dead/unlisted pages that linger in the sitemap but
        # have no usable content — they would otherwise re-triage every run).
        if exclude_urls:
            before = len(sitemap_urls)
            sitemap_urls = [u for u in sitemap_urls if u not in exclude_urls]
            dropped = before - len(sitemap_urls)
            if dropped:
                logger.info("Source %r: excluded %d URL(s) via the exclude list", name, dropped)
        # Scope the diff to this source's path so URLs owned by other sources
        # (the mapping holds all sources' URLs) are not reported as removed.
        new_urls, removed_urls = diff_docs(sitemap_urls, path_filter=path_filter)
        if removed_urls:
            # Reported only, never pruned.
            logger.info(
                "Source %r: %d URL(s) removed from sitemap: %s",
                name,
                len(removed_urls),
                removed_urls,
            )
        discovered.append((source, new_urls))
        total_new += len(new_urls)
        total_removed += len(removed_urls)

    # Step 3: Process all docs already in the mapping, stamped as ``docs``.
    mapped_docs = mapping.get("docs", [])
    logger.info("Step 3: Processing %d mapped docs", len(mapped_docs))
    for entry in mapped_docs:
        url = entry.get("url", "")
        skill = entry.get("skill", "")
        if not url or not skill:
            continue
        # Per-entry ``type`` (default "docs") so help articles carried in the
        # mapping stamp type/metrics as "help", not "docs".
        entry_type = entry.get("type", DEFAULT_SOURCE_TYPE)
        logger.info("Processing mapped doc: %s -> %s (%s)", url, skill, entry_type)
        process_doc(
            url,
            skill,
            hash_cache,
            stats,
            fetched=fetched,
            doc_type=entry_type,
            source_name=entry_type,
            metrics=metrics,
            norm_cache=norm_cache,
        )

    # Step 4: Handle newly discovered docs per source, stamping each source's type.
    logger.info("Step 4: Processing newly discovered docs (%d total)", total_new)
    for source, new_urls in discovered:
        if not new_urls:
            continue
        doc_type = source.get("type", DEFAULT_SOURCE_TYPE)
        logger.info(
            "Source %r: processing %d new doc(s) as type %r",
            source.get("name", "?"),
            len(new_urls),
            doc_type,
        )
        process_new_urls(
            new_urls,
            patterns,
            hash_cache,
            stats,
            fetched=fetched,
            doc_type=doc_type,
            source_name=source.get("name", DEFAULT_SOURCE_TYPE),
            metrics=metrics,
            norm_cache=norm_cache,
        )

    # Step 4.5: GitHub repos + wikis — an independent source with its own
    # LLM usage metrics, sharing this run's fetched date and stats counters.
    logger.info("Step 4.5: Processing GitHub repos and wikis")
    github_metrics = GitHubRunMetrics()
    github_run_start = time.perf_counter()
    process_github_source(fetched, stats, github_metrics)

    # Step 5: Persist the hash cache and the observation-only shadow cache.
    save_hash_cache(hash_cache, HASH_CACHE_PATH)
    save_norm_cache(norm_cache, NORM_HASH_CACHE_PATH)

    # Step 5.5: Emit churn metrics (JSONL line, stdout, and CI step summary).
    emit(
        metrics,
        run_ts=datetime.now(timezone.utc).isoformat(),
        wall_clock_s=time.perf_counter() - run_start,
        jsonl_path=PROJECT_ROOT / "docs" / "metrics" / "pipeline-runs.jsonl",
        step_summary_path=os.environ.get("GITHUB_STEP_SUMMARY"),
    )

    # Step 5.6: Emit the GitHub source's LLM usage/cost metrics.
    emit_github(
        github_metrics,
        run_ts=datetime.now(timezone.utc).isoformat(),
        wall_clock_s=time.perf_counter() - github_run_start,
        jsonl_path=PROJECT_ROOT / "docs" / "metrics" / "github-runs.jsonl",
        step_summary_path=os.environ.get("GITHUB_STEP_SUMMARY"),
    )

    # Step 6: Final report.
    logger.info(
        "Pipeline complete: %d updated, %d skipped (unchanged), %d failed | "
        "%d new docs discovered, %d docs removed from sitemaps",
        stats["updated"],
        stats["skipped"],
        stats["failed"],
        total_new,
        total_removed,
    )
    if stats["failed"] > 0:
        logger.warning(
            "%d doc(s) failed during this run; see WARNING/ERROR lines above. "
            "These will be retried on the next scheduled run.",
            stats["failed"],
        )

    # Return non-zero only when nothing succeeded at all (0 updated, 0 skipped).
    if stats["updated"] == 0 and stats["skipped"] == 0:
        logger.error(
            "Fatal: no docs were processed successfully (0 updated, 0 skipped)."
        )
        return 1
    return 0


def seed_norm_cache(
    norm_path: Path = NORM_HASH_CACHE_PATH,
    hash_path: Path = HASH_CACHE_PATH,
) -> int:
    """Seed the shadow-hash cache for every URL already in the raw hash cache.

    For each URL in the raw hash cache, fetches the page and stores the
    normalized-content hash in ``norm_path``. Makes no Claude API calls and
    writes no reference files. URLs that fail to fetch are logged and skipped.

    Args:
        norm_path: Path to the shadow-hash cache to populate.
        hash_path: Path to the raw hash cache whose URLs are the seed set.

    Returns:
        Exit code ``0`` (always; individual fetch failures are non-fatal).
    """
    hash_cache = load_hash_cache(hash_path)
    norm_cache = load_norm_cache(norm_path)
    urls = sorted(hash_cache)
    logger.info("Seeding shadow-hash cache from %d URL(s) in %s", len(urls), hash_path)

    seeded = 0
    failed = 0
    for url in urls:
        html = fetch_doc_html(url)
        if html is None:
            logger.warning("Seed: fetch failed for %s, skipping", url)
            failed += 1
            continue
        norm_cache[url] = content_hash(normalize_for_hash(extract_text_from_html(html)))
        seeded += 1
        logger.info("Seed: %s -> %s", url, norm_cache[url][:12])

    save_norm_cache(norm_cache, norm_path)
    logger.info(
        "Seed complete: %d seeded, %d failed to fetch, %d total in shadow cache",
        seeded,
        failed,
        len(norm_cache),
    )
    return 0


def seed_github(fetched: str | None = None) -> int:
    """Run the first full GitHub pass: cold-start full-summarize everything.

    One-time local entrypoint that calls :func:`process_github_source` with no
    existing ``.repo_state.json``, populating the state file and the initial
    ``gh-*.md`` corpus. ``ANTHROPIC_API_KEY`` is required; ``GITHUB_TOKEN`` is
    optional (used for a higher rate limit when present). Run with::

        ANTHROPIC_API_KEY=... .venv/Scripts/python scripts/update_references.py --seed-github

    Args:
        fetched: ISO ``YYYY-MM-DD`` date for the frontmatter; defaults to today.

    Returns:
        Exit code ``0`` on completion, or ``1`` if ``ANTHROPIC_API_KEY`` is
        missing.
    """
    if not os.environ.get("ANTHROPIC_API_KEY"):
        logger.error("Fatal: ANTHROPIC_API_KEY is not set. --seed-github requires it.")
        return 1

    if os.environ.get("GITHUB_TOKEN"):
        logger.info("GITHUB_TOKEN present; the seed will run authenticated (faster).")
    else:
        logger.info(
            "GITHUB_TOKEN not set; the seed will run unauthenticated with the "
            "adaptive rate-limit throttle enabled (slower, but it will complete)."
        )

    resolved_fetched = fetched if fetched is not None else date.today().isoformat()
    stats: dict[str, int] = {"updated": 0, "skipped": 0, "failed": 0}
    github_metrics = GitHubRunMetrics()
    run_start = time.perf_counter()

    process_github_source(resolved_fetched, stats, github_metrics)

    emit_github(
        github_metrics,
        run_ts=datetime.now(timezone.utc).isoformat(),
        wall_clock_s=time.perf_counter() - run_start,
        jsonl_path=PROJECT_ROOT / "docs" / "metrics" / "github-runs.jsonl",
        step_summary_path=os.environ.get("GITHUB_STEP_SUMMARY"),
    )
    logger.info(
        "GitHub seed complete: %d updated, %d skipped, %d failed",
        stats["updated"],
        stats["skipped"],
        stats["failed"],
    )
    return 0


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Twingate docs reference update pipeline."
    )
    parser.add_argument(
        "--seed-norm-cache",
        action="store_true",
        help=(
            "Seed the observation-only shadow-hash cache from the existing raw "
            "hash cache (fetch + normalize only; no API calls, no writes to "
            "references), then exit. Run once before the first observed run."
        ),
    )
    parser.add_argument(
        "--seed-github",
        action="store_true",
        help=(
            "Run the first full GitHub pass: cold-start full-summarize every "
            "mapped/discovered repo and wiki across all four Twingate orgs, "
            "populating .repo_state.json and the initial gh-*.md corpus, then "
            "exit. Requires ANTHROPIC_API_KEY. GITHUB_TOKEN is optional — this "
            "source is token-free by design and throttles to the unauthenticated "
            "rate limit when it's unset; a token, if present, is only a speed-up. "
            "Run this once locally before the weekly GitHub Action can operate "
            "incrementally: ANTHROPIC_API_KEY=... "
            ".venv/Scripts/python scripts/update_references.py --seed-github"
        ),
    )
    args = parser.parse_args()

    if args.seed_norm_cache:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        )
        sys.exit(seed_norm_cache())

    if args.seed_github:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        )
        sys.exit(seed_github())

    sys.exit(main())
