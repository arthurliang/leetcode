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
        WrongSum = 0

        # act
        actRslt = self.testedobj.hasPathSum(None, WrongSum)

        # assert
        self.assertEqual(False, actRslt)


    def testHasPathSumWhenRootIsNoneAndSumIs1(self):
        # arrange
        wrongSum = 1

        # act
        actRslt = self.testedobj.hasPathSum(None, wrongSum)

        # assert
        self.assertEqual(False, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisRight(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        rightSum = 1

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, rightSum)

        # assert
        self.assertEqual(True, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()