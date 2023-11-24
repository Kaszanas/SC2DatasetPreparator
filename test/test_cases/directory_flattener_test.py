import unittest
from sc2datasetpreparator.directory_flattener.directory_flattener import (
    directory_flattener,
)

from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
)

SCRIPT_NAME = "directory_flattener"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class DirectoryFlattenerTest(unittest.TestCase):
    def setUp(self) -> None:
        # Get test directory input and output:
        self.input_path = get_test_input_dir(script_name=SCRIPT_NAME)
        self.output_path = get_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Create nested directory structure mimicking how real replaypacks look like:
        # TODO: Use one replay placed in these nested directories.
        # TODO: Place some additional files that will be scrapped in processing,
        # for example some_notes.txt

        pass

    def test_directory_flattener(self) -> None:
        # TODO: Assert the final directory not to contain any other nested directories.
        # TODO: Assert the final directory have the same number of files with the selected extension.
        # TODO: Assert the final flattened directory to have one .json file
        # containing mapping of the files.

        directory_flattener()

        pass
