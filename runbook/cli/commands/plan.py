import ast
import json
import os
import subprocess
from datetime import datetime, timezone
from os import path
from pathlib import Path

import click
import nbformat
import papermill as pm

from runbook.cli.notebook_io import RawExpression, get_notebook_language, inject_parameters_and_write
from runbook.cli.validators import validate_plan_params, validate_runbook_file_path
from runbook.constants import RUNBOOK_METADATA


def get_parser_by_language(language: str):
    if language == "typescript":
        return json.loads
    elif language == "python":
        return ast.literal_eval
    else:
        # Default to json.loads for unknown languages
        return json.loads


@click.command()
@click.argument(
    "input",
    type=click.Path(file_okay=True),
    callback=validate_runbook_file_path,
)
# TODO allow for specifying output filename to allow for easier naming
@click.option(
    "-e",
    "--embed",
    type=click.Path(exists=True),
    multiple=True,
    help="Path to file(s) to embed in the runbook output directory",
)
@click.option(
    "-p",
    "--params",
    default={},
    type=click.UNPROCESSED,
    callback=validate_plan_params,
    help="Parameters to inject into the runbook in json object format where the key is the parameter name and the value is the parameter value",
)
@click.option(
    "-i",
    "--identifier",
    default="",
    type=click.STRING,
    help="Optional identifier to append to the output filename",
)
@click.option(
    "-r",
    "--prompter",
    default="",
    type=click.Path(file_okay=True),
    help="[Experimental] Path to a prompter script that will be used to gather parameters from the user",
)
@click.pass_context
def plan(ctx, input, embed, identifier="", params={}, prompter=""):
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
            "CREATED_AT": str(datetime.now(timezone.utc)),
            "CREATED_BY": os.environ["USER"],
        }
    }

    # TODO: add test cases for auto-planning
    # As of 2025 Jan it's manual regression testing
    if len(params) == 0 or prompter:
        inferred_params = pm.inspect_notebook(input)
        notebook_language = get_notebook_language(input)
        value_parser = get_parser_by_language(notebook_language)
        # Inferred_type_name is language specific
        formatted_params = {}
        for key, value in inferred_params.items():
            if key != RUNBOOK_METADATA:
                default = value["default"].rstrip(";")
                typing = value["inferred_type_name"] or ""
                help = value["help"] or ""
                formatted_params[key] = {
                    "default": default,
                    "typing": typing,
                    "help": help,
                }

        if prompter:
            # Input format: params: {'server': {'default': '"main.xargs.io"', 'typing': 'string', 'help': ''}, 'arg': {'default': '1', 'typing': 'number', 'help': ''}, 'anArray': {'default': '["a", "b"]', 'typing': 'string[]', 'help': 'normally a / b'}, '__RUNBOOK_METADATA__': {'default': '{}', 'typing': 'None', 'help': ''}}
            # Run prompter with inferred params passed via stdin
            result = subprocess.run(
                [prompter],
                input=json.dumps(formatted_params),
                capture_output=True,
                text=True,
            )
            # Response format: params: {'server': '"main.xargs.io"', 'arg': '1', 'anArray': '["a", "b"]'}
            params = json.loads(result.stdout.strip())
        else:
            for key, value in formatted_params.items():
                default_str = value["default"]

                def value_proc(user_input, _default=default_str, _parser=value_parser):
                    if user_input is None or (
                        isinstance(user_input, str) and user_input.strip() == ""
                    ):
                        try:
                            return _parser(_default)
                        except (json.JSONDecodeError, ValueError, SyntaxError):
                            return RawExpression(_default)
                    try:
                        return _parser(user_input)
                    except (json.JSONDecodeError, ValueError, SyntaxError):
                        return RawExpression(user_input)

                parsed_value = click.prompt(
                    f"""Enter value for {key} {value["typing"]} {value["help"]}""",
                    default=default_str,
                    value_proc=value_proc,
                )
                params[key] = parsed_value

    injection_params = {**runbook_param_injection, **params}

    if not Path(output_folder).exists():
        os.makedirs(output_folder, exist_ok=True)

    inject_parameters_and_write(
        input,
        full_output,
        injection_params,
        clear_output=True,
    )

    for f in embed:
        shutil.copyfile(src=f, dst=f"{output_folder}/{path.basename(f)}")

    cmd = click.style(f"$> runbook run {full_output}", fg="green", bold=True)
    click.echo(click.style(f"Run your new runbook instance with:\n\t{cmd}"))
