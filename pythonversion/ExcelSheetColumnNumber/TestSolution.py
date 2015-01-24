'''
Created on Jan 24, 2015

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


    def testConvertToTitle_TC1(self):
        # arrange
        s = 'A'
        expRslt = 1

        # act
        actRslt = self.testedobj.titleToNumber(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC2(self):
        # arrange
        s = 'B'
        expRslt = 2

        # act
        actRslt = self.testedobj.titleToNumber(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC3(self):
        # arrange
        s = 'C'
        expRslt = 3

        # act
        actRslt = self.testedobj.titleToNumber(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC4(self):
        # arrange
        s = 'Z'
        expRslt = 26

        # act
        actRslt = self.testedobj.titleToNumber(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC5(self):
        # arrange
        s = 'AA'
        expRslt = 27

        # act
        actRslt = self.testedobj.titleToNumber(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC6(self):
        # arrange
        s = 'AB'
        expRslt = 28

        # act
        actRslt = self.testedobj.titleToNumber(s)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
