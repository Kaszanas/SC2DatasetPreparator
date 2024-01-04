import unittest

from datasetpreparator.file_renamer.file_renamer import file_renamer

from tests.test_settings import (
    DELETE_SCRIPT_TEST_DIR,
    DELETE_SCRIPT_TEST_OUTPUT_DIR,
    DELETE_SCRIPT_TEST_INPUT_DIR,
)

from tests.test_utils import (
    create_script_test_input_dir,
    create_script_test_output_dir,
    test_cleanup,
)


SCRIPT_NAME = "file_renamer"


class FileRenamerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Create and get test input and output directories:
        cls.input_path = create_script_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = create_script_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Mock the directory structure:

    def test_file_renamer(self) -> None:
        file_renamer(input_path=self.input_path)
        # TODO: Assert that the files with old name do not exist.
        # TODO: Assert that files with new names exist.

    @classmethod
    def tearDownClass(cls) -> None:
        test_cleanup(
            script_name=SCRIPT_NAME,
            delete_script_test_dir=DELETE_SCRIPT_TEST_DIR,
            delete_script_test_input=DELETE_SCRIPT_TEST_INPUT_DIR,
            delete_script_test_output=DELETE_SCRIPT_TEST_OUTPUT_DIR,
        )
