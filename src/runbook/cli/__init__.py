import click
from notebook.notebookapp import NotebookApp


@click.group()
def cli():
    pass

@click.command()
def plan():
    """Entrypoint for script"""
    click.echo('planning')
    # Use papermill to inject parameters

@click.command()
def init():
    """Entrypoint for script"""
    click.echo('init')

@click.command()
def serve():
    """Entrypoint for script"""
    app = NotebookApp()

    # Square brackets are the command line arguments. Might want to set port and
    # token, if you actually want to talk to it.
    app.initialize(["8889", "SECURE_TOKEN_TODO"])
    # jupyter notebook FILENAME

@click.command()
def create():
    """Entrypoint for script"""
    click.echo('create')

@click.command()
def run():
    """Entrypoint for script"""
    click.echo('run')
    # see nb.py examples

@click.command()
def review():
    """Entrypoint for script"""
    click.echo('review')

cli.add_command(init)
cli.add_command(plan)
cli.add_command(serve)
cli.add_command(create)
cli.add_command(run)
cli.add_command(review)
