import argparse
from pathlib import Path
import sc2reader


def replay_reader(
    replay_filepath: str,
    output_dir: str,
) -> None:
    """
    Fill this

    :param replay_filepath: Specifies the path of a replay within the replay_root.
    :type replay_filepath: str
    :param output_dir: Specifies the directory where sorted files will be copied with a custom directory structure.
    :type output_dir: str
    """
    try:
        replay = sc2reader.load_replay(replay_filepath, load_map=True)
        replay_url = replay.map_file.url
        print(replay_url)
        replay_map_hash = replay.map_hash
        # TODO: Copy the file

    except:
        print("Error detected!")
        return


def replay_sorter(input_dir: Path, output_dir: Path):
    """
    _summary_

    :param input_dir: _description_
    :type input_dir: Path
    :param output_dir: _description_
    :type output_dir: Path
    """

    # TODO: If the directory with the name version does not exist create it:
    for member in input_dir.iterdir():
        if member.is_dir():
            for file_path in member.iterdir():
                if file_path.suffix == ".SC2Replay":
                    replay_reader(replay_filepath=file_path, output_dir=output_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo"
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Please provide input path to the directory containing the dataset that is going to be processed.",
        default="../processing/directory_flattener/output",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        help="Please provide output path for replays to be sorted by game version.",
        default="../processing/version_sorter/output",
    )
