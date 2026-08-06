"""Churn-attribution and cost metrics for the docs update pipeline."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import cast

SCRIPTS_DIR = Path(__file__).parent

NORM_HASH_CACHE_PATH = SCRIPTS_DIR / ".doc_norm_hashes.json"

# Per-source counter fields, in display order.
COUNTER_FIELDS: tuple[str, ...] = (
    "fetched_ok",
    "fetch_fail",
    "skipped",
    "resummarized",
    "noise_only",
    "real_change",
    "triaged",
    "manual_skipped",
)

# Approximate Claude Sonnet pricing (USD per million tokens).
SONNET_INPUT_USD_PER_MTOK = 3.0
SONNET_OUTPUT_USD_PER_MTOK = 15.0

GITHUB_MODES: tuple[str, ...] = ("delta", "full", "stub", "wiki")


def load_norm_cache(path: Path = NORM_HASH_CACHE_PATH) -> dict[str, str]:
    """Load the URL-to-normalized-hash shadow cache from disk.

    Args:
        path: Filesystem path to the JSON cache file.

    Returns:
        A dict mapping doc URLs to normalized SHA-256 hex digests; empty if
        the file does not exist.
    """
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)  # type: ignore[no-any-return]


def save_norm_cache(cache: dict[str, str], path: Path = NORM_HASH_CACHE_PATH) -> None:
    """Persist the URL-to-normalized-hash shadow cache to disk.

    Args:
        cache: Dict mapping doc URLs to normalized SHA-256 hex digests.
        path: Filesystem path to write the JSON file.
    """
    with path.open("w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=2, sort_keys=True)


@dataclass
class RunMetrics:
    """Accumulates per-source pipeline counters for one run."""

    sources: dict[str, dict[str, int]] = field(default_factory=dict)

    def _bucket(self, source: str) -> dict[str, int]:
        """Return (creating if needed) the zeroed counter bucket for ``source``."""
        return self.sources.setdefault(source, {f: 0 for f in COUNTER_FIELDS})

    def record(self, source: str, event: str) -> None:
        """Increment one counter for one source.

        Args:
            source: Source name the event belongs to (e.g. ``"docs"``).
            event: One of :data:`COUNTER_FIELDS`.

        Raises:
            ValueError: If ``event`` is not a known counter field.
        """
        if event not in COUNTER_FIELDS:
            raise ValueError(f"Unknown metric event: {event!r}")
        self._bucket(source)[event] += 1

    def totals(self) -> dict[str, int]:
        """Return the per-field sums across all sources."""
        out = {f: 0 for f in COUNTER_FIELDS}
        for counts in self.sources.values():
            for f in COUNTER_FIELDS:
                out[f] += counts.get(f, 0)
        return out

    def to_dict(self, *, run_ts: str, wall_clock_s: float) -> dict[str, object]:
        """Return a JSON-serializable snapshot for one JSONL line.

        Args:
            run_ts: ISO-8601 UTC timestamp for when the run finished.
            wall_clock_s: Wall-clock duration of the run in seconds.

        Returns:
            A dict with run timestamp, wall-clock seconds, per-field
            ``totals``, and per-``sources`` counters.
        """
        return {
            "run_ts": run_ts,
            "wall_clock_seconds": round(wall_clock_s, 3),
            "totals": self.totals(),
            "sources": {
                name: dict(self.sources[name]) for name in sorted(self.sources)
            },
        }

    def plain_text_summary(self) -> str:
        """Return a human-readable multi-line summary for stdout."""
        totals = self.totals()
        lines = ["Pipeline churn metrics (observation only):"]
        for name in sorted(self.sources):
            counts = self.sources[name]
            lines.append(
                f"  [{name}] fetched_ok={counts['fetched_ok']} "
                f"fetch_fail={counts['fetch_fail']} "
                f"skipped={counts['skipped']} "
                f"resummarized={counts['resummarized']} "
                f"(noise_only={counts['noise_only']}, "
                f"real_change={counts['real_change']}) "
                f"triaged={counts['triaged']} "
                f"manual_skipped={counts['manual_skipped']}"
            )
        lines.append(
            f"  [TOTAL] resummarized={totals['resummarized']} "
            f"(noise_only={totals['noise_only']}, "
            f"real_change={totals['real_change']}) "
            f"skipped={totals['skipped']} "
            f"fetch_fail={totals['fetch_fail']}"
        )
        return "\n".join(lines)

    def markdown_summary(self) -> str:
        """Return a GitHub-flavored markdown table (for GITHUB_STEP_SUMMARY)."""
        header = (
            "### Pipeline churn metrics (observation only)\n\n"
            "| source | fetched_ok | fetch_fail | skipped | resummarized "
            "| noise_only | real_change | triaged | manual_skipped |\n"
            "|---|---|---|---|---|---|---|---|---|\n"
        )
        rows = []
        for name in sorted(self.sources):
            c = self.sources[name]
            rows.append(
                f"| {name} | {c['fetched_ok']} | {c['fetch_fail']} | "
                f"{c['skipped']} | {c['resummarized']} | {c['noise_only']} | "
                f"{c['real_change']} | {c['triaged']} | {c['manual_skipped']} |"
            )
        t = self.totals()
        rows.append(
            f"| **total** | {t['fetched_ok']} | {t['fetch_fail']} | "
            f"{t['skipped']} | {t['resummarized']} | {t['noise_only']} | "
            f"{t['real_change']} | {t['triaged']} | {t['manual_skipped']} |"
        )
        return header + "\n".join(rows) + "\n"


def _as_int(value: object) -> int:
    """Coerce a metrics-record field to ``int``.

    Args:
        value: Value pulled from a per-repo record dict.

    Returns:
        ``int(value)`` when ``value`` is an ``int``, ``float``, or numeric
        ``str``; ``0`` otherwise.
    """
    if isinstance(value, (int, float, str)):
        return int(value)
    return 0


@dataclass
class GitHubRunMetrics:
    """Accumulates per-repo LLM summarization records for one GitHub pipeline run."""

    records: list[dict[str, object]] = field(default_factory=list)

    def append(self, record: dict[str, object]) -> None:
        """Append one per-repo (or per-wiki) summarization record.

        Args:
            record: A summarization record dict.
        """
        self.records.append(record)

    def _estimated_cost_usd(self, input_tokens: int, output_tokens: int) -> float:
        """Return the approximate USD cost for the given token counts."""
        return (
            input_tokens / 1_000_000 * SONNET_INPUT_USD_PER_MTOK
            + output_tokens / 1_000_000 * SONNET_OUTPUT_USD_PER_MTOK
        )

    def to_aggregate(self, *, wall_clock_s: float) -> dict[str, object]:
        """Return a JSON-serializable aggregate summary of this run.

        Args:
            wall_clock_s: Wall-clock duration of the GitHub step in seconds.

        Returns:
            A dict with ``repos_summarized``, ``total_input_tokens``,
            ``total_output_tokens``, ``estimated_cost_usd``,
            ``total_wall_clock_s``, and a ``by_mode`` breakdown (count and
            token totals per mode).
        """
        total_input = sum(_as_int(r.get("input_tokens", 0)) for r in self.records)
        total_output = sum(_as_int(r.get("output_tokens", 0)) for r in self.records)

        by_mode: dict[str, dict[str, int]] = {}
        for record in self.records:
            mode = str(record.get("mode", "unknown"))
            bucket = by_mode.setdefault(
                mode, {"count": 0, "input_tokens": 0, "output_tokens": 0}
            )
            bucket["count"] += 1
            bucket["input_tokens"] += _as_int(record.get("input_tokens", 0))
            bucket["output_tokens"] += _as_int(record.get("output_tokens", 0))

        return {
            "repos_summarized": len(self.records),
            "total_input_tokens": total_input,
            "total_output_tokens": total_output,
            "estimated_cost_usd": round(
                self._estimated_cost_usd(total_input, total_output), 4
            ),
            "total_wall_clock_s": round(wall_clock_s, 3),
            "by_mode": {name: by_mode[name] for name in sorted(by_mode)},
        }

    def plain_text_summary(self, *, wall_clock_s: float) -> str:
        """Return a human-readable multi-line summary for stdout."""
        aggregate = self.to_aggregate(wall_clock_s=wall_clock_s)
        lines = [
            "GitHub pipeline source metrics:",
            f"  repos_summarized={aggregate['repos_summarized']} "
            f"total_input_tokens={aggregate['total_input_tokens']} "
            f"total_output_tokens={aggregate['total_output_tokens']} "
            f"estimated_cost_usd={aggregate['estimated_cost_usd']} "
            f"total_wall_clock_s={aggregate['total_wall_clock_s']}",
        ]
        by_mode = cast(dict[str, dict[str, int]], aggregate["by_mode"])
        for mode in sorted(by_mode):
            counts = by_mode[mode]
            lines.append(
                f"  [{mode}] count={counts['count']} "
                f"input_tokens={counts['input_tokens']} "
                f"output_tokens={counts['output_tokens']}"
            )
        return "\n".join(lines)

    def markdown_summary(self, *, wall_clock_s: float) -> str:
        """Return a GitHub-flavored markdown table (for ``GITHUB_STEP_SUMMARY``)."""
        aggregate = self.to_aggregate(wall_clock_s=wall_clock_s)
        by_mode = cast(dict[str, dict[str, int]], aggregate["by_mode"])
        header = (
            "### GitHub pipeline source metrics\n\n"
            f"Repos summarized: **{aggregate['repos_summarized']}** | "
            f"Total input tokens: **{aggregate['total_input_tokens']}** | "
            f"Total output tokens: **{aggregate['total_output_tokens']}** | "
            f"Estimated cost: **${aggregate['estimated_cost_usd']}** | "
            f"Wall clock: **{aggregate['total_wall_clock_s']}s**\n\n"
            "| mode | count | input_tokens | output_tokens |\n"
            "|---|---|---|---|\n"
        )
        rows = [
            f"| {mode} | {counts['count']} | {counts['input_tokens']} | "
            f"{counts['output_tokens']} |"
            for mode, counts in sorted(by_mode.items())
        ]
        return header + "\n".join(rows) + "\n"


def emit_github(
    metrics: GitHubRunMetrics,
    *,
    run_ts: str,
    wall_clock_s: float,
    jsonl_path: Path,
    step_summary_path: str | None,
) -> None:
    """Persist and print one GitHub pipeline run's LLM cost/usage metrics.

    Args:
        metrics: The accumulated :class:`GitHubRunMetrics` for the run.
        run_ts: ISO-8601 UTC timestamp for when the GitHub step finished.
        wall_clock_s: Wall-clock duration of the GitHub step in seconds.
        jsonl_path: Path to the append-only ``github-runs.jsonl`` log.
        step_summary_path: Value of ``GITHUB_STEP_SUMMARY``, or ``None``
            outside GitHub Actions.
    """
    line = json.dumps(
        {"run_ts": run_ts, **metrics.to_aggregate(wall_clock_s=wall_clock_s)},
        sort_keys=True,
        separators=(",", ":"),
    )
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    with jsonl_path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")

    print(metrics.plain_text_summary(wall_clock_s=wall_clock_s))

    if step_summary_path:
        with open(step_summary_path, "a", encoding="utf-8") as fh:
            fh.write(metrics.markdown_summary(wall_clock_s=wall_clock_s))


def emit(
    metrics: RunMetrics,
    *,
    run_ts: str,
    wall_clock_s: float,
    jsonl_path: Path,
    step_summary_path: str | None,
) -> None:
    """Persist and print one run's metrics.

    Args:
        metrics: The accumulated :class:`RunMetrics` for the run.
        run_ts: ISO-8601 UTC timestamp for when the run finished.
        wall_clock_s: Wall-clock duration of the run in seconds.
        jsonl_path: Path to the append-only ``pipeline-runs.jsonl`` log.
        step_summary_path: Value of ``GITHUB_STEP_SUMMARY``, or ``None``
            outside GitHub Actions.
    """
    line = json.dumps(
        metrics.to_dict(run_ts=run_ts, wall_clock_s=wall_clock_s),
        sort_keys=True,
        separators=(",", ":"),
    )
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    with jsonl_path.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")

    print(metrics.plain_text_summary())

    if step_summary_path:
        with open(step_summary_path, "a", encoding="utf-8") as fh:
            fh.write(metrics.markdown_summary())
