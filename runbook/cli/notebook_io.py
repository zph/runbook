"""Inject parameters into a notebook and clear cell outputs. Replaces papermill prepare_only and nbconvert clear-output for the plan command."""

import json
from pathlib import Path

import nbformat

from runbook.constants import RUNBOOK_METADATA


class RawExpression:
    """A value that should be injected verbatim as source code, not serialized."""

    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


def get_notebook_language(notebook_path: str) -> str:
    """Determine the language of the notebook from metadata. Returns 'python', 'typescript', or 'unknown'."""
    nb = nbformat.read(notebook_path, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code":
            if "kernelspec" in nb.metadata:
                kernel_name = nb.metadata.kernelspec.name.lower()
                if "python" in kernel_name:
                    return "python"
                if "typescript" in kernel_name or "ts" in kernel_name:
                    return "typescript"
            if "language_info" in nb.metadata:
                language = nb.metadata.language_info.name.lower()
                if "python" in language:
                    return "python"
                if "typescript" in language or "ts" in language:
                    return "typescript"
    return "unknown"

PARAMETERS_TAG = "parameters"


def _parameters_cell_index(nb):
    """Return the index of the code cell with 'parameters' in metadata.tags, or None."""
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        tags = cell.get("metadata", {}).get("tags") or []
        if PARAMETERS_TAG in tags:
            return i
    return None


def _inject_source_python(params: dict) -> str:
    """Build Python source that assigns each parameter."""
    lines = ["# Injected parameters"]
    for name, value in params.items():
        if isinstance(value, RawExpression):
            lines.append(f"{name} = {value.value}")
        else:
            lines.append(f"{name} = {repr(value)}")
    return "\n".join(lines) + "\n"


def _inject_source_typescript(params: dict) -> str:
    """Build TypeScript/JavaScript source that assigns each parameter."""
    lines = ["// Injected parameters"]
    for name, value in params.items():
        if isinstance(value, RawExpression):
            lines.append(f"var {name} = {value.value};")
        else:
            lines.append(f"var {name} = {json.dumps(value)};")
    return "\n".join(lines) + "\n"


def inject_parameters(nb, params: dict, language: str) -> None:
    """Replace the parameters cell source with assignments for the given params. Modifies nb in place."""
    idx = _parameters_cell_index(nb)
    if idx is None:
        return
    if language == "python":
        source = _inject_source_python(params)
    else:
        source = _inject_source_typescript(params)
    nb.cells[idx].source = source


def clear_cell_outputs(nb) -> None:
    """Clear outputs and execution_count for all cells. Modifies nb in place."""
    for cell in nb.cells:
        cell["outputs"] = []
        cell["execution_count"] = None
        cell.get("metadata", {}).pop("execution", None)


def inject_parameters_and_write(
    input_path: str,
    output_path: str,
    injection_params: dict,
    *,
    clear_output: bool = True,
) -> None:
    """Read notebook, inject parameters, optionally clear outputs, write to output_path."""
    nb = nbformat.read(input_path, as_version=4)
    language = get_notebook_language(input_path)
    inject_parameters(nb, injection_params, language)
    if clear_output:
        clear_cell_outputs(nb)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, output_path)
