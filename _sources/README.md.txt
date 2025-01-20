# Runbook

## Summary

Runbook is a powerful CLI tool that transforms your operational procedures into interactive, executable notebooks. It combines the best of documentation and automation by letting you create dynamic runbooks using Markdown, Deno, or Python.

Think of it as "infrastructure as code" meets "documentation as code" - perfect for DevOps teams who want both flexibility and reliability.

**At work, it empowered us to move 300 Mysql Clusters to TiDB with a small team [recording](https://www.youtube.com/watch?app=desktop&v=-_JoqZthrI8) over the course of 18 months.**

# Quick Start

```sh
uv tool install git+https://github.com/zph/runbook.git@1.0.0-rc2

# Initialize a new runbook project in a repo of your choosing
runbook init

# Create a new runbook
runbook create -l deno runbook-name.ipynb

# Edit the runbook
runbook edit runbook-name.ipynb

# Plan the runbook
runbook plan runbook-name.ipynb --embed file.json --parameters '{"arg": 1, "foo": "baz"}'

# Run the runbook
runbook run runbook-name.ipynb
```

# Background

## What is a Runbook?
A runbook is an executable document that combines:
- Clear markdown documentation
- Runnable code blocks
- Parameterized inputs for reusability
- Built-in safety checks

It's ideal for operations like encoding your Disaster Recovery Operations, spinning up a new cluster, or restoring from snapshots.

## When Should You Use This?
- ✅ When you need **semi-automated tools** with audit trails and safety checks
- ✅ When you want **rapid iteration** on operational procedures with built-in rollback steps
- ✅ When you need something more powerful than shell scripts but don't want to build a full application
- ✅ When you want to make complex operations both **safe and repeatable**

## Runbook Best Practices
1. Structure your runbooks with:
   - Clear purpose and summary
   - Step-by-step descriptions
   - Warning signs and precautions
   - Verification steps
   - Execution steps in logical order
   - Rollback and cleanup steps
2. Keep read-only operations flexible
3. Require explicit confirmation for destructive actions using the `confirm` flag
4. Include pre-flight checks before any system modifications
5. For critical operations, use pair execution:
   - One person to run the procedure
   - Another to verify and validate safety checks

## Workflow

1. Initialize a new folder project with `runbook init...`
1. Create a new runbook with `runbook create -l deno runbook-name.ipynb`
1. Edit the runbook with `runbook edit runbook-name.ipynb` (or using editor of choice) and add your title, description, steps
1. For complex runbooks, offload the coding details into an SDK that you build beside the runbooks that can be reused across multiple runbooks
1. Plan that runbook for a specific run `runbook plan runbook-name.ipynb --embed file.json --parameters '{"arg": 1, "foo": "baz"}'
1. Run the instance of a runbook with either `runbook run runbook-name.ipynb` or use VSCode to run it `code runbooks/runs/runbook-name.ipynb`
1. Depending on auditing needs, you can either commit the "runs" folder to your repo or only keep the "binder" folder committed.
   1. In case of strict auditing needs, we recommend you add auditing of commands in the local SDK as well as in your cloud provider

# Installation

We recommend using [uv](https://docs.astral.sh/uv/) for installing runbook as a cli tool. If you already use pipx, you can use that instead.

```sh
uv tool install git+https://github.com/zph/runbook.git
```

Or pin to a version

```sh
uv tool install git+https://github.com/zph/runbook.git@1.0.0-rc2
```

# CLI

```sh
Usage: runbook [OPTIONS] COMMAND [ARGS]...

Options:
  --cwd PATH  Directory for operations (normally at root above runbooks, ie
              ../.runbook.yaml) and can be set with RUNBOOK_WORKING_DIR or
              WORKING_DIR environment variables
  --help      Show this message and exit.

Commands:
  check    Check the language validity and formatting of a Jupyter notebook.
  convert  Convert a Jupyter notebook between different formats.
  create   Create a new runbook from a template.
  diff     Compare two Jupyter notebooks and show their differences.
  edit     Edit an existing runbook
  init     Initialize a folder as a runbook repository
  list     list runbooks
  plan     Prepares the runbook for execution by injecting parameters.
  review   [Unimplemented] Entrypoint for reviewing runbook
  run      Run a notebook
  show     Show runbook parameters and metadata
  version  Display version information about runbook
```

Shell completion is included via click library and enabled as follows [link](https://click.palletsprojects.com/en/8.1.x/shell-completion/#enabling-completion)

```
# Bash
# Add this to ~/.bashrc:
eval "$(_RUNBOOK_COMPLETE=bash_source runbook)"

# Zsh
# Add this to ~/.zshrc:
eval "$(_RUNBOOK_COMPLETE=zsh_source runbook)"

# Fish
# Add this to ~/.config/fish/completions/foo-bar.fish:
_RUNBOOK_COMPLETE=fish_source runbook | source
```

For advanced completion setup see [docs](https://click.palletsprojects.com/en/8.1.x/shell-completion/#enabling-completion)

# Principles

- Prefer deno for better package management and developer ergonomics with typing
    - But allow for other kernels (python) as secondary option, via compatible libraries
- Make `runbook` batteries included for interfacing with shell commands and common runbook
operations

# Caveats

1. Running notebook in VScode does not set the timings necessary in notebook for being auditable and exported later
   1. Recommendation: if auditable runs are needed, use jupyter via browser `runbook run TITLE`
1. Notebooks have different structured ids per cell depending on run environment
   1. Recommendation: if requiring consistency, write your own pre-processor to standardize on an id format
1. Built-in shell package requires a shell environment and is only expected to run on Linux or Mac not Windows.
   1. Recommendation: Windows support is out of scope for now but we'll review PRs

## Deno / Typescript
1. Parameter cells must use `let` declarations to allow for param overriding
   - `var` or `let` work in Deno notebooks but only `let` works if using `runbook convert a.ipynb a.ts` and running the ts version

# Developing runbook cli

For development we use the following tools:
- [hermit](https://hermit.dev/) to manage developement tool dependencies (see .hermit/bin)
- [uv](https://docs.astral.sh/uv/) python package manager and cli runner (see pyproject.toml)

Necessary deps can be seen in pyproject.toml and .hermit/bin

Use .hermit/bin/activate-hermit to activate the environment.

# Readme Changes

README.md is generated from .config/README.md.template and should be updated there.
