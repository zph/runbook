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
    default="./runbooks/binder/_template-deno.ipynb",
    type=click.Path(exists=True, file_okay=True),
    callback=validate_template,
)

# TODO: switch to language and template defaulting to Deno
# based on operational experience at work
@click.option(
    "-l",
    "--language",
    envvar="LANGUAGE",
    default="deno",
    callback=validate_create_language,
)
@click.pass_context
def create(ctx, filename, template, language):
    """Create a new runbook from [template]"""

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
            f"$> runbook edit ./runbooks/binder/{filename}.ipynb", fg="green", bold=True
        )
    )
