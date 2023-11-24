import os
from pathlib import Path
from zipfile import ZipFile, ZIP_BZIP2

import click


def dir_file_packager(input_path: str) -> None:
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

        nested_dir_path = os.path.join(input_path, directory)
        with ZipFile(nested_dir_path + ".zip", "w") as zip_file:
            for file in os.listdir(nested_dir_path):
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
def main(input_path: Path):
    dir_file_packager(input_path=input_path)


if __name__ == "__main__":
    main()
