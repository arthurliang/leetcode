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
        self.testedobj = None
        pass


    def testIsSameTreeWhen2NoneTree(self):
        # arrange

        # act
        actRslt = self.testedobj.isSameTree(None, None)

        # assert
        self.assertEqual(True, actRslt)


    def testIsSameTreeWhen1NoneTreeAsLeftPara(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isSameTree(None, bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


    def testIsSameTreeWhen1NoneTreeAsRightPara(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isSameTree(bt.rootnode, None)

        # assert
        self.assertEqual(False, actRslt)


    def testIsSameTreeWhen2BinaryTreeNotNone(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isSameTree(bt.rootnode, bt.rootnode)

        # assert
        self.assertEqual(True, actRslt)


    def testIsSameTreeWhen2BinaryTreeNotNoneWithSameLeftSubTree(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isSameTree(bt.rootnode, bt.rootnode)

        # assert
        self.assertEqual(True, actRslt)


    def testIsSameTreeWhen2BinaryTreeNotNoneWithSameRightSubTree(self):
        # arrange
        testdataTrue = "{1,#,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isSameTree(bt.rootnode, bt.rootnode)

        # assert
        self.assertEqual(True, actRslt)


    def testIsSameTreeWhen2BinaryTreeNotNoneWithDifferentLeftRightSubTree(self):
        # arrange
        testdataTrue = "{1,2}"
        btwlt = BinTree.BinTree()
        btwlt.DeserializationOnOJ(testdataTrue)
        testdataTrue = "{1,#,2}"
        btwrt = BinTree.BinTree()
        btwrt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isSameTree(btwlt.rootnode, btwrt.rootnode)

        # assert
        self.assertEqual(False, actRslt)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()