# File Renamer

Utility script that is merging two JSON files.

# CLI Usage

Please keep in mind that the  ```src/json_merger.py``` contains default flag values and can be customized with the following command line flags:
```
usage: json_merger.py [-h] [--json_one JSON_ONE] [--json_two JSON_TWO] [--output_filepath OUTPUT_FILEPATH]

Tool used for merging two .json files. Created in order to merge two mappings created by
https://github.com/Kaszanas/SC2MapLocaleExtractor

options:
  -h, --help            show this help message and exit
  --json_one JSON_ONE (default = ../../processing/json_merger/json1.json)
                    Please provide the path to the first .json file that is going to be merged.
  --json_two JSON_TWO (default = ../../processing/json_merger/json2.json)
                    Please provide the path to the second .json file that is going to be merged.
  --output_filepath OUTPUT_FILEPATH (default = ../../processing/json_merger/merged.json)
                        Please provide output path where sc2 map files will be downloaded.
```
