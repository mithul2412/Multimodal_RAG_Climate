# eval package

import sys as _sys
from pathlib import Path as _Path

# `src/` holds config.py and the other pipeline modules that some eval
# submodules (e.g. eval.run) import as bare top-level modules.
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "src"))
