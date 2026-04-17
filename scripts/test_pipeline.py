"""Hybrid test script for the auto-update pipeline.

Runs every pipeline step except the Claude API call. Saves extracted state
to ``test_output/pipeline_state.json``, prints the exact prompt that would be
sent to Claude, then (with ``--write``) reads a summary from stdin and writes
it to the correct reference file.

Usage
-----
Phase 1 — fetch sitemap, match a doc, extract text, print prompt::

    python scripts/test_pipeline.py [--url URL]

Phase 2 — write the Claude-provided summary to the reference file::

    python scripts/test_pipeline.py --write --summary-file summary.md
    # or via stdin (ensure UTF-8):
    python scripts/test_pipeline.py --write < summary.md

``--url URL``             Pick a specific doc URL instead of the first mapped entry.
``--write``               Phase 2: read summary and write reference file.
``--summary-file PATH``   Read summary from this file (UTF-8) instead of stdin.
``--quiet``               Suppress the PROMPT FOR CLAUDE text block (state JSON still written).
                          Use this when running automated: read extracted_text from pipeline_state.json.
"""

import argparse
import json
import sys
from pathlib import Path

# Allow running from any working directory.
SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

from diff_docs import auto_assign, diff_docs, load_mapping  # noqa: E402
from fetch_sitemap import fetch_sitemap  # noqa: E402
from summarize_docs import (  # noqa: E402
    SYSTEM_PROMPT,
    content_hash,
    extract_text_from_html,
    fetch_doc_html,
)

PROJECT_ROOT = SCRIPTS_DIR.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
TEST_OUTPUT_DIR = SCRIPTS_DIR / "test_output"
STATE_FILE = TEST_OUTPUT_DIR / "pipeline_state.json"

MAX_TEXT_LENGTH = 60000  # matches summarize_docs.py


def url_to_slug(url: str) -> str:
    """Last non-empty URL path segment, dots replaced with hyphens."""
    parts = [p for p in url.rstrip("/").split("/") if p]
    return parts[-1].replace(".", "-") if parts else "index"


def phase1(target_url: str | None, quiet: bool = False) -> None:
    """Fetch sitemap, pick a doc, extract text, save state, print prompt."""

    # ── Step 1: sitemap ──────────────────────────────────────────────────────
    print("=" * 60)
    print("STEP 1: Fetching sitemap...")
    sitemap_urls = fetch_sitemap()
    print(f"  Found {len(sitemap_urls)} /docs/ URLs")

    # ── Step 2: diff ─────────────────────────────────────────────────────────
    print("\nSTEP 2: Diffing against doc_mapping.yaml...")
    new_urls, removed_urls = diff_docs(sitemap_urls)
    print(f"  {len(new_urls)} new URLs, {len(removed_urls)} removed URLs")
    if new_urls:
        print(f"  New: {new_urls[:3]}{'...' if len(new_urls) > 3 else ''}")
    if removed_urls:
        print(f"  Removed: {removed_urls[:3]}{'...' if len(removed_urls) > 3 else ''}")

    # ── Step 3: pick a doc ───────────────────────────────────────────────────
    print("\nSTEP 3: Selecting doc to process...")
    mapping = load_mapping()
    docs = mapping.get("docs", [])
    patterns = mapping.get("auto_assign_patterns", [])

    if target_url:
        # Find the requested URL in the mapping.
        entry = next((d for d in docs if d.get("url") == target_url), None)
        if entry:
            url = entry["url"]
            skill = entry["skill"]
            print(f"  Using requested URL: {url} -> {skill}")
        else:
            # Not in mapping — try auto-assign.
            assigned = auto_assign(target_url, patterns)
            if assigned:
                url = target_url
                skill = assigned
                print(f"  URL not in mapping, auto-assigned: {url} -> {skill}")
            else:
                url = target_url
                skill = "_triage"
                print("  URL not in mapping and no auto-assign match: routing to _triage")
    else:
        # Default: pick first mapped entry.
        if not docs:
            print("  ERROR: No docs in mapping.")
            sys.exit(1)
        entry = docs[0]
        url = entry["url"]
        skill = entry["skill"]
        print(f"  Defaulting to first mapped doc: {url} -> {skill}")

    slug = url_to_slug(url)

    # ── Step 4: fetch HTML ───────────────────────────────────────────────────
    print(f"\nSTEP 4: Fetching {url} ...")
    html = fetch_doc_html(url)
    if html is None:
        print("  ERROR: Failed to fetch page.")
        sys.exit(1)
    print(f"  Fetched {len(html)} bytes of HTML")

    # ── Step 5: extract text ─────────────────────────────────────────────────
    print("\nSTEP 5: Extracting text from HTML...")
    text = extract_text_from_html(html)
    print(f"  Extracted {len(text)} chars of plain text")

    if len(text) > MAX_TEXT_LENGTH:
        text = text[:MAX_TEXT_LENGTH] + "\n\n[Content truncated for length]"
        print(f"  Truncated to {MAX_TEXT_LENGTH} chars")

    page_hash = content_hash(text)
    print(f"  Content hash: {page_hash}")

    # ── Step 6: save state ───────────────────────────────────────────────────
    TEST_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    state = {
        "url": url,
        "skill": skill,
        "slug": slug,
        "page_hash": page_hash,
        "extracted_text": text,
    }
    # Always write the shared state file (used by --write).
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    # Also write a slug-named file so parallel runs don't clobber each other.
    slug_state_file = TEST_OUTPUT_DIR / f"{slug}.state.json"
    slug_state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nState saved to: {slug_state_file}")

    # ── Step 7: print the prompt ─────────────────────────────────────────────
    if not quiet:
        print("\n" + "=" * 60)
        print("PROMPT FOR CLAUDE")
        print("=" * 60)
        print("\n[SYSTEM PROMPT]")
        print(SYSTEM_PROMPT)
        print("\n[USER MESSAGE]")
        print(f"URL: {url}\n")
        print(text)
        print("\n" + "=" * 60)

    print("Phase 1 complete.")
    print(f"  Doc:    {url}")
    print(f"  Skill:  {skill}")
    print(f"  Target: skills/{skill}/references/{slug}.md")
    print(f"  State:  {STATE_FILE}")
    if not quiet:
        print("\nNext steps:")
        print("  1. Copy the prompt above and generate a summary")
        print("  2. Save summary to a .md file")
        print("  3. Run: python scripts/test_pipeline.py --write --summary-file <path>")


def phase2(summary_file: str | None) -> None:
    """Read summary from a file or stdin, write to the reference file."""

    if not STATE_FILE.exists():
        print(f"ERROR: No state file found at {STATE_FILE}")
        print("Run Phase 1 first: python scripts/test_pipeline.py")
        sys.exit(1)

    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    url: str = state["url"]
    skill: str = state["skill"]
    slug: str = state["slug"]

    print(f"Reading summary for: {url}")

    if summary_file:
        summary = Path(summary_file).read_text(encoding="utf-8").strip()
        print(f"Read from file: {summary_file}")
    else:
        print("Reading from stdin (paste summary, then Ctrl+D / Ctrl+Z+Enter)...")
        summary = sys.stdin.buffer.read().decode("utf-8").strip()

    if not summary:
        print("ERROR: No summary provided.")
        sys.exit(1)

    print(f"\nReceived {len(summary)} chars of summary")

    # Write reference file.
    if skill == "_triage":
        out_dir = SKILLS_DIR / "_triage"
        content = f"<!-- triage: unassigned URL: {url} -->\n\n{summary}"
    else:
        out_dir = SKILLS_DIR / skill / "references"
        content = summary

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug}.md"
    out_path.write_text(content, encoding="utf-8")

    print(f"\nWrote: {out_path}")
    print("Phase 2 complete.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--url", help="Specific doc URL to process (default: first mapped entry)")
    parser.add_argument("--write", action="store_true", help="Phase 2: read summary and write reference file")
    parser.add_argument("--summary-file", help="Path to summary .md file (Phase 2); reads stdin if omitted")
    parser.add_argument("--quiet", action="store_true", help="Suppress PROMPT FOR CLAUDE block; state JSON still written")
    args = parser.parse_args()

    if args.write:
        phase2(args.summary_file)
    else:
        phase1(args.url, quiet=args.quiet)


if __name__ == "__main__":
    main()
