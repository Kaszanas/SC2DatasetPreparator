import unittest
from sc2datasetpreparator.directory_flattener.directory_flattener import (
    directory_flattener,
)

from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
    create_test_text_files,
    create_nested_test_directories,
)

SCRIPT_NAME = "directory_flattener"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class DirectoryFlattenerTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        # Get test directory input and output:
        cls.input_path = get_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = get_test_output_dir(script_name=SCRIPT_NAME)
        cls.file_extension = ".SC2Replay"

        # Create nested directory structure mimicking how real replaypacks look like:
        nested_dirs = create_nested_test_directories(input_path=cls.input_path)
        for directory in nested_dirs:
            # Create multiple test files with the selected extension:.
            create_test_text_files(
                input_path=directory, n_files=4, extension=cls.file_extension
            )
            # Create additional files that should not be present in the output:,
            create_test_text_files(input_path=directory, n_files=1, extension=".txt")

    def test_directory_flattener(self) -> None:
        directory_flattener(
            input_path=self.input_path,
            output_path=self.output_path,
            file_extension=self.file_extension,
        )
        # TODO: Assert the final directory not to contain any other nested directories.
        # TODO: Assert the final directory have the same number of files with the selected extension.
        # TODO: Assert the final flattened directory to have one .json file
        # containing mapping of the files.
