import os
import argparse
import shutil
import subprocess
import logging
from typing import List, Tuple
from tqdm import tqdm
from multiprocessing import Pool


def multiprocessing_scheduler(
    processing_arguments: List[Tuple[str, str]], number_of_processes: int
) -> None:
    """
    Responsible for spawning the multiprocessing_client functions.

    :param processing_arguments: Processing arguments holds a list of input and output directories for the https://github.com/Kaszanas/SC2InfoExtractorGo
    :type processing_arguments: List[Tuple[str, str]]
    :param number_of_processes: Specifies how many processes will be spawned.
    :type number_of_processes: int
    """

    with Pool(processes=number_of_processes) as pool:
        pool.imap_unordered(multiprocessing_client, processing_arguments)
        pool.close()
        pool.join()


def multiprocessing_client(arguments: tuple) -> None:
    """
    Responsible for running a single process that will extract data from a replaypack.

    :param arguments: Arguments tuple containing the input and output directory.
    :type arguments: tuple
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


def multiproc_replaypack_processor(
    input_dir: str,
    output_dir: str,
    n_processes: int,
    perform_chat_anonymization: str,
):
    """
    Processes multiple StarCraft II replaypacks by using https://github.com/Kaszanas/SC2InfoExtractorGo

    :param input_dir: Input directory which contains the replaypacks in separate folders. The replay folders should have their replays at the top level.
    :type input_dir: str
    :param output_dir: Output directory which will contain all of the output produced by the https://github.com/Kaszanas/SC2InfoExtractorGo
    :type output_dir: str
    :param n_processes: Specifies the number of Python processes that will be spawned and used for replaypack processing.
    :type n_processes: int
    :param perform_chat_anonymization: Specifies if the chat anonymization should be done.
    :type perform_chat_anonymization: str
    """
    multiprocessing_list = []
    for directory in tqdm(os.listdir(input_dir)):

        logging.debug("Processing entry: %s", directory)
        is_input_dir = os.path.abspath(os.path.join(input_dir, directory))
        if not os.path.isdir(is_input_dir):
            logging.debug("not dir, skipping")
            continue

        logging.debug("Output dir: %s", output_dir)
        # Create the main output directory:
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        path, output_directory_name = os.path.split(directory)
        logging.debug("Output dir name: %s", output_directory_name)
        if output_directory_name == "input":
            continue

        output_directory_filepath = os.path.join(output_dir, output_directory_name)
        logging.debug("Output filepath: %s", output_directory_filepath)

        # Create the output subdirectories:
        if not os.path.exists(output_directory_filepath):
            os.mkdir(output_directory_filepath)

        multiprocessing_list.append(
            (is_input_dir, output_directory_filepath, perform_chat_anonymization)
        )

    multiprocessing_scheduler(multiprocessing_list, int(n_processes))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo"
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Please provide input path to the directory containing the dataset that is going to be processed.",
        default="../processing/directory_flattener/output",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        help="Please provide an output directory for the resulting files.",
        default="../processing/sc2_replaypack_processor/output",
    )
    parser.add_argument(
        "--perform_chat_anonymization",
        type=str,
        help="Provide 'true' if chat should be anonymized, otherwise 'false'",
        default="false",
    )
    parser.add_argument(
        "--n_processes",
        type=int,
        help="Please provide the number of processes to be spawned for the dataset processing.",
        default=4,
    )
    parser.add_argument(
        "--log", type=str, help="Log level (INFO, DEBUG, ERROR)", default="WARN"
    )
    args = parser.parse_args()

    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % numeric_level)
    logging.basicConfig(level=numeric_level)

    args_input_dir = args.input_dir
    args_output_dir = args.output_dir
    args_n_processes = args.n_processes
    perform_chat_anonymization = args.perform_chat_anonymization
    multiproc_replaypack_processor(
        input_dir=args_input_dir,
        output_dir=args_output_dir,
        n_processes=args_n_processes,
        perform_chat_anonymization=perform_chat_anonymization,
    )
