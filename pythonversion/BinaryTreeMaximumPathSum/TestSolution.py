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


    def testMaxPathSum_TC1(self):
        # arrange
        expRst = 0

        # act
        actRslt = self.testedobj.maxPathSum(None)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC2(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 1

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC3(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 3

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC4(self):
        # arrange
        testdataTrue = "{2,#,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 5

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC5(self):
        # arrange
        testdataTrue = "{2,1,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 6

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC6(self):
        # arrange
        testdataTrue = "{2,-1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 2

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC7(self):
        # arrange
        testdataTrue = "{-1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 2

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC8(self):
        # arrange
        testdataTrue = "{-1,#,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 2

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC9(self):
        # arrange
        testdataTrue = "{-3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = -3

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC10(self):
        # arrange
        testdataTrue = "{-2,-1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = -1

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC11(self):
        # arrange
        testdataTrue = "{-2,#,-1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = -1

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC12(self):
        # arrange
        testdataTrue = "{-2,-3,-1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = -1

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC13(self):
        # arrange
        testdataTrue = "{-1,-3,-2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = -1

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC14(self):
        # arrange
        testdataTrue = "{-3,-1,-2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = -1

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC15(self):
        # arrange
        testdataTrue = "{1,-2,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 4

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC16(self):
        # arrange
        testdataTrue = "{1,3,-2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 4

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC17(self):
        # arrange
        testdataTrue = "{-2,3,1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 3

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC18(self):
        # arrange
        testdataTrue = "{1,-2,-3,1,3,-2,#,-1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 3

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testMaxPathSum_TC19(self):
        # arrange
        testdataTrue = "{0}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = 0

        # act
        actRslt = self.testedobj.maxPathSum(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()