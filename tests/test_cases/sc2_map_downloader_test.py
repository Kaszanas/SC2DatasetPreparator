import unittest

from datasetpreparator.sc2.sc2_map_downloader.sc2_map_downloader import (
    sc2_map_downloader,
)
from tests.test_settings import DELETE_OUTPUT, DELETE_INPUT

from tests.test_utils import (
    create_test_input_dir,
    create_test_output_dir,
    delete_test_input,
    delete_test_output,
)

SCRIPT_NAME = "sc2_map_downloader"


class SC2MapDownloaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Create and get test input and output directories:
        cls.input_path = create_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = create_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Have at least one valid SC2Replay to download its map.

    def test_sc2_map_downloader_test(self):
        sc2_map_downloader(input_path=self.input_path, output_path=self.output_path)
        # TODO: Assert that map was downloaded succseefully.

    @classmethod
    def tearDownClass(cls) -> None:
        if DELETE_INPUT:
            delete_test_input(script_name=SCRIPT_NAME)
        if DELETE_OUTPUT:
            delete_test_output(script_name=SCRIPT_NAME)
