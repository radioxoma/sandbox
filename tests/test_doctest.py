#!/usr/bin/env python

import sys
import unittest
import doctest
from sandbox import __main__ as main


def suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(main))
    return suite


runner = unittest.TextTestRunner()
result = runner.run(suite())
sys.exit(not result.wasSuccessful())
