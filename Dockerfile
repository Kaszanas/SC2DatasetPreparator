# Built .exe replay parsing tool is required to run sc2_replaypack_processor
# https://github.com/Kaszanas/SC2InfoExtractorGo
FROM sc2-info-extractor

FROM python:3.10-alpine

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
