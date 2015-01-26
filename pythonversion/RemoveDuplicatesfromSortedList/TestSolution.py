'''
Created on Jan 26, 2015

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
        headoj = "{1,2}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        expheadoj = "{1,2}"

        # act
        self.expsll.listhead = self.testedobj.deleteDuplicates(head)

        # assert
        actheadoj = self.expsll.SerializationOnOJ()
        self.assertEqual(expheadoj, actheadoj)


    def testDeleteDuplicates_TC2(self):
        # arrange
        head = None

        # act
        actHead = self.testedobj.deleteDuplicates(head)

        # assert
        self.assertEqual(head, actHead)


    def testDeleteDuplicates_TC3(self):
        # arrange
        headoj = "{1,1,2}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        expheadoj = "{1,2}"

        # act
        self.expsll.listhead = self.testedobj.deleteDuplicates(head)

        # assert
        actheadoj = self.expsll.SerializationOnOJ()
        self.assertEqual(expheadoj, actheadoj)


    def testDeleteDuplicates_TC4(self):
        # arrange
        headoj = "{1,1,2,3,3}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        expheadoj = "{1,2,3}"

        # act
        self.expsll.listhead = self.testedobj.deleteDuplicates(head)

        # assert
        actheadoj = self.expsll.SerializationOnOJ()
        self.assertEqual(expheadoj, actheadoj)


    def testDeleteDuplicates_TC5(self):
        # arrange
        headoj = "{1}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        expheadoj = "{1}"

        # act
        self.expsll.listhead = self.testedobj.deleteDuplicates(head)

        # assert
        actheadoj = self.expsll.SerializationOnOJ()
        self.assertEqual(expheadoj, actheadoj)


    def testDeleteDuplicates_TC6(self):
        # arrange
        headoj = "{1,1}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        expheadoj = "{1}"

        # act
        self.expsll.listhead = self.testedobj.deleteDuplicates(head)

        # assert
        actheadoj = self.expsll.SerializationOnOJ()
        self.assertEqual(expheadoj, actheadoj)


    def testDeleteDuplicates_TC7(self):
        # arrange
        headoj = "{1,1,1}"
        self.sll.DeserializationOnOJ(headoj)
        self.assertNotEqual(self.sll.listhead, None)

        head = self.sll.listhead
        expheadoj = "{1}"

        # act
        self.expsll.listhead = self.testedobj.deleteDuplicates(head)

        # assert
        actheadoj = self.expsll.SerializationOnOJ()
        self.assertEqual(expheadoj, actheadoj)



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
