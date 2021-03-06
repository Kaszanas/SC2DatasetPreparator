import os
import argparse
from zipfile import ZipFile, ZIP_BZIP2


def dir_file_packager(input_dir: str) -> None:
    for directory in os.listdir(path=input_dir):
        if not os.path.isdir(os.path.join(input_dir, directory)):
            continue

        nested_dir_path = os.path.join(input_dir, directory)
        with ZipFile(nested_dir_path + ".zip", "w") as zip_file:
            for file in os.listdir(nested_dir_path):
                abs_filepath = os.path.join(nested_dir_path, file)
                zip_file.write(
                    filename=abs_filepath, arcname=file, compress_type=ZIP_BZIP2
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo"
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Please provide input path to the directory containing the dataset that is going to be processed by packaging into .zip archives.",
        default="../processing/sc2_replaypack_processor/output",
    )
    args = parser.parse_args()
    dir_file_packager(input_dir=args.input_dir)
