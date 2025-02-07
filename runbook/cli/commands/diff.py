from os import path

import click

from runbook.cli.completions import EditableNotebook
from runbook.cli.validators import validate_runbook_file_path


@click.command()
@click.argument(
    "notebook_1",
    type=EditableNotebook(file_okay=True),
    callback=validate_runbook_file_path,
)
@click.argument(
    "notebook_2",
    type=EditableNotebook(file_okay=True),
    callback=validate_runbook_file_path,
)
@click.pass_context
def diff(ctx, notebook_1, notebook_2):
    """Compare two runbooks and show their differences

    This command uses nbdime to display a detailed comparison between two runbooks.

    Arguments:
        NOTEBOOK_1: Path to the first runbook for comparison
        NOTEBOOK_2: Path to the second runbook for comparison

    Examples:
        runbook diff notebook1.ipynb notebook2.ipynb     # Compare two notebooks
        runbook diff original.ipynb modified.ipynb       # Show changes between versions

    The diff output will be displayed in a terminal-friendly format, with:
    - Added content in green
    - Removed content in red
    - Modified content showing both versions
    """
    argv = [path.abspath(notebook_1), path.abspath(notebook_2)]
    from nbdime import nbdiffapp

    nbdiffapp.main(args=argv)
