import argparse
import json
from typing import Dict


def json_merger(path_to_json_one: str, path_to_json_two: str) -> Dict[str, str]:
    """
    Exposes the logic to merge two json files by loading their contents from supplied paths.

    :param path_to_json_one: Specifies the filepath of a .json file that is going to be merged.
    :type path_to_json_one: str
    :param path_to_json_two: Specifies the filepath of a .json file that is going to be merged.
    :type path_to_json_two: str
    :return: Returns a merged dictionary.
    :rtype: dict
    """

    # Loading the supplied .json files and deserializing them:
    json_one_file = open(path_to_json_one, encoding="utf-8")
    loaded_json_one = json.loads(json_one_file.read())
    json_one_file.close()

    json_two_file = open(path_to_json_two, encoding="utf-8")
    loaded_json_two = json.loads(json_two_file.read())
    json_two_file.close()

    # Merging the loaded dictionaries:
    result_dict = loaded_json_one | loaded_json_two

    return result_dict


def save_output(output_filepath: str, output_dict: Dict[str, str]) -> None:
    """
    Exposes the logic for saving a dict to a .json file.

    :param output_filepath: Speciifies the full output filepath which will be used, this includes the filename.
    :type output_filepath: str
    :param output_dict: Specifies the Python dictionary which will be serialized into a JSON.
    :type output_dict: Dict[str, str]
    """
    with open(output_filepath, "w") as output_file:
        json.dump(output_dict, output_file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool used for merging two .json files. Created in order to merge two mappings created by https://github.com/Kaszanas/SC2MapLocaleExtractor"
    )
    parser.add_argument(
        "--json_one",
        type=str,
        help="Please provide the path to the first .json file that is going to be merged.",
        default="../../processing/json_merger/json1.json",
    )
    parser.add_argument(
        "--json_two",
        type=str,
        help="Please provide the path to the second .json file that is going to be merged.",
        default="../../processing/json_merger/json2.json",
    )
    parser.add_argument(
        "--output_filepath",
        type=str,
        help="Please provide output path where sc2 map files will be downloaded.",
        default="../../processing/json_merger/merged.json",
    )

    args = parser.parse_args()
    args_path_json_one = args.json_one
    args_path_json_two = args.json_two
    args_output_filepath = args.output_filepath

    output_dict = json_merger(
        path_to_json_one=args_path_json_one, path_to_json_two=args_path_json_two
    )

    save_output(output_filepath=args_output_filepath, output_dict=output_dict)
