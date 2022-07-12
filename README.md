[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5296664.svg)](https://doi.org/10.5281/zenodo.5296664)

# SC2DatasetPreparator

Tools in this repository were used to create the **[SC2ReSet: StarCraft II Esport Replaypack Set](https://doi.org/10.5281/zenodo.5575796)**, and finally **[SC2EGSet: StarCraft II Esport Game State Dataset](https://doi.org/10.5281/zenodo.5503997)**.

## Dataset Preparation Steps

To reproduce our experience with defining a dataset and to be able to compare your results with our work we describe how to perform the processing below.

### Using Docker

1. Build the docker image from: https://github.com/Kaszanas/SC2InfoExtractorGo
2. Run the commands as described in the ```Makefile```. But first make sure that all of the script parameters are set according to your needs.

### Using Python

0. Obtain replays to process. This can be a replaypack or your own replay folder.
1. Download latest version of [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo), or build it from source.
2. **Optional** If the replays that you have are held in nested directories it is best to use  ```src/directory_flattener.py```. This will copy the directory and place all of the files to the top directory where it can be further processed. In order to preserve the old directory structure, a .json file is created. The file contains the old directory tree to a mapping: ```{"replayUniqueHash": "whereItWasInOldStructure"}```. This step is is required in order to properly use [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo) as it only lists the files immediately available on the top level of the input directory. [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo).
3. **Optional** Use the map downloader ```src/sc2_map_downloader.py``` to download maps that were used in the replays that you obtained. This is required for the next step.
4. **Optional** Use the [SC2MapLocaleExtractor](https://github.com/Kaszanas/SC2MapLocaleExtractor) to obtain the mapping of ```{"foreign_map_name": "english_map_name"}``` which is required for the [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo) to translate the map names in the output .json files.
5. Perform replaypack processing using ```src/sc2_replaypack_processor.py``` with the [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo) placed in PATH, or next to the script.
6. **Optional** Using the ```src/file_renamer.py```, rename the files that were generated in the previous step. This is not required and is done to increase the readibility of the directory structure for the output.
7. Using the ```src/file_packager.py```, create .zip archives containing the datasets and the supplementary files. By finishing this stage, your dataset should be ready to upload.

#### Customization

In order to specify different processing flags for https://github.com/Kaszanas/SC2InfoExtractorGo please modify the ```src/sc2_replaypack_processor``` file directly

## Scripts Command Line Arguments Usage

Before using this software please install Python >= 3.10 and ```requirements.txt```.

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

Please keep in mind that the  ```src/sc2_map_downloader.py``` does not contain default flag values and can be customized with the following command line flags:
```
usage: sc2_map_downloader.py [-h] [--input_path INPUT_PATH] [--output_path OUTPUT_PATH]

Tool for downloading StarCraft 2 (SC2) maps based on the data that is available within .SC2Replay file.       

options:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH (default = ../processing/directory_flattener/output)
                        Please provide input path to the dataset that is going to be processed.
  --output_path OUTPUT_PATH (default = ../processing/sc2_map_downloader/output)
                        Please provide output path where sc2 map files will be downloaded.
```

Please keep in mind that the ```src/sc2_replaypack_processor.py```  contains default flag values and can be customized with the following command line flags:
```
usage: sc2_replaypack_processor.py [-h] [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR]
                                   [--n_processes N_PROCESSES]

Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo      

options:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR (default = ../processing/directory_flattener/output)
                        Please provide input path to the directory containing the dataset that is going to be processed.
  --output_dir OUTPUT_DIR (default = ../processing/sc2_replaypack_processor/output)
                        Please provide an output directory for the resulting files.
  --n_processes N_PROCESSES (default = 4)
                        Please provide the number of processes to be spawned for the dataset processing.
```

Please keep in mind that the  ```src/file_renamer.py``` contains default flag values and can be customized with the following command line flags:
```
usage: file_renamer.py [-h] [--input_dir INPUT_DIR]

Tool used for processing StarCraft 2 (SC2) datasets with https://github.com/Kaszanas/SC2InfoExtractorGo       

options:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR (default = ../processing/sc2_replaypack_processor/output)
                        Please provide input path to the directory containing the dataset that is going to be processed.
```

Please keep in mind that the  ```src/file_packager.py``` contains default flag values and can be customized with the following command line flags:
```
usage: file_packager.py [-h] [--input_dir INPUT_DIR]

Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo      

options:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR (default = ../processing/sc2_replaypack_processor/output)
                        Please provide input path to the directory containing the dataset that is going to be processed by packaging into .zip archives.
```

Please keep in mind that the  ```src/json_merger.py``` contains default flag values and can be customized with the following command line flags:
```
usage: json_merger.py [-h] [--json_one JSON_ONE] [--json_two JSON_TWO] [--output_filepath OUTPUT_FILEPATH]

Tool used for merging two .json files. Created in order to merge two mappings created by
https://github.com/Kaszanas/SC2MapLocaleExtractor

options:
  -h, --help            show this help message and exit
  --json_one JSON_ONE (default = ../processing/json_merger/json1.json)
                    Please provide the path to the first .json file that is going to be merged.
  --json_two JSON_TWO (default = ../processing/json_merger/json2.json)
                    Please provide the path to the second .json file that is going to be merged.
  --output_filepath OUTPUT_FILEPATH (default = ../processing/json_merger/merged.json)
                        Please provide output path where sc2 map files will be downloaded.
```

Please keep in mind that the  ```src/processed_mapping_copier.py``` contains default flag values and can be customized with the following command line flags:
```
usage: processed_mapping_copier.py [-h] [--input_path INPUT_PATH] [--output_path OUTPUT_PATH]

Tool for copying the processed_mapping.json files that are required to define the StarCraft 2 (SC2) dataset.  

options:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH (default = ../processing/directory_flattener/output)
                        Please provide input path to the flattened replaypacks that contain
                        procesed_mapping.json files.
  --output_path OUTPUT_PATH (default = ../processing/sc2_replaypack_processor/output)
                        Please provide output path where processed_mapping.json will be copied.
```


# Citation

```
@software{Białecki_2022_6366039,
  author    = {Białecki, Andrzej and
               Białecki, Piotr and
               Krupiński, Leszek},
  title     = {{Kaszanas/SC2DatasetPreparator: 1.2.0 
               SC2DatasetPreparator Release}},
  month     = {jun},
  year      = {2022},
  publisher = {Zenodo},
  version   = {1.2.0},
  doi       = {10.5281/zenodo.5296664},
  url       = {https://doi.org/10.5281/zenodo.5296664}
}

```
