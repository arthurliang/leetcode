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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
