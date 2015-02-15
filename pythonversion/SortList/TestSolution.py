'''
Created on Feb 15, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.CustomList import SinglyLinkedList

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.sllA = SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testSortList_TC1(self):
        #arrange
        expRslt = None

        #act
        actRslt = self.testedobj.sortList(None)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testSortList_TC2(self):
        #arrange
        testData = "{1}"
        self.sllA.DeserializationOnOJ(testData)

        expRslt = "{1}"

        #act
        self.sllA.listhead = self.testedobj.sortList(self.sllA.listhead)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortList_TC3(self):
        #arrange
        testData = "{2,1}"
        self.sllA.DeserializationOnOJ(testData)

        expRslt = "{1,2}"

        #act
        self.sllA.listhead = self.testedobj.sortList(self.sllA.listhead)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortList_TC4(self):
        #arrange
        testData = "{3,2,1}"
        self.sllA.DeserializationOnOJ(testData)

        expRslt = "{1,2,3}"

        #act
        self.sllA.listhead = self.testedobj.sortList(self.sllA.listhead)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortList_TC5(self):
        #arrange
        testData = "{3,2,1,4}"
        self.sllA.DeserializationOnOJ(testData)

        expRslt = "{1,2,3,4}"

        #act
        self.sllA.listhead = self.testedobj.sortList(self.sllA.listhead)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testSortList_TC6(self):
        #arrange
        testData = "{1,2,6,4,5,2,1}"
        self.sllA.DeserializationOnOJ(testData)

        expRslt = "{1,1,2,2,4,5,6}"

        #act
        self.sllA.listhead = self.testedobj.sortList(self.sllA.listhead)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()