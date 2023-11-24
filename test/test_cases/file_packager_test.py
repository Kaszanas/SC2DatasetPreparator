import unittest

from sc2datasetpreparator.file_packager.file_packager import file_packager

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
        self.output_path = get_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Create a sample directory containing some files to package:
        pass

    def test_file_packager(self) -> None:
        # REVIEW: What should I assert here? It is not clear that this could fail.
        # I am using standard zip implementation. Minimal custom code was created here.
        pass
