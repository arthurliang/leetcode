'''
Created on Dec 14, 2014

@author: Arthur
'''
import unittest
import Solution
import BinTree

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        pass


    def testHasPathSumWhenRootIsNoneAndSumIs0(self):
        # arrange

        # act
        actRslt = self.testedobj.hasPathSum(None, 0)

        # assert
        self.assertEqual(True, actRslt)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()