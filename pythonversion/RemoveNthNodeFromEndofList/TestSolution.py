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


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
