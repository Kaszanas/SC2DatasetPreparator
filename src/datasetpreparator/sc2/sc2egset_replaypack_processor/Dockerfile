# Built .exe replay parsing tool is required to run sc2_replaypack_processor
# https://github.com/Kaszanas/SC2InfoExtractorGo
FROM sc2-info-extractor

FROM python:3.10-alpine

WORKDIR /sc2_dataset_preparator

# Copying the replay parsing tool:
COPY --from=0 /SC2InfoExtractorGo /SC2InfoExtractorGo

# Installing Python dependencies:
RUN pip install click tqdm

# Copying all Python scripts
COPY . .

WORKDIR /sc2_dataset_preparator/src

CMD ["python3", "sc2egset_replaypack_processor.py"]
