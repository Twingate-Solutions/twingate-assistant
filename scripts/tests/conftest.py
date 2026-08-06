"""Shared pytest configuration: adds scripts/ to sys.path for test imports."""

import sys
from pathlib import Path

import pytest

_scripts_dir = str(Path(__file__).resolve().parent.parent)
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)


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
