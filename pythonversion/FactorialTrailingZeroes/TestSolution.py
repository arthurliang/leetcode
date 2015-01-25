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

    def slowTrailingZeroes(self, n):
        factorial = 1
        i = 2
        while i <= n:
            factorial *= i
            i += 1

        rslt = 0
        while (factorial % 10) == 0:
            rslt += 1
            factorial /= 10

        return rslt


    def testTrailingZeroes_TC1(self):
        # arrange
        n = 1
        expRslt = 0

        # act
        actRslt = self.testedobj.trailingZeroes(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testTrailingZeroes_TC2(self):
        # arrange
        n = 5
        expRslt = 1

        # act
        actRslt = self.testedobj.trailingZeroes(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testTrailingZeroes_TC3(self):
        # arrange
        n = 10
        expRslt = 2

        # act
        actRslt = self.testedobj.trailingZeroes(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testTrailingZeroes_TC4(self):
        # arrange
        n = 15
        expRslt = 3

        # act
        actRslt = self.testedobj.trailingZeroes(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testTrailingZeroes_TC5(self):
        # arrange
        n = 20
        expRslt = 4

        # act
        actRslt = self.testedobj.trailingZeroes(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testTrailingZeroes_TC6(self):
        # arrange
        n = 25
        expRslt = 6

        # act
        actRslt = self.testedobj.trailingZeroes(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testTrailingZeroes_TC7(self):
        # arrange
        n = 30
        expRslt = 7

        # act
        actRslt = self.testedobj.trailingZeroes(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testTrailingZeroes_TC8(self):
        print "{:-^30}".format("start")
        i = 5
        while i < 252:
            expRslt = self.slowTrailingZeroes(i)
            actRslt = self.testedobj.trailingZeroes(i)
            print "n is {:}, Zeroes is {:}".format(i, expRslt)
            self.assertEqual(actRslt, expRslt)
            i += 5
        print "{:-^30}".format("end")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
