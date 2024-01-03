import unittest
import zipfile

from datasetpreparator.dir_packager.dir_packager import multiple_dir_packager

from tests.test_settings import DELETE_INPUT


from tests.test_utils import (
    delete_test_input,
    create_test_input_dir,
    create_test_text_files,
    create_nested_test_directories,
)

SCRIPT_NAME = "file_packager"


class TestDirPackagerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Get test directory input and output:
        cls.input_path = create_test_input_dir(script_name=SCRIPT_NAME)

        cls.n_dirs = 1
        # Create multiple nested directories:
        nested_dirs = create_nested_test_directories(
            input_path=cls.input_path, n_dirs=cls.n_dirs
        )

        cls.n_files = 5
        for directory in nested_dirs:
            # Create multiple files in the directory:
            create_test_text_files(input_path=directory, n_files=cls.n_files)

    def test_multiple_dir_packager(self) -> None:
        archives = multiple_dir_packager(input_path=self.input_path)

        # Archive should exists:
        self.assertTrue(archives[0].exists())

        files_in_archive = 0
        with zipfile.ZipFile(archives[0], "r") as zip_ref:
            # Get a list of all files and directories in the zip file
            file_list = zip_ref.namelist()

            # Count the number of files in the zip file
            files_in_archive = len(file_list)

        # Assert equal number of files in input vs output:
        self.assertEqual(self.n_files, files_in_archive)

    @classmethod
    def tearDownClass(cls) -> None:
        if DELETE_INPUT:
            delete_test_input(script_name=SCRIPT_NAME)
