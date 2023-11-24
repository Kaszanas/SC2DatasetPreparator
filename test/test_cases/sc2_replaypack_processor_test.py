import unittest

from sc2datasetpreparator.sc2_replaypack_processor.sc2_replaypack_processor import (
    sc2_replaypack_processor,
)

from test.test_utils import dir_test_create_cleanup

SCRIPT_NAME = "sc2_replaypack_processor"


@dir_test_create_cleanup(script_name=SCRIPT_NAME, delete_output=False)
class SC2ReplaypackProcessorTest(unittest.TestCase):
    def setUpClass(cls) -> None:
        # TODO: Verify that SC2InfoExtractorGo is available in path.
        # If not available download from GitHub release page.

        # TODO: Set up a test directory with at least
        # two replaypacks with at least one SC2Replay file within.
        pass

    def test_sc2_replaypack_processor(self):
        # TODO: Check if output contains the same directories as for input.
        # TODO: Check if outputs contain extracted JSON files with valid fields.
        pass
