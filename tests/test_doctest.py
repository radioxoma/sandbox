#!/usr/bin/env python

import sys
import unittest
import doctest
from sandbox import __main__


def suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(__main__))
    return suite


runner = unittest.TextTestRunner()
result = runner.run(suite())
sys.exit(not result.wasSuccessful())
