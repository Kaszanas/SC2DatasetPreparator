from pathlib import Path
import os


class SC2InfoExtractorGoArguments:
    """
    Arguments for the SC2InfoExtractorGo binary.

    Parameters
    ----------
    game_mode_filter : int, optional
        Specifies which game mode should be included from the processed files
        in a format of a binary flag: AllGameModes: 0b11111111.
    input : Path, optional
        Input directory where .SC2Replay files are held.
    log_dir : Path, optional
        Specifies directory which will hold the logging information
    log_level : int, optional
        Specifies a log level from 1-7:
        Panic - 1, Fatal - 2,
        Error - 3, Warn - 4,
        Info - 5, Debug - 6,
        Trace - 7.
    number_of_packages : int, optional
        Provide a number of zip packages to be created and compressed
        into a zip archive. Please remember that this number needs to be lower
        than the number of processed files. If set to 0, will ommit the
        zip packaging and output .json directly to drive
    only_map_download : bool, optional
        Specifies if the tool is supposed to only download
        the maps and not process the replays
    output : Path, optional
        Output directory where compressed zip packages will be saved
    perform_chat_anonymization : bool, optional
        Specifies if the chat anonymization should be performed
    perform_cleanup: bool, optional
        Provide if the tool is supposed to perform the cleaning
        functions within the processing pipeline
    perform_filtering : bool, optional
        Specifies if the pipeline ought to verify different hard coded game modes.
        If set to false completely bypasses the filtering
    perform_integrity_checks : bool, optional
        If the software is supposed to check the hardcoded
        integrity checks for the provided replays
    perform_player_anonymization : bool, optional
        Specifies if the tool is supposed to perform player anonymization
        functions within the processing pipeline.
        If set to true please remember to download and run
        an anonymization server: https://doi.org/10.5281/zenodo.5138313.
    perform_validity_checks : bool, optional
        Provide if the tool is supposed to use hardcoded validity checks
        and verify if the replay file variables
        are within 'common sense' ranges.
    max_procs : int, optional
        Specifies the number of logic cores of a processor
        that will be used for processing, by default os.cpu_count()
    """

    def __init__(
        self,
        game_mode_filter: int,
        processing_input: Path,
        log_dir: Path,
        log_level: int,
        number_of_packages: int,
        only_map_download: bool,
        output: Path,
        perform_chat_anonymization: bool,
        perform_cleanup: bool,
        perform_filtering: bool,
        perform_integrity_checks: bool,
        perform_player_anonymization: bool,
        perform_validity_checks: bool,
        max_procs: int = os.cpu_count(),
    ):
        self.game_mode_filter = game_mode_filter
        self.processing_input = processing_input
        self.log_dir = log_dir
        self.log_level = log_level
        self.max_procs = max_procs
        self.number_of_packages = number_of_packages
        self.only_map_download = "true" if only_map_download else "false"
        self.output = output
        self.perform_chat_anonymization = (
            "true" if perform_chat_anonymization else "false"
        )
        self.perform_cleanup = "true" if perform_cleanup else "false"
        self.perform_filtering = "true" if perform_filtering else "false"
        self.perform_integrity_checks = "true" if perform_integrity_checks else "false"
        self.perform_player_anonymization = (
            "true" if perform_player_anonymization else "false"
        )
        self.perform_validity_checks = "true" if perform_validity_checks else "false"

    @staticmethod
    def get_download_maps_args(
        processing_input: Path, output: Path
    ) -> "SC2InfoExtractorGoArguments":
        arguments = SC2InfoExtractorGoArguments(
            processing_input=processing_input,
            output=output,
            only_map_download=True,
            max_procs=4,
        )

        return arguments

    @staticmethod
    def get_sc2egset_processing_args(
        processing_input: Path,
        output: Path,
        perform_chat_anonymization: bool,
    ) -> "SC2InfoExtractorGoArguments":
        #     # FIXME hardcoded binary name
        #     "/SC2InfoExtractorGo",
        #     f"-processing_input={directory}/",
        #     f"-output={output_directory_filepath}/",
        #     "-perform_integrity_checks=true",
        #     "-perform_validity_checks=false",
        #     "-perform_cleanup=true",
        #     f"-perform_chat_anonymization={perform_chat_anonymization}",
        #     "-number_of_packages=1",
        #     # FIXME hardcoded path
        #     "-localized_maps_file=../processing/json_merger/merged.json",
        #     "-max_procs=1",
        #     "-log_level=3",
        #     f"-log_dir={output_directory_filepath}/",
        # ]

        arguments = SC2InfoExtractorGoArguments(
            processing_input=processing_input,
            output=output,
            perform_integrity_checks=True,
            perform_validity_checks=False,
            perform_cleanup=True,
            perform_chat_anonymization=perform_chat_anonymization,
            number_of_packages=1,
            max_procs=1,
            log_level=3,
            log_dir=output,
        )

        return arguments


class ReplaypackProcessorArguments:
    """
    Arguments for the ReplaypackProcessor.

    Parameters
    ----------
    input_path : Path
        Input path that contains multiple replaypacks.
    output_path : Path
        Output path where the processed replaypacks will be saved.
    n_processes : int
        Number of SC2InfoExtractorGo processes that will be spawned.
    """

    def __init__(
        self,
        input_path: Path,
        output_path: Path,
        n_processes: int,
    ):
        self.input_path = input_path
        self.output_path = output_path
        self.n_processes = n_processes
