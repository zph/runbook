import glob
from os import path
import click
import json
from pathlib import Path


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


def validate_plan_params(ctx, param, value):
    if isinstance(value, dict):
        return value

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


def validate_planned_runbook_file_path(ctx, param, value):
    base_name = path.basename(value)
    ext = path.splitext(value)[-1].lower()
    if not ext == ".ipynb":
        raise click.BadOptionUsage(
            param, "format for param is not an notebook ending with ipynb"
        )
    try:
        if Path(value).exists():
            return value
        elif glob.glob(f"./runbooks/runs/**/{value}", recursive=True):
            return glob.glob(f"./runbooks/runs/**/{value}", recursive=True)[0]
        elif glob.glob(f"./runbooks/runs/**/{base_name}", recursive=True):
            return glob.glob(f"./runbooks/runs/**/{base_name}", recursive=True)[0]
        else:
            raise click.BadOptionUsage(
                "FILENAME", f"unable to find {value} file", value
            )
    except ValueError:
        raise click.BadOptionUsage("FILENAME", f"unable to find {value} file")
