# SC2 Map Downloader

Utility script that opens each of the provided replays and downloads the map from the Blizzard servers. This is required to later create the localization mapping for map translation with [SC2MapLocaleExtractor](https://github.com/Kaszanas/SC2MapLocaleExtractor).

# CLI Usage

Please keep in mind that the  ```src/sc2_map_downloader.py``` does not contain default flag values and can be customized with the following command line flags:
```
usage: sc2_map_downloader.py [-h] [--input_path INPUT_PATH] [--output_path OUTPUT_PATH]

Tool for downloading StarCraft 2 (SC2) maps based on the data that is available within .SC2Replay file.       

options:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH (default = ../../processing/directory_flattener/output)
                        Please provide input path to the dataset that is going to be processed.
  --output_path OUTPUT_PATH (default = ../../processing/sc2_map_downloader/output)
                        Please provide output path where sc2 map files will be downloaded.
```