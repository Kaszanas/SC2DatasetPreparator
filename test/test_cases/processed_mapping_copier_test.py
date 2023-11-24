import unittest

from sc2datasetpreparator.processed_mapping_copier.processed_mapping_copier import (
    processed_mapping_copier,
)

from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
)

SCRIPT_NAME = "processed_mapping_copier"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class ProcessedMappingCopierTest(unittest.TestCase):
    def setUp(self) -> None:
        # Get test directory input and output:
        self.input_path = get_test_input_dir(script_name=SCRIPT_NAME)
        self.output_path = get_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Define test directory structure
        pass

    def test_processed_mapping_copier(self):
        # TODO: Check if the

        pass
