'''
Created on Feb 15, 2015

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


    def testRemoveDuplicates_TC1(self):
        # arrange
        A = [1, 1, 2]
        expLen = 3
        expA = [1, 1, 2]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveDuplicates_TC2(self):
        # arrange
        A = []
        expLen = 0
        expA = []

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveDuplicates_TC3(self):
        # arrange
        A = [1, 1]
        expLen = 2
        expA = [1, 1]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveDuplicates_TC4(self):
        # arrange
        A = [1,1,1]
        expLen = 2
        expA = [1,1,1]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveDuplicates_TC5(self):
        # arrange
        A = [1]
        expLen = 1
        expA = [1]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveDuplicates_TC6(self):
        # arrange
        A = [1,1,1,2,2,3]
        expLen = 5
        expA = [1,1,2,2,3,3]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveDuplicates_TC7(self):
        # arrange
        A = [1,2,2]
        expLen = 3
        expA = [1,2,2]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveDuplicates_TC8(self):
        # arrange
        A = [1,1,1,1,3,3]
        expLen = 4
        expA = [1,1,3,3,3,3]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


    def testRemoveDuplicates_TC9(self):
        # arrange
        A = [1,1,1,1,2,2,3]
        expLen = 5
        expA = [1,1,2,2,3,2,3]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
