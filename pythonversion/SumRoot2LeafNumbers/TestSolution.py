'''
Created on Feb 6, 2015

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


    def testSumNumbers_TC1(self):
        # arrange

        # act
        actRslt = self.testedobj.sumNumbers(None)

        # assert
        self.assertEqual(0, actRslt)


    def testSumNumbers_TC2(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = 1

        # act
        actRslt = self.testedobj.sumNumbers(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSumNumbers_TC3(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = 1*10 + 2

        # act
        actRslt = self.testedobj.sumNumbers(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSumNumbers_TC4(self):
        # arrange
        testdataTrue = "{1,#,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = 1*10 + 3

        # act
        actRslt = self.testedobj.sumNumbers(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSumNumbers_TC5(self):
        # arrange
        testdataTrue = "{1,2,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = (1*10 + 2) + (1*10 + 3)

        # act
        actRslt = self.testedobj.sumNumbers(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()