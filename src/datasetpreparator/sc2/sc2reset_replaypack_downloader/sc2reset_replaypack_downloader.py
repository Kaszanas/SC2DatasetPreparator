import logging
import click

from datasetpreparator.sc2.sc2reset_replaypack_downloader.available_replaypacks import (
    SC2RESET_REPLAYPACKS,
)
from datasetpreparator.settings import LOGGING_FORMAT


@click.command(
    help="Tool used for downloading SC2EGSet: StarCraft II Esport Game State Dataset (https://zenodo.org/doi/10.5281/zenodo.5503997)."
)
@click.option(
    "--log",
    type=click.Choice(["INFO", "DEBUG", "ERROR"], case_sensitive=False),
    default="WARN",
    help="Log level (INFO, DEBUG, ERROR)",
)
def main(log: str):
    numeric_level = getattr(logging, log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {numeric_level}")
    logging.basicConfig(format=LOGGING_FORMAT, level=numeric_level)


if __name__ == "__main__":
    main()
