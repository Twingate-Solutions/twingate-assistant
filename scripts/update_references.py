"""Orchestrate the full documentation update pipeline.

This is the main entry point for the auto-update pipeline. It:

1. Fetches the Twingate sitemap to discover current documentation URLs
2. Diffs the sitemap against ``doc_mapping.yaml`` to detect new/removed docs
3. Processes all mapped docs: fetches HTML, checks content hash, calls
   the Claude API for a structured summary, and writes to ``skills/*/references/``
4. Routes newly discovered docs to their auto-assigned skill, or to a
   ``_triage/`` directory if no pattern matches
5. Reports updated / skipped / failed counts and exits non-zero on failures
"""

import json
import logging
import random
import sys
import time
from pathlib import Path

import anthropic

from diff_docs import auto_assign, diff_docs, load_mapping
from fetch_sitemap import fetch_sitemap
from summarize_docs import content_hash, extract_text_from_html, fetch_doc_html, summarize_doc

logger = logging.getLogger(__name__)

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
TRIAGE_DIR = SKILLS_DIR / "_triage"
HASH_CACHE_PATH = SCRIPTS_DIR / ".doc_hashes.json"

# Exponential backoff configuration for rate-limit retries.
BACKOFF_BASE_SECONDS = 1.0
BACKOFF_MAX_SECONDS = 60.0
BACKOFF_MAX_RETRIES = 4


def load_hash_cache(path: Path = HASH_CACHE_PATH) -> dict[str, str]:
    """Load the persisted URL-to-content-hash cache from disk.

    Args:
        path: Filesystem path to the JSON cache file.

    Returns:
        A dictionary mapping documentation URL strings to their last-seen
        MD5 hex-digest. Returns an empty dict if the file does not exist.
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
        cache: Dictionary mapping URL strings to MD5 hex-digests.
        path: Filesystem path to write the JSON file.
    """
    logger.debug("Saving hash cache to %s (%d entries)", path, len(cache))
    with path.open("w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=2, sort_keys=True)


def url_to_slug(url: str) -> str:
    """Convert a documentation URL to a filesystem-safe filename slug.

    Uses the last non-empty path segment of the URL. Replaces dots with
    hyphens. Falls back to ``"index"`` for bare-domain or root-only URLs.

    Args:
        url: A full documentation page URL.

    Returns:
        A filename-safe string suitable for use as a ``.md`` file stem.
    """
    parts = [p for p in url.rstrip("/").split("/") if p]
    if not parts:
        return "index"
    return parts[-1].replace(".", "-")


def references_dir_for_skill(skill: str) -> Path:
    """Return the ``references/`` directory path for the given skill.

    Args:
        skill: Skill directory name (e.g. ``"twingate-connectors"``).

    Returns:
        Absolute path to ``skills/{skill}/references/``.
    """
    return SKILLS_DIR / skill / "references"


def summarize_with_backoff(url: str, html: str) -> str | None:
    """Call ``summarize_doc`` with exponential backoff on rate-limit errors.

    Retries up to ``BACKOFF_MAX_RETRIES`` times when the Claude API returns
    a 429 rate-limit response. Non-rate-limit API errors are not retried.

    Args:
        url: URL of the documentation page (passed to ``summarize_doc``
            for context in the prompt).
        html: Raw HTML content of the page.

    Returns:
        The Claude-generated markdown summary string, or ``None`` if all
        retries are exhausted or a non-retryable API error occurs.
    """
    for attempt in range(BACKOFF_MAX_RETRIES + 1):
        try:
            return summarize_doc(url, html)
        except anthropic.RateLimitError as exc:
            if attempt == BACKOFF_MAX_RETRIES:
                logger.error(
                    "Rate limit exceeded after %d retries for %s: %s",
                    BACKOFF_MAX_RETRIES,
                    url,
                    exc,
                )
                return None
            delay = min(
                BACKOFF_BASE_SECONDS * (2**attempt) + random.uniform(0, 1),
                BACKOFF_MAX_SECONDS,
            )
            logger.warning(
                "Rate limited on %s, retrying in %.1fs (attempt %d/%d)",
                url,
                delay,
                attempt + 1,
                BACKOFF_MAX_RETRIES,
            )
            time.sleep(delay)
        except anthropic.APIError as exc:
            logger.error("Claude API error for %s: %s", url, exc)
            return None
    return None  # unreachable; satisfies mypy


def write_reference_file(skill: str, slug: str, content: str) -> Path:
    """Write a summary to the skill's ``references/`` directory.

    Creates the directory tree if it does not already exist.

    Args:
        skill: Skill name (e.g. ``"twingate-connectors"``).
        slug: File stem to use (without the ``.md`` extension).
        content: Markdown content to write.

    Returns:
        The absolute path of the file that was written.
    """
    refs_dir = references_dir_for_skill(skill)
    refs_dir.mkdir(parents=True, exist_ok=True)
    output_path = refs_dir / f"{slug}.md"
    output_path.write_text(content, encoding="utf-8")
    logger.info("Wrote reference file: %s", output_path)
    return output_path


def process_doc(
    url: str,
    skill: str,
    hash_cache: dict[str, str],
    stats: dict[str, int],
    triage: bool = False,
) -> None:
    """Fetch, hash-check, summarize, and write one documentation page.

    Modifies ``hash_cache`` and ``stats`` in-place. Never raises; failures
    are logged and counted in ``stats["failed"]``.

    Args:
        url: Documentation page URL to process.
        skill: Target skill directory name (e.g. ``"twingate-connectors"``).
            Ignored when ``triage=True``.
        hash_cache: Mutable URL-to-hash dictionary; updated on success.
        stats: Mutable counters with keys ``"updated"``, ``"skipped"``,
            and ``"failed"``; incremented as appropriate.
        triage: When ``True``, write the output to the ``_triage/``
            directory instead of the skill's ``references/`` directory.
    """
    slug = url_to_slug(url)

    # Determine the expected output path before fetching (used for hash check).
    if triage or not skill:
        output_path = TRIAGE_DIR / f"{slug}.md"
    else:
        output_path = references_dir_for_skill(skill) / f"{slug}.md"

    # Fetch HTML.
    html = fetch_doc_html(url)
    if html is None:
        logger.warning("Skipping %s: fetch failed", url)
        stats["failed"] += 1
        return

    # Hash check — skip if content is identical to last run and file exists.
    text = extract_text_from_html(html)
    current_hash = content_hash(text)
    if hash_cache.get(url) == current_hash and output_path.exists():
        logger.info("Content unchanged for %s, skipping", url)
        stats["skipped"] += 1
        return

    # Summarize via Claude API with backoff.
    summary = summarize_with_backoff(url, html)
    if summary is None:
        stats["failed"] += 1
        return

    # Write output.
    if triage or not skill:
        TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
        triage_content = f"<!-- triage: unassigned URL: {url} -->\n\n{summary}"
        output_path.write_text(triage_content, encoding="utf-8")
        logger.info("Wrote triage file: %s", output_path)
    else:
        write_reference_file(skill, slug, summary)

    hash_cache[url] = current_hash
    stats["updated"] += 1


def main() -> int:
    """Orchestrate the full documentation update pipeline.

    Returns:
        Exit code ``0`` on full success, ``1`` if the sitemap fetch fails
        or any individual document fails to process.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    # Step 1: Fetch the live sitemap.
    logger.info("Step 1: Fetching sitemap")
    try:
        sitemap_urls = fetch_sitemap()
    except Exception as exc:
        logger.error("Fatal: sitemap fetch failed: %s", exc)
        return 1
    logger.info("Sitemap returned %d /docs/ URLs", len(sitemap_urls))

    # Step 2: Diff against doc_mapping.yaml.
    logger.info("Step 2: Diffing against doc_mapping.yaml")
    new_urls, removed_urls = diff_docs(sitemap_urls)
    if removed_urls:
        logger.info("Docs removed from sitemap: %s", removed_urls)

    # Step 3: Load mapping and hash cache.
    mapping = load_mapping()
    hash_cache = load_hash_cache(HASH_CACHE_PATH)
    patterns = mapping.get("auto_assign_patterns", [])
    stats: dict[str, int] = {"updated": 0, "skipped": 0, "failed": 0}

    # Step 4: Process all docs already in the mapping.
    mapped_docs = mapping.get("docs", [])
    logger.info("Step 3: Processing %d mapped docs", len(mapped_docs))
    for entry in mapped_docs:
        url = entry.get("url", "")
        skill = entry.get("skill", "")
        if not url or not skill:
            continue
        logger.info("Processing mapped doc: %s -> %s", url, skill)
        process_doc(url, skill, hash_cache, stats)

    # Step 5: Handle newly discovered docs.
    if new_urls:
        logger.info("Step 4: Processing %d new docs", len(new_urls))
        for url in new_urls:
            assigned_skill = auto_assign(url, patterns) or ""
            if assigned_skill:
                logger.info("Auto-assigned new doc %s -> %s", url, assigned_skill)
                process_doc(url, assigned_skill, hash_cache, stats)
            else:
                logger.warning("No auto-assign match for %s, routing to triage", url)
                process_doc(url, "", hash_cache, stats, triage=True)

    # Step 6: Persist the updated hash cache.
    save_hash_cache(hash_cache, HASH_CACHE_PATH)

    # Step 7: Final report.
    logger.info(
        "Pipeline complete: %d updated, %d skipped (unchanged), %d failed | "
        "%d new docs discovered, %d docs removed from sitemap",
        stats["updated"],
        stats["skipped"],
        stats["failed"],
        len(new_urls),
        len(removed_urls),
    )

    return 0 if stats["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
