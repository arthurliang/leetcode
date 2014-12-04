'''
Created on Nov 16, 2014

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


    def testIsSymmetricWithFalseWhenRootNodeIsNone(self):
        # arrange

        # act
        actRslt = self.testedobj.isSymmetric(None)

        # assert
        self.assertEqual(True, actRslt)


    def testIsSymmetricWithTrueWhenBinTreeJustHasARootNode(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isSymmetric(bt.rootnode)

        # assert
        self.assertEqual(True, actRslt)


    def testIsSymmetricWithFalseWhenLeftRightValDifferent(self):
        # arrange
        testdataFalse = "{1,2,1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataFalse)

        # act
        actRslt = self.testedobj.isSymmetric(bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


    def testIsSymmetricWithFalseWhenLeftIsNotNullButRightIsNull(self):
        # arrange
        testdataFalse = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataFalse)

        # act
        actRslt = self.testedobj.isSymmetric(bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


    def testIsSymmetricWithFalseWhenLeftIsNullButRightIsNotNull(self):
        # arrange
        testdataFalse = "{1,#,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataFalse)

        # act
        actRslt = self.testedobj.isSymmetric(bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


    def testIsSymmetricWithFalseWhenLeftTreeIsDeeperThanRightTree(self):
        # arrange
        testdataFalse = "{1,2,2,#,#,4,#,#,5}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataFalse)

        # act
        actRslt = self.testedobj.isSymmetric(bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


    def testIsSymmetricWithFalse(self):
        # arrange
        testdataFalse = "{1,2,2,#,3,#,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataFalse)

        # act
        actRslt = self.testedobj.isSymmetric(bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


    def testIsSymmetricWithTrue(self):
        # arrange
        testdataTrue = "{1,2,2,3,4,4,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isSymmetric(bt.rootnode)

        # assert
        self.assertEqual(True, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()