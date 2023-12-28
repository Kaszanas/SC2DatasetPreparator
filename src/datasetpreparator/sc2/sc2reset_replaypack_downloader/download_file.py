from pathlib import Path
import requests
import tqdm


def download_file(file_url: str, download_filepath: Path, chunk_size: int = 8192):
    with requests.get(url=file_url, stream=True) as response:
        response.raise_for_status()
        total = int(response.headers.get("content-length", 0))

        tqdm_params = {
            "desc": download_filepath.name,
            "total": total,
            "miniters": 1,
            "unit": "B",
            "unit_scale": True,
            "unit_divisor": 1024,
        }

        with download_filepath.open(mode="wb") as output_zip_file:
            with tqdm.tqdm(**tqdm_params) as pb:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    pb.update(len(chunk))
                    output_zip_file.write(chunk)

    return download_filepath
