import unittest

import json

from sc2datasetpreparator.json_merger.json_merger import json_merger

from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
    create_test_json_files,
)

SCRIPT_NAME = "json_merger"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class JSONMergerTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        # Get test directory input and output:
        cls.input_path = get_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = get_test_output_dir(script_name=SCRIPT_NAME)

        cls.test_key = "test_key"
        cls.test_key_other = "test_key_other"
        cls.test_key_content = "test_key_data"

        # Create two json files with some overlapping keys and values:
        json_file_paths = create_test_json_files(
            input_path=cls.input_path,
            test_key=cls.test_key,
            test_key_other=cls.test_key_other,
            test_key_content=cls.test_key_content,
        )

        cls.path_to_json_one = json_file_paths[0]
        cls.path_to_json_two = json_file_paths[1]

    def test_json_merger(self):
        merged_json_filepath = json_merger(
            path_to_json_one=self.path_to_json_one,
            path_to_json_two=self.path_to_json_two,
            output_filepath=self.output_filepath,
        )

        # Read merged file:
        merged_json_file = merged_json_filepath.open()
        merged_json_content = json.load(merged_json_file)
        merged_json_file.close()

        # Test key should be in the merged data:
        self.assertIn(member=self.test_key, container=merged_json_content)
        self.assertIn(member=self.test_key_other, container=merged_json_content)
