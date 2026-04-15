"""Compare sitemap URLs against doc_mapping.yaml to detect changes.

This module identifies new and removed documentation pages by diffing
the live sitemap URL list against the URLs already tracked in
``doc_mapping.yaml``. New URLs can be auto-assigned to a skill based
on URL path patterns defined in the mapping file.
"""

import logging
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

DEFAULT_MAPPING_PATH = Path(__file__).parent / "doc_mapping.yaml"


def load_mapping(mapping_path: str | Path = DEFAULT_MAPPING_PATH) -> dict:
    """Load and return the parsed doc_mapping.yaml file.

    Args:
        mapping_path: Filesystem path to the YAML mapping file.
            Defaults to ``doc_mapping.yaml`` in the same directory
            as this script.

    Returns:
        The parsed YAML document as a dictionary.

    Raises:
        FileNotFoundError: If the mapping file does not exist.
        yaml.YAMLError: If the file contains invalid YAML.
    """
    path = Path(mapping_path)
    logger.info("Loading doc mapping from %s", path)
    with path.open("r", encoding="utf-8") as fh:
        data: dict = yaml.safe_load(fh) or {}
    doc_count = len(data.get("docs", []))
    pattern_count = len(data.get("auto_assign_patterns", []))
    logger.info(
        "Loaded mapping: %d docs, %d auto-assign patterns",
        doc_count,
        pattern_count,
    )
    return data


def diff_docs(
    sitemap_urls: list[str],
    mapping_path: str | Path = DEFAULT_MAPPING_PATH,
) -> tuple[list[str], list[str]]:
    """Compare sitemap URLs against doc_mapping.yaml.

    Computes which URLs are new (present in the sitemap but not in the
    mapping) and which are removed (present in the mapping but no longer
    in the sitemap).

    Args:
        sitemap_urls: List of documentation URLs discovered from the
            live sitemap.
        mapping_path: Filesystem path to the YAML mapping file.

    Returns:
        A tuple of ``(new_urls, removed_urls)`` where each element is
        a sorted list of URL strings.
    """
    mapping = load_mapping(mapping_path)
    mapped_urls: set[str] = {
        entry["url"] for entry in mapping.get("docs", []) if "url" in entry
    }
    sitemap_set: set[str] = set(sitemap_urls)

    new_urls = sorted(sitemap_set - mapped_urls)
    removed_urls = sorted(mapped_urls - sitemap_set)

    logger.info(
        "Diff result: %d new URLs, %d removed URLs",
        len(new_urls),
        len(removed_urls),
    )
    if new_urls:
        logger.info("New URLs: %s", new_urls)
    if removed_urls:
        logger.info("Removed URLs: %s", removed_urls)

    return new_urls, removed_urls


def auto_assign(url: str, patterns: list[dict]) -> str | None:
    """Try to assign a new URL to a skill based on URL path patterns.

    Iterates through the pattern list in order and returns the skill
    for the first pattern whose ``pattern`` value is a substring of the
    URL. Returns ``None`` if no pattern matches.

    Args:
        url: The documentation URL to classify.
        patterns: A list of pattern dictionaries, each with ``pattern``
            (a substring to match) and ``skill`` (the target skill name).
            First matching pattern wins.

    Returns:
        The skill name string if a pattern matches, or ``None`` if no
        pattern matches the URL.
    """
    for entry in patterns:
        pattern = entry.get("pattern", "")
        skill = entry.get("skill")
        if pattern and pattern in url:
            logger.debug("URL %s matched pattern %r -> %s", url, pattern, skill)
            return skill
    logger.debug("URL %s did not match any auto-assign pattern", url)
    return None


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    # Quick self-test: load mapping and show stats
    mapping = load_mapping()
    docs = mapping.get("docs", [])
    patterns = mapping.get("auto_assign_patterns", [])
    print(f"Loaded {len(docs)} mapped docs, {len(patterns)} auto-assign patterns")

    # Example: diff against the mapped URLs themselves (should produce no diff)
    mapped_urls = [entry["url"] for entry in docs if "url" in entry]
    new, removed = diff_docs(mapped_urls)
    print(f"Self-diff: {len(new)} new, {len(removed)} removed (expected 0, 0)")
