import unittest

from sc2datasetpreparator.file_renamer.file_renamer import file_renamer

from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
)

SCRIPT_NAME = "file_renamer"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class FileRenamerTest(unittest.TestCase):
    def setUp(self) -> None:
        # Get test directory input and output:
        self.input_path = get_test_input_dir(script_name=SCRIPT_NAME)
        self.output_path = get_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Mock the directory structure:
        pass

    def test_file_renamer(self) -> None:
        file_renamer(input_path=self.input_path)
        # TODO: Assert that the files with old name do not exist.
        # TODO: Assert that files with new names exist.
