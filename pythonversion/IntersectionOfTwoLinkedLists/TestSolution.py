'''
Created on Dec 24, 2014

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
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testGetIntersectionNodeWillReturnNoneWhen2ListAreNone(self):
        #arrange
        headAoj = "{}"
        headBoj = "{}"

        self.sllA.DeserializationOnOJ(headAoj)
        self.sllB.DeserializationOnOJ(headBoj)
        self.assertEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllB.listhead, None)

        headA = self.sllA.listhead
        headB = self.sllB.listhead
        expRslt = None

        #act
        actRslt = self.testedobj.getIntersectionNode(headA, headB)

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllB.listhead, None)


    def testGetIntersectionNodeWillReturnRealValWhen2ListHasSameLength(self):
        #arrange
        headAoj = "{1}"
        self.sllA.DeserializationOnOJ(headAoj)

        # headBoj = "{1}"
        self.sllB.listhead = self.sllA.listhead

        self.assertNotEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllA.listhead.val, 1)
        self.assertEqual(self.sllA.listhead.next, None)
        self.assertNotEqual(self.sllB.listhead, None)
        self.assertEqual(self.sllB.listhead.val, 1)
        self.assertEqual(self.sllB.listhead.next, None)

        headA = self.sllA.listhead
        headB = self.sllB.listhead
        expRslt = self.sllA.listhead

        #act
        actRslt = self.testedobj.getIntersectionNode(headA, headB)

        #assert
        self.assertEqual(expRslt, actRslt)

        self.assertNotEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllA.listhead.val, 1)
        self.assertNotEqual(self.sllB.listhead, None)
        self.assertEqual(self.sllB.listhead.val, 1)


    def testGetIntersectionNodeWillReturnRealValWhenALongerThanB(self):
        #arrange
        headAoj = "{1,2}"
        self.sllA.DeserializationOnOJ(headAoj)

        # headBoj = "{2}"
        self.sllB.listhead = self.sllA.listhead.next

        self.assertNotEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllA.listhead.val, 1)
        self.assertNotEqual(self.sllA.listhead.next, None)
        self.assertEqual(self.sllA.listhead.next.val, 2)
        self.assertEqual(self.sllA.listhead.next.next, None)

        self.assertNotEqual(self.sllB.listhead, None)
        self.assertEqual(self.sllB.listhead.val, 2)
        self.assertEqual(self.sllB.listhead.next, None)

        headA = self.sllA.listhead
        headB = self.sllB.listhead
        expRslt = self.sllB.listhead

        #act
        actRslt = self.testedobj.getIntersectionNode(headA, headB)

        #assert
        self.assertEqual(expRslt, actRslt)

        self.assertNotEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllA.listhead.val, 1)
        self.assertNotEqual(self.sllA.listhead.next, None)
        self.assertEqual(self.sllA.listhead.next.val, 2)
        self.assertEqual(self.sllA.listhead.next.next, None)

        self.assertNotEqual(self.sllB.listhead, None)
        self.assertEqual(self.sllB.listhead.val, 2)
        self.assertEqual(self.sllB.listhead.next, None)


    def testGetIntersectionNodeWillReturnRealValWhenBLongerThanA(self):
        #arrange
        headBoj = "{1,2}"
        self.sllB.DeserializationOnOJ(headBoj)


        # headAoj = "{2}"
        self.sllA.listhead = self.sllB.listhead.next

        self.assertNotEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllA.listhead.val, 2)
        self.assertEqual(self.sllA.listhead.next, None)

        self.assertNotEqual(self.sllB.listhead, None)
        self.assertEqual(self.sllB.listhead.val, 1)
        self.assertNotEqual(self.sllB.listhead.next, None)
        self.assertEqual(self.sllB.listhead.next.val, 2)
        self.assertEqual(self.sllB.listhead.next.next, None)

        headA = self.sllA.listhead
        headB = self.sllB.listhead
        expRslt = self.sllA.listhead

        #act
        actRslt = self.testedobj.getIntersectionNode(headA, headB)

        #assert
        self.assertEqual(expRslt, actRslt)

        self.assertNotEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllA.listhead.val, 2)
        self.assertEqual(self.sllA.listhead.next, None)

        self.assertNotEqual(self.sllB.listhead, None)
        self.assertEqual(self.sllB.listhead.val, 1)
        self.assertNotEqual(self.sllB.listhead.next, None)
        self.assertEqual(self.sllB.listhead.next.val, 2)
        self.assertEqual(self.sllB.listhead.next.next, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()