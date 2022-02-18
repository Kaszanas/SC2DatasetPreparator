import os
import argparse


def file_renamer(input_dir: str) -> None:
    for directory, _, file_list in os.walk(input_dir):
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool used for processing SC2 datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo"
    )
    parser.add_argument(
        "--input_dir",
        help="Please provide input path to the directory containing the dataset that is going to be processed.",
    )
    args = parser.parse_args()
    file_renamer(input_dir=args.input_dir)
