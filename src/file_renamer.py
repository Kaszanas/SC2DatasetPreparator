import os
import argparse
from zipfile import ZipFile, ZIP_BZIP2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool used for processing SC2 datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo"
    )
    parser.add_argument(
        "--input_dir",
        help="Please provide input path to the directory containing the dataset that is going to be processed.",
    )
    args = parser.parse_args()

    for directory, _, file_list in os.walk(args.input_dir):
        for file in file_list:
            if file.endswith(".zip"):
                os.rename(
                    os.path.join(directory, file),
                    os.path.join(directory, os.path.basename(directory) + "_data.zip"),
                )
            if file.endswith(".json"):
                os.rename(
                    os.path.join(directory, file),
                    os.path.join(
                        directory, os.path.basename(directory) + "_summary.json"
                    ),
                )
