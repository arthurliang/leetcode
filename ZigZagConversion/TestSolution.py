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


    def testConvertWhenStringIsNullandNRowis1_TC1(self):
        # arrange
        s = ""
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringIsNotNullandNRowis1_TC2(self):
        # arrange
        s = "a"
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)



    def testConvertWhenStringIsNotNullandNRowis1_TC3(self):
        # arrange
        s = "ab"
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasNlettersAndNRowisN_TC1(self):
        # arrange
        s = "a"
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasNlettersAndNRowisN_TC2(self):
        # arrange
        s = "ab"
        nRows = 2
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()