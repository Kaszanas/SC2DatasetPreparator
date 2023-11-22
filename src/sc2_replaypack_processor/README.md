# SC2 Replaypack Processor

# CLI Usage

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