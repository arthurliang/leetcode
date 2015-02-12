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
        self.sllA.DeserializationOnOJ(testdata)
        bt = BinTree()

        expRslt = "{}"

        # act
        bt.rootnode = self.testedobj.sortedListToBST(self.sllA.listhead)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()