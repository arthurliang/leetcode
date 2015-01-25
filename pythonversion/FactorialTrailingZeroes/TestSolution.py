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


    def testTrailingZeroes_TC1(self):
        # arrange
        n = 1
        expRslt = 0

        # act
        actRslt = self.testedobj.trailingZeroes(n)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
