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
        n = 1
        expRslt = [["Q"]]

        # act
        actRslt = self.testedobj.solveNQueens(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC2(self):
        # arrange
        n = 2
        expRslt = []

        # act
        actRslt = self.testedobj.solveNQueens(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC3(self):
        # arrange
        n = 3
        expRslt = []

        # act
        actRslt = self.testedobj.solveNQueens(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC4(self):
        # arrange
        n = 4
        expRslt = [[".Q..",
                    "...Q",
                    "Q...",
                    "..Q."],

                    ["..Q.",
                    "Q...",
                    "...Q",
                    ".Q.."]
                   ]

        # act
        actRslt = self.testedobj.solveNQueens(n)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
