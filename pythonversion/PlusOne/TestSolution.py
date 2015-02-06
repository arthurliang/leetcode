'''
Created on Feb 5, 2015

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


    def testPlusOne_TC1(self):
        #arrange
        digits = [6]
        expRslt = [7]

        #act
        actRslt = self.testedobj.plusOne(digits)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testPlusOne_TC2(self):
        #arrange
        digits = [9]
        expRslt = [1,0]

        #act
        actRslt = self.testedobj.plusOne(digits)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testPlusOne_TC3(self):
        #arrange
        digits = [9,9]
        expRslt = [1,0,0]

        #act
        actRslt = self.testedobj.plusOne(digits)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
