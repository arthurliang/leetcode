'''
Created on Feb 16, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.CustomList import SinglyLinkedList

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.sll = SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testInsertionSortList_TC1(self):
        # arrange
        testdata = "{}"
        self.sll.DeserializationOnOJ(testdata)
        expRslt = "{}"

        # act
        self.sll.listhead = self.testedobj.insertionSortList(self.sll.listhead)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertionSortList_TC2(self):
        # arrange
        testdata = "{1}"
        self.sll.DeserializationOnOJ(testdata)
        expRslt = "{1}"

        # act
        self.sll.listhead = self.testedobj.insertionSortList(self.sll.listhead)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertionSortList_TC3(self):
        # arrange
        testdata = "{2,1}"
        self.sll.DeserializationOnOJ(testdata)
        expRslt = "{1,2}"

        # act
        self.sll.listhead = self.testedobj.insertionSortList(self.sll.listhead)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertionSortList_TC4(self):
        # arrange
        testdata = "{3,2,1}"
        self.sll.DeserializationOnOJ(testdata)
        expRslt = "{1,2,3}"

        # act
        self.sll.listhead = self.testedobj.insertionSortList(self.sll.listhead)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertionSortList_TC5(self):
        # arrange
        testdata = "{1,1}"
        self.sll.DeserializationOnOJ(testdata)
        expRslt = "{1,1}"

        # act
        self.sll.listhead = self.testedobj.insertionSortList(self.sll.listhead)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertionSortList_TC6(self):
        # arrange
        testdata = "{3,2,4}"
        self.sll.DeserializationOnOJ(testdata)
        expRslt = "{2,3,4}"

        # act
        self.sll.listhead = self.testedobj.insertionSortList(self.sll.listhead)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)




if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
