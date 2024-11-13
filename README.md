[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5296664.svg)](https://doi.org/10.5281/zenodo.5296664)

# DatasetPreparator

Tools in this repository were used to create the **[SC2ReSet: StarCraft II Esport Replaypack Set](https://doi.org/10.5281/zenodo.5575796)**, and finally **[SC2EGSet: StarCraft II Esport Game State Dataset](https://doi.org/10.5281/zenodo.5503997)**, citation information [Cite Us!](#cite-us).

## Installation

Our prefered way of distributing the toolset is through DockerHub. We Use the Docker Image to provide a fully reproducible environment for our scripts.

To build the image please run the following command:

```bash
make docker_build
```

After building the image, please refer to the **[Command Line Arguments Usage](#command-line-arguments-usage)** section for the usage of the scripts.

<!-- To install current version of the toolset as separate CLI tools run the following command:

```
pip install datasetpreparator[all]
```

After that each of the scripts should be available to call from the command line directly. -->

## Command Line Arguments Usage

When using Docker, you will have to pass the arguments through the `docker run` command and mount the input/output directory. Below is an example of how to run the `directory_flattener` script using Docker. For ease of use we have prepared example directory structure in the `processing` directory. The command below uses that to issue a command to flatten the directory structure:

```bash
docker run -v "./processing:/app/processing" datasetpreparator python3 directory_flattener.py --input_path /app/processing/directory_flattener/input --output_path /app/processing/directory_flattener/output
```

### Table of Contents

Each of the scripts has its usage described in their respective `README.md` files, you can find the table of contents below.

#### CLI Usage Generic scripts
1. [Directory Packager (dir_packager): README](src/dir_packager/README.md)
2. [Directory Flattener (directory_flattener): README](src/directory_flattener/README.md)
3. [File Renamer (file_renamer): README](src/file_renamer/README.md)
4. [JSON Merger (json_merger): README](src/json_merger/README.md)
5. [Processed Mapping Copier (processed_mapping_copier): README](src/processed_mapping_copier/README.md)

#### CLI Usage StarCraft 2 Specific Scripts
1. [SC2 Map Downloader (sc2_map_downloader): README](src/sc2/sc2_map_downloader/README.md)
2. [SC2EGSet Replaypack Processor (sc2egset_replaypack_processor): README](src/sc2/sc2egset_replaypack_processor/README.md)
3. [SC2ReSet Replaypack Downloader (sc2reset_replaypack_downloader): README](src/sc2/sc2reset_replaypack_downloader/README.md)

## SC2EGSet Dataset Preparation Steps

To reproduce our experience with defining a dataset and to be able to compare your results with our work we describe how to perform the processing below.

### Using Docker

We provide a release image containing all of the scripts. To see the usage of these scripts please refer to their respective ``README.md`` files as described above.

The following steps were used to prepare the SC2EGSet dataset:
1. Build the docker image from: https://github.com/Kaszanas/SC2InfoExtractorGo
2. Build the docker image for the DatasetPreparator using the provided ```makefile``` command: ```make docker_build```.
3. Place the input replaypacks into `./processing/directory_flattener/` directory.
4. Run the command ```make all``` to process the replaypacks and create the dataset. The output will be placed in `./processing/sc2_replaypack_processor/output` directory.

<!-- ### Using Python

1. Obtain replays to process. This can be a replaypack or your own replay folder.
2. Download latest version of [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo), or build it from source.
3. **Optional** If the replays that you have are held in nested directories it is best to use  ```src/directory_flattener.py```. This will copy the directory and place all of the files to the top directory where it can be further processed. In order to preserve the old directory structure, a .json file is created. The file contains the old directory tree to a mapping: ```{"replayUniqueHash": "whereItWasInOldStructure"}```. This step is is required in order to properly use [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo) as it only lists the files immediately available on the top level of the input directory. [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo).
4. **Optional** Use the map downloader ```src/sc2_map_downloader.py``` to download maps that were used in the replays that you obtained. This is required for the next step.
5. **Optional** Use the [SC2MapLocaleExtractor](https://github.com/Kaszanas/SC2MapLocaleExtractor) to obtain the mapping of ```{"foreign_map_name": "english_map_name"}``` which is required for the [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo) to translate the map names in the output .json files.
6. Perform replaypack processing using ```src/sc2_replaypack_processor.py``` with the [SC2InfoExtractorGo](https://github.com/Kaszanas/SC2InfoExtractorGo) placed in PATH, or next to the script.
7. **Optional** Using the ```src/file_renamer.py```, rename the files that were generated in the previous step. This is not required and is done to increase the readibility of the directory structure for the output.
8. Using the ```src/file_packager.py```, create .zip archives containing the datasets and the supplementary files. By finishing this stage, your dataset should be ready to upload. -->


## Contributing and Reporting Issues

If you want to report a bug, request a feature, or open any other issue, please do so in the **[issue tracker](https://github.com/Kaszanas/SC2DatasetPreparator/issues/new/choose)**.

Please see **[CONTRIBUTING.md](https://github.com/Kaszanas/SC2DatasetPreparator/blob/main/CONTRIBUTING.md)** for detailed development instructions and contribution guidelines.

## Cite Us!

### This Repository

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

### [SC2EGSet: Dataset Description](https://www.researchgate.net/publication/373767449_SC2EGSet_StarCraft_II_Esport_Replay_and_Game-state_Dataset)

```
@article{Bialecki2023_SC2EGSet,
  author   = {Bia{\l}ecki, Andrzej
              and Jakubowska, Natalia
              and Dobrowolski, Pawe{\l}
              and Bia{\l}ecki, Piotr
              and Krupi{\'{n}}ski, Leszek
              and Szczap, Andrzej
              and Bia{\l}ecki, Robert
              and Gajewski, Jan},
  title    = {SC2EGSet: StarCraft II Esport Replay and Game-state Dataset},
  journal  = {Scientific Data},
  year     = {2023},
  month    = {Sep},
  day      = {08},
  volume   = {10},
  number   = {1},
  pages    = {600},
  issn     = {2052-4463},
  doi      = {10.1038/s41597-023-02510-7},
  url      = {https://doi.org/10.1038/s41597-023-02510-7}
}
```
