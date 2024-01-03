# Built .exe replay parsing tool is required to run sc2_replaypack_processor
# https://github.com/Kaszanas/SC2InfoExtractorGo

ARG PYTHON_VERSION=3.11

# TODO: This should be on DockerHub:
FROM kaszanas/sc2infoextractorgo:latest

FROM python:${PYTHON_VERSION}-alpine

WORKDIR /app

# Copying the replay parsing tool:
COPY --from=0 /SC2InfoExtractorGo /SC2InfoExtractorGo

# Copy only what is required to install the project:
COPY pyproject.toml poetry.lock /app/

# Install only dependencies without installing current project:
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy entire repository contents
COPY . .

# Install current project:
RUN poetry install --all-extras
