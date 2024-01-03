import unittest

from datasetpreparator.sc2.sc2_replaypack_processor.sc2_replaypack_processor import (
    sc2_replaypack_processor,
)

from tests.test_settings import DELETE_OUTPUT, DELETE_INPUT


from tests.test_utils import (
    create_test_input_dir,
    create_test_output_dir,
    delete_test_input,
    delete_test_output,
)

SCRIPT_NAME = "sc2_replaypack_processor"

# TODO: sc2_replaypack_processor by default uses another piece of software for parsing SC2 replays.
# So it will be downloading the data from another repository.


class SC2ReplaypackProcessorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Create and get test input and output directories:
        cls.input_path = create_test_input_dir(script_name=SCRIPT_NAME)
        cls.output_path = create_test_output_dir(script_name=SCRIPT_NAME)

        # TODO: Verify that SC2InfoExtractorGo is available in path.
        # If not available download from GitHub release page.

        # TODO: Set up a test directory with at least
        # two replaypacks with at least one SC2Replay file within.

    def test_sc2_replaypack_processor(self):
        sc2_replaypack_processor(
            input_path=self.input_path,
            output_path=self.output_path,
            n_processes=1,
            perform_chat_anonymization=False,
        )
        # TODO: Check if output contains the same directories as for input.
        # TODO: Check if outputs contain extracted JSON files with valid fields.

    @classmethod
    def tearDownClass(cls) -> None:
        if DELETE_INPUT:
            delete_test_input(script_name=SCRIPT_NAME)
        if DELETE_OUTPUT:
            delete_test_output(script_name=SCRIPT_NAME)
