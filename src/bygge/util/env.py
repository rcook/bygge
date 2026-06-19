from __future__ import annotations

import os


def env_truthy(name: str, default: bool = True) -> bool:
    value = os.getenv(name)
    if value is None:
        return default

    s = value.strip().lower()
    return s in {"1", "true", "yes", "on", "y"}
