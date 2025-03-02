import glob
import json
from os import path
from pathlib import Path

import click


# TODO: ensure no duplicate extension here
def validate_template(ctx, param, value):
    try:
        ext = path.splitext(value)[-1].lower()
        if ext == ".ipynb":
            return value
        else:
            raise click.BadOptionUsage(
                param, "format for param is not an notebook ending with ipynb"
            )
    except ValueError:
        raise click.BadOptionUsage(
            param, "format for param is not an notebook ending with ipynb"
        )


def validate_create_language(ctx, param, value):
    if value == "./runbooks/binder/_template-python.ipynb":
        return value
    if value == "./runbooks/binder/_template-deno.ipynb":
        return value
    if value in ["python", "deno"]:
        return f"./runbooks/binder/_template-{value}.ipynb"
    else:
        raise click.BadOptionUsage("--language", "options are python or deno")


def validate_plan_params(ctx, param, value):
    if isinstance(value, dict):
        return value

    # We allow this for the auto-plan case
    if value == "" or value == None:
        return {}

    try:
        v = json.loads(value)
        if isinstance(v, dict):
            return v
        else:
            raise click.BadOptionUsage("--param", "format for param is not an object")
    except ValueError:
        raise click.BadOptionUsage(
            "--param", "format must be json with an outermost structure of an object"
        )


def validate_runbook_file_path(ctx, param, value):
    try:
        if Path(value).exists():
            return value
        elif Path(f"./runbooks/binder/{value}").exists():
            return f"./runbooks/binder/{value}"
        elif Path(f"./runbooks/runs/{value}").exists():
            return f"./runbooks/runs/{value}"
        else:
            raise click.BadOptionUsage("FILENAME", "unable to find file")
    except ValueError:
        raise click.BadOptionUsage("FILENAME", "unable to find file")


def process_glob_matches(options):
    options = sorted(options)
    options.reverse()
    if len(options) == 1:
        return options[0]
    elif len(options) > 1:
        return click.prompt("Which file?", type=click.Choice(options))
    else:
        raise click.BadOptionUsage("FILENAME", f"unable to find {value} file")


def validate_has_notebook_extension(ctx, param, value):
    if not value.lower().endswith(".ipynb"):
        value = value + ".ipynb"
    return value


def validate_planned_runbook_file_path(ctx, param, value):
    value = validate_has_notebook_extension(ctx, param, value)
    base_name = path.basename(value)
    try:
        if Path(value).exists():
            return value
        elif glob.glob(f"./runbooks/runs/**/{value}", recursive=True):
            return process_glob_matches(
                glob.glob(f"./runbooks/runs/**/{value}", recursive=True)
            )
        elif glob.glob(f"./runbooks/runs/**/{base_name}", recursive=True):
            return process_glob_matches(
                glob.glob(f"./runbooks/runs/**/{base_name}", recursive=True)
            )
        else:
            raise click.BadOptionUsage(
                "FILENAME", f"unable to find {value} file", value
            )
    except ValueError:
        raise click.BadOptionUsage("FILENAME", f"unable to find {value} file")
