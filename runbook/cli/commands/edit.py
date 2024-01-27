import click
from os import path
from runbook.cli.validators import validate_runbook_file_path


@click.command()
@click.argument(
    "filename", type=click.Path(file_okay=True), callback=validate_runbook_file_path
)
@click.pass_context
def edit(ctx, filename):
    """Edit an existing runbook"""
    # Must override argv because it's used in launch instance and there isn't a way
    # to pass via argument in ExtensionApp.lauch_instance
    # TODO:
    argv = [path.abspath(filename)]
    # Lazily loaded for performance
    from notebook.app import JupyterNotebookApp

    JupyterNotebookApp.launch_instance(argv=argv)
    # TODO: insert post run hooks here
