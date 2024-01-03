import unittest

from datasetpreparator.file_renamer.file_renamer import file_renamer

from tests.test_settings import DELETE_OUTPUT, DELETE_INPUT

from tests.test_utils import (
    create_test_input_dir,
    create_test_output_dir,
    delete_test_input,
    delete_test_output,
)


SCRIPT_NAME = "file_renamer"


class FileRenamerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Create and get test input and output directories:
        cls.input_path = create_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = create_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Mock the directory structure:

    def test_file_renamer(self) -> None:
        file_renamer(input_path=self.input_path)
        # TODO: Assert that the files with old name do not exist.
        # TODO: Assert that files with new names exist.

    @classmethod
    def tearDownClass(cls) -> None:
        if DELETE_INPUT:
            delete_test_input(script_name=SCRIPT_NAME)
        if DELETE_OUTPUT:
            delete_test_output(script_name=SCRIPT_NAME)
