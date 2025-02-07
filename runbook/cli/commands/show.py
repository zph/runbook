import click
import nbformat
import papermill as pm
from rich.console import Console
from rich.table import Table

from runbook.cli.commands.plan import get_notebook_language
from runbook.cli.validators import validate_runbook_file_path
from runbook.constants import RUNBOOK_METADATA


def get_notebook_header(notebook_path):
    """Get the title (H1) and description (H2) from the notebook's markdown cells.

    Args:
        notebook_path (str): Path to the notebook file

    Returns:
        str: The header of the first markdown cell, or None if not found
    """
    nb = nbformat.read(notebook_path, as_version=4)
    header = None

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            header = cell.source
            break

    return header


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

    # Get and print title and description if available
    header = get_notebook_header(runbook)
    if header:
        console.print(f"[bold blue]Header:\n[/]{header}\n")

    # Create and populate parameters table
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Parameter")
    table.add_column("Default Value")
    table.add_column("Type")
    table.add_column("Help")

    for param, value in inferred_params.items():
        default = value["default"].rstrip(";")
        typing = value["inferred_type_name"] or ""
        help_text = value["help"] or ""
        if param != RUNBOOK_METADATA:
            table.add_row(param, default, typing, help_text)

    console.print(table)
