# Processed Mapping Copier

Utility script that enters each of the processed replaypack directories and copies the log files that are left after processing with `sc2_replaypack_processor`.

# CLI Usage

Please keep in mind that the  ```src/processed_mapping_copier.py``` contains default flag values and can be customized with the following command line flags:
```
usage: processed_mapping_copier.py [-h] [--input_path INPUT_PATH] [--output_path OUTPUT_PATH]

Tool for copying the processed_mapping.json files that are required to define the StarCraft 2 (SC2) dataset.

options:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH (default = ../../processing/directory_flattener/output)
                        Please provide input path to the flattened replaypacks that contain
                        procesed_mapping.json files.
  --output_path OUTPUT_PATH (default = ../../processing/sc2_replaypack_processor/output)
                        Please provide output path where processed_mapping.json will be copied.
```
