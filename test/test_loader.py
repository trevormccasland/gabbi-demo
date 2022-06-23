import os

# The module that build_tests comes from.
from gabbi import driver

# By convention the YAML files are put in a directory named
# "gabbits" that is in the same directory as the Python test file.
TESTS_DIR = 'gabbits'


def load_tests(loader, tests, pattern):
    """Provide a TestSuite to the discovery process."""
    test_dir = os.path.join(os.path.dirname(__file__), TESTS_DIR)
    # Pass "require_ssl=True" as an argument to force all tests
    # to use SSL in requests.
    return driver.build_tests(test_dir, loader, url='127.0.0.1:3500')
