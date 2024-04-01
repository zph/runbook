import os

import click

from runbook.cli.commands import create, edit, export, convert, init, plan, review, run, version

# TODO: not working, needs a custom underlying class to handle the auto-env
CONTEXT_SETTINGS = dict(auto_envvar_prefix="RUNBOOK")


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--cwd",
    envvar="WORKING_DIR",
    default=os.curdir,
    type=click.Path(exists=True, resolve_path=True, dir_okay=True),
    help="Directory for operations (normally at root above runbooks, ie ../.runbook.yaml)",
)
@click.pass_context
def cli(ctx, cwd):
    os.chdir(cwd)
    ctx.ensure_object(dict)
    ctx.obj["WORKING_DIR"] = cwd


cli.add_command(init)
cli.add_command(plan)
cli.add_command(edit)
cli.add_command(create)
cli.add_command(convert)
cli.add_command(run)
cli.add_command(review)
cli.add_command(version)
# cli.add_command(export)
cli.name = "runbook"
cli


def main(**args):
    cli(**args, **CONTEXT_SETTINGS)


if __name__ == "main":
    import sys

    main(sys.arv)
