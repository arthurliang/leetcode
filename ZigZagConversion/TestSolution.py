'''
Created on Dec 19, 2014

@author: Arthur
'''
import unittest
import Solution

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        pass


    def testConvertWhenStringIsNullandNis1(self):
        # arrange
        s = ""
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()