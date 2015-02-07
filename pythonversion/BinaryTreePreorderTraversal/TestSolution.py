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


    def testPreorderTraversal_TC1(self):
        # arrange
        expRst = []

        # act
        actRslt = self.testedobj.preorderTraversal(None)

        # assert
        self.assertEqual(expRst, actRslt)


    def testPreorderTraversal_TC2(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1]

        # act
        actRslt = self.testedobj.preorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testPreorderTraversal_TC3(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1,2]

        # act
        actRslt = self.testedobj.preorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testPreorderTraversal_TC4(self):
        # arrange
        testdataTrue = "{1,#,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1,2]

        # act
        actRslt = self.testedobj.preorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testPreorderTraversal_TC5(self):
        # arrange
        testdataTrue = "{1,2,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1,2,3]

        # act
        actRslt = self.testedobj.preorderTraversal(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()