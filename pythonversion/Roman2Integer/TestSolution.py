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


    def testRomanToIntWhenSisI(self):
        # arrange
        s = 'I'
        expRslt = 1

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisII(self):
        # arrange
        s = 'II'
        expRslt = 2

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisIII(self):
        # arrange
        s = 'III'
        expRslt = 3

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisX(self):
        # arrange
        s = 'X'
        expRslt = 10

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisXX(self):
        # arrange
        s = 'XX'
        expRslt = 20

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisXXX(self):
        # arrange
        s = 'XXX'
        expRslt = 30

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisC(self):
        # arrange
        s = 'C'
        expRslt = 100

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisCC(self):
        # arrange
        s = 'CC'
        expRslt = 200

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisCCC(self):
        # arrange
        s = 'CCC'
        expRslt = 300

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisM(self):
        # arrange
        s = 'M'
        expRslt = 1000

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisMMM(self):
        # arrange
        s = 'MMM'
        expRslt = 3000

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisV(self):
        # arrange
        s = 'V'
        expRslt = 5

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisL(self):
        # arrange
        s = 'L'
        expRslt = 50

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisD(self):
        # arrange
        s = 'D'
        expRslt = 500

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisIV(self):
        # arrange
        s = 'IV'
        expRslt = 4

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisIX(self):
        # arrange
        s = 'IX'
        expRslt = 9

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisXL(self):
        # arrange
        s = 'XL'
        expRslt = 40

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisXC(self):
        # arrange
        s = 'XC'
        expRslt = 90

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisCD(self):
        # arrange
        s = 'CD'
        expRslt = 400

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisCM(self):
        # arrange
        s = 'CM'
        expRslt = 900

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisMMMDCCCLXXXVIII(self):
        # arrange
        s = 'MMMDCCCLXXXVIII'
        expRslt = 3888

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testRomanToIntWhenSisMMMCMXCIX(self):
        # arrange
        s = 'MMMCMXCIX'
        expRslt = 3999

        # act
        actRslt = self.testedobj.romanToInt(s)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()