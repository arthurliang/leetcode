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
        self.slltemp = SinglyLinkedList()
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


    def testMergeKLists_TC2(self):
        # arrange
        lists = None
        expRslt = "{}"

        # act
        self.sll.listhead = self.testedobj.mergeKLists(lists)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeKLists_TC3(self):
        # arrange
        lists = []

        testdatas = ["{1}"]
        for item in testdatas:
            self.slltemp.DeserializationOnOJ(item)
            lists.append(self.slltemp.listhead)

        expRslt = "{1}"

        # act
        self.sll.listhead = self.testedobj.mergeKLists(lists)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeKLists_TC4(self):
        # arrange
        lists = []

        testdatas = ["{1}", "{2}"]
        for item in testdatas:
            self.slltemp.DeserializationOnOJ(item)
            lists.append(self.slltemp.listhead)

        expRslt = "{1,2}"

        # act
        self.sll.listhead = self.testedobj.mergeKLists(lists)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeKLists_TC5(self):
        # arrange
        lists = []

        testdatas = ["{1}", "{2}", "{3}"]
        for item in testdatas:
            self.slltemp.DeserializationOnOJ(item)
            lists.append(self.slltemp.listhead)

        expRslt = "{1,2,3}"

        # act
        self.sll.listhead = self.testedobj.mergeKLists(lists)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeKLists_TC6(self):
        # arrange
        lists = []

        testdatas = ["{1,4}", "{2}"]
        for item in testdatas:
            self.slltemp.DeserializationOnOJ(item)
            lists.append(self.slltemp.listhead)

        expRslt = "{1,2,4}"

        # act
        self.sll.listhead = self.testedobj.mergeKLists(lists)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testMergeKLists_TC7(self):
        # arrange
        lists = []

        testdatas = ["{1,4}", "{2,6}", "{3}", "{5}"]
        for item in testdatas:
            self.slltemp.DeserializationOnOJ(item)
            lists.append(self.slltemp.listhead)

        expRslt = "{1,2,3,4,5,6}"

        # act
        self.sll.listhead = self.testedobj.mergeKLists(lists)

        # assert
        actRslt = self.sll.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
