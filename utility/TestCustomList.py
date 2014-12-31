'''
Created on Dec 24, 2014

@author: Arthur
'''
import unittest
import CustomList


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = CustomList.SinglyLinkedList()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testSinglyLinkedListIsNullAfterConstruct(self):
        self.assertEqual(self.testedobj.listhead, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()