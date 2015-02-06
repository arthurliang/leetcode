'''
Created on Feb 6, 2015

@author: Arthur
'''
import unittest
import Solution
from utility import CustomList

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.sllA = CustomList.SinglyLinkedList()
        self.sllB = CustomList.SinglyLinkedList()
        self.sllN = CustomList.SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testMergeTwoLists_TC1(self):
        #arrange
        headAoj = "{}"
        headBoj = "{}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeTwoLists_TC2(self):
        #arrange
        headAoj = "{}"
        headBoj = "{0}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeTwoLists_TC3(self):
        #arrange
        headAoj = "{0}"
        headBoj = "{}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeTwoLists_TC4(self):
        #arrange
        headAoj = "{0}"
        headBoj = "{1}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0,1}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeTwoLists_TC5(self):
        #arrange
        headAoj = "{1}"
        headBoj = "{0}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0,1}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeTwoLists_TC6(self):
        #arrange
        headAoj = "{0,2}"
        headBoj = "{1}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0,1,2}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeTwoLists_TC7(self):
        #arrange
        headAoj = "{0,1}"
        headBoj = "{2}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0,1,2}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeTwoLists_TC8(self):
        #arrange
        headAoj = "{0,1}"
        headBoj = "{1}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0,1,1}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeTwoLists_TC9(self):
        #arrange
        headAoj = "{0,1,4}"
        headBoj = "{1,2,3}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0,1,1,2,3,4}"

        #act
        newHead = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.sllN.listhead = newHead
        actRslt = self.sllN.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()