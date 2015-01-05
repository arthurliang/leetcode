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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()