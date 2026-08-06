"""One-time backfill of provenance frontmatter onto existing reference files."""

from __future__ import annotations

import argparse
import logging
import re
import sys
from datetime import date
from pathlib import Path

# Ensure the scripts/ directory is importable regardless of the working directory.
sys.path.insert(0, str(Path(__file__).parent))

from diff_docs import load_mapping
from summarize_docs import build_frontmatter, content_hash
from update_references import (
    MANUAL_REFERENCE_MARKER,
    SKILLS_DIR,
    is_manual_reference,
    url_to_slug,
)

logger = logging.getLogger(__name__)

# Leading characters inspected for a manual marker or a legacy ``URL:`` comment.
HEAD_INSPECT_CHARS = 1024

# Matches a source URL embedded in a legacy ``URL:`` HTML comment.
_URL_COMMENT_RE = re.compile(r"URL:\s*(https://\S+?)\s*(?:-->|$)", re.IGNORECASE)


def has_frontmatter(text: str) -> bool:
    """Return True if ``text`` already opens with a YAML frontmatter fence.

    Args:
        text: Full file contents.

    Returns:
        True if the file already carries frontmatter.
    """
    return text.startswith("---\n") or text.startswith("---\r\n")


def build_inverse_index(
    mapping: dict, skills_dir: Path
) -> dict[Path, str]:
    """Build a reference-file-path -> source-URL index from the doc mapping.

    Args:
        mapping: Parsed ``doc_mapping.yaml`` document.
        skills_dir: Root ``skills/`` directory to resolve reference paths under.

    Returns:
        A dict mapping resolved reference-file ``Path`` to its source URL. On
        a slug collision the last entry wins and a warning is logged.
    """
    index: dict[Path, str] = {}
    for entry in mapping.get("docs", []):
        url = entry.get("url", "")
        skill = entry.get("skill", "")
        if not url or not skill:
            continue
        slug = url_to_slug(url)
        path = (skills_dir / skill / "references" / f"{slug}.md").resolve()
        if path in index and index[path] != url:
            logger.warning(
                "Slug collision for %s: %s overwrites %s in the inverse index",
                path,
                url,
                index[path],
            )
        index[path] = url
    logger.info("Built inverse index with %d mapped reference paths", len(index))
    return index


def iter_reference_files(skills_dir: Path):
    """Yield every ``*.md`` reference file under ``skills/*/references/``, sorted.

    Args:
        skills_dir: Root ``skills/`` directory to walk.

    Yields:
        ``Path`` objects for each reference file.
    """
    yield from sorted(skills_dir.glob("*/references/*.md"))


def resolve_source_url(
    path: Path, text: str, inverse_index: dict[Path, str]
) -> str | None:
    """Resolve the source URL for a reference file.

    Tries the inverse index first, then a legacy ``URL:`` header comment.

    Args:
        path: Path to the reference file.
        text: Full file contents.
        inverse_index: Path -> URL index.

    Returns:
        The resolved source URL, or ``None`` if neither source yields one.
    """
    mapped = inverse_index.get(path.resolve())
    if mapped is not None:
        return mapped
    match = _URL_COMMENT_RE.search(text[:HEAD_INSPECT_CHARS])
    if match:
        return match.group(1)
    return None


def process_file(
    path: Path,
    inverse_index: dict[Path, str],
    fetched: str,
    *,
    apply: bool,
) -> str:
    """Classify one reference file and, when applying, backfill its frontmatter.

    Read/write failures are logged and reported as ``"failed"``.

    Args:
        path: Reference file to process.
        inverse_index: Path -> URL index.
        fetched: ISO ``YYYY-MM-DD`` date recorded in the frontmatter.
        apply: When False (dry-run), classify only and write nothing.

    Returns:
        One of ``"backfilled"``, ``"has_frontmatter"``, ``"manual"``,
        ``"unresolved"``, or ``"failed"``.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        logger.error("Could not read %s: %s", path, exc)
        return "failed"

    if has_frontmatter(text):
        logger.debug("Skipping %s: already has frontmatter", path)
        return "has_frontmatter"

    if MANUAL_REFERENCE_MARKER in text[:HEAD_INSPECT_CHARS] or is_manual_reference(path):
        logger.debug("Skipping %s: hand-authored (manual-reference marker)", path)
        return "manual"

    url = resolve_source_url(path, text, inverse_index)
    if url is None:
        logger.warning("UNRESOLVED: no mapping or URL comment for %s", path)
        return "unresolved"

    source_version = content_hash(text)
    frontmatter = build_frontmatter(
        source=url, type_="docs", fetched=fetched, source_version=source_version
    )
    new_content = f"{frontmatter}\n{text}"

    if apply:
        try:
            path.write_text(new_content, encoding="utf-8", newline="\n")
        except OSError as exc:
            logger.error("Could not write %s: %s", path, exc)
            return "failed"
        logger.info("Backfilled frontmatter: %s (source=%s)", path, url)
    else:
        logger.info("[dry-run] would backfill %s (source=%s)", path, url)
    return "backfilled"


def run_backfill(
    skills_dir: Path, fetched: str, *, apply: bool
) -> dict[str, int]:
    """Backfill frontmatter across a references tree and return outcome counts.

    Args:
        skills_dir: Root ``skills/`` directory to walk.
        fetched: ISO ``YYYY-MM-DD`` date recorded in generated frontmatter.
        apply: When False (dry-run), classify only and write nothing.

    Returns:
        A dict of outcome -> count with keys ``backfilled``,
        ``has_frontmatter``, ``manual``, ``unresolved``, ``failed``, ``total``.
    """
    mapping = load_mapping()
    inverse_index = build_inverse_index(mapping, skills_dir)

    stats = {
        "backfilled": 0,
        "has_frontmatter": 0,
        "manual": 0,
        "unresolved": 0,
        "failed": 0,
        "total": 0,
    }
    for path in iter_reference_files(skills_dir):
        stats["total"] += 1
        outcome = process_file(path, inverse_index, fetched, apply=apply)
        stats[outcome] += 1
    return stats


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for the one-time frontmatter backfill.

    Returns:
        Exit code ``0`` on success, ``1`` if any file failed to read/write.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    parser = argparse.ArgumentParser(
        description=(
            "One-time backfill of provenance frontmatter onto existing "
            "reference files. Dry-run by default; pass --apply to write."
        )
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to disk. Without this, runs in dry-run mode.",
    )
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing (the default).",
    )
    parser.add_argument(
        "--fetched",
        default=None,
        help=(
            "ISO YYYY-MM-DD date to record in the frontmatter 'fetched' field. "
            "Defaults to today's date, computed at runtime."
        ),
    )
    parser.add_argument(
        "--skills-dir",
        default=None,
        help="Override the skills/ root (mainly for testing). Defaults to the "
        "pipeline's skills directory.",
    )
    args = parser.parse_args(argv)

    apply = args.apply
    fetched = args.fetched if args.fetched is not None else date.today().isoformat()
    skills_dir = Path(args.skills_dir).resolve() if args.skills_dir else SKILLS_DIR

    logger.info(
        "Backfill starting: skills_dir=%s fetched=%s mode=%s",
        skills_dir,
        fetched,
        "APPLY" if apply else "DRY-RUN",
    )

    stats = run_backfill(skills_dir, fetched, apply=apply)

    logger.info(
        "Backfill %s complete: %d total | %d %s | %d already had frontmatter | "
        "%d manual-skipped | %d unresolved | %d failed",
        "APPLY" if apply else "DRY-RUN",
        stats["total"],
        stats["backfilled"],
        "backfilled" if apply else "to-backfill",
        stats["has_frontmatter"],
        stats["manual"],
        stats["unresolved"],
        stats["failed"],
    )

    return 1 if stats["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
