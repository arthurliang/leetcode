'''
Created on Dec 13, 2014

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
        self.testedobj = None
        pass


    def testminDepthWhenRootNodeIsNone(self):
        # arrange

        # act
        actRslt = self.testedobj.minDepth(None)

        # assert
        self.assertEqual(0, actRslt)


    def testminDepthWithOneLevelTree(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.minDepth(bt.rootnode)

        # assert
        self.assertEqual(1, actRslt)


    def testminDepthWithTwoLevelButLeftIsNullTree(self):
        # arrange
        testdataTrue = "{1,#,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.minDepth(bt.rootnode)

        # assert
        self.assertEqual(2, actRslt)


    def testminDepthWithTwoLevelButRightIsNullTree(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.minDepth(bt.rootnode)

        # assert
        self.assertEqual(2, actRslt)


    def testminDepthWithTwoLevelTree(self):
        # arrange
        testdataTrue = "{1,2,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.minDepth(bt.rootnode)

        # assert
        self.assertEqual(2, actRslt)


    def testminDepthWithThreeLevel(self):
        # arrange
        testdataTrue = "{3,9,20,15,7,2,30}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.minDepth(bt.rootnode)

        # assert
        self.assertEqual(3, actRslt)


    def testminDepthWithThreeLevelNotFull(self):
        # arrange
        testdataTrue = "{3,9,20,#,#,15,7}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.minDepth(bt.rootnode)

        # assert
        self.assertEqual(2, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()