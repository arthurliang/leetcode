'''
Created on Feb 15, 2015

@author: Arthur
'''
import unittest
import Solution
from utility import CustomList

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.sll = CustomList.SinglyLinkedList()
        self.expsll = CustomList.SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testDeleteDuplicates_TC1(self):
        # arrange
        head = None

        # act
        actHead = self.testedobj.deleteDuplicates(head)

        # assert
        self.assertEqual(head, actHead)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
