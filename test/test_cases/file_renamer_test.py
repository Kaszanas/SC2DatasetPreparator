import unittest

from sc2datasetpreparator.file_renamer.file_renamer import file_renamer

from test.test_utils import dir_test_create_cleanup

SCRIPT_NAME = "file_renamer"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class FileRenamerTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        # TODO: Mock the directory structure:
        pass

    def test_file_renamer(self) -> None:
        # TODO: Assert that the files with old name do not exist.
        # TODO: Assert that files with new names exist.
        pass
