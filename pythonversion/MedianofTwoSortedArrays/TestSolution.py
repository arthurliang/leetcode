'''
Created on Feb 16, 2015

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


    def testFindMedianSortedArrays_TC1(self):
        # arrange
        A = []
        B = [1]
        expRslt = 1

        # act
        actRslt = self.testedobj.findMedianSortedArrays(A, B)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()