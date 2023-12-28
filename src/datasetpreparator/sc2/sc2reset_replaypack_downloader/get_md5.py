import hashlib
from pathlib import Path


# REVIEW: This can be done in chunks to avoid loading the whole file into memory:
def get_md5(file: Path):
    with file.open("rb") as f:
        md5 = hashlib.md5(f.read()).hexdigest()

    return md5
