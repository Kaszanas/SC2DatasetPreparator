import os
import argparse
import shutil
import subprocess
from typing import List, Tuple
from tqdm import tqdm
from multiprocessing import Pool


def multiprocessing_scheduler(
    processing_arguments: List[Tuple[str, str]], number_of_processes: int
) -> None:
    """
    Responsible for spawning the multiprocessing_client functions.

    :param processing_arguments: Processing arguments argument holds a list of input and output directories for the https://github.com/Kaszanas/SC2InfoExtractorGo
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

    directory, output_directory_filepath = arguments

    # TODO: This needs to be verified
    # Copying the mapping file that contains directory tree information:
    directory_contents = os.listdir(directory)
    if "processed_mapping.json" in directory_contents:
        mapping_filepath = os.path.join(directory, "processed_mapping.json")
        output_mapping_filepath = os.path.join(
            output_directory_filepath, "processed_mapping.json"
        )
        shutil.copy(mapping_filepath, output_mapping_filepath)

    subprocess.run(
        [
            "SC2InfoExtractorGo.exe",
            f"-input={directory}/",
            f"-output={output_directory_filepath}/",
            "-perform_integrity_checks=true",
            "-perform_validity_checks=false",
            "-perform_cleanup=true",
            "-number_of_packages=1",
            "-localized_maps_file=F:\\Projects\\SC2DatasetPreparator\\processing\\json_merger\\merged.json",
            "-max_procs=1",
            "-log_level=3",
            f"-log_dir={output_directory_filepath}/",
        ]
    )


def multiproc_replaypack_processor(input_dir: str, output_dir: str, n_processes: int):
    """
    Processes multiple StarCraft II replaypacks by using https://github.com/Kaszanas/SC2InfoExtractorGo

    :param input_dir: Input directory which contains the replaypacks in separate folders. The replay folders should have their replays at the top level.
    :type input_dir: str
    :param output_dir: Output directory which will contain all of the output produced by the https://github.com/Kaszanas/SC2InfoExtractorGo
    :type output_dir: str
    :param n_processes: Specifies the number of Python processes that will be spawned and used for replaypack processing.
    :type n_processes: int
    """
    multiprocessing_list = []
    for directory in tqdm(os.listdir(input_dir)):

        is_input_dir = os.path.abspath(os.path.join(input_dir, directory))
        if not os.path.isdir(is_input_dir):
            continue

        # Create the main output directory:
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        output_directory_name = directory.split("\\")[-1]
        if output_directory_name == "input":
            continue

        output_directory_filepath = os.path.join(output_dir, output_directory_name)

        # Create the output subdirectories:
        if not os.path.exists(output_directory_filepath):
            os.mkdir(output_directory_filepath)

        multiprocessing_list.append((is_input_dir, output_directory_filepath))

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
        "--n_processes",
        type=int,
        help="Please provide the number of processes to be spawned for the dataset processing.",
        default=4,
    )
    args = parser.parse_args()
    args_input_dir = args.input_dir
    args_output_dir = args.output_dir
    args_n_processes = args.n_processes
    multiproc_replaypack_processor(
        input_dir=args_input_dir,
        output_dir=args_output_dir,
        n_processes=args_n_processes,
    )
