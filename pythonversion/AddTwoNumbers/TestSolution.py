'''
Created on March 1, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.CustomList import SinglyLinkedList

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.sllA = SinglyLinkedList()
        self.sllB = SinglyLinkedList()
        self.sllC = SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testAddTwoNumbers_TC1(self):
        #arrange
        headAoj = "{}"
        headBoj = "{}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)
        self.assertEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllB.listhead, None)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = None

        #act
        actRslt = self.testedobj.addTwoNumbers(l1, l2)

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllB.listhead, None)


    def testAddTwoNumbers_TC2(self):
        #arrange
        headAoj = "{}"
        headBoj = "{1}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)
        self.assertEqual(self.sllA.listhead, None)
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{1}"

        #act
        acthead = self.testedobj.addTwoNumbers(l1, l2)

        #assert
        self.sllC.listhead = acthead
        actRslt = self.sllC.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())


    def testAddTwoNumbers_TC3(self):
        #arrange
        headAoj = "{2}"
        headBoj = "{}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(self.sllB.listhead, None)

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{2}"

        #act
        acthead = self.testedobj.addTwoNumbers(l1, l2)

        #assert
        self.sllC.listhead = acthead
        actRslt = self.sllC.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())


    def testAddTwoNumbers_TC4(self):
        #arrange
        headAoj = "{1}"
        headBoj = "{2}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{3}"

        #act
        acthead = self.testedobj.addTwoNumbers(l1, l2)

        #assert
        self.sllC.listhead = acthead
        actRslt = self.sllC.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())


    def testAddTwoNumbers_TC5(self):
        #arrange
        headAoj = "{1,2}"
        headBoj = "{2,3}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{3,5}"

        #act
        acthead = self.testedobj.addTwoNumbers(l1, l2)

        #assert
        self.sllC.listhead = acthead
        actRslt = self.sllC.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())


    def testAddTwoNumbers_TC6(self):
        #arrange
        headAoj = "{5}"
        headBoj = "{5}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{0,1}"

        #act
        acthead = self.testedobj.addTwoNumbers(l1, l2)

        #assert
        self.sllC.listhead = acthead
        actRslt = self.sllC.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())


    def testAddTwoNumbers_TC7(self):
        #arrange
        headAoj = "{1,5}"
        headBoj = "{2,5}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())

        l1 = self.sllA.listhead
        l2 = self.sllB.listhead
        expRslt = "{3,0,1}"

        #act
        acthead = self.testedobj.addTwoNumbers(l1, l2)

        #assert
        self.sllC.listhead = acthead
        actRslt = self.sllC.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(headAoj, self.sllA.SerializationOnOJ())
        self.assertEqual(headBoj, self.sllB.SerializationOnOJ())


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
