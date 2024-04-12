import os
from datetime import datetime
from os import path
from pathlib import Path

import click
from runbook.cli.validators import validate_plan_params, validate_runbook_file_path

import papermill as pm


# TODO: standardize ids in output files through custom processor
# use something like ulid, we don't need full UUIDs
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
    output_basename_without_ext = basename_without_ext + "-" + identifier
    output = "-".join([str(date), basename_without_ext])
    # Output to folder to allow for embedding other files in same folder
    output_folder = f"./runbooks/runs/{output}"
    full_output = f"{output_folder}/{output_basename_without_ext}.ipynb"

    runbook_param_injection = {
        "__RUNBOOK_METADATA__": {
            "RUNBOOK_FOLDER": output_folder,
            "RUNBOOK_FILE": full_output,
            "RUNBOOK_SOURCE": input,
            "CREATED_AT": str(datetime.utcnow()),
            "CREATED_BY": os.environ["USER"],
        }
    }

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
        "--ClearOutputPreprocessor.enabled=True",
        # "--ClearMetadataPreprocessor.enabled=True",
        # "--ClearMetadataPreprocessor.clear_notebook_metadata=False",
        # """--ClearMetadataPreprocessor.preserve_cell_metadata_mask='[("tags")]'""",
        "--inplace",
        full_output,
    ]

    # TODO: join the unified logic of create and plan

    # TODO: hide the nbconvert verbose output?
    from nbconvert.nbconvertapp import NbConvertApp

    NbConvertApp().launch_instance(argv=argv)

    for f in embed:
        shutil.copyfile(src=f, dst=f"{output_folder}/{path.basename(f)}")

    cmd = click.style(
        f"$> runbook run {path.basename(full_output)}", fg="green", bold=True
    )
    click.echo(click.style(f"Run your new runbook instance with:\n\t{cmd}"))
