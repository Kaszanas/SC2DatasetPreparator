import unittest

from sc2datasetpreparator.processed_mapping_copier.processed_mapping_copier import (
    processed_mapping_copier,
)

from test.test_utils import dir_test_create_cleanup

SCRIPT_NAME = "processed_mapping_copier"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class ProcessedMappingCopierTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        # TODO: Define test directory structure
        pass

    def test_processed_mapping_copier(self):
        # TODO: Check if the

        pass
