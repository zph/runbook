# TODO
## P0
- [ ] Setup versioning and bumper (using versioner from npm ecosystem @release-it and @release-it/bumper)
- [x] Fix tag key getting stripped out of planned runbooks b/c it breaks papermill
- [ ] Setup a watcher for auto-exporting html or other formats
- [ ] Setup tagging in the notebooks to auto-set those values
- [ ] Setup git to autoclear cell outputs for a given folder's notebooks (ie templates) https://stackoverflow.com/a/58004619
- [x] Assess if we need shell completions
   - [x] Yes, very nice and use https://click.palletsprojects.com/en/8.1.x/shell-completion/#custom-type-completion to define for custom types, ie only find ipynb files for edit, create, etc
- [ ] Integrate mechanisms to read Grafana or other data sources and package "pre/post check" helpers
  - [ ] ie poll for values over N period and if exceeding Y or Z then throw error and suggest rollbacks

## P1
- [ ] Include safe way to retry when APIs fail but with confirmation
    - for handling the case when infrastructure API calls fail when made in large async batch
- [ ] Immutably store everything with bookstore https://github.com/nteract/bookstore
- [x] Use slack notify for posting execution steps: https://github.com/keitakurita/jupyter-slack-notify
- [ ] Install pre-commit.yml or git integration during `init`

## P2
- [x] Setup different folder from runbooks for execution files?
- [x] Only allow for executing runbooks that are pre-processed
- [x] Should I follow the tf convention of `plan | apply`
- [x] Setup decorator to embed dry_run into shell command
- [ ] (won't do yet) Allow for executing cell by cell from commandline in a repl?
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
