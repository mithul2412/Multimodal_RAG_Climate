"""Pytest bootstrap: make `src/` modules importable as bare top-level modules
(e.g. `from pipeline_utils import ...`) without changing any test file."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
