from pathlib import Path
import unittest

from sc2datasetpreparator.dir_packager.dir_packager import multiple_dir_packager

from test.test_utils import (
    dir_test_create_cleanup,
    create_test_input_dir,
    create_test_text_files,
    create_nested_test_directories,
)

SCRIPT_NAME = "file_packager"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class DirPackagerTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        # Get test directory input and output:
        cls.input_path = create_test_input_dir(script_name=SCRIPT_NAME)

        # Create multiple nested directories:
        nested_dirs = create_nested_test_directories(
            input_path=cls.input_path, n_dirs=3
        )

        for directory in nested_dirs:
            # Create multiple files in the directory:
            create_test_text_files(input_path=directory, n_files=5)

    def test_multiple_dir_packager(self) -> None:
        archives = multiple_dir_packager(input_path=self.input_path)

        # TODO: Assert that the file archive exists:

        # TODO: Assert equal number of files in input vs output:
