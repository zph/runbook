.DEFAULT_GOAL := help

.PHONY: help test test-watch open clear-binder-output clear-output lint lint-all profile release clean build benchmark readme docs docs-release

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

test: ## Run pytest and deno tests
	uv run pytest --disable-warnings -s
	deno test -A --reload https://raw.githubusercontent.com/zph/runbook/main/ext/deno/runbook/mod.ts --parallel tests/cli_test.ts

test-watch: ## Run tests on file changes
	watchexec -- make test

open: ## Open a notebook (usage: make open NOTEBOOK=path/to/nb)
	uv run runbook edit $(NOTEBOOK)

clear-binder-output: ## Clear outputs from binder notebooks
	uv run runbook clear-output ./runbook/data/*.ipynb

clear-output: ## Clear outputs from notebooks (usage: make clear-output FILES="a.ipynb b.ipynb")
	uv run runbook clear-output $(FILES)

lint: ## Run pre-commit hooks on staged files
	pre-commit run

lint-all: ## Run pre-commit hooks on all files
	pre-commit run --all-files

profile: ## Profile the CLI with cProfile
	uv run python3 -m cProfile runbook/cli/__init__.py

release: ## Create a release via release-it
	deno run -A npm:release-it

clean: ## Remove build artifacts
	rm -rf ./dist

build: ## Build the package
	uv build

benchmark: ## Run benchmark and export to docs/PERFORMANCE.md
	hyperfine --export-markdown=docs/PERFORMANCE.md -- runbook

readme: ## Regenerate README from template
	.config/templating.sh

docs: ## Build documentation site
	cp -f README.md docs/
	uvx --with sphinx-click --with myst_parser --with . --from sphinx sphinx-build -b html docs/ site

docs-release: ## Publish documentation
	bash .hermit/bin/publish-docs

run: ## Run the CLI (usage: make run ARGS="command args")
	uv run runbook $(ARGS)
