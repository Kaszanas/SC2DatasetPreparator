from pathlib import Path
import unittest
from datasetpreparator.sc2.sc2reset_replaypack_downloader.get_md5 import get_md5
from datasetpreparator.sc2.sc2reset_replaypack_downloader.sc2reset_replaypack_downloader import (
    sc2reset_replaypack_downloader,
)

from tests.test_settings import DELETE_OUTPUT, DELETE_INPUT


from tests.test_utils import (
    create_test_input_dir,
    create_test_output_dir,
    delete_test_input,
    delete_test_output,
)


SCRIPT_NAME = "sc2reset_replaypack_downloader"


class TestSC2ReplaypackProcessor(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        # Create and get test input and output directories:
        cls.input_path = create_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = create_test_output_dir(script_name=SCRIPT_NAME)

        cls.test_replaypack_list = [
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

    @classmethod
    def tearDownClass(cls) -> None:
        if DELETE_INPUT:
            delete_test_input(script_name=SCRIPT_NAME)
        if DELETE_OUTPUT:
            delete_test_output(script_name=SCRIPT_NAME)
