import hashlib

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
