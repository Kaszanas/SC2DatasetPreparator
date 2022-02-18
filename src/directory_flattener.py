import os
import argparse
import uuid
import json
import shutil


def directory_flattener(input_path: str) -> dict:

    dir_structure_mapping = {}

    # Iterate over the supplied directory:
    for root, _, filename in os.walk(args.input_path):
        # Performing action for every file that was detected
        for file in filename:
            if file.endswith(args.file_extension):

                # Prepare relative paths:
                relative_dir = os.path.relpath(root, args.input_path)
                relative_file = os.path.join(relative_dir, file)
                # Get unique filename:
                unique_filename = uuid.uuid4().hex

                # Create directory if it doesn't exist:
                new_root_directory = args.input_path + "_processed"
                if not os.path.exists(new_root_directory):
                    os.makedirs(new_root_directory)

                # Moving and renaming files:
                current_file = os.path.join(root, file)
                new_path_and_filename = os.path.join(
                    new_root_directory, unique_filename + args.file_extension
                )

                # Copying files:
                shutil.copy(current_file, new_path_and_filename)

                # Add to a mapping
                dir_structure_mapping[unique_filename] = relative_file


def save_dir_mapping(input_path: str, dir_mapping: dict) -> None:
    with open(
        os.path.join(args.input_path + "_processed", "processed_mapping.json"), "w"
    ) as json_file:
        json.dump(dir_structure_mapping, json_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Directory restructuring tool used in order to flatten the structure, map the old structure to a separate file, and for later processing with other tools."
    )
    parser.add_argument(
        "--input_path",
        help="Please provide input path to the dataset that is going to be processed.",
    )
    parser.add_argument(
        "--file_extension",
        help="Please provide a file extension for files that will be moved and renamed.",
    )
    args = parser.parse_args()

    args_input_path = args.input_path
    dir_structure_mapping = directory_flattener(input_path=args_input_path)
    save_dir_mapping(input_path=args_input_path, dir_mapping=dir_structure_mapping)
