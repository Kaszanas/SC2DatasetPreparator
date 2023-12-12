# Built .exe replay parsing tool is required to run sc2_replaypack_processor
# https://github.com/Kaszanas/SC2InfoExtractorGo

ARG PYTHON_VERSION=3.11

# TODO: This should be on DockerHub:
FROM sc2-info-extractor

FROM python:${PYTHON_VERSION}-alpine

RUN mkdir /sc2-dataset-preparator

WORKDIR /sc2-dataset-preparator

# Copying the replay parsing tool:
COPY --from=0 /SC2InfoExtractorGo /SC2InfoExtractorGo

# Installing Python dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copying all Python scripts
COPY . .

WORKDIR /sc2-dataset-preparator/src


CMD ["python3", "sc2_replaypack_processor.py"]
