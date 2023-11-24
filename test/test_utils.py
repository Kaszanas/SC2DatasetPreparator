import os
import logging
from pathlib import Path

TEST_DIR_NAME = "test"


def get_workspace_dir() -> Path:
    """
    Getting path to the workspace where tests are run.
    This function is future proof for testing outsite of local environments.

    Returns
    -------
    Path
        Returns the path to the workspace.
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

    Parameters
    ----------
    script_name : str
        Script name for which the test input dir will be retrieved.

    Returns
    -------
    Path
        Returns an absolute path to the test input directory.
    """
    workspace_dir = get_workspace_dir()
    logging.info(f"Successfully set workspace_dir = {workspace_dir}")

    input_dir = Path(
        workspace_dir, f"{TEST_DIR_NAME}/test_files/{script_name}/input"
    ).resolve()
    logging.info(f"Successfully set input_dir = {input_dir}, returning.")

    return input_dir


def create_test_input_dir(script_name: str) -> Path:
    """
    Creates test input directory for tests.

    Parameters
    ----------
    script_name : str
        Script name for which the test output dir will be created.

    Returns
    -------
    Path
        Returns path to the test input directory.
    """

    workspace_dir = get_workspace_dir()

    input_dir = Path(
        workspace_dir, f"{TEST_DIR_NAME}/test_files/{script_name}/input"
    ).resolve()

    if not input_dir.exists():
        input_dir.mkdir()

    return input_dir


def create_test_output_dir(script_name: str) -> Path:
    """
    Creates test output directories for tests.

    Parameters
    ----------
    script_name : str
        Script name for which the test oput dir will be created.

    Returns
    -------
    Path
        Returns path to the test output directory.
    """

    workspace_dir = get_workspace_dir()
    logging.info(f"Successfully set workspace_dir = {workspace_dir}")

    test_output_path = Path(
        workspace_dir, f"{TEST_DIR_NAME}/test_files/{script_name}/output"
    ).resolve()

    if not test_output_path.exists():
        logging.info(
            f"Detected that output_path does not exist, \
            calling os.mkdir({test_output_path})"
        )
        test_output_path.mkdir()

    return test_output_path


def get_test_output_dir(script_name: str) -> Path:
    """
    Getting the path to the test output directory
    and to the thumbnail output directory.

    Parameters
    ----------
    script_name : str
        Script name for which the test input dir will be retrieved.

    Returns
    -------
    Path
        Paths to the test output directory.
    """

    logging.info(
        "Entered get_output_dir(), calling workspace_dir = get_workspace_dir()"
    )
    workspace_dir = get_workspace_dir()
    logging.info(
        f"Successfully set workspace_dir = {workspace_dir}, returning output_dir = "
    )
    test_output_dir = Path(
        workspace_dir, f"{TEST_DIR_NAME}/test_files/{script_name}/output"
    ).resolve()

    return test_output_dir


def delete_test_output(script_name: str) -> None:
    """
    Deletes output of tests.

    Parameters
    ----------
    script_name : str
        Script name for which the directory will be cleaned.
    """

    test_dir = get_test_output_dir(script_name=script_name)
    logging.info(f"Successfully set {test_dir.as_posix()=}")

    if not test_dir.exists():
        logging.info("Did not detect test_output to exist, exiting function")
        return

    logging.info(
        f"Detected that test_output exists, \
            performing removal by calling shutil.rmtree({test_dir})"
    )
    # shutil.rmtree(test_output)


class AssetError(Exception):
    pass


# TODO:This needs to take into consideration the script name.
def dir_test_create_cleanup(func):
    """
    Decorator that is creating output directories for tests,
    and deletes them along with the output after the tests are finished.
    """

    def wrapper(*args, **kwargs):
        create_test_output_dir()

        try:
            exit_value = func(*args, **kwargs)
        finally:
            logging.info("Deleting output dir in decorator is turned off")
            # delete_test_output_dir()
        return exit_value

    return wrapper