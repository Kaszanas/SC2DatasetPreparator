import unittest

from datasetpreparator.processed_mapping_copier.processed_mapping_copier import (
    processed_mapping_copier,
)

from tests.test_settings import (
    DELETE_SCRIPT_TEST_DIR,
    DELETE_SCRIPT_TEST_OUTPUT_DIR,
    DELETE_SCRIPT_TEST_INPUT_DIR,
)


from tests.test_utils import (
    create_script_test_input_dir,
    create_script_test_output_dir,
    dir_test_cleanup,
)


class ProcessedMappingCopierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.SCRIPT_NAME = "processed_mapping_copier"
        # Create and get test input and output directories:
        cls.input_path = create_script_test_input_dir(script_name=cls.SCRIPT_NAME)
        cls.output_path = create_script_test_output_dir(script_name=cls.SCRIPT_NAME)

        # TODO: Define test directory structure

    def test_processed_mapping_copier(self):
        processed_mapping_copier(
            input_path=self.input_path, output_path=self.output_path
        )
        # TODO: Check if the

    @classmethod
    def tearDownClass(cls) -> None:
        dir_test_cleanup(
            script_name=cls.SCRIPT_NAME,
            delete_script_test_dir_bool=DELETE_SCRIPT_TEST_DIR,
            delete_script_test_input_bool=DELETE_SCRIPT_TEST_INPUT_DIR,
            delete_script_test_output_bool=DELETE_SCRIPT_TEST_OUTPUT_DIR,
        )
