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
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testMergeTwoLists(self):
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
        actRslt = self.testedobj.mergeTwoLists(l1, l2)

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(self.sllA.listhead, None)
        self.assertEqual(self.sllB.listhead, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()