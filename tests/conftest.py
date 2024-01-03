import os
import sys

import logging


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """

    # Add tests module to path before the tests are run:
    path_to_add = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.environ.get("TEST_WORKSPACE"))
    )
    logging.info(f"Adding tests module to path {path_to_add}")
    sys.path.insert(0, path_to_add)


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """

    path_to_remove = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.environ.get("TEST_WORKSPACE"))
    )

    sys.path.remove(path_to_remove)
    logging.info(f"Removing tests module from path {path_to_remove}")
