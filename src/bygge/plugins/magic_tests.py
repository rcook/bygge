from __future__ import annotations

from pathlib import Path

from bygge.contracts import Input
from bygge.util import TomlValue


class MagicTests:
    def fetch_test_dirs(self, input: Input, blob: TomlValue) -> list[Path] | None:  # pyright: ignore[reportUnusedParameter]
        test_dir = input.pyproject_path.parent / "test"
        return [test_dir] if test_dir.is_dir() else None
