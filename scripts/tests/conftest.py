"""Shared pytest configuration for scripts tests.

Adds the scripts/ directory to sys.path so test modules can import
pipeline scripts directly (e.g., ``from fetch_sitemap import ...``).
"""

import sys
from pathlib import Path

# Add the scripts/ directory to the front of sys.path
_scripts_dir = str(Path(__file__).resolve().parent.parent)
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)
