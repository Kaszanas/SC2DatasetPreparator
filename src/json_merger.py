import argparse
import json

def json_merger(path_to_json_one:str, path_to_json_two:str):

    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool used for merging two .json files. Created in order to merge two mappings created by https://github.com/Kaszanas/SC2MapLocaleExtractor"
    )
    parser.add_argument(
        "--json_one",
        type=str,
        help="Please provide the path to the first .json file that is going to be merged.",
        default="../processing/json_merger/json1.json",
    )
    parser.add_argument(
        "--json_two",
        type=str,
        help="Please provide the path to the second .json file that is going to be merged.",
        default="../processing/json_merger/json2.json",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        help="Please provide output path where sc2 map files will be downloaded.",
        default="../processing/json_merger",
    )

    args = parser.parse_args()
    args_input_dir = args.json_one
    args_output_dir = args.json_two

    json_merger()