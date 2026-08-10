import logging
import shutil
from pathlib import Path

from tqdm import tqdm

from datasetpreparator.utils.user_prompt import user_prompt_overwrite_ok

logger = logging.getLogger(__name__)


def move_files(
    input_path: Path,
    output_path: Path,
    force_overwrite: bool,
    extension: str = ".zip",
    recursive: bool = True,
) -> None:
    """
    Move files from one directory to another.

    Parameters
    ----------
    input_path : Path
        Input directory containing files/directories to be moved.
    output_path : Path
        Output directory where the files/directories will be moved.
    force_overwrite : bool
        Flag that specifies if the user wants to overwrite files or directories without being prompted.
    extension : str, optional
        Specifies which file extension files will be detected and moved, by default ".zip"\
    recursive : bool, optional
        Flag that specifies if the search for files should be recursive, by default True
    """

    # Make sure that the output directory exists, and potentially overwrite
    # its contents if the user agrees:
    if user_prompt_overwrite_ok(path=output_path, force_overwrite=force_overwrite):
        output_path.mkdir(exist_ok=True)

    logger.info(f"Searching for files with extension {extension} in {input_path!s}...")

    search_method = input_path.rglob if recursive else input_path.glob
    files = list(search_method(f"*{extension}"))
    if not files:
        logger.warning(f"No files with extension {extension} found in {input_path!s}.")
        return

    logger.info(f"Moving {len(files)} files to {output_path!s}...")

    for file in tqdm(
        files,
        desc="Moving files",
        unit="file",
    ):
        shutil.move(file, output_path / file.name)
