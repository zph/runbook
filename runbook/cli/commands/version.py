import click

from runbook import __version__ as VERSION


@click.command()
@click.pass_context
def version(ctx):
    """Display version information about runbook"""

    click.echo(f"Runbook version: {VERSION}")
