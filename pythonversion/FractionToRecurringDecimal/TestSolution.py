'''
Created on Jan 5, 2015

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


    def testSolveNQueens_TC1(self):
        # arrange
        numerator = 1
        denominator = 2
        expRslt = "0.5"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
