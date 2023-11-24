import unittest

from sc2datasetpreparator.sc2_map_downloader.sc2_map_downloader import (
    sc2_map_downloader,
)

from test.test_utils import dir_test_create_cleanup

SCRIPT_NAME = "sc2_map_downloader"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class SC2MapDownloaderTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        # TODO: Have at least one valid SC2Replay to download its map.
        pass

    def test_sc2_map_downloader_test(self):
        # TODO: Assert that map was downloaded succseefully.
        pass
