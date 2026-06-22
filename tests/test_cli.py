from __future__ import annotations

import os
from pathlib import Path

from click import BadParameter
from pytest import raises

from bygge.util.cli import CWD_OPT, NamedChoice


def test_named_choice_basics() -> None:
    choice = NamedChoice[int]([("one", 1), ("two", 2), ("three", 3)])

    assert choice.convert("one", param=None, ctx=None) == 1
    assert choice.convert("two", param=None, ctx=None) == 2
    assert choice.convert("three", param=None, ctx=None) == 3

    with raises(BadParameter):
        _ = choice.convert("(unknown)", param=None, ctx=None)

    assert choice.get_metavar(param=None, ctx=None) == "[one|two|three]"

    assert choice.get_missing_message(param=None, ctx=None) == "Choose from one, two, three."


def test_cwd_opt_evaluated_at_invocation_time(tmp_path: Path) -> None:
    """Test that CWD_OPT default is evaluated at invocation time, not import time."""
    import click
    from click.testing import CliRunner

    # Create a command that uses CWD_OPT
    @click.command()
    @CWD_OPT
    def dummy_command(cwd: Path) -> None:
        # Return the cwd path as output so we can check it
        click.echo(str(cwd))

    runner = CliRunner()

    # Change to tmp_path and invoke without -C option
    original_cwd = Path.cwd()
    try:
        os.chdir(tmp_path)
        result = runner.invoke(dummy_command, [])
        assert result.exit_code == 0
        # The default should be the current directory at invocation time
        assert Path(result.output.strip()) == tmp_path
    finally:
        os.chdir(original_cwd)

    # Now invoke with explicit -C option
    result = runner.invoke(dummy_command, ["-C", str(tmp_path)])
    assert result.exit_code == 0
    assert Path(result.output.strip()) == tmp_path
