# Runbook

## CLI

```
# Initialize a folder for use as runbook repository
runbook init

# Create runbook from a template
runbook create [--template=TEMPLATE] TITLE

# Create an instance of a runbook for execution by filling in parameterization
# Adds metadata indicating that runbook is ready to execute
runbook plan TITLE

# Run a notebook server in browser (starts jupyter server and opens page)
runbook serve

# Review a runbook which inserts metadata to allow a type of execution
runbook review TITLE

# Run runbook straight through
runbook run TITLE


```

# Decisions
- Use python for interop with ipynb and the supporting libraries
- Make this batteries included for interfacing with shell commands
- Determine and use correct modern standard for python dependency management
- Sets up necessary requirements to ensure cell executions are timed and displayed
- Consider click for cli lib https://click.palletsprojects.com/en/8.1.x/

# TODO
- Setup different folder from runbooks for execution files?
- Only allow for executing runbooks that are pre-processed
- Should I follow the tf convention of `plan | apply`
- Allow for executing cell by cell from commandline in a repl?
- Setup decorator to embed dry_run into shell command
- Use slack notify for posting execution steps: https://github.com/keitakurita/jupyter-slack-notify
- Running cell by cell: https://github.com/odewahn/ipynb-examples/blob/master/Importing%20Notebooks.ipynb
