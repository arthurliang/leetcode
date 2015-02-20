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


    def testSolveNQueens_TC2(self):
        # arrange
        numerator = 1
        denominator = 4
        expRslt = "0.25"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC3(self):
        # arrange
        numerator = 2
        denominator = 1
        expRslt = "2"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC4(self):
        # arrange
        numerator = 6
        denominator = 2
        expRslt = "3"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC5(self):
        # arrange
        numerator = 5
        denominator = 2
        expRslt = "2.5"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC6(self):
        # arrange
        numerator = 0
        denominator = 2
        expRslt = "0"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC7(self):
        # arrange
        numerator = 2
        denominator = 3
        expRslt = "0.(6)"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC8(self):
        # arrange
        numerator = 2
        denominator = 6
        expRslt = "0.(3)"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC9(self):
        # arrange
        numerator = 1
        denominator = 7
        expRslt = "0.(142857)"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC10(self):
        # arrange
        numerator = 1
        denominator = 9
        expRslt = "0.(1)"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC11(self):
        # arrange
        numerator = 1
        denominator = 333
        expRslt = "0.(003)"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC12(self):
        # arrange
        numerator = -5
        denominator = 6
        expRslt = "-0.8(3)"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSolveNQueens_TC13(self):
        # arrange
        numerator = -5
        denominator = 0
        expRslt = "error"

        # act
        actRslt = self.testedobj.fractionToDecimal(numerator, denominator)

        # assert
        self.assertEqual(expRslt, actRslt)



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
