'''
Created on Jan 25, 2015

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
        expLen = 2
        expA = [1, 2]

        # act
        actLen = self.testedobj.removeDuplicates(A)

        # assert
        self.assertEqual(expLen, actLen)
        self.assertEqual(expA, A)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
