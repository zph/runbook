import click


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
        rprint(f"📔 {runbook}")

    rprint("\n[bold blue]Runs:[/bold blue]")
    for runbook in sorted(runs):
        rprint(f"📔 {runbook}")
