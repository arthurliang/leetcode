'''
Created on Feb 6, 2015

@author: Arthur
'''
import unittest
import Solution
from utility import BinTree

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testSumNumbers_TC1(self):
        # arrange

        # act
        actRslt = self.testedobj.sumNumbers(None)

        # assert
        self.assertEqual(0, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()