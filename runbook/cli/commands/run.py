import click
from runbook.cli.validators import validate_planned_runbook_file_path


@click.command()
@click.argument(
    "filename",
    type=click.Path(file_okay=True),
    callback=validate_planned_runbook_file_path,
)
@click.option("--interactive/--no-interactive", default=True)
@click.pass_context
def run(ctx, filename, interactive):
    """Run a notebook"""
    if interactive:
        argv = [filename]

        # Lazily loaded for performance
        from notebook.app import JupyterNotebookApp

        JupyterNotebookApp.launch_instance(argv=argv)
    else:
        raise RuntimeError("Not Implemented but will do with papermill")
