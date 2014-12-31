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


    def testSinglyLinkedListDeserializationOnOJforEmptyStr(self):
        # arrange
        srlztn = "{}"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, True)
        self.testSinglyLinkedListIsNullAfterConstruct()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()