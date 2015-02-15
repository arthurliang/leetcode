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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()