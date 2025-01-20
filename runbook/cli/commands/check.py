# metadata.kernelspec.name = deno || python3

import io
import json
import sys
from contextlib import redirect_stderr, redirect_stdout
from os import path

import click
from runbook.cli.completions import EditableNotebook
from runbook.cli.validators import validate_runbook_file_path


@click.command()
@click.argument(
    "filename",
    type=EditableNotebook(file_okay=True),
    callback=validate_runbook_file_path,
)
@click.option(
    "-c",
    "--command",
    default=None,
    help="Run a notebook through this custom command, ie 'deno check {}' where the {} is the temporary filename.",
)
@click.pass_context
def check(ctx, filename, command):
    """Check language validity and formatting of a notebook."""
    full_path = path.abspath(filename)
    content = None
    with open(full_path, "r") as f:
        txt = f.read()
        content = json.loads(txt)

    # Default
    language_specific_tool = "black --diff {}"
    if command:
        language_specific_tool = command
    else:
        kernel_name = content["metadata"]["kernelspec"]["name"]
        if kernel_name == "deno":
            language_specific_tool = "deno check {}"

    argv = ["--check", language_specific_tool, full_path]
    # Lazily loaded for performance
    from jupytext.cli import jupytext as jupytext_main

    stdout = io.StringIO()
    stderr = io.StringIO()

    result = None
    with redirect_stdout(stdout), redirect_stderr(stderr):
        result = jupytext_main(args=argv)

    stdout_content = stdout.getvalue()
    stderr_content = stderr.getvalue()

    click.echo(f"Checked {full_path}")
    if result is not None and result != 0:
        if stderr_content:
            click.echo(f"Error: {stderr_content}", err=True)
        if stdout_content:
            click.echo(f"Output: {stdout_content}")
        sys.exit(result)
