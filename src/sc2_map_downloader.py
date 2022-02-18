import sc2reader
import os
import requests
import argparse
import asyncio


async def replay_reader(output_path, filepath, hash_set, lock):
    """_summary_

    :param output_path: _description_
    :type output_path: _type_
    :param filepath: _description_
    :type filepath: _type_
    :param hash_set: _description_
    :type hash_set: bool
    :param lock: _description_
    :type lock: _type_
    :return: _description_
    :rtype: _type_
    """
    try:
        replay = sc2reader.load_replay(os.path.join(root, filepath), load_map=True)
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
            output_filepath = os.path.join(
                args.output_path, f"{replay_map_hash}.SC2Map"
            )
            with open(output_filepath, "wb") as output_map_file:
                output_map_file.write(response.content)
                return True
    except:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool for downloading maps based on the data that is available within .SC2Replay file."
    )
    parser.add_argument(
        "--input_path",
        default="D:\\Projects\\SC2MapDownloader\\Download",
        help="Please provide input path to the dataset that is going to be processed.",
    )
    parser.add_argument(
        "--output_path",
        default="D:\\Projects\\SC2MapDownloader\\Maps4",
        help="Please provide output path where sc2 map files will be downloaded.",
    )
    parser.add_argument(
        "--file_extension",
        default=".SC2Replay",
        help="Please provide a file extension for files that will be moved and renamed.",
    )
    args = parser.parse_args()

    replay_map_archive_hashes = set()

    list_of_replay_files = []
    loop = asyncio.get_event_loop()
    lock = asyncio.Lock(loop=loop)
    futures = []

    args_file_extension = args.file_extension
    args_output_path = args.output_path

    for root, _, filename in os.walk(args.input_path):
        # Performing action for every file that was detected
        for file in filename:
            if file.endswith(".SC2Replay"):
                # Asynchronously download maps
                filepath = os.path.join(root, file)

                futures.append(
                    replay_reader(
                        output_path=args_output_path,
                        filepath=filepath,
                        hash_set=replay_map_archive_hashes,
                        lock=lock,
                    )
                )

    result = loop.run_until_complete(asyncio.gather(*futures))
