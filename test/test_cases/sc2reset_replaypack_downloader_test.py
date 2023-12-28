from pathlib import Path
import unittest
from datasetpreparator.sc2.sc2reset_replaypack_downloader.get_md5 import get_md5
from datasetpreparator.sc2.sc2reset_replaypack_downloader.sc2reset_replaypack_downloader import (
    sc2reset_replaypack_downloader,
)
from test.test_utils import (
    dir_test_create_cleanup,
    get_test_input_dir,
    get_test_output_dir,
)


SCRIPT_NAME = "sc2reset_replaypack_downloader"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class SC2ReplaypackProcessorTest(unittest.TestCase):
    def setUp(self) -> None:
        # Get test directory input and output:
        self.input_path = get_test_input_dir(script_name=SCRIPT_NAME)
        self.output_path = get_test_output_dir(script_name=SCRIPT_NAME)

        self.test_replaypack_list = [
            (
                "2016_IEM_10_Taipei",
                "https://zenodo.org/record/5575797/files/2016_IEM_10_Taipei.zip?download=1",
                "f9150577d08216ce5ec5de954d8d536c",
            ),
        ]

    def sc2reset_replaypack_downloader_test(self):
        replaypack_name, replaypack_url, archive_md5 = self.test_replaypack_list[0]

        sc2reset_replaypack_downloader(
            download_path=self.input_path,
            unpack_path=self.output_path,
            n_workers=1,
            replaypack_list=self.test_replaypack_list,
        )

        # Check if the replaypack was downloaded:
        archive_name = f"{replaypack_name}.zip"
        self.assertTrue(
            Path(self.input_path, archive_name).exists(),
            msg="The replaypack was not downloaded.",
        )
        # Check the md5 of the downloaded archive:
        self.assertEqual(
            archive_md5,
            get_md5(Path(self.input_path, archive_name)),
            msg="The md5 of the downloaded archive is not correct.",
        )
        # Check if the replaypack was unpacked:
        self.assertTrue(
            Path(self.output_path, replaypack_name).exists(),
            msg="The replaypack was not unpacked.",
        )
        # Check if the replaypack was unpacked correctly:
        self.assertGreater(
            0, len(list(Path(self.output_path, replaypack_name).glob(".SC2Replay")))
        )
