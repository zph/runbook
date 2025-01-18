import json
import os
from datetime import datetime
from os import path
from pathlib import Path

import click
from runbook.cli.lib import nbconvert_launch_instance
from runbook.cli.validators import validate_plan_params, validate_runbook_file_path
from runbook.constants import RUNBOOK_METADATA

import papermill as pm


@click.command()
@click.argument(
    "input", type=click.Path(file_okay=True), callback=validate_runbook_file_path
)
# TODO allow for specifying output filename to allow for easier naming
@click.option("-e", "--embed", type=click.Path(exists=True), multiple=True)
@click.option(
    "-p", "--params", default={}, type=click.UNPROCESSED, callback=validate_plan_params
)
@click.option("-i", "--identifier", default="", type=click.STRING)
@click.pass_context
def plan(ctx, input, embed, identifier="", params={}):
    """Prepares the runbook for execution by injecting parameters. Doesn't run runbook."""
    import shutil

    date = datetime.now().date()
    basename = path.basename(input)
    basename_without_ext = basename[0:-6]
    output_basename_without_ext = basename_without_ext
    if len(identifier) > 0:
        output_basename_without_ext = "-".join(
            [output_basename_without_ext, identifier]
        )
    output = "-".join([str(date), output_basename_without_ext])
    output_folder = f"./runbooks/runs/{output}"
    full_output = f"{output_folder}/{output_basename_without_ext}.ipynb"

    runbook_param_injection = {
        RUNBOOK_METADATA: {
            "RUNBOOK_FOLDER": output_folder,
            "RUNBOOK_FILE": full_output,
            "RUNBOOK_SOURCE": input,
            "CREATED_AT": str(datetime.utcnow()),
            "CREATED_BY": os.environ["USER"],
        }
    }

    if len(params) == 0:
        inferred_params = pm.inspect_notebook(input)
        # Inferred_type_name is language specific
        # we make the simplifying assumption to show user and then treat inputs as potentially json
        for key, value in inferred_params.items():
            if key != RUNBOOK_METADATA:
                default = value["default"].rstrip(";")
                typing = value["inferred_type_name"]
                type_hint = ""
                help_hint = ""
                if typing:
                    type_hint = f" ({typing})"
                if value["help"]:
                    help_hint = f"(hint: {value['help']})"

                raw_value = click.prompt(
                    f"""Enter value for {key}{type_hint}{help_hint}""",
                    default=default,
                    value_proc=json.loads,
                )
                params[key] = raw_value

    injection_params = {**runbook_param_injection, **params}

    if not Path(output_folder).exists():
        os.makedirs(output_folder, exist_ok=True)

    # TODO: safety check if we already have one with this SHA in folder, in which case prompt
    # and offer to skip.

    pm.execute_notebook(
        input_path=input,
        output_path=full_output,
        parameters=injection_params,
        prepare_only=True,
    )

    argv = [
        "--inplace",
        full_output,
    ]

    # TODO: join the unified logic of create and plan

    nbconvert_launch_instance(argv, clear_output=True)

    for f in embed:
        shutil.copyfile(src=f, dst=f"{output_folder}/{path.basename(f)}")

    cmd = click.style(f"$> runbook run {full_output}", fg="green", bold=True)
    click.echo(click.style(f"Run your new runbook instance with:\n\t{cmd}"))
