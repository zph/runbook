import json
from pathlib import Path

import nbformat
from click.testing import CliRunner

from runbook import cli


def invoker(runner, argv, working_dir, prog_name="runbook"):
    return runner.invoke(
        cli, argv, env={"RUNBOOK_WORKING_DIR": working_dir}, prog_name=prog_name
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
              ../.runbook.yaml)
  --help      Show this message and exit.

Commands:
  create  Create a new runbook from [template]
  edit    Edit an existing runbook
  init    Initialize a folder as a runbook repository
  plan    Prepares the runbook for execution by injecting parameters.
  review  [Unimplemented] Entrypoint for reviewing runbook
  run     Run a notebook
"""
        assert result.output == output


def test_cli_init():
    runner = CliRunner()
    with runner.isolated_filesystem() as dir:
        result = invoker(runner, ["init"], dir)
        assert result.exit_code == 0
        paths = [
            "./runbooks",
            "./runbooks/binder",
            "./runbooks/runs",
            "./runbooks/.runbook.json",
            "./runbooks/binder/_template-python.ipynb",
            "./runbooks/binder/_template-deno.ipynb",
        ]
        for p in paths:
            assert Path(p).exists()


def test_cli_create():
    runner = CliRunner()
    with runner.isolated_filesystem() as dir:
        result = invoker(runner, ["init"], dir)
        result = invoker(runner, ["create", "new-template"], dir)
        assert result.exit_code == 0
        paths = [
            "./runbooks",
            "./runbooks/binder",
            "./runbooks/runs",
            "./runbooks/.runbook.json",
            "./runbooks/binder/_template-python.ipynb",
            "./runbooks/binder/_template-deno.ipynb",
            "./runbooks/binder/new-template.ipynb",
        ]
        for p in paths:
            assert Path(p).exists()

        with open("./runbooks/binder/_template-python.ipynb", encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open("./runbooks/binder/_template-deno.ipynb", encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open("./runbooks/binder/new-template.ipynb", encoding="utf8") as f:
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
        paths = [
            "./runbooks",
            "./runbooks/binder",
            "./runbooks/runs",
            "./runbooks/.runbook.json",
            "./runbooks/binder/_template-python.ipynb",
            "./runbooks/binder/_template-deno.ipynb",
            "./runbooks/binder/new-template.ipynb",
        ]
        for p in paths:
            assert Path(p).exists()

        with open("./runbooks/binder/_template-python.ipynb", encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open("./runbooks/binder/_template-deno.ipynb", encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open("./runbooks/binder/new-template.ipynb", encoding="utf8") as f:
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
        paths = [
            "./runbooks",
            "./runbooks/binder",
            "./runbooks/runs",
            "./runbooks/.runbook.json",
            "./runbooks/binder/_template-python.ipynb",
            "./runbooks/binder/_template-deno.ipynb",
            "./runbooks/binder/new-template.ipynb",
        ]
        for p in paths:
            assert Path(p).exists()

        with open("./runbooks/binder/_template-python.ipynb", encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        with open("./runbooks/binder/_template-deno.ipynb", encoding="utf8") as f:
            nb = nbformat.read(f, 4)
            c = nb.cells[2]
            assert "parameters" in c.metadata.tags

        # TODO: fix tags being not present for parameters despite being there in _template
        # with open("./runbooks/binder/new-template.ipynb", encoding="utf8") as f:
        #     nb = nbformat.read(f, 4)
        #     c = nb.cells[2]
        #     assert "parameters" in c.metadata.tags

        # TODO: fix multiple singletons of ServerApp
        # result = invoker(runner, ["run", "./runbooks/binder/new-template.ipynb"], dir)
        # assert result.exit_code == 0
