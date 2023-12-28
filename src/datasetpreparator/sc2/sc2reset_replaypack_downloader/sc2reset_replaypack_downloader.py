import logging
from pathlib import Path
from typing import List, Tuple
import click

from datasetpreparator.sc2.sc2reset_replaypack_downloader.available_replaypacks import (
    SC2RESET_REPLAYPACKS,
)
from datasetpreparator.sc2.sc2reset_replaypack_downloader.download_replaypack import (
    download_replaypack,
)
from datasetpreparator.sc2.sc2reset_replaypack_downloader.unpack_zipfile import (
    unpack_zipfile,
)
from datasetpreparator.settings import LOGGING_FORMAT


def sc2reset_replaypack_downloader(
    download_path: Path, unpack_path: Path, n_workers: int
):
    # Download replaypacks:
    downloaded_paths: List[Tuple[str, str]] = []
    for replaypack_name, replaypack_url, file_md5 in SC2RESET_REPLAYPACKS:
        downloaded_replaypack_path = download_replaypack(
            destination_dir=download_path,
            replaypack_name=replaypack_name,
            replaypack_url=replaypack_url,
            replaypack_md5=file_md5,
        )
        downloaded_paths.append((replaypack_name, downloaded_replaypack_path))

    # Unpack replaypacks:
    for replaypack_name, downloaded_replaypack_path in downloaded_paths:
        destination_subdir = Path(replaypack_name)
        unpack_zipfile(
            destination_dir=unpack_path,
            destination_subdir=destination_subdir,
            zip_path=downloaded_replaypack_path,
            n_workers=n_workers,
        )


@click.command(
    help="Tool used for downloading SC2ReSet: StarCraft II Esport Replaypack Set (https://zenodo.org/doi/10.5281/zenodo.5575796)."
)
@click.option(
    "--download_path",
    type=click.Path(
        exists=False, dir_okay=True, file_okay=False, resolve_path=True, path_type=Path
    ),
    required=True,
    help="Please provide a path to which the archives will be downloaded.",
)
@click.option(
    "--unpack_path",
    type=click.Path(
        exists=False, dir_okay=True, file_okay=False, resolve_path=True, path_type=Path
    ),
    required=True,
    help="Please provide a path to which the archives will be unpacked.",
)
@click.option(
    "--n_workers",
    type=int,
    default=4,
    required=True,
    help="Number of workers used for extracting the .zip archives.",
)
@click.option(
    "--log",
    type=click.Choice(["INFO", "DEBUG", "ERROR", "WARN"], case_sensitive=False),
    default="WARN",
    help="Log level (INFO, DEBUG, ERROR)",
)
def main(download_path: Path, unpack_path: Path, n_workers: int, log: str):
    numeric_level = getattr(logging, log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {numeric_level}")
    logging.basicConfig(format=LOGGING_FORMAT, level=numeric_level)

    sc2reset_replaypack_downloader(
        download_path=download_path.resolve(),
        unpack_path=unpack_path.resolve(),
        n_workers=n_workers,
    )


if __name__ == "__main__":
    main()
