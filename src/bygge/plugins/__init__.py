from __future__ import annotations

from .basedpyright import Basedpyright
from .hatchling import Hatchling
from .magic_sources import MagicSources
from .magic_tests import MagicTests
from .plugins import Plugins
from .pytest import Pytest
from .pytest_cov import PytestCov
from .pytest_discovery import PytestDiscovery
from .ruff_check import RuffCheck
from .ruff_format import RuffFormat
from .setuptools import Setuptools
from .vulture import Vulture

__all__ = [
    "Basedpyright",
    "Hatchling",
    "MagicSources",
    "MagicTests",
    "Plugins",
    "Pytest",
    "PytestCov",
    "PytestDiscovery",
    "RuffCheck",
    "RuffFormat",
    "Setuptools",
    "Vulture",
]
