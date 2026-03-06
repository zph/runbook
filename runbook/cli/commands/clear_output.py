"""Clear cell outputs from notebook(s). Replaces jupyter nbconvert --clear-output --inplace."""

import click
import nbformat

from runbook.cli.notebook_io import clear_cell_outputs


@click.command()
@click.argument(
    "notebooks",
    nargs=-1,
    required=True,
    type=click.Path(exists=True, path_type=str),
)
def clear_output(notebooks):
    """Clear outputs and execution counts from one or more notebooks (in place)."""
    for path in notebooks:
        nb = nbformat.read(path, as_version=4)
        clear_cell_outputs(nb)
        nbformat.write(nb, path)
        click.echo(path)
