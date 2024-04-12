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
@click.argument(
    "output",
    type=click.Path(exists=False, file_okay=True, writable=True),
)
@click.pass_context
def convert(ctx, filename, output):
    """Convert an existing runbook to different format"""
    # Must override argv because it's used in launch instance and there isn't a way
    # to pass via argument in ExtensionApp.lauch_instance
    # TODO:
    argv = [path.abspath(filename), "--output", output]
    # Lazily loaded for performance
    from jupytext.cli import jupytext as jupytext_main

    jupytext_main(args=argv)
    # TODO: insert post run hooks here
