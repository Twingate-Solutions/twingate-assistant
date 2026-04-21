"""Batch runner for the documentation reference update pipeline.

Two-step process designed for interactive AI summarization (testing mode):

    # Step 1: Fetch docs, extract text, write prompt work files
    python scripts/run_batch.py --skip 0 --limit 5 --prepare

    # Step 2: Fill in summaries in .batch_work/*.json, then finalize
    python scripts/run_batch.py --finalize

The standard one-shot API mode (requires ANTHROPIC_API_KEY) is also supported:

    python scripts/run_batch.py --skip 0 --limit 5

Work files are written to ``scripts/.batch_work/`` (gitignored). Each JSON
file contains the extracted page text and a ``summary`` field initially set to
``null``. After summaries are filled in, ``--finalize`` writes the reference
``.md`` files and updates the hash cache.

Uses the same hash cache (``scripts/.doc_hashes.json``) as
``update_references.py``. GitHub repository entries in ``doc_mapping.yaml``
are automatically excluded (pipeline cannot fetch non-twingate.com URLs).

Progress is tracked in ``docs/sessions/18-reference-pipeline-run.md``.
"""

import argparse
import json
import logging
import sys
from pathlib import Path

# Ensure scripts/ is on the path for sibling module imports.
sys.path.insert(0, str(Path(__file__).parent))

from diff_docs import load_mapping
from summarize_docs import (
    SYSTEM_PROMPT,
    content_hash,
    extract_text_from_html,
    fetch_doc_html,
)
from update_references import (
    HASH_CACHE_PATH,
    SCRIPTS_DIR,
    SKILLS_DIR,
    TRIAGE_DIR,
    load_hash_cache,
    references_dir_for_skill,
    save_hash_cache,
    url_to_slug,
    write_reference_file,
)

logger = logging.getLogger(__name__)

BATCH_WORK_DIR = SCRIPTS_DIR / ".batch_work"

MAX_TEXT_LENGTH = 60_000  # matches summarize_docs.py


# ── Helpers ──────────────────────────────────────────────────────────────────


def twingate_docs(mapping: dict) -> list[dict]:
    """Return only the twingate.com entries from the mapping (no GitHub)."""
    return [
        d for d in mapping.get("docs", [])
        if "twingate.com" in d.get("url", "")
    ]


def work_file_path(index: int, slug: str) -> Path:
    """Return the path for a batch work JSON file."""
    return BATCH_WORK_DIR / f"{index:05d}_{slug}.json"


def output_path_for(skill: str, slug: str) -> Path:
    """Return the expected reference file path for a given skill/slug."""
    if not skill:
        return TRIAGE_DIR / f"{slug}.md"
    return references_dir_for_skill(skill) / f"{slug}.md"


# ── Prepare step ─────────────────────────────────────────────────────────────


def prepare_batch(skip: int, limit: int) -> int:
    """Fetch docs, extract text, write JSON work files for AI summarization.

    Skips docs whose content hash matches the cache and whose reference file
    already exists (no change since last run).

    Args:
        skip: Number of docs to skip from the start of the list.
        limit: Maximum number of docs to process.

    Returns:
        Exit code 0 on success, 1 if any fetch failed.
    """
    mapping = load_mapping()
    all_docs = twingate_docs(mapping)
    total = len(all_docs)
    batch = all_docs[skip : skip + limit]

    if not batch:
        print(f"Nothing to prepare -- skip={skip} is at or past end ({total} total).")
        return 0

    end_idx = skip + len(batch)
    print(f"Preparing docs {skip + 1}-{end_idx} of {total}")
    print()

    BATCH_WORK_DIR.mkdir(parents=True, exist_ok=True)

    hash_cache = load_hash_cache(HASH_CACHE_PATH)
    prepared = 0
    skipped = 0
    failed = 0

    for i, entry in enumerate(batch):
        url = entry.get("url", "")
        skill = entry.get("skill", "")
        pos = skip + i + 1
        slug = url_to_slug(url)
        out_path = output_path_for(skill, slug)

        print(f"[{pos}/{total}] {url}")

        if not url or not skill:
            logger.warning("Skipping entry with missing url or skill: %s", entry)
            continue

        # Fetch HTML.
        html = fetch_doc_html(url)
        if html is None:
            print(f"  FAILED: could not fetch page")
            failed += 1
            continue

        # Extract text and compute hash.
        text = extract_text_from_html(html)
        current_hash = content_hash(text)

        # Skip if content unchanged and file already exists.
        if hash_cache.get(url) == current_hash and out_path.exists():
            print(f"  SKIPPED: content unchanged")
            skipped += 1
            continue

        # Truncate text to match pipeline behaviour.
        prompt_text = text
        if len(text) > MAX_TEXT_LENGTH:
            prompt_text = text[:MAX_TEXT_LENGTH] + "\n\n[Content truncated for length]"

        # Write work file.
        work = {
            "index": pos,
            "url": url,
            "skill": skill,
            "slug": slug,
            "text_hash": current_hash,
            "system_prompt": SYSTEM_PROMPT,
            "prompt": f"URL: {url}\n\n{prompt_text}",
            "summary": None,
        }
        work_path = work_file_path(pos, slug)
        work_path.write_text(json.dumps(work, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  -> {work_path.name}")
        prepared += 1

    print()
    print("-" * 60)
    print(f"  prepared : {prepared}  (waiting for AI summarization)")
    print(f"  skipped  : {skipped}  (content unchanged)")
    print(f"  failed   : {failed}")
    print("-" * 60)

    if prepared > 0:
        print(f"\nWork files written to: {BATCH_WORK_DIR}")
        print("Fill in the 'summary' field in each .json file, then run:")
        print("  python scripts/run_batch.py --finalize")
    elif failed == 0:
        print("\nNothing to do -- all docs in this batch are up to date.")

    return 0 if failed == 0 else 1


# ── Finalize step ─────────────────────────────────────────────────────────────


def finalize_batch() -> int:
    """Read completed work files, write reference docs, update hash cache.

    Reads all JSON files in ``.batch_work/`` where ``summary`` is not null.
    Writes reference markdown files to the appropriate skill directory and
    updates the hash cache. Cleans up processed work files.

    Returns:
        Exit code 0 on success, 1 if any writes failed.
    """
    work_files = sorted(BATCH_WORK_DIR.glob("*.json")) if BATCH_WORK_DIR.exists() else []

    if not work_files:
        print("No work files found in .batch_work/ -- nothing to finalize.")
        return 0

    hash_cache = load_hash_cache(HASH_CACHE_PATH)
    written = 0
    pending = 0
    failed = 0

    for work_path in work_files:
        try:
            work = json.loads(work_path.read_text(encoding="utf-8"))
        except Exception as exc:
            logger.error("Could not read %s: %s", work_path, exc)
            failed += 1
            continue

        summary = work.get("summary")
        if summary is None:
            print(f"[{work_path.name}] PENDING -- summary not yet filled in")
            pending += 1
            continue

        url = work["url"]
        skill = work["skill"]
        slug = work["slug"]
        text_hash = work["text_hash"]

        print(f"[{work_path.name}] Writing {skill}/references/{slug}.md")

        try:
            if skill:
                write_reference_file(skill, slug, summary)
            else:
                # Triage
                TRIAGE_DIR.mkdir(parents=True, exist_ok=True)
                triage_path = TRIAGE_DIR / f"{slug}.md"
                triage_content = f"<!-- triage: unassigned URL: {url} -->\n\n{summary}"
                triage_path.write_text(triage_content, encoding="utf-8")
        except Exception as exc:
            logger.error("Failed to write reference file for %s: %s", url, exc)
            failed += 1
            continue

        hash_cache[url] = text_hash
        work_path.unlink()
        written += 1

    save_hash_cache(hash_cache, HASH_CACHE_PATH)

    print()
    print("-" * 60)
    print(f"  written  : {written}")
    print(f"  pending  : {pending}  (summary not yet filled in)")
    print(f"  failed   : {failed}")
    print("-" * 60)

    if pending > 0:
        print(f"\n{pending} file(s) still need summaries. Fill them in and re-run --finalize.")

    return 0 if failed == 0 else 1


# ── API mode (production) ─────────────────────────────────────────────────────


def run_api_batch(skip: int, limit: int) -> int:
    """Process docs directly via the Anthropic API (requires ANTHROPIC_API_KEY).

    Args:
        skip: Number of docs to skip.
        limit: Number of docs to process.

    Returns:
        Exit code 0 on success, 1 if any docs failed.
    """
    # Import here so missing API key is only an error in this mode.
    from update_references import process_doc, summarize_with_backoff  # noqa: F401

    mapping = load_mapping()
    all_docs = twingate_docs(mapping)
    total = len(all_docs)
    batch = all_docs[skip : skip + limit]

    if not batch:
        print(f"Nothing to process -- skip={skip} is at or past end ({total} total).")
        return 0

    end_idx = skip + len(batch)
    print(f"Batch: docs {skip + 1}-{end_idx} of {total}")
    print()

    hash_cache = load_hash_cache(HASH_CACHE_PATH)
    stats: dict[str, int] = {"updated": 0, "skipped": 0, "failed": 0}

    for i, entry in enumerate(batch):
        url = entry.get("url", "")
        skill = entry.get("skill", "")
        pos = skip + i + 1
        print(f"[{pos}/{total}] {url}  ->  {skill}")
        if not url or not skill:
            continue
        process_doc(url, skill, hash_cache, stats)

    save_hash_cache(hash_cache, HASH_CACHE_PATH)

    print()
    print("-" * 60)
    print(f"  generated : {stats['updated']}")
    print(f"  skipped   : {stats['skipped']}  (content unchanged)")
    print(f"  failed    : {stats['failed']}")
    print("-" * 60)

    if end_idx < total:
        print(f"\nNext batch:")
        print(f"  python scripts/run_batch.py --skip {end_idx} --limit {skip}")
    else:
        print("\nAll docs processed!")

    return 0 if stats["failed"] == 0 else 1


# ── Entry point ───────────────────────────────────────────────────────────────


def main() -> int:
    """Dispatch to prepare, finalize, or API batch mode."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    parser = argparse.ArgumentParser(
        description="Batch runner for Twingate reference file generation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--prepare",
        action="store_true",
        help="Fetch docs and write prompt work files (no API call).",
    )
    mode.add_argument(
        "--finalize",
        action="store_true",
        help="Read completed work files and write reference docs.",
    )
    parser.add_argument(
        "--skip",
        type=int,
        default=0,
        metavar="N",
        help="Docs to skip (used with --prepare or API mode; default: 0).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        metavar="M",
        help="Docs to process (used with --prepare or API mode; default: 5).",
    )
    args = parser.parse_args()

    if args.prepare:
        return prepare_batch(args.skip, args.limit)
    elif args.finalize:
        return finalize_batch()
    else:
        return run_api_batch(args.skip, args.limit)


if __name__ == "__main__":
    sys.exit(main())
