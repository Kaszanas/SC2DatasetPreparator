import os
import argparse
import uuid
import json
import shutil
import logging


def save_dir_mapping(output_path: str, dir_mapping: dict) -> None:
    """
    Saves a JSON file containing the mapping of the directory structure before it was "flattened".

    :param output_path: Specifies the path where the mapping will be saved.
    :type output_path: str
    :param dir_mapping: Specifies the directory mapping dict.
    :type dir_mapping: dict
    """
    with open(os.path.join(output_path, "processed_mapping.json"), "w") as json_file:
        json.dump(dir_mapping, json_file)


def directory_flattener(input_path: str, output_path: str, file_extension: str) -> None:
    """
    Provides the main logic for "directory flattening". Detects a files that end with a specific extension,
    and moves them to the top of the input path. This function returns a file mapping for all of the files that were moved.
    This file mapping represents the relative directory structure before the processing occured.

    :param input_path: Specifies the path that will be searched for files.
    :type input_path: str
    :param output_path: Specifies the path where directories will be created and files will be copied in a flat directory structure.
    :type output_path: dict
    """

    # Iterate over directories:
    for item in os.listdir(input_path):
        maybe_dir = os.path.join(input_path, item)
        if os.path.isdir(maybe_dir):
            # Output directory is created if it doesn't exist:
            full_output_path = os.path.join(os.path.abspath(output_path), item)
            if not os.path.exists(full_output_path):
                os.makedirs(full_output_path)

            # Walk over the directory
            dir_structure_mapping = {}
            for root, _, filenames in os.walk(maybe_dir):
                for file in filenames:
                    if file.endswith(file_extension):

                        # Get abspath from root
                        # Prepare relative paths:
                        root_abspath = os.path.join(os.path.abspath(root), file)
                        input_abspath = os.path.abspath(input_path)
                        relative_file = root_abspath.removeprefix(input_abspath)

                        # Get unique filename:
                        unique_filename = uuid.uuid4().hex
                        unique_filename_with_ext = unique_filename + file_extension
                        new_path_and_filename = os.path.join(
                            full_output_path, unique_filename_with_ext
                        )

                        current_file = os.path.abspath(os.path.join(root, file))
                        logging.debug("Current file: %s", current_file)

                        # Copying files:
                        if os.path.exists(current_file):
                            shutil.copy(current_file, new_path_and_filename)
                            logging.debug("File copied")
                        else:
                            logging.error("File does not exist. Path len: %d", len(current_file))

                        # Add to a mapping
                        dir_structure_mapping[unique_filename_with_ext] = relative_file
            save_dir_mapping(
                output_path=full_output_path, dir_mapping=dir_structure_mapping
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Directory restructuring tool used in order to flatten the structure, map the old structure to a separate file, and for later processing with other tools. Created primarily to define StarCraft 2 (SC2) datasets."
    )
    parser.add_argument(
        "--input_path",
        type=str,
        help="Please provide input path to the dataset that is going to be processed.",
        default="../processing/directory_flattener/input",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        help="Please provide output path where sc2 map files will be downloaded.",
        default="../processing/directory_flattener/output",
    )
    parser.add_argument(
        "--file_extension",
        type=str,
        help="Please provide a file extension for files that will be moved and renamed.",
        default=".SC2Replay",
    )
    parser.add_argument(
        "--log",
        type=str,
        help="Log level (INFO, DEBUG, ERROR)",
        default="WARN"
    )
    args = parser.parse_args()

    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level)

    args_input_path = args.input_path
    args_output_path = args.output_path
    args_file_extension = args.file_extension
    directory_flattener(
        input_path=args_input_path,
        output_path=args_output_path,
        file_extension=args_file_extension,
    )
