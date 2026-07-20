"""Orchestrate the full documentation update pipeline.

This is the main entry point for the auto-update pipeline. It:

1. Fetches the Twingate sitemap to discover current documentation URLs
2. Diffs the sitemap against ``doc_mapping.yaml`` to detect new/removed docs
3. Processes all mapped docs: fetches HTML, checks content hash, calls
   the Claude API for a structured summary, and writes to ``skills/*/references/``
4. Routes newly discovered docs to their auto-assigned skill, or to a
   ``_triage/`` directory if no pattern matches
5. Reports updated / skipped / failed counts and exits non-zero on failures

Hand-authored reference files — those whose header contains
``manual-reference: do-not-overwrite`` (e.g.
``skills/twingate-idfw/references/gateway-troubleshooting.md``) — are never
overwritten or deleted by this pipeline. Any future cleanup/pruning logic
must preserve them.
"""

import json
import logging
import os
import random
import re
import sys
import time
from pathlib import Path

# Ensure the scripts/ directory is on the path for sibling module imports,
# regardless of the working directory from which the script is invoked.
sys.path.insert(0, str(Path(__file__).parent))

import anthropic

from diff_docs import auto_assign, diff_docs, load_mapping
from fetch_sitemap import fetch_sitemap
from summarize_docs import CLAUDE_MODEL, content_hash, extract_text_from_html, fetch_doc_html, summarize_doc

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

# Files carrying this marker are hand-authored references (not generated from
# a public doc page). The pipeline must never overwrite or delete them.
MANUAL_REFERENCE_MARKER = "manual-reference: do-not-overwrite"


def is_manual_reference(path: Path) -> bool:
    """Return True if ``path`` is a hand-authored reference file.

    Hand-authored references carry ``MANUAL_REFERENCE_MARKER`` in a comment
    near the top of the file. Only the first 1024 characters are inspected,
    so the marker must appear in the file's header block.

    Args:
        path: Candidate output path in a skill's ``references/`` directory.

    Returns:
        True if the file exists and contains the marker; False otherwise
        (including on read errors, which are logged and treated as manual
        to fail safe against overwriting).
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
    """Verify the Claude API is reachable before starting the pipeline.

    Makes a minimal API call (max_tokens=1) to confirm that the API key
    is valid and the service is responding. Called at pipeline start so
    that an outage or misconfiguration is detected immediately — before
    the pipeline fetches any doc HTML — ensuring no existing reference
    files are touched when the API is unavailable.

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
        A dictionary mapping documentation URL strings to their last-seen
        SHA-256 hex-digest. Returns an empty dict if the file does not exist.
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

    Uses the last non-empty path segment of the URL. Replaces dots with
    hyphens, then strips any characters outside ``[a-zA-Z0-9\\-_]`` to
    prevent path traversal via crafted URL segments. Falls back to
    ``"index"`` for bare-domain, root-only, or fully-stripped URLs.

    Args:
        url: A full documentation page URL.

    Returns:
        A filename-safe string suitable for use as a ``.md`` file stem.
    """
    parts = [p for p in url.rstrip("/").split("/") if p]
    if not parts:
        return "index"
    raw = parts[-1].replace(".", "-")
    # Allow only alphanumeric, hyphens, and underscores.
    slug = re.sub(r"[^a-zA-Z0-9\-_]", "-", raw)
    # Collapse consecutive hyphens and strip leading/trailing hyphens.
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
        except Exception as exc:
            logger.error("Unexpected error summarizing %s: %s", url, exc)
            return None
    return None  # unreachable; satisfies mypy


def write_reference_file(skill: str, slug: str, content: str) -> Path:
    """Write a summary to the skill's ``references/`` directory.

    Creates the directory tree if it does not already exist. Validates
    that the resolved output path stays within ``SKILLS_DIR`` to prevent
    path traversal via crafted skill or slug values.

    Args:
        skill: Skill name (e.g. ``"twingate-connectors"``).
        slug: File stem to use (without the ``.md`` extension).
        content: Markdown content to write.

    Returns:
        The absolute path of the file that was written.

    Raises:
        ValueError: If the resolved output path escapes ``SKILLS_DIR``, or
            if it would overwrite a hand-authored (manual) reference file.
    """
    refs_dir = references_dir_for_skill(skill)
    refs_dir.mkdir(parents=True, exist_ok=True)
    output_path = refs_dir / f"{slug}.md"

    # Guard against path traversal via crafted skill or slug values.
    resolved = output_path.resolve()
    if not resolved.is_relative_to(SKILLS_DIR.resolve()):
        raise ValueError(f"Output path escapes skills directory: {resolved}")

    # Never overwrite hand-authored reference files (e.g. a doc URL whose
    # slug collides with one). process_doc skips these earlier; this is the
    # last line of defense at the single write chokepoint.
    if is_manual_reference(output_path):
        raise ValueError(f"Refusing to overwrite hand-authored reference: {resolved}")

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

    # Hand-authored references are never regenerated — skip before fetching
    # so a slug collision costs nothing and touches nothing.
    if is_manual_reference(output_path):
        logger.warning(
            "Skipping %s: output %s is a hand-authored reference (slug collision?)",
            url,
            output_path,
        )
        stats["skipped"] += 1
        return

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
        resolved = output_path.resolve()
        if not resolved.is_relative_to(TRIAGE_DIR.resolve()):
            raise ValueError(f"Triage output path escapes triage directory: {resolved}")
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
        Exit code ``0`` on full success, ``1`` if the API health check fails,
        the sitemap fetch fails, or any individual document fails to process.
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
    logger.info("Step 4: Processing %d mapped docs", len(mapped_docs))
    for entry in mapped_docs:
        url = entry.get("url", "")
        skill = entry.get("skill", "")
        if not url or not skill:
            continue
        logger.info("Processing mapped doc: %s -> %s", url, skill)
        process_doc(url, skill, hash_cache, stats)

    # Step 5: Handle newly discovered docs.
    if new_urls:
        logger.info("Step 5: Processing %d new docs", len(new_urls))
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
    if stats["failed"] > 0:
        logger.warning(
            "%d doc(s) failed during this run; see WARNING/ERROR lines above. "
            "These will be retried on the next scheduled run.",
            stats["failed"],
        )

    # Soft-fail policy: individual doc failures don't abort the run. We
    # return non-zero only when nothing succeeded at all (no doc was
    # updated AND no doc was unchanged), which indicates a fatal issue
    # like complete API/network failure. The Step 0 health check already
    # short-circuits on a fully-broken API, so reaching this point with
    # zero successes typically means the pipeline state itself is bad.
    if stats["updated"] == 0 and stats["skipped"] == 0:
        logger.error(
            "Fatal: no docs were processed successfully (0 updated, 0 skipped)."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
