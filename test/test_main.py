# Standard imports:
import unittest
import sys
import os
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Own imports
# import test.test_utils.test_utils as test_utils  # noqa E402


# TODO: Fix this file so that the tests can be run with debugger.
def suite():
    suite = unittest.TestSuite()
    start_dir = os.path.join(test_utils.get_workspace_dir(), "test")
    suite = unittest.TestLoader().discover(
        start_dir=start_dir,
        pattern="*_test.py",  # *_test.py
    )
    return suite


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    print(test_utils.get_workspace_dir())
    my_suite = suite()
    result = unittest.TextTestRunner(verbosity=2).run(my_suite)

    # if result.wasSuccessful():
    #     exit(0)
    # else:
    #     exit(1)
