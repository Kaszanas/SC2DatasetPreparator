FROM python:latest

WORKDIR /app

RUN pip install sc2reader requests

COPY . .

CMD ["python3", "sc2_map_downloader.py"]
