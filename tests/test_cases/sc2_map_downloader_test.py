import unittest

from datasetpreparator.sc2.sc2_map_downloader.sc2_map_downloader import (
    sc2_map_downloader,
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


class SC2MapDownloaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.SCRIPT_NAME = "sc2_map_downloader"
        # Create and get test input and output directories:
        cls.input_path = create_script_test_input_dir(script_name=cls.SCRIPT_NAME)
        cls.output_path = create_script_test_output_dir(script_name=cls.SCRIPT_NAME)

        # TODO: Have at least one valid SC2Replay to download its map.

    def test_sc2_map_downloader(self):
        sc2_map_downloader(input_path=self.input_path, output_path=self.output_path)
        # TODO: Assert that map was downloaded succseefully.

    @classmethod
    def tearDownClass(cls) -> None:
        dir_test_cleanup(
            script_name=cls.SCRIPT_NAME,
            delete_script_test_dir_bool=DELETE_SCRIPT_TEST_DIR,
            delete_script_test_input_bool=DELETE_SCRIPT_TEST_INPUT_DIR,
            delete_script_test_output_bool=DELETE_SCRIPT_TEST_OUTPUT_DIR,
        )
