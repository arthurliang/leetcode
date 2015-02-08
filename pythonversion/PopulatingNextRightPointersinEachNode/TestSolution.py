'''
Created on Feb 8, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.BinTree import BinTree


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testConnect_TC1(self):
        # arrange

        # act
        self.testedobj.connect(None)

        # assert


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()