from shlex import quote as Q
from shx.shx import SHX, gather
from shx.shx import _CVAR as cv
from asyncio.subprocess import Process

class ShellProcess(Process):
    def __init__(self, process, command, dry_run=False, tags={}):
        self.stdout = str(process.stdout).rstrip("\n")
        self.stdout_raw = process.stdout
        self.stderr = process.stderr
        self.stdin  = process.stdin
        self.command = command
        self.pid    = process.pid
        self.dry_run = dry_run
        self.tags = tags

    def to_dict(self):
        return {'command': self.command, 'stdout': self.stdout, 'stderr': self.stderr, 'stdin': self.stdin, 'pid': self.pid, 'dry_run': self.dry_run, 'tags': self.tags}

    def __str__(self):
        return f"ShellProcess({self.to_dict()})"

    def __repr__(self):
        return f"ShellProcess({self.to_dict()})"

def shell_builder(dry_run):
    def sh(cmd: str, tags={}, **kwargs):
        return shell(cmd, dry_run, tags, **kwargs)

    return sh

async def shell(cmd: str, dry_run, tags={}, **kwargs):
    tags_default = kwargs.pop('tags_default', None)
    trace = cv["trace"].get()
    prefix = cv["prefix"].get()
    capture = True
    if tags_default:
        tags = {**tags_default, **tags}

    if dry_run:
        cmd_mod = f"echo {Q(cmd)}"
    else:
        cmd_mod = cmd

    result = await SHX(cmd_mod, prefix, trace, capture, **kwargs)

    if dry_run:
        result.command = cmd
        result.stdout = ''
    return ShellProcess(result, cmd, dry_run, tags)
