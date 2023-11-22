# Directory Flattener

# CLI Usage

Please keep in mind that ```src/directory_flattener.py``` does not contain default flag values and can be customized with the following command line flags:

```
usage: directory_flattener.py [-h] [--input_path INPUT_PATH] [--output_path OUTPUT_PATH]
                              [--file_extension FILE_EXTENSION]

Directory restructuring tool used in order to flatten the structure, map the old structure to a separate
file, and for later processing with other tools. Created primarily to define StarCraft 2 (SC2) datasets.

options:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH (default = ../processing/directory_flattener/input)
                        Please provide input path to the dataset that is going to be processed.
  --output_path OUTPUT_PATH (default = ../processing/directory_flattener/output)
                        Please provide output path where sc2 map files will be downloaded.
  --file_extension FILE_EXTENSION (default = .SC2Replay)
                        Please provide a file extension for files that will be moved and renamed.
```