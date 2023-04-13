#!/usr/bin/env python

import doctest
import pathlib
import sys
import unittest

curdir = pathlib.Path(__file__)
sys.path.append(str(curdir.parent.parent))

from sandbox import __main__ as main


class TestSandbox(unittest.TestCase):
    def test_something(self):
        self.assertTrue(True)


def load_tests(loader: unittest.TestLoader, tests, pattern) -> unittest.TestSuite:
    """Callback to load doctests from modules."""
    tests.addTests(doctest.DocTestSuite(main))
    return tests


if __name__ == "__main__":
    unittest.main()
