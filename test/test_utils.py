import os
import logging
from pathlib import Path
from typing import Dict

TEST_DIR_NAME = "test"


def get_workspace_dir() -> Path:
    """
    Getting path to the workspace where tests are run.
    This function is future proof for testing outsite of local environments.

    :return: Returns string representation of the path \
    to the workspace "ProcessingModule/"
    :rtype: str
    """
    logging.info(
        "Entered get_workspace_dir(), attempting to set \
        workspace_dir = os.environ.get('TEST_WORKSPACE')"
    )

    workspace_dir = Path(os.environ.get("TEST_WORKSPACE")).resolve()
    logging.info(
        f"Successfully set workspace_dir = {workspace_dir}, \
        Attempting to return workspace_dir."
    )
    return workspace_dir


# TODO: This should be creating input directory if it doesn't exist:
# TODO: Additionally, there should be a script that downloads test input files if they are not already available:
def get_test_input_dir(script_name: str) -> Path:
    """
    Getting path to the files required for testing.

    :return: Returns a absoolute path to the test_files dir
    :rtype: Path
    """
    logging.info("Entered get_input_dir(), calling workspace_dir = get_workspace_dir()")
    workspace_dir = get_workspace_dir()
    logging.info(f"Successfully set workspace_dir = {workspace_dir}")

    logging.info(
        f"Attempting to set \
        input_dir = os.path.join(workspace_dir, '{TEST_DIR_NAME}/test_files/{script_name}/output')"
    )
    input_dir = Path(
        workspace_dir, f"{TEST_DIR_NAME}/test_files/{script_name}/input"
    ).resolve()
    logging.info(f"Successfully set input_dir = {input_dir}, returning input_dir")

    return input_dir


def create_test_output_dirs(script_name: str) -> Dict[str, str]:
    """
    Creating output directories for tests

    :return: Returns a dictionary of output directories, \
    example: {video_output_dir, thumbnail_output_dir}
    :rtype: Dict
    """

    workspace_dir = get_workspace_dir()
    logging.info(f"Successfully set workspace_dir = {workspace_dir}")

    test_output_path = os.path.join(
        workspace_dir, f"{TEST_DIR_NAME}/test_files/{script_name}/output"
    )

    if not os.path.exists(test_output_path):
        logging.info(
            f"Detected that output_path does not exist, \
            calling os.mkdir({test_output_path})"
        )
        os.mkdir(test_output_path)

    return {
        "test_output_path": test_output_path,
    }


def get_test_output_dirs(script_name: str) -> Dict[str, str]:
    """
    Getting the paths to the video output directory
    and to the thumbnail output directory.

    :return: Paths to the video output directory and to \
    the thumbnail output directory.
    :rtype: Dict
    """

    logging.info(
        "Entered get_output_dir(), calling workspace_dir = get_workspace_dir()"
    )
    workspace_dir = get_workspace_dir()
    logging.info(
        f"Successfully set workspace_dir = {workspace_dir}, returning output_dir = "
    )
    test_output_dir = os.path.join(
        workspace_dir, f"{TEST_DIR_NAME}/test_files/{script_name}/output"
    )

    return {"test_output_dir": test_output_dir}


def delete_test_output():
    """
    Deleting output of video processing tests.
    """

    test_dirs = get_test_output_dirs()

    test_output = test_dirs["test_output_dir"]
    logging.info(f"Successfully set test_output = {test_output}")

    for _, directory in test_dirs:
        if os.path.exists(directory):
            logging.info(
                f"Detected that test_output exists, \
                performing removal by calling shutil.rmtree({test_output})"
            )
            # shutil.rmtree(test_output)
        else:
            logging.info("Did not detect test_output to exist, exiting function")
            pass


class AssetError(Exception):
    pass


def dir_test_create_cleanup(func):
    """
    Decorator that is creating output directories for tests,
    and deletes them along with the output after the tests are finished.
    """

    def wrapper(*args, **kwargs):
        create_test_output_dirs()

        try:
            exit_value = func(*args, **kwargs)
        finally:
            logging.info("Deleting output dir in decorator is turned off")
            # delete_test_output_dir()

        return exit_value

    return wrapper
