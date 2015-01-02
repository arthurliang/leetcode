'''
Created on Jan 1, 2015

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


    def testCountAndSayWhenNis1(self):
        #arrange
        n = 1
        expRslt = "1"

        #act
        actRslt = self.testedobj.countAndSay(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCountAndSayWhenNis2(self):
        #arrange
        n = 2
        expRslt = "11"

        #act
        actRslt = self.testedobj.countAndSay(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCountAndSayWhenNis3(self):
        #arrange
        n = 3
        expRslt = "21"

        #act
        actRslt = self.testedobj.countAndSay(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCountAndSayWhenNis4(self):
        #arrange
        n = 4
        expRslt = "1211"

        #act
        actRslt = self.testedobj.countAndSay(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCountAndSayWhenNis5(self):
        #arrange
        n = 5
        expRslt = "111221"

        #act
        actRslt = self.testedobj.countAndSay(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCountAndSayWhenNi6(self):
        #arrange
        n = 6
        expRslt = "312211"

        #act
        actRslt = self.testedobj.countAndSay(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCountAndSayWhenNis7(self):
        #arrange
        n = 7
        expRslt = "13112221"

        #act
        actRslt = self.testedobj.countAndSay(n)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
