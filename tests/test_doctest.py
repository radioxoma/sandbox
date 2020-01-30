#!/usr/bin/env python

import unittest
import doctest
from sandbox import __main__


def suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(__main__))
    return suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite())
