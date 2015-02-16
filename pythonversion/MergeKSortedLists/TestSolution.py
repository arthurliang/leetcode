'''
Created on Feb 16, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.CustomList import SinglyLinkedList

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.sll = SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testMergeKLists_TC1(self):
        # arrange
        lists = []
        expRslt = "{}"

        # act
        self.sll.listhead = self.testedobj.mergeKLists(lists)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
