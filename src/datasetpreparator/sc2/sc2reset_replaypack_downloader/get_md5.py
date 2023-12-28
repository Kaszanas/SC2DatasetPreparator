import hashlib
from pathlib import Path


# REVIEW: This can be done in chunks to avoid loading the whole file into memory:
def get_md5(file: Path) -> str:
    """
    Calculates and returns the md5 hash of a file.

    Parameters
    ----------
    file : Path
        Path to the file for which the md5 hash will be calculated.

    Returns
    -------
    str
        Returns the string of a md5 hash of a file.
    """

    with file.open("rb") as f:
        md5 = hashlib.md5(f.read()).hexdigest()

    return md5
