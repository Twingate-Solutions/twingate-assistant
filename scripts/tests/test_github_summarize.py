"""Unit tests for github_summarize.py — the LLM half of the GitHub pipeline source."""

import dataclasses

import pytest
from unittest.mock import MagicMock, patch

import github_summarize
from github_summarize import (
    MAX_DELTA_FILES,
    SummaryResult,
    build_metrics_record,
    summarize_repo_delta,
    summarize_repo_full,
)
from summarize_docs import MAX_TEXT_LENGTH


def _mock_message(text: str = "## Summary", input_tokens: int = 100, output_tokens: int = 50):
    """Build a mock anthropic Message with a text content block and usage."""
    block = MagicMock()
    block.text = text
    message = MagicMock()
    message.content = [block]
    message.usage = MagicMock(input_tokens=input_tokens, output_tokens=output_tokens)
    return message


# ── SummaryResult ────────────────────────────────────────────────────────────


def test_summary_result_is_frozen() -> None:
    """SummaryResult is an immutable dataclass — assignment raises."""
    result = SummaryResult(text="x", input_tokens=1, output_tokens=2, model="claude-x")
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.text = "y"  # type: ignore[misc]


def test_summary_result_carries_all_fields() -> None:
    result = SummaryResult(text="body", input_tokens=10, output_tokens=20, model="claude-x")
    assert result.text == "body"
    assert result.input_tokens == 10
    assert result.output_tokens == 20
    assert result.model == "claude-x"


# ── MAX_DELTA_FILES ──────────────────────────────────────────────────────────


def test_max_delta_files_constant() -> None:
    assert MAX_DELTA_FILES == 30


# ── summarize_repo_delta ─────────────────────────────────────────────────────


@patch("github_summarize.anthropic.Anthropic")
def test_summarize_repo_delta_sends_prior_doc_diff_and_metadata(mock_anthropic_cls) -> None:
    """The user message sent to messages.create carries the prior doc text,
    the filtered diff text, and the repo metadata (full_name)."""
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.return_value = _mock_message(
        text="## Updated Summary", input_tokens=250, output_tokens=90
    )
    metadata = {
        "full_name": "Twingate/example-repo",
        "description": "An example repo",
        "default_branch": "main",
    }

    result = summarize_repo_delta(
        "This is the prior summary body.", "This is the filtered diff patch text.", metadata
    )

    assert isinstance(result, SummaryResult)
    assert result.text == "## Updated Summary"
    assert result.input_tokens == 250
    assert result.output_tokens == 90
    assert result.model == github_summarize.CLAUDE_MODEL

    mock_client.messages.create.assert_called_once()
    sent_kwargs = mock_client.messages.create.call_args.kwargs
    user_message = sent_kwargs["messages"][0]["content"]
    assert "This is the prior summary body." in user_message
    assert "This is the filtered diff patch text." in user_message
    assert "Twingate/example-repo" in user_message


@patch("github_summarize.anthropic.Anthropic")
def test_summarize_repo_delta_makes_exactly_one_api_call(mock_anthropic_cls) -> None:
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.return_value = _mock_message()

    summarize_repo_delta("prior", "diff", {"full_name": "Twingate/r"})

    assert mock_client.messages.create.call_count == 1


@patch("github_summarize.anthropic.Anthropic")
def test_summarize_repo_delta_token_usage_comes_from_message_usage(mock_anthropic_cls) -> None:
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.return_value = _mock_message(input_tokens=777, output_tokens=333)

    result = summarize_repo_delta("prior", "diff", {"full_name": "Twingate/r"})

    assert result.input_tokens == 777
    assert result.output_tokens == 333


# ── summarize_repo_full ──────────────────────────────────────────────────────


@patch("github_summarize.anthropic.Anthropic")
def test_summarize_repo_full_sends_readme_in_corpus(mock_anthropic_cls) -> None:
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.return_value = _mock_message(
        text="## Fresh Summary", input_tokens=300, output_tokens=120
    )
    metadata = {"full_name": "Twingate/example-repo"}

    result = summarize_repo_full("This is the README content.", [], metadata)

    assert result.text == "## Fresh Summary"
    assert result.input_tokens == 300
    assert result.output_tokens == 120

    sent_kwargs = mock_client.messages.create.call_args.kwargs
    user_message = sent_kwargs["messages"][0]["content"]
    assert "This is the README content." in user_message
    assert "Twingate/example-repo" in user_message


@patch("github_summarize.anthropic.Anthropic")
def test_summarize_repo_full_includes_key_docs(mock_anthropic_cls) -> None:
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.return_value = _mock_message()

    summarize_repo_full("README body", ["Extra doc file content"], {"full_name": "Twingate/r"})

    sent_kwargs = mock_client.messages.create.call_args.kwargs
    user_message = sent_kwargs["messages"][0]["content"]
    assert "Extra doc file content" in user_message


@patch("github_summarize.anthropic.Anthropic")
def test_summarize_repo_full_truncates_oversized_corpus(mock_anthropic_cls) -> None:
    """A corpus over MAX_TEXT_LENGTH is truncated with a marker."""
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.return_value = _mock_message()
    huge_readme = "x" * (MAX_TEXT_LENGTH + 5000)

    summarize_repo_full(huge_readme, [], {"full_name": "Twingate/big-repo"})

    sent_kwargs = mock_client.messages.create.call_args.kwargs
    user_message = sent_kwargs["messages"][0]["content"]
    assert "[Content truncated for length]" in user_message
    assert len(user_message) < len(huge_readme)


@patch("github_summarize.anthropic.Anthropic")
def test_summarize_repo_full_makes_exactly_one_api_call(mock_anthropic_cls) -> None:
    mock_client = mock_anthropic_cls.return_value
    mock_client.messages.create.return_value = _mock_message()

    summarize_repo_full("readme", [], {"full_name": "Twingate/r"})

    assert mock_client.messages.create.call_count == 1


# ── build_metrics_record ─────────────────────────────────────────────────────


def test_build_metrics_record_with_no_result_has_zero_tokens() -> None:
    """A stub repo (or a failed call) passes result=None; tokens are zero."""
    record = build_metrics_record(
        full_name="Twingate/stub-repo", mode="stub", result=None, wall_clock_s=0.0, diff_bytes=0
    )
    assert record == {
        "full_name": "Twingate/stub-repo",
        "mode": "stub",
        "input_tokens": 0,
        "output_tokens": 0,
        "wall_clock_s": 0.0,
        "diff_bytes": 0,
    }


def test_build_metrics_record_with_result_uses_its_token_counts() -> None:
    result = SummaryResult(text="t", input_tokens=111, output_tokens=222, model="claude-x")

    record = build_metrics_record(
        full_name="Twingate/example-repo",
        mode="delta",
        result=result,
        wall_clock_s=1.23456,
        diff_bytes=999,
    )

    assert record["full_name"] == "Twingate/example-repo"
    assert record["mode"] == "delta"
    assert record["input_tokens"] == 111
    assert record["output_tokens"] == 222
    assert record["diff_bytes"] == 999
    assert record["wall_clock_s"] == round(1.23456, 3)


@pytest.mark.parametrize("mode", ["delta", "full", "stub", "wiki"])
def test_build_metrics_record_accepts_every_known_mode(mode: str) -> None:
    record = build_metrics_record(
        full_name="Twingate/r", mode=mode, result=None, wall_clock_s=0.0, diff_bytes=0
    )
    assert record["mode"] == mode
