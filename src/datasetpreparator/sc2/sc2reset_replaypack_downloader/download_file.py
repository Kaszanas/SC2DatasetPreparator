from pathlib import Path
import requests
import tqdm


def download_file(
    file_url: str, download_filepath: Path, chunk_size: int = 8192
) -> Path:
    """
    Downloads a file from a url and saves it to the specified path by the chunk size.

    Parameters
    ----------
    file_url : str
        Specifies the url from which the file will be downloaded.
    download_filepath : Path
        Specifies the path to which the file will be downloaded.
    chunk_size : int, optional
        Specifies the chunk size in bytes for downloading the file, by default 8192

    Returns
    -------
    Path
        Returns the path to the downloaded file.
    """

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
