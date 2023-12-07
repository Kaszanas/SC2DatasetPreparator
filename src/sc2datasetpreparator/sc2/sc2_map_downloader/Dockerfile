FROM python:latest

WORKDIR /app

RUN pip install click requests sc2reader 

COPY . .

CMD ["python3", "sc2_map_downloader.py"]
