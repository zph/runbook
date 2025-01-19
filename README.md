# Runbook

## Summary

Runbook is a commandline tool that guides users in an opinionated approach to creating dynamic runbooks.

In this context, a runbook is a mixture of markdown and executable code that contains the steps needed for successful operational executions such as server maintenance, database management, or creating a weekly report.

### When would you use this?
1. When you want quick to write tools that can't be entirely automated, but want the safey of auditable tools.
2. When your tooling needs to adjust rapidly and contain prepared rollback procedures.
3. When this is a semi-custom situation that doesn't warrant building dedicated and expensive tooling
4. When you've grown out of shell scripts but aren't ready to build it in Golang or Rust

### Runbook Best Practices
1. Include a Summary/Purpose, Step descriptions, Warning signs, Verification Steps and Execution Steps in their natural order
2. Non-mutative actions can be included anyhere
3. Mutative actions (destroy a server or force a failover) must use the `confirm` flag
4. Write pre-check steps before mutation steps in order to increase safety of the procedure
5. Runbooks for critical operations should be run by pairs of staff members
   1. One to execute the book
   2. A second to validate and perform safety checks

## Workflow

1. Initialize a new folder project with `runbook init...`
1. Create a new runbook with `runbook create -l deno runbook-name.ipynb`
1. Plan that runbook for a specific run `runbook plan runbook-name.ipynb --embed file.json --parameters '{"arg": 1, "foo": "baz"}'
1. Run the instance of a runbook with either `runbook run runbook-name.ipynb` or use VSCode to run it `code runbooks/run/runbook-name.ipynb`

## Installation

We recommend using [uv](https://docs.astral.sh/uv/) or [pipx](https://pypi.org/project/pipx/) for installing runbook as a cli tool.

```sh
uv tool install git+https://github.com/zph/runbook.git
# or
pipx install git+https://github.com/zph/runbook.git
```

Or pin to a version

```sh
uv tool install git+https://github.com/zph/runbook.git@v0.0.1

pipx install git+https://github.com/zph/runbook.git@v0.0.1
```

## CLI

```sh
Usage: runbook [OPTIONS] COMMAND [ARGS]...

Options:
  --cwd PATH  Directory for operations (normally at root above runbooks, ie
              ../.runbook.yaml) and can be set with RUNBOOK_WORKING_DIR or
              WORKING_DIR environment variables
  --help      Show this message and exit.

Commands:
  check    Check language validity and formatting of a notebook.
  convert  Convert an existing runbook to different format
  create   Create a new runbook from [template]
  diff     Diff two notebooks
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

- Prefer deno for better package management and developer ergonomics
    - But allow for other kernels (python) as secondary option, via compatible libraries
- Make `runbook` batteries included for interfacing with shell commands and common runbook
operations (ie grafana and notifications)
- Sets up necessary requirements to ensure cell executions are timed and displayed as
long as executions run through `runbook run ...` command

# Caveats

1. Running notebook in VScode does not set the timings necessary in notebook for being auditable and exported later
   1. Recommendation: if auditable runs are needed, use jupyter via browser `runbook run TITLE`
1. Notebooks have different structured ids per cell depending on run environment
   1. Recommendation: if requiring consistency, write your own pre-processor to standardize on an id format
1. Builting shell package requires a shell environment and is only expected to run on Linux or Mac not Windows.
   1. Recommendation: suggest fixes in PR or Issues on Github

## Deno / Typescript
1. Parameter cells should use `let` declarations to allow for param overriding
    - This is required to correctly support executing the ts version of notebooks.

# Developing runbook cli

We use [hermit](https://hermit.dev/) to manage developement dependencies.

Use [uv](https://docs.astral.sh/uv/) as the package manager/execution environment.

Necessary deps can be seen in [pyproject.toml](pyproject.toml) and .hermit/bin

Use .hermit/bin/activate-hermit to activate the environment.

# Readme Changes

README.md is generated from .config/README.md.template and should be updated there.
