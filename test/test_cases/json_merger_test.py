import unittest

from sc2datasetpreparator.json_merger.json_merger import json_merger

from test.test_utils import dir_test_create_cleanup

SCRIPT_NAME = "json_merger"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class JSONMergerTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        # TODO: Create two json files with some overlapping keys and values
        pass

    def test_json_merger(self):
        # TODO: Assert that the json files were merged.
        # TODO: Validate what should be the desired behavior for overlapping keys.
        pass
