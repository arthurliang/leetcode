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


    def testSortColors_TC1(self):
        # arrange
        A = None
        expRslt =  None

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC2(self):
        # arrange
        A = [1,2,0]
        expRslt =  [0,1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC3(self):
        # arrange
        A = [1,0,2,2,0,1]
        expRslt =  [0,0,1,1,2,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
