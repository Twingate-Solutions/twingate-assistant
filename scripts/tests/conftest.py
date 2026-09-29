"""Shared pytest configuration: adds scripts/ to sys.path for test imports."""

import sys
from pathlib import Path

import pytest

_scripts_dir = str(Path(__file__).resolve().parent.parent)
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)


@pytest.fixture(autouse=True)
def _isolate_committed_state(tmp_path, monkeypatch):
    """Redirect main()'s committed state/metrics files into tmp_path.

    Without this, any test that calls ``update_references.main()`` appends to
    the real ``docs/metrics/*.jsonl`` logs and rewrites ``.doc_norm_hashes.json``.
    Tests that need a specific path still patch it themselves on top of this.
    """
    import update_references

    state_dir = tmp_path / "_isolated_state"
    state_dir.mkdir()
    monkeypatch.setattr(update_references, "PIPELINE_RUNS_PATH", state_dir / "pipeline-runs.jsonl")
    monkeypatch.setattr(update_references, "GITHUB_RUNS_PATH", state_dir / "github-runs.jsonl")
    monkeypatch.setattr(update_references, "NORM_HASH_CACHE_PATH", state_dir / ".doc_norm_hashes.json")
    monkeypatch.setattr(update_references, "HASH_CACHE_PATH", state_dir / ".doc_hashes.json")
    for var in ("GITHUB_OUTPUT", "GITHUB_STEP_SUMMARY", "SECURITY_REVIEW_REPORT"):
        monkeypatch.delenv(var, raising=False)
    yield


@pytest.fixture(autouse=True)
def _reset_rate_limit_toggle():
    """Reset the GitHub throttle's module-global toggle around every test."""
    try:
        import github_repos
    except Exception:  # pragma: no cover - module import is exercised elsewhere
        yield
        return
    github_repos.set_rate_limit_wait(False)
    yield
    github_repos.set_rate_limit_wait(False)
