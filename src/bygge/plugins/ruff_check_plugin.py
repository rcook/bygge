from __future__ import annotations

from bygge.contracts import Input, Payload, PluginResult
from bygge.plugins.ruff_run_mixin import RuffRunMixin
from bygge.plugins.util import check_requirements
from bygge.util import TomlValue
from bygge.workspace import Workspace


class RuffCheckPlugin(RuffRunMixin):
    def is_installed(self, input: Input, blob: TomlValue) -> bool:
        return check_requirements(input=input, blob=blob, required_deps=["ruff"])

    def run_lint(
        self,
        workspace: Workspace,
        payload: Payload,
        fix: bool,
        args: tuple[str, ...],
    ) -> PluginResult:
        return self.run_ruff(
            cmd=[
                str(workspace.make_bin_path("ruff")),
                "check",
                *(["--fix"] if fix else []),
                *[str(p) for p in payload.source_dirs],
                *[str(p) for p in payload.test_dirs],
                *args,
            ],
            cwd=workspace.cwd,
        )
