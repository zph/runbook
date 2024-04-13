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

## CLI

```sh
# Initialize a folder for use as runbook repository
runbook init

# Create runbook from a template
runbook create [--template=TEMPLATE] TITLE

# Edit a notebook server in browser (starts jupyter server and opens page)
runbook edit RUNBOOK_PATH

# Create an instance of a runbook for execution by filling in parameterization
# Adds metadata indicating that runbook is ready to execute
runbook plan RUNBOOK_PATH

# [Future Implementation]
# Review a runbook which inserts metadata to allow a type of execution
runbook review TITLE

# Execute a runbook where default is --interactive=true
# Note can only find runbooks that have been prepared
runbook run TITLE

# [Future Implementation]
# Export runbook to HTML / PDF / MD
runbook export TITLE
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
1. Confirm/prompt functions always return false in notebooks due to lack of support
    in deno kernel. We may invest in upstreaming a patch to support this as it has support
    in python notebooks
