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


def sc2reset_replaypack_downloader(download_path: Path, unpack_path: Path):
    # Download replaypacks:
    downloaded_paths: List[Tuple[str, str]] = []
    for replaypack_name, replaypack_url in SC2RESET_REPLAYPACKS:
        downloaded_replaypack_path = download_replaypack(
            destination_dir=download_path,
            replaypack_name=replaypack_name,
            replaypack_url=replaypack_url,
        )
        downloaded_paths.append((replaypack_name, downloaded_replaypack_path))

    # Unpack replaypacks:
    for replaypack_name, downloaded_replaypack_path in downloaded_paths:
        unpack_zipfile(
            destination_dir=unpack_path,
            subdir=replaypack_name,
            zip_path=downloaded_replaypack_path,
            n_workers=6,
        )


@click.command(
    help="Tool used for downloading SC2ReSet: StarCraft II Esport Replaypack Set (https://zenodo.org/doi/10.5281/zenodo.5575796)."
)
@click.option(
    "--download_path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    required=True,
    help="Please provide a path to which the archives will be downloaded.",
)
@click.option(
    "--unpack_path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    required=True,
    help="Please provide a path to which the archives will be unpacked.",
)
@click.option(
    "--log",
    type=click.Choice(["INFO", "DEBUG", "ERROR"], case_sensitive=False),
    default="WARN",
    help="Log level (INFO, DEBUG, ERROR)",
)
def main(download_path: Path, unpack_path: Path, log: str):
    numeric_level = getattr(logging, log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {numeric_level}")
    logging.basicConfig(format=LOGGING_FORMAT, level=numeric_level)

    sc2reset_replaypack_downloader(download_path=download_path, unpack_path=unpack_path)


if __name__ == "__main__":
    main()
