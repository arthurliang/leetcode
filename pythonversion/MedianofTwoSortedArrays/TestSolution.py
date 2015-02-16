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
        B = [2]
        expRslt = 2

        # act
        actRslt = self.testedobj.findMedianSortedArrays(A, B)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testFindMedianSortedArrays_TC2(self):
        # arrange
        A = [3]
        B = []
        expRslt = 3

        # act
        actRslt = self.testedobj.findMedianSortedArrays(A, B)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testFindMedianSortedArrays_TC3(self):
        # arrange
        A = [3]
        B = [1, 2]
        expRslt = 2

        # act
        actRslt = self.testedobj.findMedianSortedArrays(A, B)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testFindMedianSortedArrays_TC4(self):
        # arrange
        A = [2]
        B = [1]
        expRslt = 1.5

        # act
        actRslt = self.testedobj.findMedianSortedArrays(A, B)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testFindMedianSortedArrays_TC5(self):
        # arrange
        A = [2,3]
        B = [1,5]
        expRslt = 2.5

        # act
        actRslt = self.testedobj.findMedianSortedArrays(A, B)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testFindMedianSortedArrays_TC6(self):
        # arrange
        A = [2,3]
        B = [1,4,5]
        expRslt = 3

        # act
        actRslt = self.testedobj.findMedianSortedArrays(A, B)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
