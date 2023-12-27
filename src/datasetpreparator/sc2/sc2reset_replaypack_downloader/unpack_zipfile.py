from concurrent.futures import ProcessPoolExecutor
import math
from pathlib import Path
from typing import List
import zipfile

from datasetpreparator.sc2.sc2reset_replaypack_downloader.unpack_chunk import (
    unpack_chunk,
)

import tqdm


def unpack_zipfile(
    destination_dir: Path, subdir: str, zip_path: Path, n_workers: int
) -> str:
    """
    Helper function that unpacks the content of .zip archive.

    Parameters
    ----------
    destination_dir : Path
        Specifies the path where the .zip file will be extracted.
    subdir : str
        Specifies the subdirectory where the content will be extracted.
    zip_path : Path
        Specifies the path to the zip file that will be extracted.
    n_workers : int
        Specifies the number of workers that will be used for unpacking the archive.

    Returns
    -------
    str
        Returns a path to the extracted content.

    Raises
    ------
    Exception
        Raises an exception if the number of workers is less or equal to zero.

    Examples
    --------
    The use of this method is intended to extract a zipfile.

    You should set every parameter, destination, subdir, zip_path and n_workers.

    May help you to work with dataset.

    The parameters should be set as in the example below.

    >>> unpack_zipfile_object = unpack_zipfile(
    ... destination_dir="./directory/destination_dir",
    ... subdir="./directory/subdir",
    ... zip_path="./directory/zip_path",
    ... n_workers=1)

    >>> assert isinstance(destination_dir, str)
    >>> assert isinstance(subdir, str)
    >>> assert isinstance(zip_path, str)
    >>> assert isinstance(n_workers, int)
    >>> assert n_workers >= 1
    """

    if n_workers <= 0:
        raise Exception("Number of workers cannot be equal or less than zero!")

    file_list: List[str] = []
    path_to_extract = Path(destination_dir, subdir)
    with zipfile.ZipFile(zip_path, "r") as zip_file:
        # Checking the existence of the extraction output directory
        # If it doesn't exist it will be created:
        if not path_to_extract.exists():
            path_to_extract.mkdir(parents=True, exist_ok=False)

        file_list = zip_file.namelist()

    chunksize = math.ceil(len(file_list) / n_workers)

    with ProcessPoolExecutor(n_workers) as exe:
        for index in tqdm(
            range(0, len(file_list), chunksize),
            desc=f"Extracting {destination_dir.name}: ",
        ):
            filenames = file_list[index : (index + chunksize)]
            _ = exe.submit(unpack_chunk, zip_path, filenames, path_to_extract)

    return path_to_extract
