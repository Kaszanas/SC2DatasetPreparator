import unittest

from sc2datasetpreparator.json_merger.json_merger import json_merger

from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
)

SCRIPT_NAME = "json_merger"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class JSONMergerTest(unittest.TestCase):
    def setUp(self) -> None:
        # Get test directory input and output:
        self.input_path = get_test_input_dir(script_name=SCRIPT_NAME)
        self.output_path = get_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Create two json files with some overlapping keys and values

        self.path_to_json_one = ""
        self.path_to_json_two = ""

    def test_json_merger(self):
        json_merger(
            path_to_json_one=self.path_to_json_one,
            path_to_json_two=self.path_to_json_two,
            output_filepath=self.output_filepath,
        )
        # TODO: Assert that the json files were merged.
        # TODO: Validate what should be the desired behavior for overlapping keys.
