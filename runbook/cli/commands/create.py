from os import path
from datetime import datetime
import os
from nbconvert.nbconvertapp import NbConvertApp
import click
from runbook.cli.validators import validate_template


@click.command()
@click.argument("filename", type=click.Path(exists=False, file_okay=True))
@click.option(
    "-t",
    "--template",
    envvar="TEMPLATE",
    default="./runbooks/binder/_template.ipynb",
    type=click.Path(exists=True, file_okay=True),
    callback=validate_template,
)
@click.pass_context
def create(ctx, filename, template):
    """Create a new runbook from [template]"""
    # TODO: guard against anything other than a bare name
    if path.basename(filename) != filename:
        raise click.UsageError(
            "Supplied filename included more than a basename, should look like 'maintenance-operation.ipynb'"
        )
    # TODO: remove hardcoding of folder outer name and rely on config file
    full_output = path.join("runbooks", "binder", filename)
    # TODO: hide the nbconvert verbose output?
    argv = [
        "--ClearOutputPreprocessor.enabled=True",
        # Do not use this to clear metadata for cells
        # """--ClearMetadataPreprocessor.preserve_cell_metadata_mask='["tags"]'""",
        template,
        "--to",
        "notebook",
        "--output",
        filename,
        "--output-dir",
        path.join("runbooks", "binder"),
    ]

    NbConvertApp().launch_instance(argv=argv)

    runbook_param_injection = {
        "__RUNBOOK_METADATA__": {
            "RUNBOOK_FOLDER": "./runbooks/binder",
            "RUNBOOK_FILE": full_output,
            "RUNBOOK_SOURCE": template,
            "CREATED_AT": str(datetime.utcnow()),
            "CREATED_BY": os.environ["USER"],
        }
    }

    click.echo(
        click.style(
            f"$> runbook edit ./runbooks/binder/{filename}.ipynb", fg="green", bold=True
        )
    )
