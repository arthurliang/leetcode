'''
Created on Feb 12, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.BinTree import BinTree


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testSortedArrayToBST_TC1(self):
        # arrange
        testdata = None
        bt = BinTree()

        expRslt = "{}"

        # act
        bt.rootnode = self.testedobj.sortedArrayToBST(testdata)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedArrayToBST_TC2(self):
        # arrange
        testdata = []
        bt = BinTree()

        expRslt = "{}"

        # act
        bt.rootnode = self.testedobj.sortedArrayToBST(testdata)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedArrayToBST_TC3(self):
        # arrange
        testdata = [1]
        bt = BinTree()

        expRslt = "{1}"

        # act
        bt.rootnode = self.testedobj.sortedArrayToBST(testdata)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedArrayToBST_TC4(self):
        # arrange
        testdata = [1,2]
        bt = BinTree()

        expRslt = "{1,#,2}"

        # act
        bt.rootnode = self.testedobj.sortedArrayToBST(testdata)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedArrayToBST_TC5(self):
        # arrange
        testdata = [1,2,3]
        bt = BinTree()

        expRslt = "{2,1,3}"

        # act
        bt.rootnode = self.testedobj.sortedArrayToBST(testdata)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedArrayToBST_TC6(self):
        # arrange
        testdata = [1,2,3,4]
        bt = BinTree()

        expRslt = "{2,1,3,#,#,#,4}"

        # act
        bt.rootnode = self.testedobj.sortedArrayToBST(testdata)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedArrayToBST_TC7(self):
        # arrange
        testdata = [0,1,2,3,4]
        bt = BinTree()

        expRslt = "{2,0,3,#,1,#,4}"

        # act
        bt.rootnode = self.testedobj.sortedArrayToBST(testdata)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()