"""Unit tests for the --claude-code mode in test_pipeline.py."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

import sys

SCRIPTS_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from test_pipeline import claude_code_mode  # noqa: E402
from summarize_docs import SYSTEM_PROMPT  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fake_mapping(tmp_path: Path) -> dict:
    """Minimal doc_mapping.yaml content for tests."""
    return {
        "docs": [
            {
                "url": "https://www.twingate.com/docs/how-twingate-works",
                "skill": "twingate-architect",
                "keywords": ["architecture"],
            }
        ],
        "auto_assign_patterns": [],
    }


def _fake_html() -> str:
    return "<html><body><p>Twingate architecture overview.</p></body></html>"


def _fake_summary() -> str:
    return "# How Twingate Works\n\nSummary of architecture.\n"


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_claude_code_mode_invokes_subprocess_with_correct_prompt(tmp_path: Path) -> None:
    """--claude-code mode passes system prompt + user message to the subprocess."""
    target_url = "https://www.twingate.com/docs/how-twingate-works"

    fake_result = MagicMock()
    fake_result.returncode = 0
    fake_result.stdout = _fake_summary()
    fake_result.stderr = ""

    with (
        patch("test_pipeline.load_mapping", return_value=_fake_mapping(tmp_path)),
        patch("test_pipeline.fetch_doc_html", return_value=_fake_html()),
        patch("test_pipeline.SKILLS_DIR", tmp_path / "skills"),
        patch("subprocess.run", return_value=fake_result) as mock_run,
    ):
        claude_code_mode(target_url, count=1)

    # subprocess.run must have been called once.
    assert mock_run.call_count == 1

    call_args = mock_run.call_args
    cmd = call_args[0][0]  # first positional arg is the command list

    # Command must include the claude CLI with --print flag.
    assert cmd[0] == "claude"
    assert "--print" in cmd

    # The combined prompt argument must contain the system prompt.
    combined_prompt = cmd[-1]
    assert SYSTEM_PROMPT[:50] in combined_prompt

    # The combined prompt must contain the doc URL.
    assert target_url in combined_prompt


def test_claude_code_mode_writes_reference_file(tmp_path: Path) -> None:
    """--claude-code mode writes the summary to the correct reference file path."""
    target_url = "https://www.twingate.com/docs/how-twingate-works"

    fake_result = MagicMock()
    fake_result.returncode = 0
    fake_result.stdout = _fake_summary()
    fake_result.stderr = ""

    skills_dir = tmp_path / "skills"

    with (
        patch("test_pipeline.load_mapping", return_value=_fake_mapping(tmp_path)),
        patch("test_pipeline.fetch_doc_html", return_value=_fake_html()),
        patch("test_pipeline.SKILLS_DIR", skills_dir),
        patch("subprocess.run", return_value=fake_result),
    ):
        claude_code_mode(target_url, count=1)

    expected_path = skills_dir / "twingate-architect" / "references" / "how-twingate-works.md"
    assert expected_path.exists(), f"Expected reference file not found: {expected_path}"
    assert _fake_summary().strip() in expected_path.read_text(encoding="utf-8")


def test_claude_code_mode_handles_subprocess_failure(tmp_path: Path, capsys: pytest.CaptureFixture) -> None:
    """--claude-code mode logs the error and counts as failed on non-zero returncode."""
    target_url = "https://www.twingate.com/docs/how-twingate-works"

    fake_result = MagicMock()
    fake_result.returncode = 1
    fake_result.stdout = ""
    fake_result.stderr = "some error"

    skills_dir = tmp_path / "skills"

    with (
        patch("test_pipeline.load_mapping", return_value=_fake_mapping(tmp_path)),
        patch("test_pipeline.fetch_doc_html", return_value=_fake_html()),
        patch("test_pipeline.SKILLS_DIR", skills_dir),
        patch("subprocess.run", return_value=fake_result),
    ):
        claude_code_mode(target_url, count=1)

    out = capsys.readouterr().out
    assert "ERROR" in out
    assert "0 written, 1 failed" in out

    # No file should have been written.
    ref_dir = skills_dir / "twingate-architect" / "references"
    assert not ref_dir.exists() or not any(ref_dir.iterdir())


def test_claude_code_mode_count_processes_multiple_docs(tmp_path: Path) -> None:
    """--claude-code --count N processes N docs from the mapping when no URL is given."""
    mapping = {
        "docs": [
            {"url": "https://www.twingate.com/docs/doc-one", "skill": "twingate-architect", "keywords": []},
            {"url": "https://www.twingate.com/docs/doc-two", "skill": "twingate-connectors", "keywords": []},
        ],
        "auto_assign_patterns": [],
    }

    fake_result = MagicMock()
    fake_result.returncode = 0
    fake_result.stdout = "# Summary\n"
    fake_result.stderr = ""

    skills_dir = tmp_path / "skills"

    with (
        patch("test_pipeline.load_mapping", return_value=mapping),
        patch("test_pipeline.fetch_doc_html", return_value=_fake_html()),
        patch("test_pipeline.SKILLS_DIR", skills_dir),
        patch("subprocess.run", return_value=fake_result) as mock_run,
    ):
        claude_code_mode(None, count=2)

    assert mock_run.call_count == 2
    assert (skills_dir / "twingate-architect" / "references" / "doc-one.md").exists()
    assert (skills_dir / "twingate-connectors" / "references" / "doc-two.md").exists()
