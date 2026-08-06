"""Unit tests for provenance frontmatter (build_frontmatter + write_reference_file)."""

from unittest.mock import patch

import pytest
import yaml

from summarize_docs import MAIN_CONTENT_SELECTORS, build_frontmatter
from update_references import MANUAL_REFERENCE_MARKER, write_reference_file

# ---------------------------------------------------------------------------
# build_frontmatter
# ---------------------------------------------------------------------------


def test_build_frontmatter_parses_as_valid_yaml():
    """The block between the fences parses as YAML with the expected keys."""
    block = build_frontmatter(
        source="https://www.twingate.com/docs/connectors",
        type_="docs",
        fetched="2026-08-05",
        source_version="abc123",
    )

    assert block.startswith("---\n")
    assert block.endswith("---\n")

    inner = block[len("---\n") : -len("---\n")]
    parsed = yaml.safe_load(inner)

    assert parsed["source"] == "https://www.twingate.com/docs/connectors"
    assert parsed["type"] == "docs"
    # yaml.safe_load coerces an ISO date scalar to a date object; compare via str().
    assert str(parsed["fetched"]) == "2026-08-05"
    assert parsed["source_version"] == "abc123"


def test_build_frontmatter_help_type():
    """type_='help' round-trips through the block unchanged."""
    block = build_frontmatter(
        source="https://help.twingate.com/articles/123-some-slug",
        type_="help",
        fetched="2026-08-05",
        source_version="deadbeef",
    )
    inner = block[len("---\n") : -len("---\n")]
    parsed = yaml.safe_load(inner)
    assert parsed["type"] == "help"
    assert parsed["source"] == "https://help.twingate.com/articles/123-some-slug"


def test_build_frontmatter_closing_fence_followed_by_newline():
    """The closing '---' fence is followed by exactly a trailing newline."""
    block = build_frontmatter("https://example.com/x", "docs", "2026-01-01", "hash")
    assert block.endswith("---\n")
    assert block.count("---\n") == 2


def test_build_frontmatter_is_pure_function():
    """Same inputs always produce the same output (no hidden clock/IO)."""
    args = ("https://example.com/x", "docs", "2026-01-01", "hash")
    assert build_frontmatter(*args) == build_frontmatter(*args)


# ---------------------------------------------------------------------------
# MAIN_CONTENT_SELECTORS — help.twingate.com knowledge-base layout
# ---------------------------------------------------------------------------


def test_main_content_selectors_includes_kb_article_main():
    """The help-center article wrapper selector is present for extraction."""
    assert ".kb-article-main" in MAIN_CONTENT_SELECTORS


# ---------------------------------------------------------------------------
# write_reference_file — frontmatter precedes the body
# ---------------------------------------------------------------------------


def test_write_reference_file_frontmatter_precedes_body(tmp_path):
    """The frontmatter block is written before the summary body, not after."""
    skills_dir = tmp_path / "skills"

    with patch("update_references.SKILLS_DIR", skills_dir):
        output_path = write_reference_file(
            "twingate-connectors",
            "some-doc",
            "## Summary\nBody content here.",
            source="https://www.twingate.com/docs/some-doc",
            type_="docs",
            fetched="2026-08-05",
            source_version="cafebabe",
        )

    written = output_path.read_text(encoding="utf-8")
    frontmatter_end = written.index("---\n", 4) + len("---\n")
    body_start = written.index("## Summary")

    assert written.startswith("---\n")
    assert body_start > frontmatter_end
    assert written[frontmatter_end:body_start] == "\n"


# ---------------------------------------------------------------------------
# write_reference_file — manual-reference protection still holds
# ---------------------------------------------------------------------------


def _manual_content() -> str:
    return f"<!-- {MANUAL_REFERENCE_MARKER} -->\n\n# Hand-authored guide\n"


def test_write_reference_file_manual_reference_not_overwritten(tmp_path):
    """A file carrying the manual marker is never overwritten."""
    skills_dir = tmp_path / "skills"
    manual_file = skills_dir / "twingate-idfw" / "references" / "gateway-troubleshooting.md"
    manual_file.parent.mkdir(parents=True)
    manual_file.write_text(_manual_content(), encoding="utf-8")

    with (
        patch("update_references.SKILLS_DIR", skills_dir),
        pytest.raises(ValueError, match="hand-authored"),
    ):
        write_reference_file(
            "twingate-idfw",
            "gateway-troubleshooting",
            "## Generated content",
            source="https://www.twingate.com/docs/gateway-troubleshooting",
            type_="docs",
            fetched="2026-08-05",
            source_version="newversion",
        )

    assert manual_file.read_text(encoding="utf-8") == _manual_content()
