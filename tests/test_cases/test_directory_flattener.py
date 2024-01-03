import unittest
from datasetpreparator.directory_flattener.directory_flattener import (
    multiple_directory_flattener,
)

from tests.test_settings import DELETE_OUTPUT, DELETE_INPUT

from tests.test_utils import (
    create_test_input_dir,
    create_test_output_dir,
    create_test_text_files,
    create_nested_test_directories,
    delete_test_input,
    delete_test_output,
)

SCRIPT_NAME = "directory_flattener"


class TestDirectoryFlattenerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Create and get test input and output directories:
        cls.input_path = create_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = create_test_output_dir(script_name=SCRIPT_NAME)
        cls.file_extension = ".SC2Replay"

        # Create nested directory structure mimicking how real replaypacks look like:
        cls.n_dirs = 2
        nested_dirs = create_nested_test_directories(
            input_path=cls.input_path, n_dirs=cls.n_dirs
        )
        cls.n_nested_files = 4
        cls.n_out_of_distribution_files = 1
        for directory in nested_dirs:
            # Create multiple test files with the selected extension:
            create_test_text_files(
                input_path=directory,
                n_files=cls.n_nested_files,
                extension=cls.file_extension,
            )
            # Create additional files that should not be present in the output:
            create_test_text_files(
                input_path=directory,
                n_files=cls.n_out_of_distribution_files,
                extension=".txt",
            )

    def test_directory_flattener(self) -> None:
        ok, list_of_output_dirs = multiple_directory_flattener(
            input_path=self.input_path,
            output_path=self.output_path,
            file_extension=self.file_extension,
        )

        # Check if the input data was correct for processing:
        self.assertTrue(ok)

        # Check the number of output directories:
        self.assertEqual(self.n_dirs, len(list_of_output_dirs))

        for output_dir in list_of_output_dirs:
            # Assert the final directory have the same number of
            # files with the selected extension.
            out_files = output_dir.glob(f"*{self.file_extension}")
            self.assertEqual(self.n_nested_files, len(out_files))

            # Assert the final flattened directory to
            # have one .json file with the mapping
            json_file = output_dir.glob(f"*{self.file_extension}")
            self.assertEqual(1, len(json_file))

            # There should be no nested directories in the output:
            for file in output_dir.iterdir():
                self.assertFalse(file.is_dir())

            # TODO: Check the contents of the json mapping?

    @classmethod
    def tearDownClass(cls) -> None:
        if DELETE_INPUT:
            delete_test_input(script_name=SCRIPT_NAME)
        if DELETE_OUTPUT:
            delete_test_output(script_name=SCRIPT_NAME)
