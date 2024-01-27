from asyncio.subprocess import Process
from datetime import datetime
from shlex import quote as Q

import click
from click import echo, style
from shx.shx import _CVAR as cv
from shx.shx import SHX


class ShellProcess(Process):
    def __init__(
        self, process, command, dry_run=False, tags={}, start_time=None, end_time=None
    ):
        self.stdout = str(process.stdout).rstrip("\n")
        self.stdout_raw = process.stdout
        self.stderr = process.stderr
        self.stdin = process.stdin
        self.command = command
        self.pid = process.pid
        self.dry_run = dry_run
        self.tags = tags
        self.start_time = start_time
        self.end_time = end_time

        self.duration = end_time - start_time

    def to_dict(self):
        return {
            "command": self.command,
            "timestamps": {
                "start": datetime.isoformat(self.start_time),
                "end": datetime.isoformat(self.end_time),
                "duration": str(self.duration),
            },
            "stdout": self.stdout,
            "stderr": self.stderr,
            "stdin": self.stdin,
            "pid": self.pid,
            "dry_run": self.dry_run,
            "tags": self.tags,
        }

    def __str__(self):
        return f"ShellProcess({self.to_dict()})"

    def __repr__(self):
        return f"ShellProcess({self.to_dict()})"


def shell_builder(dry_run, tags_default, confirm_default):
    from functools import partial

    return partial(
        shell,
        dry_run=dry_run,
        tags_default=tags_default,
        confirm_default=confirm_default,
    )


async def shell(cmd: str, dry_run, tags={}, confirm=False, **kwargs):
    tags_default = kwargs.pop("tags_default", None)
    confirm_default = kwargs.pop("confirm_default", False)
    trace = cv["trace"].get()
    prefix = cv["prefix"].get()
    capture = True
    if tags_default:
        tags = {**tags_default, **tags}
    if confirm_default:
        confirm = confirm or confirm_default

    if dry_run:
        cmd_mod = f"echo {Q(cmd)}"
    else:
        cmd_mod = cmd

    if confirm:
        echo(f"Prepared to execute command: {cmd_mod}")
        click.confirm(style("Proceed?", fg="red", bold=True), abort=True)
    start_time = datetime.now()
    result = await SHX(cmd_mod, prefix, trace, capture, **kwargs)
    end_time = datetime.now()

    if dry_run:
        result.command = cmd
        result.stdout = ""
    return ShellProcess(result, cmd, dry_run, tags, start_time, end_time)
