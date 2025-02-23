from os import path

import click

from runbook.cli.lib import nbconvert_launch_instance
from runbook.cli.validators import (
    validate_create_language,
    validate_has_notebook_extension,
    validate_template,
)


@click.command()
@click.argument(
    "filename",
    type=click.Path(exists=False, file_okay=True),
    callback=validate_has_notebook_extension,
)
@click.option(
    "-t",
    "--template",
    envvar="TEMPLATE",
    default="./runbooks/binder/_template-deno.ipynb",
    type=click.Path(exists=True, file_okay=True),
    callback=validate_template,
    help="Path to the template file to use",
)
# TODO: switch to language and template defaulting to Deno
# based on operational experience at work
@click.option(
    "-l",
    "--language",
    envvar="LANGUAGE",
    default="deno",
    callback=validate_create_language,
    help="Language to use for the runbook",
)
@click.pass_context
def create(ctx, filename, template, language):
    """Create a new runbook from a template

    This command creates a new runbook using a specified template
    or language preset. The new runbook will be created in the runbooks/binder directory.

    FILENAME: Name for the new runbook file (e.g., 'maintenance-task.ipynb').
             Should be a basename only, without directory path.

    Options:
        --template, -t: Path to a custom template runbook to use as a base.
                       Can be set via TEMPLATE environment variable.
                       Default: ./runbooks/binder/_template-deno.ipynb

        --language, -l: Shortcut to use a predefined language template.
                       Can be set via LANGUAGE environment variable.
                       Default: deno

    Examples:
        runbook create maintenance-task.ipynb              # Creates using default Deno template
        runbook create task.ipynb -l python               # Creates using Python template
        runbook create task.ipynb -t custom-template.ipynb # Creates from custom template

    The command will create the notebook and display the edit command to open it.
    """

    if language:
        template = language
    if path.basename(filename) != filename:
        raise click.UsageError(
            "Supplied filename included more than a basename, should look like 'maintenance-operation.ipynb'"
        )
    # TODO: remove hardcoding of folder outer name and rely on config file
    path.join("runbooks", "binder", filename)
    argv = [
        template,
        "--to",
        "notebook",
        "--output",
        filename,
        "--output-dir",
        path.join("runbooks", "binder"),
    ]

    nbconvert_launch_instance(argv, clear_output=True)

    click.echo(
        click.style(
            f"$> runbook edit ./runbooks/binder/{filename}", fg="green", bold=True
        )
    )
