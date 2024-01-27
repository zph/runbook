import nbformat
from nbformat import NotebookNode
from nbclient import NotebookClient
import sys
import click
from click import echo, confirm, style
from IPython import embed


def hook_on_notebook_start(notebook):
    echo("NB start")


def hook_on_cell_start(cell: NotebookNode, cell_index: int):
    echo(style("ATTENTION!\n", blink=True, fg="red"))
    echo(cell.source)
    confirm("Start cell?", abort=True)
    print("\n")


def hook_on_cell_executed(cell: NotebookNode, cell_index: int, execute_reply):
    echo("Output\n")
    echo(cell.metadata.execution)
    echo(cell.outputs)


notebook_filename = sys.argv[1]
nb = nbformat.read(notebook_filename, as_version=4)
# This is where to hook
client = NotebookClient(
    nb,
    timeout=-1,
    on_cell_executed=hook_on_cell_executed,
    on_notebook_start=hook_on_notebook_start,
    on_cell_start=hook_on_cell_start,
    kernel_name="python3",
    resources={"metadata": {"path": "runbooks/"}},
)
embed()
client.execute()
nbformat.write(nb, f"executed-{notebook_filename}")
