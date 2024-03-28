import os
from pathlib import Path
import shutil
import subprocess
import logging
from typing import List, Tuple
import click
from tqdm import tqdm
from multiprocessing import Pool

from datasetpreparator.settings import LOGGING_FORMAT


def multiprocessing_scheduler(
    processing_arguments: List[Tuple[str, str]], number_of_processes: int
) -> None:
    """
    Responsible for spawning the multiprocessing_client functions.

    Parameters
    ----------
    processing_arguments : List[Tuple[str, str]]
        Processing arguments holds a list of input and output directories \
        for the https://github.com/Kaszanas/SC2InfoExtractorGo
    number_of_processes : int
        Specifies how many processes will be spawned.
    """

    with Pool(processes=number_of_processes) as pool:
        pool.imap_unordered(multiprocessing_client, processing_arguments)
        pool.close()
        pool.join()


def multiprocessing_client(arguments: tuple) -> None:
    """
    Responsible for running a single process that will
    extract data from a replaypack.

    Parameters
    ----------
    arguments : tuple
        Arguments tuple containing the input and output directory.
    """

    directory, output_directory_filepath, perform_chat_anonymization = arguments

    # TODO: This needs to be verified
    # Copying the mapping file that contains directory tree information:
    directory_contents = os.listdir(directory)
    if "processed_mapping.json" in directory_contents:
        logging.debug("Found mapping json in %s", directory)
        mapping_filepath = os.path.join(directory, "processed_mapping.json")
        output_mapping_filepath = os.path.join(
            output_directory_filepath, "processed_mapping.json"
        )
        shutil.copy(mapping_filepath, output_mapping_filepath)

    logging.debug(
        "Running subprocess for %s with output to %s",
        directory,
        output_directory_filepath,
    )
    subprocess.run(
        [
            # FIXME hardcoded binary name
            "/SC2InfoExtractorGo",
            f"-input={directory}/",
            f"-output={output_directory_filepath}/",
            "-perform_integrity_checks=true",
            "-perform_validity_checks=false",
            "-perform_cleanup=true",
            f"-perform_chat_anonymization={perform_chat_anonymization}",
            "-number_of_packages=1",
            # FIXME hardcoded path
            "-localized_maps_file=../processing/json_merger/merged.json",
            "-max_procs=1",
            "-log_level=3",
            f"-log_dir={output_directory_filepath}/",
        ]
    )


def sc2_replaypack_processor(
    input_path: Path,
    output_path: Path,
    n_processes: int,
    perform_chat_anonymization: bool,
):
    """
    Processes multiple StarCraft II replaypacks
    by using https://github.com/Kaszanas/SC2InfoExtractorGo

    Parameters
    ----------
    input_path : Path
        Input directory which contains the replaypacks in separate folders. \
        The replay folders should have their replays at the top level.
    output_path : Path
        Output directory which will contain all of the output produced by \
        the https://github.com/Kaszanas/SC2InfoExtractorGo
    n_processes : int
        Specifies the number of Python processes that will be spawned \
        and used for replaypack processing.
    perform_chat_anonymization : bool
        Specifies if the chat anonymization should be done.
    """

    multiprocessing_list = []
    for maybe_dir in tqdm(list(input_path.iterdir())):
        logging.debug(f"Processing entry: {maybe_dir}")
        processing_input_dir = Path(input_path, maybe_dir).resolve()
        if not processing_input_dir.is_dir():
            logging.debug("Entry is not a directory, skipping!")
            continue

        logging.debug(f"Output dir: {output_path}")
        # Create the main output directory:
        if not output_path.exists():
            output_path.mkdir()

        # TODO: use pathlib:
        path, output_directory_name = os.path.split(maybe_dir)
        logging.debug(f"Output dir name: {output_directory_name}")
        if output_directory_name == "input":
            continue

        output_directory_with_name = Path(output_path, output_directory_name).resolve()
        logging.debug(f"Output filepath: {output_directory_with_name}")

        # Create the output subdirectories:
        if not output_directory_with_name.exists():
            output_directory_with_name.mkdir()

        multiprocessing_list.append(
            (
                processing_input_dir,
                output_directory_with_name,
                perform_chat_anonymization,
            )
        )

    multiprocessing_scheduler(multiprocessing_list, int(n_processes))


@click.command(
    help="Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo."
)
@click.option(
    "--input_path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    required=True,
    help="Please provide an output directory for the resulting files.",
)
@click.option(
    "--output_path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    required=True,
    help="Please provide output path where StarCraft 2 (SC2) map files will be downloaded.",
)
@click.option(
    "--perform_chat_anonymization",
    type=bool,
    default=False,
    required=True,
    help="Provide 'True' if chat should be anonymized, otherwise 'False'.",
)
@click.option(
    "--n_processes",
    type=int,
    default=4,
    required=True,
    help="Please provide the number of processes to be spawned for the dataset processing.",
)
@click.option(
    "--log",
    type=click.Choice(["INFO", "DEBUG", "ERROR"], case_sensitive=False),
    default="WARN",
    help="Log level (INFO, DEBUG, ERROR)",
)
def main(
    input_path: Path,
    output_path: Path,
    n_processes: int,
    perform_chat_anonymization: bool,
    log: str,
) -> None:
    numeric_level = getattr(logging, log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {numeric_level}")
    logging.basicConfig(format=LOGGING_FORMAT, level=numeric_level)

    sc2_replaypack_processor(
        input_path=input_path,
        output_path=output_path,
        n_processes=n_processes,
        perform_chat_anonymization=perform_chat_anonymization,
    )


if __name__ == "__main__":
    main()
