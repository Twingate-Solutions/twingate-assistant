"""Unit tests for backfill_frontmatter.py."""

from pathlib import Path

import yaml

from backfill_frontmatter import (
    build_inverse_index,
    has_frontmatter,
    main,
    process_file,
    run_backfill,
)
from diff_docs import load_mapping
from update_references import MANUAL_REFERENCE_MARKER, url_to_slug

# A real doc_mapping.yaml entry, so the inverse index resolves via the genuine mapping.
REAL_URL = "https://www.twingate.com/docs/connector-deployment"
REAL_SKILL = "twingate-connectors"
REAL_SLUG = url_to_slug(REAL_URL)  # "connector-deployment"


def _manual_content() -> str:
    return f"<!-- {MANUAL_REFERENCE_MARKER} -->\n\n# Hand-authored guide\n"


def _make_fixture_tree(skills_dir: Path) -> Path:
    """Build a tmp skills/ tree with one real-mapping file, one file already
    carrying frontmatter, and one manual-reference file. Returns the path of
    the real-mapping generated file (pre-backfill)."""
    refs_dir = skills_dir / REAL_SKILL / "references"
    refs_dir.mkdir(parents=True)

    generated_file = refs_dir / f"{REAL_SLUG}.md"
    generated_file.write_text(
        "## Connector Deployment\nDeploy connectors on Docker or Kubernetes.\n",
        encoding="utf-8",
    )

    already_has_frontmatter = refs_dir / "already-fronted.md"
    already_has_frontmatter.write_text(
        "---\nsource: https://www.twingate.com/docs/already-fronted\n"
        "type: docs\nfetched: 2026-01-01\nsource_version: existing\n---\n\n"
        "## Already has frontmatter\n",
        encoding="utf-8",
    )

    manual_dir = skills_dir / "twingate-idfw" / "references"
    manual_dir.mkdir(parents=True)
    manual_file = manual_dir / "gateway-troubleshooting.md"
    manual_file.write_text(_manual_content(), encoding="utf-8")

    return generated_file


# ---------------------------------------------------------------------------
# build_inverse_index — real mapping + real url_to_slug
# ---------------------------------------------------------------------------


def test_build_inverse_index_resolves_real_mapping_entry(tmp_path):
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()
    mapping = load_mapping()  # the real scripts/doc_mapping.yaml

    index = build_inverse_index(mapping, skills_dir)

    expected_path = (skills_dir / REAL_SKILL / "references" / f"{REAL_SLUG}.md").resolve()
    assert index[expected_path] == REAL_URL


# ---------------------------------------------------------------------------
# has_frontmatter
# ---------------------------------------------------------------------------


def test_has_frontmatter_detects_leading_fence():
    assert has_frontmatter("---\nsource: x\n---\n\nbody") is True


def test_has_frontmatter_false_for_bare_body():
    assert has_frontmatter("## Summary\nNo frontmatter here.") is False


def test_has_frontmatter_accepts_crlf():
    assert has_frontmatter("---\r\nsource: x\r\n---\r\n\r\nbody") is True


# ---------------------------------------------------------------------------
# run_backfill — mappable file gets valid frontmatter with resolved source
# ---------------------------------------------------------------------------


def test_backfill_prepends_frontmatter_to_mappable_file(tmp_path):
    skills_dir = tmp_path / "skills"
    generated_file = _make_fixture_tree(skills_dir)
    original_body = generated_file.read_text(encoding="utf-8")

    stats = run_backfill(skills_dir, fetched="2026-08-05", apply=True)

    written = generated_file.read_text(encoding="utf-8")
    assert written.startswith("---\n")
    _, frontmatter_block, body = written.split("---\n", 2)
    parsed = yaml.safe_load(frontmatter_block)

    assert parsed["source"] == REAL_URL
    assert parsed["type"] == "docs"
    assert parsed["fetched"] == "2026-08-05" or str(parsed["fetched"]) == "2026-08-05"
    assert body == "\n" + original_body

    assert stats["backfilled"] == 1
    assert stats["manual"] == 1
    assert stats["has_frontmatter"] == 1
    assert stats["unresolved"] == 0
    assert stats["failed"] == 0
    assert stats["total"] == 3


# ---------------------------------------------------------------------------
# Idempotency — running twice never double-prepends
# ---------------------------------------------------------------------------


def test_backfill_is_idempotent_across_two_runs(tmp_path):
    skills_dir = tmp_path / "skills"
    generated_file = _make_fixture_tree(skills_dir)

    run_backfill(skills_dir, fetched="2026-08-05", apply=True)
    first_pass_content = generated_file.read_text(encoding="utf-8")

    second_stats = run_backfill(skills_dir, fetched="2026-08-06", apply=True)
    second_pass_content = generated_file.read_text(encoding="utf-8")

    assert second_pass_content == first_pass_content
    assert second_pass_content.count("---\n") == 2
    assert second_stats["backfilled"] == 0
    assert second_stats["has_frontmatter"] == 2


# ---------------------------------------------------------------------------
# Files already carrying frontmatter are skipped
# ---------------------------------------------------------------------------


def test_backfill_skips_file_already_carrying_frontmatter(tmp_path):
    skills_dir = tmp_path / "skills"
    _make_fixture_tree(skills_dir)
    refs_dir = skills_dir / REAL_SKILL / "references"
    already_fronted = refs_dir / "already-fronted.md"
    before = already_fronted.read_text(encoding="utf-8")

    stats = run_backfill(skills_dir, fetched="2026-08-05", apply=True)

    assert already_fronted.read_text(encoding="utf-8") == before
    assert stats["has_frontmatter"] == 1


# ---------------------------------------------------------------------------
# Manual-reference files are never touched
# ---------------------------------------------------------------------------


def test_backfill_never_touches_manual_reference_file(tmp_path):
    skills_dir = tmp_path / "skills"
    _make_fixture_tree(skills_dir)
    manual_file = skills_dir / "twingate-idfw" / "references" / "gateway-troubleshooting.md"
    before = manual_file.read_text(encoding="utf-8")

    stats = run_backfill(skills_dir, fetched="2026-08-05", apply=True)

    assert manual_file.read_text(encoding="utf-8") == before
    assert stats["manual"] == 1


# ---------------------------------------------------------------------------
# Dry-run writes nothing
# ---------------------------------------------------------------------------


def test_backfill_dry_run_writes_nothing(tmp_path):
    skills_dir = tmp_path / "skills"
    generated_file = _make_fixture_tree(skills_dir)
    before = generated_file.read_text(encoding="utf-8")

    stats = run_backfill(skills_dir, fetched="2026-08-05", apply=False)

    assert generated_file.read_text(encoding="utf-8") == before
    assert stats["backfilled"] == 1  # classified as "would backfill", nothing written


# ---------------------------------------------------------------------------
# Unresolved file (no mapping entry, no legacy URL comment)
# ---------------------------------------------------------------------------


def test_process_file_reports_unresolved_when_no_mapping_or_comment(tmp_path):
    skills_dir = tmp_path / "skills"
    refs_dir = skills_dir / "twingate-connectors" / "references"
    refs_dir.mkdir(parents=True)
    orphan = refs_dir / "totally-unmapped-slug.md"
    orphan.write_text("## Some content with no provenance\n", encoding="utf-8")

    outcome = process_file(orphan, inverse_index={}, fetched="2026-08-05", apply=True)

    assert outcome == "unresolved"
    assert orphan.read_text(encoding="utf-8") == "## Some content with no provenance\n"


# ---------------------------------------------------------------------------
# CLI entry point — --skills-dir override + --apply/--dry-run
# ---------------------------------------------------------------------------


def test_main_cli_dry_run_by_default_writes_nothing(tmp_path):
    skills_dir = tmp_path / "skills"
    generated_file = _make_fixture_tree(skills_dir)
    before = generated_file.read_text(encoding="utf-8")

    exit_code = main(["--skills-dir", str(skills_dir), "--fetched", "2026-08-05"])

    assert exit_code == 0
    assert generated_file.read_text(encoding="utf-8") == before


def test_main_cli_apply_backfills_and_returns_zero(tmp_path):
    skills_dir = tmp_path / "skills"
    generated_file = _make_fixture_tree(skills_dir)

    exit_code = main(["--apply", "--skills-dir", str(skills_dir), "--fetched", "2026-08-05"])

    assert exit_code == 0
    assert generated_file.read_text(encoding="utf-8").startswith("---\n")
