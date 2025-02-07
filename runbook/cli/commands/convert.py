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
    """Convert a runbook between different formats

    This command converts notebooks between various formats using jupytext.
    Supported conversions include:
    - .ipynb to .py (Python script)
    - .ipynb to .ts (Deno notebook)
    - .ipynb to .md (Markdown)
    - And other formats supported by jupytext

    FILENAME: Path to the source notebook file to convert.
    OUTPUT: Destination path for the converted file. The format is determined
           by the file extension.

    Examples:
        runbook convert notebook.ipynb script.py   # Convert to Python script
        runbook convert notebook.ipynb notebook.ts   # Convert to Deno notebook
        runbook convert notebook.ipynb notebook.md   # Convert to Markdown

    The conversion preserves cell metadata, notebook metadata, and execution outputs
    where applicable.
    """
    # Must override argv because it's used in launch instance and there isn't a way
    # to pass via argument in ExtensionApp.lauch_instance
    # TODO:
    argv = [path.abspath(filename), "--output", output]
    # Lazily loaded for performance
    from jupytext.cli import jupytext as jupytext_main

    jupytext_main(args=argv)
    # TODO: insert post run hooks here
