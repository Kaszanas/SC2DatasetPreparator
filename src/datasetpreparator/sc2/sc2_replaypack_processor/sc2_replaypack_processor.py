import os
from pathlib import Path
import logging
import click
from tqdm import tqdm

from datasetpreparator.settings import LOGGING_FORMAT
from datasetpreparator.sc2.sc2_replaypack_processor.utils.replaypack_processor_args import (
    ReplaypackProcessorArguments,
    SC2InfoExtractorGoArguments,
)
from datasetpreparator.sc2.sc2_replaypack_processor.utils.multiprocess import (
    multiprocessing_scheduler,
)


def sc2_replaypack_processor(
    arguments: ReplaypackProcessorArguments,
):
    """
    Processes multiple StarCraft II replaypacks
    by using https://github.com/Kaszanas/SC2InfoExtractorGo

    Parameters
    ----------
    arguments : ReplaypackProcessorArguments
        Specifies the arguments as per the ReplaypackProcessorArguments class fields.
    """

    input_path = arguments.input_path
    output_path = arguments.output_path
    n_processes = arguments.n_processes

    multiprocessing_list = []
    for maybe_dir in tqdm(list(input_path.iterdir())):
        logging.debug(f"Processing entry: {maybe_dir}")
        processing_input_dir = Path(input_path, maybe_dir).resolve()
        if not processing_input_dir.is_dir():
            logging.debug("Entry is not a directory, skipping!")
            continue

        logging.debug(f"Output dir: {output_path}")
        # Create the main output directory:
        if not output_path.exists():
            output_path.mkdir()

        # TODO: use pathlib:
        path, output_directory_name = os.path.split(maybe_dir)
        logging.debug(f"Output dir name: {output_directory_name}")
        if output_directory_name == "input":
            continue

        output_directory_with_name = Path(output_path, output_directory_name).resolve()
        logging.debug(f"Output filepath: {output_directory_with_name}")

        # Create the output subdirectories:
        if not output_directory_with_name.exists():
            output_directory_with_name.mkdir()

        sc2_info_extractor_go_args = (
            SC2InfoExtractorGoArguments.get_sc2egset_processing_args(
                processing_input=processing_input_dir,
                output=output_directory_with_name,
                perform_chat_anonymization=arguments.perform_chat_anonymization,
            )
        )

        multiprocessing_list.append(sc2_info_extractor_go_args)

    multiprocessing_scheduler(multiprocessing_list, int(n_processes))


@click.command(
    help="Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo."
)
@click.option(
    "--input_path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    required=True,
    help="Please provide an output directory for the resulting files.",
)
@click.option(
    "--output_path",
    type=click.Path(exists=True, dir_okay=True, file_okay=False, resolve_path=True),
    required=True,
    help="Please provide output path where StarCraft 2 (SC2) map files will be downloaded.",
)
@click.option(
    "--perform_chat_anonymization",
    type=bool,
    default=False,
    required=True,
    help="Provide 'True' if chat should be anonymized, otherwise 'False'.",
)
@click.option(
    "--n_processes",
    type=int,
    default=4,
    required=True,
    help="Please provide the number of processes to be spawned for the dataset processing.",
)
@click.option(
    "--log",
    type=click.Choice(["INFO", "DEBUG", "ERROR"], case_sensitive=False),
    default="WARN",
    help="Log level (INFO, DEBUG, ERROR)",
)
def main(
    input_path: Path,
    output_path: Path,
    n_processes: int,
    perform_chat_anonymization: bool,
    log: str,
) -> None:
    numeric_level = getattr(logging, log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {numeric_level}")
    logging.basicConfig(format=LOGGING_FORMAT, level=numeric_level)

    arguments = ReplaypackProcessorArguments(
        input_path=input_path,
        output_path=output_path,
        n_processes=n_processes,
    )

    sc2_replaypack_processor(arguments=arguments)


if __name__ == "__main__":
    main()
