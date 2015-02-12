'''
Created on Feb 12, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.BinTree import BinTree
from utility.CustomList import SinglyLinkedList


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.testedobj = Solution.Solution()
        self.sllA = SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        self.sllA.listhead = None
        pass


    def testSortedListToBST_TC1(self):
        # arrange
        testdata = "{}"
        self.assertTrue(self.sllA.DeserializationOnOJ(testdata))
        bt = BinTree()

        expRslt = "{}"

        # act
        bt.rootnode = self.testedobj.sortedListToBST(self.sllA.listhead)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedListToBST_TC2(self):
        # arrange
        testdata = "{1}"
        self.assertTrue(self.sllA.DeserializationOnOJ(testdata))
        bt = BinTree()

        expRslt = "{1}"

        # act
        bt.rootnode = self.testedobj.sortedListToBST(self.sllA.listhead)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedListToBST_TC3(self):
        # arrange
        testdata = "{1,2}"
        self.assertTrue(self.sllA.DeserializationOnOJ(testdata))
        bt = BinTree()

        expRslt = "{2,1}"

        # act
        bt.rootnode = self.testedobj.sortedListToBST(self.sllA.listhead)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedListToBST_TC4(self):
        # arrange
        testdata = "{1,2,3}"
        self.assertTrue(self.sllA.DeserializationOnOJ(testdata))
        bt = BinTree()

        expRslt = "{2,1,3}"

        # act
        bt.rootnode = self.testedobj.sortedListToBST(self.sllA.listhead)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedListToBST_TC5(self):
        # arrange
        testdata = "{1,2,3,4}"
        self.assertTrue(self.sllA.DeserializationOnOJ(testdata))
        bt = BinTree()

        expRslt = "{3,2,4,1}"

        # act
        bt.rootnode = self.testedobj.sortedListToBST(self.sllA.listhead)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortedListToBST_TC6(self):
        # arrange
        testdata = "{0,1,2,3,4}"
        self.assertTrue(self.sllA.DeserializationOnOJ(testdata))
        bt = BinTree()

        expRslt = "{2,1,4,0,#,3}"

        # act
        bt.rootnode = self.testedobj.sortedListToBST(self.sllA.listhead)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()