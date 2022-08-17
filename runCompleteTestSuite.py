#!/usr/bin/env python3

"""
.. module:: runCompleteTestSuite
   :synopsis: Runs all test suites.

.. moduleauthor:: Wolfgang Magerl <wolfgang.magerl@gmail.com>
.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>

"""

from __future__ import print_function
import sys
import unittest

def run():
    allTests = unittest.TestLoader().discover("./")
    r = unittest.TextTestRunner()
    r.shouldStop = True
    ret = r.run(allTests)
    if not ret.wasSuccessful():
        raise AssertionError("%i tests failed" %len(ret.failures))

if __name__ == "__main__":
    run()
