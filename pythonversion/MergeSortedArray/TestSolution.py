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
        A = [1]
        B = []
        expRslt = [1]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


    def testMerge_TC3(self):
        # arrange
        A = []
        B = [2]
        expRslt = [2]

        # act
        self.testedobj.merge(A, len(A), B, len(B))

        # assert
        self.assertEqual(expRslt, A)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()