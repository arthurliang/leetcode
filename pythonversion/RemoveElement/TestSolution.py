'''
Created on Jan 26, 2015

@author: Arthur
'''
import unittest
import Solution

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testRemoveElement_TC1(self):
        # arrange
        A = []
        elem = 1
        expLen = 0
        expA = []

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveElement_TC2(self):
        # arrange
        A = [1]
        elem = None
        expLen = 1
        expA = [1]

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveElement_TC3(self):
        # arrange
        A = []
        elem = None
        expLen = 0
        expA = []

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveElement_TC4(self):
        # arrange
        A = [1]
        elem = 1
        expLen = 0

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)


    def testRemoveElement_TC5(self):
        # arrange
        A = [1, 1]
        elem = 1
        expLen = 0

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)


    def testRemoveElement_TC6(self):
        # arrange
        A = [3, 3]
        elem = 5
        expLen = 2
        expA = [3, 3]

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveElement_TC7(self):
        # arrange
        A = [2]
        elem = 3
        expLen = 1
        expA = [2]

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveElement_TC8(self):
        # arrange
        A = [4, 5]
        elem = 4
        expLen = 1

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)


    def testRemoveElement_TC9(self):
        # arrange
        A = [4, 5]
        elem = 5
        expLen = 1

        # act
        actLen = self.testedobj.removeElement(A, elem)

        # assert
        self.assertEqual(expLen, actLen)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
