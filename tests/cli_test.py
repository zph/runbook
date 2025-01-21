import json
from pathlib import Path

import nbformat
from click.testing import CliRunner

from runbook import cli

python_template = "./runbooks/binder/_template-python.ipynb"
deno_template = "./runbooks/binder/_template-deno.ipynb"
new_template = "./runbooks/binder/new-template.ipynb"

base_paths = [
    "./runbooks",
    "./runbooks/binder",
    "./runbooks/runs",
    "./runbooks/.runbook.json",
    python_template,
    deno_template,
]


def invoker(runner, argv, working_dir, prog_name="runbook"):
    return runner.invoke(
        cli,
        argv,
        env={
            "RUNBOOK_WORKING_DIR": working_dir,
        },
        prog_name=prog_name,
    )


def test_cli_help():
    runner = CliRunner()
    with runner.isolated_filesystem() as dir:
        result = invoker(runner, ["--help"], dir)
        assert result.exit_code == 0
        output = """\
Usage: runbook [OPTIONS] COMMAND [ARGS]...

Options:
  --cwd PATH  Directory for operations (normally at root above runbooks, ie
              ../.runbook.yaml) and can be set with RUNBOOK_WORKING_DIR or
              WORKING_DIR environment variables
  --help      Show this message and exit.

Commands:
  check    Check the language validity and formatting of a runbook.
  convert  Convert a runbook between different formats
  create   Create a new runbook from a template
  diff     Compare two runbooks and show their differences
  edit     Edit an existing runbook
  init     Initialize a folder as a runbook repository
  list     List runbooks
  plan     Prepares the runbook for execution by injecting parameters.
  review   [Unimplemented] Entrypoint for reviewing runbook
  run      Run a runbook
  show     Show runbook parameters and metadata
  version  Display version information about runbook
"""
        assert result.output == output


def test_cli_init():
    runner = CliRunner()
    with runner.isolated_filesystem() as dir:
        result = invoker(runner, ["init"], dir)
        assert result.exit_code == 0
        for p in base_paths:
            assert Path(p).exists()


def test_cli_create():
    runner = CliRunner()
    with runner.isolated_filesystem() as dir:
        result = invoker(runner, ["init"], dir)
        result = invoker(runner, ["create", "new-template"], dir)
        assert result.exit_code == 0
        paths = [*base_paths, new_template]
        for p in paths:
            assert Path(p).exists()

        with open(python_template, encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open(deno_template, encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open(new_template, encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags


def test_cli_lifecycle_to_plan():
    runner = CliRunner()
    with runner.isolated_filesystem() as dir:
        result = invoker(runner, ["init"], dir)
        assert result.exit_code == 0
        result = invoker(runner, ["create", "new-template"], dir)
        assert result.exit_code == 0
        paths = [*base_paths, new_template]
        for p in paths:
            assert Path(p).exists()

        with open(python_template, encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open(deno_template, encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open(new_template, encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        # result = invoker(runner, ["edit", "new-template.ipynb"], dir)

        json_params = json.dumps(dict(dry_run=False))
        result = invoker(
            runner,
            ["plan", "new-template.ipynb", "--params", f"""{json_params}"""],
            dir,
        )
        assert result.exit_code == 0

        # result = invoker(runner, ["run", "new-template.ipynb"], dir)
        # assert result.exit_code == 0


def test_cli_lifecycle_to_run():
    runner = CliRunner()
    with runner.isolated_filesystem() as dir:
        result = invoker(runner, ["init"], dir)
        assert result.exit_code == 0
        result = invoker(runner, ["create", "new-template"], dir)
        assert result.exit_code == 0
        paths = [*base_paths, new_template]
        for p in paths:
            assert Path(p).exists()

        with open(python_template, encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open(deno_template, encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        # TODO: fix multiple singletons of ServerApp
        # result = invoker(runner, ["run", deno_template], dir)
        # assert result.exit_code == 0
