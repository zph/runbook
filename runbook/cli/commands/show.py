import click
from rich.console import Console
from rich.table import Table
from runbook.cli.commands.plan import get_notebook_language
from runbook.cli.validators import validate_runbook_file_path

import papermill as pm


@click.command()
@click.argument(
    "runbook", type=click.Path(file_okay=True), callback=validate_runbook_file_path
)
@click.pass_context
def show(ctx, runbook):
    """Show runbook parameters and metadata"""
    console = Console()
    inferred_params = pm.inspect_notebook(runbook)
    notebook_language = get_notebook_language(runbook)

    # Print runbook info with styling
    console.print(f"\n[bold blue]Runbook:[/] {runbook}")
    console.print(f"[bold blue]Language:[/] {notebook_language}\n")

    # Create and populate parameters table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Parameter")
    table.add_column("Default Value")
    table.add_column("Type")
    table.add_column("Help")

    for param, value in inferred_params.items():
        default = value["default"].rstrip(";")
        typing = value["inferred_type_name"] or ""
        help_text = value["help"] or ""
        table.add_row(param, default, typing, help_text)

    console.print(table)
