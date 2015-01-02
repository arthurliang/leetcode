'''
Created on Dec 14, 2014

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


    def testHasPathSumWhenRootIsNotNoneAndSumisRightTC1(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        rightSum = 1

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, rightSum)

        # assert
        self.assertEqual(True, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisWrongTC1(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        wrongSum = 2

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, wrongSum)

        # assert
        self.assertEqual(False, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisRightTC2(self):
        # arrange
        testdataTrue = "{2,1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        rightSum = 3

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, rightSum)

        # assert
        self.assertEqual(True, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisWrongTC2_1(self):
        # arrange
        testdataTrue = "{2,1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        wrongSum = 2

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, wrongSum)

        # assert
        self.assertEqual(False, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisWrongTC2_2(self):
        # arrange
        testdataTrue = "{2,1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        wrongSum = 1

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, wrongSum)

        # assert
        self.assertEqual(False, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisWrongTC2_3(self):
        # arrange
        testdataTrue = "{2,1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        wrongSum = 4

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, wrongSum)

        # assert
        self.assertEqual(False, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisRightTC3(self):
        # arrange
        testdataTrue = "{-2,#,-3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        rightSum = -5

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, rightSum)

        # assert
        self.assertEqual(True, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisWrongTC3_1(self):
        # arrange
        testdataTrue = "{-2,#,-3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        wrongSum = -1

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, wrongSum)

        # assert
        self.assertEqual(False, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisWrongTC3_2(self):
        # arrange
        testdataTrue = "{-2,#,-3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        wrongSum = -2

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, wrongSum)

        # assert
        self.assertEqual(False, actRslt)


    def testHasPathSumWhenRootIsNotNoneAndSumisWrongTC3_3(self):
        # arrange
        testdataTrue = "{-2,#,-3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        wrongSum = -3

        # act
        actRslt = self.testedobj.hasPathSum(bt.rootnode, wrongSum)

        # assert
        self.assertEqual(False, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()