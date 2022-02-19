[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5296664.svg)](https://doi.org/10.5281/zenodo.5296664)

# SC2DatasetPreparator

This repository contains tools which can be used to create an StarCraft II dataset. The following steps are suggested:

0. Obtain a number of replays to process. This can be a replaypack or your own replay folder.
1. Download latest version of [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo), or build it from source.
2. *Optional* Using ```src/directory_flattener.py``` Flatten the directory structure and save the old directory tree to a mapping: ```{"replayUniqueHash": "whereItWasInOldStructure"}```. This is required in order to properly use the [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo).
3. *Optional* Use the map downloader ```src/sc2_map_downloader.py``` to download maps that were used in the replays that you obtained.
4. *Optional* Use the SC2MapLocaleExtractor to obtain the mapping of ```{"foreign_map_name": "english_map_name"}``` which is required for the [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo) to translate the map names.
5. Perform replaypack processing using ```src/sc2_replaypack_processor.py``` with the [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo) in PATH, or next to the script.
6. *Optional* Using the ```src/file_renamer.py```, rename the files that were generated in step 5.
7. Using the ```src/file_packager.py```, create .zip archives containing the datasets and the supplementary files.

## Customization

In order to specify different processing flags for https://github.com/Kaszanas/SC2InfoExtractorGo please modify the ```src/sc2_replaypack_processor``` file directly

## Usage

Before using this software please install Python >= 3.7 and ```requirements.txt```.

Please keep in mind that ```src/directory_flattener.py``` does not contain default flag values and can be customized with the following command line flags:

```
usage: directory_flattener.py [-h] [--input_path INPUT_PATH]
                              [--file_extension FILE_EXTENSION]

Directory restructuring tool used in order to flatten the structure, map the
old structure to a separate file, and for later processing with other tools.

optional arguments:
  -h, --help            show this help message and exit
  --input_path INPUT_PATH
                        Please provide input path to the dataset that is going
                        to be processed.
  --file_extension FILE_EXTENSION
                        Please provide a file extension for files that will be
                        moved and renamed.
```


Please keep in mind that the  ```src/sc2_replaypack_processor.py``` does not contain default flag values and can be customized with the following command line flags:

```
Tool used for processing SC2 datasets. with
https://github.com/Kaszanas/SC2InfoExtractorGo

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        Please provide input path to the directory containing
                        the dataset that is going to be processed.
  --output_dir OUTPUT_DIR
                        Please provide an output directory for the resulting
                        files.
  --n_processes N_PROCESSES
                        Please provide the number of processes to be spawn for
                        the dataset processing.
```

# Citation

```
@software{Bialecki_2021_5296664,
  author       = {Białecki, Andrzej},
  title        = {{Kaszanas/SC2DatasetPreparator: 1.0.0 
                   SC2DatasetPreparator Release}},
  month        = aug,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.5296664},
  url          = {https://doi.org/10.5281/zenodo.5296664}
}
```
