import importlib
from pathlib import Path
import sys
import os
from types import ModuleType


def auto_import(dir_path: Path | str = ".") -> list[ModuleType]:
    route_dir = Path(dir_path)
    collected_modules = []
    if not route_dir.exists():
        return collected_modules
    python_root = Path(sys.path[0]).resolve()
    cwd = Path(os.getcwd())
    for root, _, files in os.walk(route_dir):
        root = cwd / root
        for f in files:
            if not f.endswith(".py"):
                continue
            f = f[: -len("__init__.py" if f.endswith("__init__.py") else ".py")]
            module_path = (root / f).relative_to(python_root)
            module = importlib.import_module(module_path.as_posix().replace("/", "."))
            collected_modules.append(module)
    return collected_modules
