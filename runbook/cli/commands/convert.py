import tempfile
from os import path

import click
import nbformat
from runbook.add_prompt_preprocessor import AddPromptPreprocessor
from runbook.cli.completions import EditableNotebook
from runbook.cli.validators import validate_runbook_file_path


@click.command()
@click.argument(
    "filename",
    type=EditableNotebook(file_okay=True),
    callback=validate_runbook_file_path,
)
@click.argument(
    "output",
    type=click.Path(exists=False, file_okay=True, writable=True),
)
@click.option(
    "-i",
    "--insert-prompts",
    default=False,
    help="Insert prompt statements at start of each cell",
)
@click.pass_context
def convert(ctx, filename, output, insert_prompts):
    """Convert an existing runbook to different format"""
    # Must override argv because it's used in launch instance and there isn't a way
    # to pass via argument in ExtensionApp.lauch_instance

    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fp:
        content = nbformat.reads(open(filename).read(), as_version=4)
        if content.metadata.get("kernelspec").get("name") == "deno":
            (nb, _resources) = AddPromptPreprocessor().preprocess(content, {})
        else:
            nb = content
        with tempfile.NamedTemporaryFile(suffix=".ipynb") as fp:
            nbformat.write(nb, fp.name)
            argv = [path.abspath(fp.name), "--output", output]
            # Lazily loaded for performance
            from jupytext.cli import jupytext as jupytext_main

            print(f"Running jupytext {argv}")
            jupytext_main(args=argv)
