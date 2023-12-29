PYTHON_VERSION = 3.11
PWD := ${CURDIR}


###################
#### PIPELINE #####
###################
all: ## Runs the entire processing pipeline to recreate SC2ReSet and SC2EGSet or any other dataset using our standard tooling.
	@make flatten
	@make json_merge
	@make process_replaypack
	@make rename_files
	@make package_dataset

# TODO: Image name changed from sc2_dataset_preparator to datasetpreparator.
flatten: ## Flattens the directory if the files are held in nested directories. This helps with streamlining the processing.
	docker run \
		-v "${PWD}/processing:/app/processing" \
		sc2_dataset_preparator \
		python3 directory_flattener.py

json_merge: ## Merges two JSON files.
	docker run \
		-v "${PWD}/processing:/app/processing" \
		sc2-dataset-preparator \
		python3 json_merger.py \
		--json_one=../processing/json_merger/map_translation.json \
		--json_two=../processing/json_merger/new_maps_processed.json

download_maps: ## Runs over directories with .SC2Replay files and downloads maps that were used in the games.
	docker run \
		-v "${PWD}/processing:/app/processing" \
		sc2_dataset_preparator \
		python3 sc2_map_downloader.py

process_replaypack: ## Parses the raw (.SC2Replay) data into JSON files.
	docker run \
		-v "${PWD}/processing:/app/processing" \
		sc2_dataset_preparator \
		python3 sc2_replaypack_processor.py \
		--n_processes 8 \
		--perform_chat_anonymization "true"

rename_files: ## Renames the files after processing with SC2InfoExtractorGo.
	docker run \
		-v "${PWD}/processing:/app/processing" \
		sc2_dataset_preparator \
		python3 file_renamer.py \
		--input_dir ../processing/sc2_replaypack_processor/output

package_reset_dataset: ## Packages the raw data. Used to prepare SC2ReSet Replaypack set.
	docker run \
		-v "${PWD}/processing:/app/processing" \
		sc2_dataset_preparator \
		python3 file_packager.py --input_dir ../processing/directory_flattener/output

package_dataset: ## Packages the pre-processed dataset from the output of sc2_dataset_preparator. Used to prepare SC2EGSet Dataset.
	docker run \
		-v "${PWD}/processing:/app/processing" \
		sc2_dataset_preparator \
		python3 file_packager.py --input_dir ../processing/sc2_replaypack_processor/output

###################
#### DOCKER #######
###################
build: ## Builds the image containing all of the tools.
	docker build \
	--build-arg="PYTHON_VERSION=$(PYTHON_VERSION)" \
	-f ./docker/Dockerfile . \
	--tag=datasetpreparator

build_dev: ## Builds the development image containing all of the tools.
	docker build \
	--build-arg="PYTHON_VERSION=$(PYTHON_VERSION)" \
	-f ./docker/Dockerfile.dev . \
	--tag=datasetpreparator:devcontainer

###################
#### DOCS #########
###################
doc_serve: ## Serves the Mkdocs documentation locally.
	poetry run mkdocs serve

doc_build: ## Builds the Mkdocs documentation.
	poetry run mkdocs build

docker_doc_build: ## Builds the Mkdocs documentation using Docker.
	docker run \
		-v "${PWD}/docs:/docs" \
		datasetpreparator:devcontainer \
		poetry run mkdocs build

###################
#### PRE-COMMIT ###
###################
# TODO: This requires the image to be rebuilt every time anything is changed in code.
# There should be a way of running this with a mounted volume on the current directory.
docker_pre_commit: ## Runs pre-commit hooks using Docker.
	docker run \
		-v "${PWD}:/app" \
		sc2_dataset_preparator:devcontainer \
		pre-commit run --all-files


.PHONY: help
help: ## Show available make targets
	@awk '/^[^\t ]*:.*?##/{sub(/:.*?##/, ""); printf "\033[36m%-30s\033[0m %s\n", $$1, substr($$0, index($$0,$$2))}' $(MAKEFILE_LIST)
