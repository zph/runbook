import click
from runbook.cli.validators import validate_planned_runbook_file_path


@click.command()
@click.argument(
    "filename",
    type=click.Path(file_okay=True),
    callback=validate_planned_runbook_file_path,
)
@click.option(
    "--output",
    type=click.Path(file_okay=True),
    default=None,
    help="Path to the output file",
)
@click.option(
    "--interactive/--no-interactive",
    default=True,
    help="Run the notebook in interactive mode or EXPERIMENTAL non-interactive mode",
)
@click.pass_context
def run(ctx, filename, output, interactive):
    """Run a runbook"""
    if interactive:
        argv = [filename]

        # Lazily loaded for performance
        from notebook.app import JupyterNotebookApp

        JupyterNotebookApp.launch_instance(argv=argv)
    else:
        if not output:
            raise click.BadOptionUsage(
                "--output", "--output is required when --interactive is false"
            )
        import papermill as pm

        pm.execute_notebook(
            input_path=filename,
            output_path=output,
        )
        print(f"Output written to {output}")
