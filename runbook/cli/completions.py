import click
from click.shell_completion import CompletionItem
from glob import glob


def runnable_shell_complete(self, ctx, param, incomplete):
    pattern = f"**/{incomplete}*.ipynb"
    if incomplete == "":
        pattern = f"**/*.ipynb"

    return [
        CompletionItem(name) for name in glob(pattern, recursive=True) if "runs" in name
    ]


RunnableNotebook = click.Path
RunnableNotebook.shell_complete = runnable_shell_complete


def editable_shell_complete(self, ctx, param, incomplete):
    pattern = f"**/{incomplete}*.ipynb"
    if incomplete == "":
        pattern = f"**/*.ipynb"

    return [CompletionItem(name) for name in glob(pattern, recursive=True)]


EditableNotebook = click.Path
EditableNotebook.shell_complete = editable_shell_complete
