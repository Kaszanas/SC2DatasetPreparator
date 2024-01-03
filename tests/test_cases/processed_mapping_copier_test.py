import unittest

from datasetpreparator.processed_mapping_copier.processed_mapping_copier import (
    processed_mapping_copier,
)

from tests.test_settings import DELETE_OUTPUT, DELETE_INPUT


from tests.test_utils import (
    create_test_input_dir,
    create_test_output_dir,
    delete_test_input,
    delete_test_output,
)

SCRIPT_NAME = "processed_mapping_copier"


class ProcessedMappingCopierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Create and get test input and output directories:
        cls.input_path = create_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = create_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Define test directory structure

    def test_processed_mapping_copier(self):
        processed_mapping_copier(
            input_path=self.input_path, output_path=self.output_path
        )
        # TODO: Check if the

    @classmethod
    def tearDownClass(cls) -> None:
        if DELETE_INPUT:
            delete_test_input(script_name=SCRIPT_NAME)
        if DELETE_OUTPUT:
            delete_test_output(script_name=SCRIPT_NAME)
