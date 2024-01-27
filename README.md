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

# Create an instance of a runbook for execution by filling in parameterization
# Adds metadata indicating that runbook is ready to execute
runbook plan RUNBOOK_PATH

# Edit a notebook server in browser (starts jupyter server and opens page)
runbook edit RUNBOOK_PATH

# Execute a runbook where default is --interactive=true
# Note can only find runbooks that have been prepared
runbook run TITLE

# Review a runbook which inserts metadata to allow a type of execution
runbook review TITLE
```

# Decisions

- Use python for interop with ipynb and the supporting libraries
    - But allow for other kernels as secondary option
- Make `runbook` batteries included for interfacing with shell commands and common runbook
operations (ie grafana and notifications)
- Use modern standard for python dependency management aka poetry.
- Sets up necessary requirements to ensure cell executions are timed and displayed

# TODO
## P0
- [ ] Fix tag key getting stripped out of planned runbooks b/c it breaks papermill
- [ ] Setup a watcher for auto-exporting html or other formats
- [ ] Setup tagging in the notebooks to auto-set those values
- [ ] Setup git to autoclear cell outputs for a given folder's notebooks (ie templates) https://stackoverflow.com/a/58004619
- [ ] Assess if we need shell completions
   - [ ] Yes, very nice and use https://click.palletsprojects.com/en/8.1.x/shell-completion/#custom-type-completion to define for custom types, ie only find ipynb files for edit, create, etc

## P1
- [ ] Immutably store everything with bookstore https://github.com/nteract/bookstore
- [ ] Use slack notify for posting execution steps: https://github.com/keitakurita/jupyter-slack-notify
- [ ] Install pre-commit.yml or git integration during `init`

## P2
- [x] Setup different folder from runbooks for execution files?
- [x] Only allow for executing runbooks that are pre-processed
- [x] Should I follow the tf convention of `plan | apply`
- [ ] (won't do yet) Allow for executing cell by cell from commandline in a repl?
- [x] Setup decorator to embed dry_run into shell command
- [ ] Running cell by cell: https://github.com/odewahn/ipynb-examples/blob/master/Importing%20Notebooks.ipynb
- [ ] figure out how to store and replay individual cells
- [ ] ~~Textualize gui for tui?~~
- [ ] ~~is euphorie's tui for notebooks helpful?~~
- [ ] Build auditability through a custom runner interface
  -- Or a custom kernel wrapper?
  -- https://ipython.readthedocs.io/en/stable/config/options/kernel.html
- [x] Jupytext runner that watches fs changes and exports to scripts (can be done via jupytext
        config)
- [ ] After execution in web browser jupyter notebook or in vscode dynamic environment, execute as HTML
   for archival. It looks great.

   - Use custom format for nbconvert exports: https://nbconvert.readthedocs.io/en/latest/customizing.html

   > jupyter nbconvert --TemplateExporter.extra_template_basedirs=nbconvert/templates --to markdown --template=mdaudit exec
   > uted-Untitled4.ipynb

- [x] (NA it's in modern jupyter) Bundle in the timing nbextension jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/execute_time/readme.html
- [x] (won't do) Freeze dangerous cells as a safegurad? https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/freeze/readme.html
- [x] (won't do) Cell filtering https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/cell_filter/README.html

## How To
How to connect to existing running notebook from different interface:
- https://stackoverflow.com/questions/31382405/ipython-notebook-how-to-connect-to-existing-kernel
1. %connect_info in the notebook and note the json file it references
2. jupyter console --existing JSONFILE

## Extensibility

- Runners
   - Run from local
   - Run against remote deployed server behind auth? can be done via Spawners
   - Store files on S3 (ie repo published to S3 for centralized repo?) https://github.com/danielfrg/s3contents

- Get extension for skip working: https://raw.githubusercontent.com/RobbeSneyders/Jupyter-skip-extension/master/skip_kernel_extension.py
