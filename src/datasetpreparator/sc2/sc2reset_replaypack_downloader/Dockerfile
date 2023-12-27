FROM python:latest

WORKDIR /app

RUN pip install click requests tqdm

COPY . .

CMD ["python3", "sc2reset_replaypack_downloader.py"]
