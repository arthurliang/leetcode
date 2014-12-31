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


    def testmaxDepthWhenRootNodeIsNone(self):
        # arrange

        # act
        actRslt = self.testedobj.maxDepth(None)

        # assert
        self.assertEqual(0, actRslt)


    def testmaxDepthWithOneLevelTree(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.maxDepth(bt.rootnode)

        # assert
        self.assertEqual(1, actRslt)


    def testmaxDepthWithTwoLevelTree(self):
        # arrange
        testdataTrue = "{1,2,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.maxDepth(bt.rootnode)

        # assert
        self.assertEqual(2, actRslt)


    def testmaxDepthWithTwoLevelButLeftIsNullTree(self):
        # arrange
        testdataTrue = "{1,#,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.maxDepth(bt.rootnode)

        # assert
        self.assertEqual(2, actRslt)


    def testmaxDepthWithTwoLevelButRightIsNullTree(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.maxDepth(bt.rootnode)

        # assert
        self.assertEqual(2, actRslt)


    def testmaxDepthWithThreeLevel(self):
        # arrange
        testdataTrue = "{3,9,20,#,#,15,7}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.maxDepth(bt.rootnode)

        # assert
        self.assertEqual(3, actRslt)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()