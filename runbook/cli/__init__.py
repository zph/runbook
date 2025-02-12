import os

import click

from runbook.cli.commands import (
    check,
    convert,
    create,
    diff,
    edit,
    init,
    list,
    plan,
    review,
    run,
    show,
    version,
)

CONTEXT_SETTINGS = dict(auto_envvar_prefix="RUNBOOK")


@click.group()
@click.option(
    "--cwd",
    envvar=["RUNBOOK_WORKING_DIR", "WORKING_DIR"],
    default=os.curdir,
    type=click.Path(exists=True, resolve_path=True, dir_okay=True),
    help="Directory for operations (normally at root above runbooks, ie ../.runbook.yaml) and can be set with RUNBOOK_WORKING_DIR or WORKING_DIR environment variables",
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
cli.add_command(check)
cli.add_command(diff)
cli.add_command(run)
cli.add_command(review)
cli.add_command(version)
cli.add_command(list)
cli.add_command(show)
cli.name = "runbook"
cli


def main(**args):
    cli(**args, **CONTEXT_SETTINGS)


if __name__ == "main":
    import sys

    main(sys.arv)
