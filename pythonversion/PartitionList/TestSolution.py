'''
Created on Feb 12, 2015

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


    def testPartition_TC1(self):
        #arrange
        head = "{}"
        self.sllA.DeserializationOnOJ(head)
        x = 0

        expRslt = "{}"

        #act
        self.sllA.listhead = self.testedobj.partition(self.sllA.listhead, x)

        #assert
        actRslt = self.sllA.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()