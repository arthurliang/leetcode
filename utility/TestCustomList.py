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


    def testSinglyLinkedListDeserializationOnOJforSimpleCase(self):
        # arrange
        srlztn = "{1,2}"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, True)

        self.assertNotEqual(self.testedobj.listhead, None)
        self.assertEqual(self.testedobj.listhead.val, 1)

        self.assertNotEqual(self.testedobj.listhead.next, None)
        self.assertEqual(self.testedobj.listhead.next.val, 2)
        self.assertEqual(self.testedobj.listhead.next.next, None)


    def testSinglyLinkedListSerializationOnOJforNullList(self):
        # arrange
        expSrlztn = "{}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSinglyLinkedListSerializationOnOJforSimpleCase(self):
        # arrange
        expSrlztn = "{1,2}"
        rulst = self.testedobj.DeserializationOnOJ(expSrlztn)
        self.assertEqual(rulst, True)

        # act
        actSrlztn = self.testedobj.SerializationOnOJ()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()