'''
Created on Dec 4, 2014

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


    def testlevelOrderForNullTree(self):
        # arrange
        expRst = []

        # act
        actRslt = self.testedobj.levelOrder(None)

        # assert
        self.assertEqual(expRst, actRslt)


    def testlevelOrderForOneLevel(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1]]

        # act
        actRslt = self.testedobj.levelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testlevelOrderForTwoLevel(self):
        # arrange
        testdataTrue = "{1,2,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1],[2,3]]

        # act
        actRslt = self.testedobj.levelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testlevelOrderForTwoLevelWithNullLeft(self):
        # arrange
        testdataTrue = "{1,#,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1],[3]]

        # act
        actRslt = self.testedobj.levelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testlevelOrderForTwoLevelWithNullRight(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1],[2]]

        # act
        actRslt = self.testedobj.levelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testlevelOrderForFullCase(self):
        # arrange
        testdataTrue = "{3,9,20,#,#,15,7}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[3],[9,20],[15,7]]

        # act
        actRslt = self.testedobj.levelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()