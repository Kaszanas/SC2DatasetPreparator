import os
import argparse
import subprocess
from tqdm import tqdm
from multiprocessing import Pool


def multiprocessing_scheduler(processing_arguments, number_of_processes):
    with Pool(processes=number_of_processes) as pool:
        pool.imap_unordered(multiprocessing_client, processing_arguments)
        pool.close()
        pool.join()


def multiprocessing_client(arguments: tuple):

    directory, output_directory_filepath = arguments

    subprocess.run(
        [
            "SC2InfoExtractorGo.exe",
            f"-input={directory}/",
            f"-output={output_directory_filepath}/",
            "-perform_integrity_checks=true",
            "-perform_validity_checks=false",
            "-perform_cleanup=true",
            "-number_of_packages=1",
            "-localized_maps_file=F:\\Projects\\EsportDataset\\processed\\program\\new_maps_processed.json",
            "-max_procs=1",
            "-log_level=3",
            f"-log_dir={output_directory_filepath}/",
        ]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool used for processing SC2 datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo"
    )
    parser.add_argument(
        "--input_dir",
        help="Please provide input path to the directory containing the dataset that is going to be processed.",
    )
    parser.add_argument(
        "--output_dir",
        help="Please provide an output directory for the resulting files.",
    )
    parser.add_argument(
        "--number_of_processes",
        help="Please provide the number of processes to be spawned for the dataset processing.",
    )
    args = parser.parse_args()

    multiprocessing_list = []
    for directory, _, file in tqdm(os.walk(args.input_dir)):

        # Create the main output directory:
        if not os.path.exists(args.output_dir):
            os.mkdir(args.output_dir)

        output_directory_name = directory.split("\\")[-1]
        if output_directory_name == "input":
            continue

        output_directory_filepath = os.path.join(args.output_dir, output_directory_name)

        # Create the output subdirectories:
        if not os.path.exists(output_directory_filepath):
            os.mkdir(output_directory_filepath)

        multiprocessing_list.append((directory, output_directory_filepath))

    multiprocessing_scheduler(multiprocessing_list, int(args.number_of_processes))
