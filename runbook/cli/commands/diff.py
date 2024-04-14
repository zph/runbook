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
    """Convert an existing runbook to different format"""
    argv = [path.abspath(notebook_1), path.abspath(notebook_2)]
    from nbdime import nbdiffapp

    nbdiffapp.main(args=argv)
