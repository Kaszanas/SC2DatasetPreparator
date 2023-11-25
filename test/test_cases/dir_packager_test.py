import unittest

from sc2datasetpreparator.dir_packager.dir_packager import dir_packager

from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
)

SCRIPT_NAME = "file_packager"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class FilePackagerTest(unittest.TestCase):
    def setUpClass(self) -> None:
        # Get test directory input and output:
        self.input_path = get_test_input_dir(script_name=SCRIPT_NAME)

        # TODO: Create a sample directory containing some files to package:

    def test_file_packager(self) -> None:
        # REVIEW: What should I assert here? It is not clear that this could fail.
        # I am using standard zip implementation. Minimal custom code was created here.
        dir_packager(input_path=self.input_path)