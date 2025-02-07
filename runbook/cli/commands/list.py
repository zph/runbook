import click

from runbook.cli.commands.show import get_notebook_header


def get_notebook_title(notebook_path):
    header = get_notebook_header(notebook_path)
    if header:
        maybe_title = [line for line in header.split("\n") if line.startswith("# ")]
        if maybe_title:
            return maybe_title[0][2:].strip()
    return None


@click.command()
@click.pass_context
def list(ctx):
    """List runbooks"""
    import glob

    from rich import print as rprint

    # Find all .ipynb files in current directory
    runbooks = glob.glob("**/*.ipynb", recursive=True)
    templates = []
    runs = []
    for runbook in runbooks:
        if "binder" in runbook:
            templates.append(runbook)
        else:
            runs.append(runbook)

    if not templates and not runs:
        rprint("[yellow]No runbooks found in current directory[/yellow]")
        return

    # Print found runbooks in a nice format
    rprint("\n[bold blue]Templates:[/bold blue]")
    for runbook in sorted(templates):
        title = get_notebook_title(runbook)
        rprint(f"📔 {title} - {runbook}")

    rprint("\n[bold blue]Runs:[/bold blue]")
    for runbook in sorted(runs):
        title = get_notebook_title(runbook)
        rprint(f"📔 {title} - {runbook}")
