'''
Created on Jan 24, 2015

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


    def testMerge_TC1(self):
        # arrange
        A = []
        B = []
        expRslt = []

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


    def testMerge_TC2(self):
        # arrange
        A = [0]
        B = [2]
        expRslt = [2]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


    def testMerge_TC3(self):
        # arrange
        A = [1]
        B = []
        expRslt = [1]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


    def testMerge_TC4(self):
        # arrange
        A = [3, 0]
        B = [3]
        expRslt = [3, 3]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


    def testMerge_TC5(self):
        # arrange
        A = [4, 0]
        B = [3]
        expRslt = [3, 4]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


    def testMerge_TC6(self):
        # arrange
        A = [1, 4, 0, 0]
        B = [2, 5]
        expRslt = [1, 2, 4, 5]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


    def testMerge_TC7(self):
        # arrange
        A = [4, 5, 6, 0, 0, 0]
        B = [1, 2, 3]
        expRslt = [1, 2, 3, 4, 5, 6]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


    def testMerge_TC8(self):
        # arrange
        A = [0, 0, 0, 0, 0]
        B = [1, 2, 3, 4, 5]
        expRslt = [1, 2, 3, 4, 5]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()