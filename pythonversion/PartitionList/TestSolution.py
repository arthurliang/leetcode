'''
Created on Feb 12, 2015

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


    def testPartition_TC1(self):
        #arrange
        head = "{}"
        self.sllA.DeserializationOnOJ(head)
        x = 0

        expRslt = "{}"

        #act
        self.sllA.listhead = self.testedobj.partition(self.sllA.listhead, x)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testPartition_TC2(self):
        #arrange
        head = "{1}"
        self.sllA.DeserializationOnOJ(head)
        x = 0

        expRslt = "{1}"

        #act
        self.sllA.listhead = self.testedobj.partition(self.sllA.listhead, x)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testPartition_TC3(self):
        #arrange
        head = "{2,1}"
        self.sllA.DeserializationOnOJ(head)
        x = 0

        expRslt = "{2,1}"

        #act
        self.sllA.listhead = self.testedobj.partition(self.sllA.listhead, x)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testPartition_TC4(self):
        #arrange
        head = "{2,1}"
        self.sllA.DeserializationOnOJ(head)
        x = 1

        expRslt = "{2,1}"

        #act
        self.sllA.listhead = self.testedobj.partition(self.sllA.listhead, x)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testPartition_TC5(self):
        #arrange
        head = "{2,1}"
        self.sllA.DeserializationOnOJ(head)
        x = 2

        expRslt = "{1,2}"

        #act
        self.sllA.listhead = self.testedobj.partition(self.sllA.listhead, x)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testPartition_TC6(self):
        #arrange
        head = "{2,1}"
        self.sllA.DeserializationOnOJ(head)
        x = 3

        expRslt = "{2,1}"

        #act
        self.sllA.listhead = self.testedobj.partition(self.sllA.listhead, x)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testPartition_TC7(self):
        #arrange
        head = "{1,4,3,2,5,2}"
        self.sllA.DeserializationOnOJ(head)
        x = 3

        expRslt = "{1,2,2,4,3,5}"

        #act
        self.sllA.listhead = self.testedobj.partition(self.sllA.listhead, x)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()