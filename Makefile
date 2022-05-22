
PWD := `pwd`

all: download_maps flatten process_replaypack

flatten:
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 directory_flattener.py

json_merge:
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 json_merger.py

download_maps:
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 sc2_map_downloader.py

process_replaypack:
	docker run \
		-v "${PWD}/processing:/sc2-dataset-preparator/processing" \
		sc2-dataset-preparator \
		python3 sc2_replaypack_processor.py

build:
	docker build . -t sc2-dataset-preparator
