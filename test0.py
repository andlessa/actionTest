#!/usr/bin/env python3

"""
.. module:: testAnalysisCombinations
   :synopsis: Tests the combination of SRs between analyses

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>

"""
import sys
import unittest


class myTest(unittest.TestCase):


	# testing Fibonacci number function
	def fib(self,n):
	    return n if n < 2 else self.fib(n-1)+self.fib(n-2)


	def testFibonacci(self):
	    self.assertTrue(self.fib(10) > 54)
	    

if __name__ == "__main__":
    unittest.main()
	    
