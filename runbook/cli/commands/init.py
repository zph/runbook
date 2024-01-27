import json
from pathlib import Path

import click

from runbook.template import TEMPLATE
from runbook.version import VERSION

RUNBOOK_CONFIG = {"version": 1, "library_version": VERSION, "directory": None}


@click.command()
@click.option(
    "-d",
    "--directory",
    envvar="DIRECTORY",
    default="runbooks",
    type=click.Path(exists=False, dir_okay=True),
)
@click.pass_context
def init(ctx, directory):
    """Initialize a folder as a runbook repository"""

    click.echo(
        "Command creates ./runbooks folder with the structure needed for runbook"
    )
    click.echo("In pseudo code it does the following")
    click.echo(f"""in {ctx.obj["WORKING_DIR"]}""")
    click.echo(
        f"""
    mkdir ./{directory}
    mkdir ./{directory}/binder
    mkdir ./{directory}/runs
    touch ./{directory}/.runbook.json
    touch ./{directory}/_template.ipynb
    """
    )

    click.confirm(click.style("Proceed?", fg="red", bold=True))
    Path(f"./{directory}/binder").mkdir(parents=True, exist_ok=True)
    Path(f"./{directory}/runs").mkdir(parents=True, exist_ok=True)
    cfg = {**RUNBOOK_CONFIG, **{"directory": directory}}
    with open(f"./{directory}/.runbook.json", "w") as f:
        f.write(json.dumps(cfg))
    with open(f"./{directory}/binder/_template.ipynb", "w") as f:
        import base64

        js = base64.b64decode(TEMPLATE).decode("utf-8")
        f.write(js)
