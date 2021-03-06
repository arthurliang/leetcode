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


    def testInorderTraversal_TC1(self):
        # arrange
        expRst = []

        # act
        actRslt = self.testedobj.inorderTraversal(None)

        # assert
        self.assertEqual(expRst, actRslt)


    def testInorderTraversal_TC2(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1]

        # act
        actRslt = self.testedobj.inorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testInorderTraversal_TC3(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [2,1]

        # act
        actRslt = self.testedobj.inorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testInorderTraversal_TC4(self):
        # arrange
        testdataTrue = "{1,#,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1,2]

        # act
        actRslt = self.testedobj.inorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testInorderTraversal_TC5(self):
        # arrange
        testdataTrue = "{1,2,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [2,1,3]

        # act
        actRslt = self.testedobj.inorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testInorderTraversal_TC6(self):
        # arrange
        testdataTrue = "{1,#,2,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1,3,2]

        # act
        actRslt = self.testedobj.inorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testInorderTraversal_TC7(self):
        # arrange
        testdataTrue = "{2,3,#,1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1,3,2]

        # act
        actRslt = self.testedobj.inorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()