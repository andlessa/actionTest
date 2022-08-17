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
    unittest.TextTestRunner().run( unittest.TestLoader().discover("./") )

if __name__ == "__main__":
    run()
