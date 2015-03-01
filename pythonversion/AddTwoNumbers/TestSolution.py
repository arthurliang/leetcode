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


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
