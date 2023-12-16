import unittest

from datasetpreparator.sc2_map_downloader.sc2_map_downloader import (
    sc2_map_downloader,
)

from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
)

SCRIPT_NAME = "sc2_map_downloader"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class SC2MapDownloaderTest(unittest.TestCase):
    def setUp(self) -> None:
        # Get test directory input and output:
        self.input_path = get_test_input_dir(script_name=SCRIPT_NAME)
        self.output_path = get_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Have at least one valid SC2Replay to download its map.

    def test_sc2_map_downloader_test(self):
        sc2_map_downloader(input_path=self.input_path, output_path=self.output_path)
        # TODO: Assert that map was downloaded succseefully.
