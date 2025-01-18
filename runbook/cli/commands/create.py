from os import path

import click
from runbook.cli.lib import nbconvert_launch_instance
from runbook.cli.validators import validate_create_language, validate_template


@click.command()
@click.argument("filename", type=click.Path(exists=False, file_okay=True))
@click.option(
    "-t",
    "--template",
    envvar="TEMPLATE",
    default="./runbooks/binder/_template-python.ipynb",
    type=click.Path(exists=True, file_okay=True),
    callback=validate_template,
)
@click.option(
    "-l",
    "--language",
    envvar="LANGUAGE",
    default="./runbooks/binder/_template-python.ipynb",
    callback=validate_create_language,
)
@click.pass_context
def create(ctx, filename, template, language):
    """Create a new runbook from [template]"""
    # TODO: guard against anything other than a bare name
    # Allow override for alternate language default
    # TODO: allow reading from project config file
    if language:
        template = language
    if path.basename(filename) != filename:
        raise click.UsageError(
            "Supplied filename included more than a basename, should look like 'maintenance-operation.ipynb'"
        )
    # TODO: remove hardcoding of folder outer name and rely on config file
    path.join("runbooks", "binder", filename)
    # TODO: hide the nbconvert verbose output?
    argv = [
        "--ClearOutputPreprocessor.enabled=True",
        template,
        "--to",
        "notebook",
        "--output",
        filename,
        "--output-dir",
        path.join("runbooks", "binder"),
    ]

    nbconvert_launch_instance(argv)

    click.echo(
        click.style(
            f"$> runbook edit ./runbooks/binder/{filename}.ipynb", fg="green", bold=True
        )
    )
