import sc2reader
import os
import requests
import argparse
import asyncio


async def replay_reader(
    output_path: str,
    replay_root: str,
    replay_filepath: str,
    hash_set: set,
    lock: asyncio.Lock,
) -> None:
    """
    Contains logic to try to read and download a map based on the information that is held within .SC2Replay file.

    :param output_path: Specifies where the final map file will be downloaded.
    :type output_path: str
    :param replay_root: Specifies the root directory of a replay.
    :type replay_root: str
    :param filepath: Specifies the path of a replay within the replay_root.
    :type filepath: str
    :param hash_set: Specifies a set that holds all of the previously seen maps.
    :type hash_set: set
    :param lock: Specifies an asyncio.Lock
    :type lock: asyncio.Lock
    """
    try:
        replay = sc2reader.load_replay(
            os.path.join(replay_root, replay_filepath), load_map=True
        )
        replay_url = replay.map_file.url
        print(replay_url)
        replay_map_hash = replay.map_hash

        download_replay = False
        async with lock:
            if replay_map_hash not in hash_set:
                hash_set.add(replay_map_hash)
                download_replay = True

        if download_replay:
            response = requests.get(replay_url, allow_redirects=True)
            output_filepath = os.path.join(output_path, f"{replay_map_hash}.SC2Map")
            with open(output_filepath, "wb") as output_map_file:
                output_map_file.write(response.content)
                return
    except:
        return


def map_downloader(input_path: str, output_path: str) -> None:
    """
    Holds the main loop for asynchronous map downloading logic.

    :param input_path: Specifies the input path that contains .SC2Replay files which will be used for map detection.
    :type input_path: str
    :param output_path: Specifies the output path where the downloaded maps will be placed.
    :type output_path: str
    """
    futures = []
    replay_map_archive_hashes = set()

    loop = asyncio.get_event_loop()
    lock = asyncio.Lock(loop=loop)
    for root, _, filename in os.walk(input_path):
        # Performing action for every file that was detected
        for file in filename:
            if file.endswith(".SC2Replay"):
                # Asynchronously download maps
                filepath = os.path.join(root, file)

                futures.append(
                    replay_reader(
                        output_path=output_path,
                        root=root,
                        filepath=filepath,
                        hash_set=replay_map_archive_hashes,
                        lock=lock,
                    )
                )

    result = loop.run_until_complete(asyncio.gather(*futures))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool for downloading maps based on the data that is available within .SC2Replay file."
    )
    parser.add_argument(
        "--input_path",
        default="../Maps/input",
        help="Please provide input path to the dataset that is going to be processed.",
    )
    parser.add_argument(
        "--output_path",
        default="../Maps/output",
        help="Please provide output path where sc2 map files will be downloaded.",
    )

    args = parser.parse_args()

    args_input_path = args.input_path
    args_output_path = args.output_path
    map_downloader(input_path=args_input_path, output_path=args_output_path)