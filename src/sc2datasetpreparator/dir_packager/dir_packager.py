import logging
import os
from pathlib import Path
from zipfile import ZipFile, ZIP_BZIP2

import click


def dir_packager(input_path: str) -> None:
    """
    Packages the specified directory into a .zip archive.

    Parameters
    ----------
    input_path : str
        Specifies the path which will be turned into a .zip archive.
    """
    for directory in os.listdir(path=input_path):
        if not os.path.isdir(os.path.join(input_path, directory)):
            continue

        nested_dir_path = Path(input_path, directory).resolve()
        final_archive_name = nested_dir_path.with_suffix(".zip")
        logging.info(f"Set final archive name to: {final_archive_name.as_posix()}")
        with ZipFile(final_archive_name.as_posix(), "w") as zip_file:
            for file in os.listdir(nested_dir_path.as_posix()):
                abs_filepath = os.path.join(nested_dir_path, file)
                zip_file.write(
                    filename=abs_filepath, arcname=file, compress_type=ZIP_BZIP2
                )


@click.command(
    help="Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo"
)
@click.option(
    "--input_path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    required=True,
    help="Please provide input path to the directory containing the dataset that is going to be processed by packaging into .zip archives.",
)
@click.option(
    "--log",
    type=click.Choice(["INFO", "DEBUG", "ERROR"], case_sensitive=False),
    default="WARN",
    help="Log level (INFO, DEBUG, ERROR)",
)
def main(input_path: Path):
    numeric_level = getattr(logging, log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {numeric_level}")
    logging.basicConfig(level=numeric_level)

    dir_packager(input_path=input_path)


if __name__ == "__main__":
    main()
