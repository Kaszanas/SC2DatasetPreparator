import argparse
import os
import shutil


def mapping_copier(input_path: str, output_path: str) -> None:
    """
    Exposes logic for copying a specific file from all of the immediate subdirectories
    of the input path to the matching immediate subdirectories in the output path.

    :param input_path: Specifies the input path that contains subdirectories with the desired file to be copied.
    :type input_path: str
    :param output_path: Specifies the output path that contains matching subdirectories which will be the destination of the copied file.
    :type output_path: str
    """

    # Iterating over the input path to find all of the immediate directories:
    for item in os.listdir(input_path):
        maybe_dir = os.path.join(input_path, item)
        if os.path.isdir(maybe_dir):
            # if the output directory does not exist the copying is ommited:
            dir_output_path = os.path.join(os.path.abspath(output_path), item)
            if not os.path.exists(dir_output_path):
                continue

            # The mapping was detected within the input directory
            # So the path is created and the file is copied:
            if "processed_mapping.json" in os.listdir(maybe_dir):
                mapping_filepath = os.path.join(maybe_dir, "processed_mapping.json")
                mapping_out_filepath = os.path.join(
                    dir_output_path, "processed_mapping.json"
                )
                shutil.copy(mapping_filepath, mapping_out_filepath)

    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool for copying the processed_mapping.json files that are required to define the dataset."
    )
    parser.add_argument(
        "--input_path",
        type=str,
        help="Please provide input path to the flattened replaypacks that contain procesed_mapping.json files.",
        default="../processing/directory_flattener/output",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        help="Please provide output path where processed_mapping.json will be copied.",
        default="../processing/sc2_replaypack_processor/output",
    )

    args = parser.parse_args()

    args_input_path = args.input_path
    args_output_path = args.output_path
    mapping_copier(input_path=args_input_path, output_path=args_output_path)
