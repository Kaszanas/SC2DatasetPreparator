
PWD := ${CURDIR}

all: flatten json_merge process_replaypack rename_files package_dataset

flatten: ## Flattens the directory if the files are held in nested directories. This helps with streamlining the processing.
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 directory_flattener.py

json_merge: ## Merges two JSON files.
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 json_merger.py \
		--json_one=../processing/json_merger/map_translation.json \
		--json_two=../processing/json_merger/new_maps_processed.json

download_maps: ## Runs over directories with .SC2Replay files and downloads maps that were used in the games.
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 sc2_map_downloader.py

process_replaypack: ## Parses the raw (.SC2Replay) data into JSON files.
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 sc2_replaypack_processor.py \
		--n_processes 8 \
		--perform_chat_anonymization "true"

rename_files: ## Renames the files after processing with SC2InfoExtractorGo.
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 file_renamer.py \
		--input_dir ../processing/sc2_replaypack_processor/output

package_reset_dataset: ## Packages the raw data. Used to prepare SC2ReSet Replaypack set.
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 file_packager.py --input_dir ../processing/directory_flattener/output

package_dataset: ## Packages the pre-processed dataset from the output of sc2_dataset_preparator. Used to prepare SC2EGSet Dataset.
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 file_packager.py --input_dir ../processing/sc2_replaypack_processor/output

build: ## Builds the image containing all of the tools.
	docker build . --tag=sc2_dataset_preparator

.PHONY: help
help: ## Show available make targets
	@awk '/^[^\t ]*:.*?##/{sub(/:.*?##/, ""); printf "\033[36m%-30s\033[0m %s\n", $$1, substr($$0, index($$0,$$2))}' $(MAKEFILE_LIST)
