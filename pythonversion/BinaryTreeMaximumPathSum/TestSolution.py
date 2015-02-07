'''
Created on Feb 7, 2015

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


    def testMaxPathSum_TC1(self):
        # arrange
        expRst = 0

        # act
        actRslt = self.testedobj.maxPathSum(None)

        # assert
        self.assertEqual(expRst, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()