import nbformat
from nbformat import NotebookNode
from nbclient import NotebookClient
import sys
import click

def hook_on_notebook_start(notebook):
  input("Request input")

def hook_on_cell_start(cell: NotebookNode, cell_index: int):
  click.echo(click.style('ATTENTION!', blink=True, fg='red'))
  input("Start cell?\n")
  print(cell.source)
  print("\n")

def hook_on_cell_executed(cell: NotebookNode, cell_index: int, execute_reply):
  print("Output\n")
  print(cell.metadata.execution)
  print(cell.outputs)
  print("\n")


notebook_filename = sys.argv[1]
nb = nbformat.read(notebook_filename, as_version=4)
# This is where to hook
client = NotebookClient(nb, timeout=-1, on_cell_executed=hook_on_cell_executed, on_notebook_start=hook_on_notebook_start, on_cell_start=hook_on_cell_start, kernel_name='python3', resources={'metadata': {'path': 'runbooks/'}})
client.execute()
nbformat.write(nb, f'executed-{notebook_filename}')
