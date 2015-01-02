'''
Created on Dec 21, 2014

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


    def testConvertToTitleWhenNumIs1(self):
        # arrange
        num = 1
        expRslt = "A"

        # act
        actRslt = self.testedobj.convertToTitle(num)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitleWhenNumIs2(self):
        # arrange
        num = 2
        expRslt = "B"

        # act
        actRslt = self.testedobj.convertToTitle(num)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitleWhenNumIs26(self):
        # arrange
        num = 26
        expRslt = "Z"

        # act
        actRslt = self.testedobj.convertToTitle(num)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitleWhenNumIs27(self):
        # arrange
        num = 27
        expRslt = "AA"

        # act
        actRslt = self.testedobj.convertToTitle(num)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitleWhenNumIs28(self):
        # arrange
        num = 28
        expRslt = "AB"

        # act
        actRslt = self.testedobj.convertToTitle(num)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitleWhenNumIs229(self):
        # arrange
        num = 256
        expRslt = "IV"

        # act
        actRslt = self.testedobj.convertToTitle(num)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitleWhenNumIs208827064597(self):
        # arrange
        num = 208827064597
        expRslt = "YYYYYYZU"

        # act
        actRslt = self.testedobj.convertToTitle(num)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
