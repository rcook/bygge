from __future__ import annotations

from bygge.plugins import (
    Basedpyright,
    Hatchling,
    MagicSources,
    MagicTests,
    Plugins,
    Pytest,
    PytestCov,
    PytestDiscovery,
    RuffCheck,
    RuffFormat,
    Setuptools,
    Vulture,
)

PLUGINS: Plugins = Plugins(
    source_dir_plugins=[Hatchling(), Setuptools(), MagicSources()],
    test_dir_plugins=[PytestDiscovery(), MagicTests()],
    test_plugins=[Pytest()],
    coverage_plugins=[PytestCov()],
    type_check_plugins=[Basedpyright()],
    format_plugins=[RuffFormat()],
    lint_plugins=[RuffCheck()],
    dead_code_plugins=[Vulture()],
)
