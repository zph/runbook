import sys

if sys.version_info >= (3, 7):
    from importlib import resources as importlib_resources
else:
    import pkgutil


def read_embedded_file(package: str, filename: str) -> str:
    """
    Reads an embedded file from a given package using the appropriate method
    based on the Python version.

    :param package: The package name where the file is located (e.g., "mypackage.data").
    :param filename: The name of the file inside the package (e.g., "myfile.txt").
    :return: The contents of the file as a string.
    """
    if sys.version_info >= (3, 7):
        # Use importlib.resources (Python 3.7+)
        with (
            importlib_resources.files(package)
            .joinpath(filename)
            .open("r", encoding="utf-8") as f
        ):
            return f.read()
    else:
        # Use pkgutil.get_data() for older versions
        data = pkgutil.get_data(package, filename)
        return data.decode("utf-8") if data else None


TEMPLATES = {
    "python": read_embedded_file("runbook.data", "_template-python.ipynb").strip(),
    "deno": read_embedded_file("runbook.data", "_template-deno.ipynb").strip(),
}
