"""Unit tests for pipeline_metrics.py — churn metrics and shadow-hash cache helpers."""

import json
from typing import cast

import pytest

from pipeline_metrics import (
    COUNTER_FIELDS,
    SONNET_INPUT_USD_PER_MTOK,
    SONNET_OUTPUT_USD_PER_MTOK,
    GitHubRunMetrics,
    RunMetrics,
    emit,
    emit_github,
    load_norm_cache,
    save_norm_cache,
)

# ---------------------------------------------------------------------------
# RunMetrics.record
# ---------------------------------------------------------------------------


def test_record_unknown_event_raises() -> None:
    """An event name outside COUNTER_FIELDS raises ValueError."""
    metrics = RunMetrics()
    with pytest.raises(ValueError, match="Unknown metric event"):
        metrics.record("docs", "not_a_real_event")


def test_record_increments_the_named_counter() -> None:
    metrics = RunMetrics()
    metrics.record("docs", "fetched_ok")
    metrics.record("docs", "fetched_ok")

    assert metrics.sources["docs"]["fetched_ok"] == 2
    assert all(
        metrics.sources["docs"][f] == 0 for f in COUNTER_FIELDS if f != "fetched_ok"
    )


# ---------------------------------------------------------------------------
# RunMetrics.totals
# ---------------------------------------------------------------------------


def test_totals_sums_across_multiple_sources() -> None:
    metrics = RunMetrics()
    metrics.record("docs", "resummarized")
    metrics.record("docs", "real_change")
    metrics.record("help", "resummarized")
    metrics.record("help", "noise_only")
    metrics.record("help", "resummarized")
    metrics.record("help", "real_change")

    totals = metrics.totals()

    assert totals["resummarized"] == 3
    assert totals["real_change"] == 2
    assert totals["noise_only"] == 1
    assert totals["fetched_ok"] == 0


# ---------------------------------------------------------------------------
# RunMetrics.to_dict
# ---------------------------------------------------------------------------


def test_to_dict_has_expected_top_level_keys() -> None:
    metrics = RunMetrics()
    metrics.record("docs", "fetched_ok")

    snapshot = metrics.to_dict(run_ts="2026-08-05T00:00:00+00:00", wall_clock_s=1.5)

    assert set(snapshot) == {"run_ts", "wall_clock_seconds", "totals", "sources"}
    assert snapshot["run_ts"] == "2026-08-05T00:00:00+00:00"
    assert snapshot["wall_clock_seconds"] == 1.5
    totals = cast("dict[str, int]", snapshot["totals"])
    sources = cast("dict[str, dict[str, int]]", snapshot["sources"])
    assert totals["fetched_ok"] == 1
    assert sources["docs"]["fetched_ok"] == 1


def test_to_dict_noise_only_plus_real_change_equals_resummarized() -> None:
    """Every resummarize is classified as exactly one of noise_only/real_change."""
    metrics = RunMetrics()
    for _ in range(3):
        metrics.record("docs", "resummarized")
        metrics.record("docs", "noise_only")
    for _ in range(2):
        metrics.record("docs", "resummarized")
        metrics.record("docs", "real_change")

    totals = cast("dict[str, int]", metrics.to_dict(run_ts="ts", wall_clock_s=0.0)["totals"])

    assert totals["noise_only"] + totals["real_change"] == totals["resummarized"]
    assert totals["resummarized"] == 5


# ---------------------------------------------------------------------------
# load_norm_cache / save_norm_cache
# ---------------------------------------------------------------------------


def test_norm_cache_roundtrip(tmp_path) -> None:
    cache_file = tmp_path / "norm.json"
    data = {
        "https://example.com/docs/a": "hash-a",
        "https://example.com/docs/b": "hash-b",
    }

    save_norm_cache(data, cache_file)
    loaded = load_norm_cache(cache_file)

    assert loaded == data


def test_load_norm_cache_missing_file_returns_empty_dict(tmp_path) -> None:
    assert load_norm_cache(tmp_path / "nope.json") == {}


def test_save_norm_cache_writes_sorted_indented_json(tmp_path) -> None:
    cache_file = tmp_path / "norm.json"
    save_norm_cache({"b": "2", "a": "1"}, cache_file)

    raw = cache_file.read_text(encoding="utf-8")
    assert raw.index('"a"') < raw.index('"b"')
    assert "\n  " in raw


# ---------------------------------------------------------------------------
# emit
# ---------------------------------------------------------------------------


def test_emit_appends_one_jsonl_line_per_call(tmp_path) -> None:
    jsonl_path = tmp_path / "runs" / "pipeline-runs.jsonl"
    metrics = RunMetrics()
    metrics.record("docs", "fetched_ok")

    emit(metrics, run_ts="ts1", wall_clock_s=1.0, jsonl_path=jsonl_path, step_summary_path=None)
    emit(metrics, run_ts="ts2", wall_clock_s=2.0, jsonl_path=jsonl_path, step_summary_path=None)

    lines = jsonl_path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["run_ts"] == "ts1"
    assert json.loads(lines[1])["run_ts"] == "ts2"


def test_emit_prints_plain_text_summary_to_stdout(tmp_path, capsys) -> None:
    jsonl_path = tmp_path / "pipeline-runs.jsonl"
    metrics = RunMetrics()
    metrics.record("docs", "fetched_ok")

    emit(metrics, run_ts="ts", wall_clock_s=0.1, jsonl_path=jsonl_path, step_summary_path=None)

    captured = capsys.readouterr()
    assert "Pipeline churn metrics" in captured.out


def test_emit_writes_markdown_when_step_summary_path_given(tmp_path) -> None:
    jsonl_path = tmp_path / "pipeline-runs.jsonl"
    step_summary_path = tmp_path / "step-summary.md"
    metrics = RunMetrics()
    metrics.record("docs", "fetched_ok")

    emit(
        metrics,
        run_ts="ts",
        wall_clock_s=0.1,
        jsonl_path=jsonl_path,
        step_summary_path=str(step_summary_path),
    )

    written = step_summary_path.read_text(encoding="utf-8")
    assert "Pipeline churn metrics" in written


def test_emit_with_step_summary_path_none_does_not_touch_env(tmp_path, monkeypatch) -> None:
    """When step_summary_path is None, emit must not depend on the
    GITHUB_STEP_SUMMARY env var at all — deleting it must not matter."""
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    jsonl_path = tmp_path / "pipeline-runs.jsonl"
    metrics = RunMetrics()

    emit(metrics, run_ts="ts", wall_clock_s=0.0, jsonl_path=jsonl_path, step_summary_path=None)

    assert jsonl_path.exists()


# ---------------------------------------------------------------------------
# GitHubRunMetrics.append / to_aggregate
# ---------------------------------------------------------------------------


def _record(
    full_name: str = "Twingate/example-repo",
    mode: str = "delta",
    input_tokens: int = 0,
    output_tokens: int = 0,
    wall_clock_s: float = 0.0,
    diff_bytes: int = 0,
) -> dict[str, object]:
    """Build a build_metrics_record-shaped dict without importing github_summarize."""
    return {
        "full_name": full_name,
        "mode": mode,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "wall_clock_s": round(wall_clock_s, 3),
        "diff_bytes": diff_bytes,
    }


def test_github_run_metrics_append_accumulates_records() -> None:
    metrics = GitHubRunMetrics()
    metrics.append(_record(full_name="Twingate/a"))
    metrics.append(_record(full_name="Twingate/b"))

    assert len(metrics.records) == 2
    assert metrics.records[0]["full_name"] == "Twingate/a"
    assert metrics.records[1]["full_name"] == "Twingate/b"


def test_to_aggregate_sums_input_and_output_tokens_across_records() -> None:
    metrics = GitHubRunMetrics()
    metrics.append(_record(mode="delta", input_tokens=100, output_tokens=40))
    metrics.append(_record(mode="full", input_tokens=250, output_tokens=90))

    aggregate = metrics.to_aggregate(wall_clock_s=5.0)

    assert aggregate["repos_summarized"] == 2
    assert aggregate["total_input_tokens"] == 350
    assert aggregate["total_output_tokens"] == 130
    assert aggregate["total_wall_clock_s"] == 5.0


def test_to_aggregate_estimated_cost_uses_documented_rate() -> None:
    """estimated_cost_usd applies the documented per-MTok input/output rates."""
    metrics = GitHubRunMetrics()
    metrics.append(_record(input_tokens=1_000_000, output_tokens=1_000_000))

    aggregate = metrics.to_aggregate(wall_clock_s=0.0)

    expected = round(
        1_000_000 / 1_000_000 * SONNET_INPUT_USD_PER_MTOK
        + 1_000_000 / 1_000_000 * SONNET_OUTPUT_USD_PER_MTOK,
        4,
    )
    assert aggregate["estimated_cost_usd"] == expected
    assert aggregate["estimated_cost_usd"] == round(SONNET_INPUT_USD_PER_MTOK + SONNET_OUTPUT_USD_PER_MTOK, 4)


def test_to_aggregate_zero_tokens_yields_zero_cost() -> None:
    metrics = GitHubRunMetrics()
    metrics.append(_record(mode="stub", input_tokens=0, output_tokens=0))

    aggregate = metrics.to_aggregate(wall_clock_s=0.0)

    assert aggregate["estimated_cost_usd"] == 0.0


def test_to_aggregate_by_mode_counts_each_mode_independently() -> None:
    """by_mode counts delta/full/stub/wiki records independently, each with
    its own token sums."""
    metrics = GitHubRunMetrics()
    metrics.append(_record(mode="delta", input_tokens=10, output_tokens=5))
    metrics.append(_record(mode="delta", input_tokens=20, output_tokens=15))
    metrics.append(_record(mode="full", input_tokens=100, output_tokens=50))
    metrics.append(_record(mode="stub", input_tokens=0, output_tokens=0))
    metrics.append(_record(mode="wiki", input_tokens=7, output_tokens=3))

    by_mode = cast("dict[str, dict[str, int]]", metrics.to_aggregate(wall_clock_s=0.0)["by_mode"])

    assert by_mode["delta"]["count"] == 2
    assert by_mode["delta"]["input_tokens"] == 30
    assert by_mode["delta"]["output_tokens"] == 20
    assert by_mode["full"]["count"] == 1
    assert by_mode["full"]["input_tokens"] == 100
    assert by_mode["stub"]["count"] == 1
    assert by_mode["stub"]["input_tokens"] == 0
    assert by_mode["wiki"]["count"] == 1
    assert by_mode["wiki"]["input_tokens"] == 7


def test_to_aggregate_with_no_records_has_zero_totals() -> None:
    metrics = GitHubRunMetrics()

    aggregate = metrics.to_aggregate(wall_clock_s=1.0)

    assert aggregate["repos_summarized"] == 0
    assert aggregate["total_input_tokens"] == 0
    assert aggregate["total_output_tokens"] == 0
    assert aggregate["estimated_cost_usd"] == 0.0
    assert aggregate["by_mode"] == {}


# ---------------------------------------------------------------------------
# emit_github
# ---------------------------------------------------------------------------


def test_emit_github_appends_one_jsonl_line_per_call(tmp_path) -> None:
    jsonl_path = tmp_path / "runs" / "github-runs.jsonl"
    metrics = GitHubRunMetrics()
    metrics.append(_record(mode="full", input_tokens=10, output_tokens=5))

    emit_github(metrics, run_ts="ts1", wall_clock_s=1.0, jsonl_path=jsonl_path, step_summary_path=None)
    emit_github(metrics, run_ts="ts2", wall_clock_s=2.0, jsonl_path=jsonl_path, step_summary_path=None)

    lines = jsonl_path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["run_ts"] == "ts1"
    assert json.loads(lines[1])["run_ts"] == "ts2"


def test_emit_github_prints_plain_text_summary_to_stdout(tmp_path, capsys) -> None:
    jsonl_path = tmp_path / "github-runs.jsonl"
    metrics = GitHubRunMetrics()
    metrics.append(_record(mode="delta"))

    emit_github(metrics, run_ts="ts", wall_clock_s=0.1, jsonl_path=jsonl_path, step_summary_path=None)

    captured = capsys.readouterr()
    assert "GitHub pipeline source metrics" in captured.out


def test_emit_github_writes_markdown_when_step_summary_path_given(tmp_path) -> None:
    jsonl_path = tmp_path / "github-runs.jsonl"
    step_summary_path = tmp_path / "step-summary.md"
    metrics = GitHubRunMetrics()
    metrics.append(_record(mode="full"))

    emit_github(
        metrics,
        run_ts="ts",
        wall_clock_s=0.1,
        jsonl_path=jsonl_path,
        step_summary_path=str(step_summary_path),
    )

    written = step_summary_path.read_text(encoding="utf-8")
    assert "GitHub pipeline source metrics" in written
