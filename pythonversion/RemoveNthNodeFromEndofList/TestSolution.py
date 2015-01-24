'''
Created on Jan 24, 2015

@author: Arthur
'''
import unittest
import Solution
from utility import CustomList

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.sll = CustomList.SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testRemoveNthFromEnd_TC1(self):
        #arrange
        head = None
        n = 0
        expRslt = head

        #act
        actRslt = self.testedobj.removeNthFromEnd(head, n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testRemoveNthFromEnd_TC2(self):
        #arrange
        headoj = "{1}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        n = 0
        expRslt = head

        #act
        actRslt = self.testedobj.removeNthFromEnd(head, n)

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next, None)


    def testRemoveNthFromEnd_TC3(self):
        #arrange
        headoj = "{1}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        n = 1
        expRslt = None

        #act
        actRslt = self.testedobj.removeNthFromEnd(head, n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testRemoveNthFromEnd_TC4(self):
        #arrange
        headoj = "{1, 2}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        n = 1
        expRslt = head

        #act
        actRslt = self.testedobj.removeNthFromEnd(head, n)

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next, None)


    def testRemoveNthFromEnd_TC5(self):
        #arrange
        headoj = "{1, 2}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        n = 2
        expRslt = head.next

        #act
        actRslt = self.testedobj.removeNthFromEnd(head, n)

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(actRslt.val, 2)
        self.assertEqual(actRslt.next, None)


    def testRemoveNthFromEnd_TC6(self):
        #arrange
        headoj = "{1, 2, 3}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        n = 2
        expRslt = head

        #act
        actRslt = self.testedobj.removeNthFromEnd(head, n)

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(actRslt.val, 1)
        self.assertNotEqual(actRslt.next, None)
        self.assertEqual(actRslt.next.val, 3)
        self.assertEqual(actRslt.next.next, None)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
