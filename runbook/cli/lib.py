import hashlib
import sys
from io import StringIO

from ulid import ULID


def sha256sum(filename):
    with open(filename, "rb", buffering=0) as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


# 10 is a pure timestamp to millisecond precision
# 11 allows or a few generations per ms without collisions
# if needing collision resistance greater than casual and low generation rate
# use ULID() directly
def ts_id(length=10):
    return str(ULID())[0:length]


# Suppresses nbconvert output
def nbconvert_launch_instance(argv, clear_output=True):
    # Imported here to avoid performance hit of importing it
    from nbconvert.nbconvertapp import NbConvertApp

    if clear_output:
        argv.insert(0, "--ClearOutputPreprocessor.enabled=True")
    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdout = StringIO()
    sys.stderr = StringIO()
    try:
        NbConvertApp().launch_instance(argv=argv)
    except Exception as e:
        print(sys.stdout.getvalue())
        print(sys.stderr.getvalue())
        raise e
    finally:
        # Restore stdout/stderr
        sys.stdout = stdout
        sys.stderr = stderr
