import click
from notebook.app import JupyterNotebookApp
from nbconvert.nbconvertapp import NbConvertApp
import sys
import papermill as pm
import os
from os import path
import hashlib
import json
from datetime import datetime
from pathlib import Path
import pkg_resources
from ..template import TEMPLATE
import IPython

def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

@click.group()
# TODO: decide if we want a cwd command
@click.option('--cwd', default=os.curdir, type=click.Path(exists=True, resolve_path=True, dir_okay=True),  help='Directory for operations (normally at root above runbooks, ie ../.runbook.yaml)')
def cli(cwd):
    os.chdir(cwd)
    pass

def validate_plan_params(ctx, param, value):
    if isinstance(value, dict):
        return value

    try:
        v = json.loads(value)
        if isinstance(v, dict):
            return v
        else:
            raise click.BadOptionUsage("format for param is not an object")
    except ValueError:
        raise click.BadOptionUsage("format must be json with an outermost structure of an object")

@click.command()
@click.argument('input', type=click.Path(exists=True, file_okay=True))
@click.option('-p', '--params', type=click.UNPROCESSED, callback=validate_plan_params)
def plan(input, params={}):
    """Prepares the runbook for execution by injecting parameters. Doesn't run runbook."""

    date = datetime.now().date()
    basename = path.basename(input)
    hash = sha256sum(input)[0:8]
    output = "-".join([str(date), hash, basename])
    full_output = f'./runbooks/runs/{output}'

    # TODO: confirm we're in the right folder

    # TODO: safety check if we already have one with this SHA in folder, in which case prompt
    # and offer to skip.
    pm.execute_notebook(
       input_path=input,
       output_path=full_output,
       parameters = params,
       prepare_only=True,
    )

    argv = [ "--ClearOutputPreprocessor.enabled=True",
                """--ClearMetadataPreprocessor.enabled=True""",
                """--ClearMetadataPreprocessor.preserve_cell_metadata_mask='[("tags"),("parameters"),("editable")]'""",
                "--inplace",
                full_output]
    # TODO: hide the nbconvert verbose output?
    NbConvertApp().launch_instance(argv=argv)
    cmd = click.style(f"$> runbook run {output}", fg='green', bold=True)
    click.echo(click.style(f"Run your new runbook instance with:\n\t{cmd}"))

RUNBOOK_CONFIG = {
     'version': 1,
     'library_version': None,
     'directory': None
                 }

@click.command()
@click.option('-d', '--directory', default='runbooks', type=click.Path(exists=False, dir_okay=True))
def init(directory):
    """Initialize a folder as a runbook repository"""

    click.echo('Command creates ./runbooks folder with the structure needed for runbook')
    click.echo('In pseudo code it does the following')
    click.echo("""
    mkdir ./{directory}
    mkdir ./{directory}/binder
    mkdir ./{directory}/runs
    touch ./{directory}/.runbook.yaml
    touch ./{directory}/_template.ipynb
    """)

    version = pkg_resources.get_distribution("runbook").version
    click.confirm(click.style('Proceed?', fg='red', bold=True))
    Path("./{directory}/binder").mkdir(parents=True, exist_ok=True)
    Path("./{directory}/runs").mkdir(parents=True, exist_ok=True)
    # TODO: insert starter values
    cfg = RUNBOOK_CONFIG.merge({'library_version': version, 'directory': directory})
    with open(f"./{directory}/.runbook.json") as f:
        f.write(json.dumps(cfg))
    with open("./{directory}/binder/_template.ipynb") as f:
        f.write(TEMPLATE)
    Path().touch(exist_ok=True)

import glob

def validate_file_path(ctx, param, value):
    try:
        if Path(value).exists():
            return value
        elif Path("./runbooks/binder/{value}").exists():
            return "./runbooks/binder/{value}"
        elif glob.glob("**/**/_template.ipynb")[0]:
            return glob.glob("**/**/_template.ipynb")[0]
        else:
            raise click.BadOptionUsage("unable to find _template.ipynb file")
    except ValueError:
        raise click.BadOptionUsage("unable to find _template.ipynb file")


@click.command()
@click.argument('filename', type=click.Path(file_okay=True), callback=validate_file_path)
def edit(filename):
    """Entrypoint for script"""
    # Must override argv because it's used in launch instance and there isn't a way
    # to pass via argument in ExtensionApp.lauch_instance
    # TODO:
    argv = [filename]
    JupyterNotebookApp.launch_instance(argv=argv)
    # TODO: insert post run hooks here

def validate_template(ctx, param, value):
    try:
        ext = path.splitext(value)[-1].lower()
        if ext == ".ipynb":
            return value
        else:
            raise click.BadOptionUsage("format for param is not an notebook ending with ipynb")
    except ValueError:
        raise click.BadOptionUsage("format for param is not an notebook ending with ipynb")


@click.command()
@click.argument('filename', type=click.Path(exists=False, file_okay=True))
@click.option('-t', '--template', type=click.Path(exists=True, file_okay=True), callback=validate_template)
def create(filename):
    """Create a new runbook from [template]"""
    # TODO: guard against anything other than a bare name
    if path.basename(filename) != filename:
        raise click.UsageError("Supplied filename included more than a basename, should look like 'maintenance-operation.ipynb'")
    full_output = path.join(["runbooks", "binder", filename])
    argv = [ "--ClearOutputPreprocessor.enabled=True",
             """--ClearMetadataPreprocessor.enabled=True""",
             """--ClearMetadataPreprocessor.preserve_cell_metadata_mask='[("tags"),("parameters"),("editable")]'""",
             "--inplace",
             full_output]
    # TODO: hide the nbconvert verbose output?
    NbConvertApp().launch_instance(argv=argv)
    click.echo(click.style(f"$> runbook edit {filename}", fg='green', bold=True))


@click.command()
@click.argument('filename', type=click.Path(exists=True, file_okay=True))
def run(filename):
    """Run a notebook"""
    argv = ["notebook", filename]
    JupyterNotebookApp.launch_instance(argv=argv)

@click.command()
def review():
    """Entrypoint for script"""
    click.echo('review')

cli.add_command(init)
cli.add_command(plan)
cli.add_command(edit)
cli.add_command(create)
cli.add_command(run)
cli.add_command(review)
