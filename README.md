# Runbook

## CLI

```sh
# Initialize a folder for use as runbook repository
runbook init

# Create runbook from a template
runbook create [--template=TEMPLATE] TITLE

# Create an instance of a runbook for execution by filling in parameterization
# Adds metadata indicating that runbook is ready to execute
runbook plan TITLE

# Edit a notebook server in browser (starts jupyter server and opens page)
runbook edit FILENAME

# Review a runbook which inserts metadata to allow a type of execution
runbook review TITLE

# Execute a runbook where default is --interactive=true
# Note can only find runbooks that have been prepared
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
- figure out how to store and replay individual cells
- Textualize gui for tui?
- is euphorie's tui for notebooks helpful?
- Build auditability through a custom runner interface
   -- Or a custom kernel wrapper?
   -- https://ipython.readthedocs.io/en/stable/config/options/kernel.html
- Jupytext runner that watches fs changes and exports to scripts
- After execution in web browser jupyter notebook or in vscode dynamic environment, execute as HTML
   for archival. It looks great.

   - Use custom format for nbconvert exports: https://nbconvert.readthedocs.io/en/latest/customizing.html

   > jupyter nbconvert --TemplateExporter.extra_template_basedirs=nbconvert/templates --to markdown --template=mdaudit exec
   > uted-Untitled4.ipynb

- Bundle in the timing nbextension jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/execute_time/readme.html
- Dependency management
- Freeze dangerous cells as a safegurad? https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/freeze/readme.html
- Cell filtering https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/cell_filter/README.html
- https://stackoverflow.com/questions/31382405/ipython-notebook-how-to-connect-to-existing-kernel
- Setup git to autoclear cell outputs for a given folder's notebooks (ie templates) https://stackoverflow.com/a/58004619
- Immutably store everything with bookstore https://github.com/nteract/bookstore

How to connect to existing running notebook from different interface:
1. %connect_info in the notebook and note the json file it references
2. jupyter console --existing JSONFILE

## Extensibility

- Runners
   - Run from local
   - Run against remote deployed server behind auth? can be done via Spawners
   - Store files on S3 (ie repo published to S3 for centralized repo?) https://github.com/danielfrg/s3contents

- Get extension for skip working: https://raw.githubusercontent.com/RobbeSneyders/Jupyter-skip-extension/master/skip_kernel_extension.py

## Use magics for powering runbooks

- Confirm?
