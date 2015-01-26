'''
Created on Jan 26, 2015

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


    def testStrStr_TC1(self):
        # arrange
        haystack=""
        needle="a"
        expRslt = -1

        # act
        actRslt= self.testedobj.strStr(haystack, needle)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testStrStr_TC2(self):
        # arrange
        haystack="a"
        needle="a"
        expRslt = 0

        # act
        actRslt= self.testedobj.strStr(haystack, needle)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testStrStr_TC3(self):
        # arrange
        haystack="ba"
        needle="a"
        expRslt = 1

        # act
        actRslt= self.testedobj.strStr(haystack, needle)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testStrStr_TC4(self):
        # arrange
        haystack="bcabc"
        needle="abc"
        expRslt = 2

        # act
        actRslt= self.testedobj.strStr(haystack, needle)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testStrStr_TC5(self):
        # arrange
        haystack="bcabcabc"
        needle="abc"
        expRslt = 2

        # act
        actRslt= self.testedobj.strStr(haystack, needle)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testStrStr_TC6(self):
        # arrange
        haystack=""
        needle=""
        expRslt = 0

        # act
        actRslt= self.testedobj.strStr(haystack, needle)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testStrStr_TC7(self):
        # arrange
        haystack="a"
        needle=""
        expRslt = 0

        # act
        actRslt= self.testedobj.strStr(haystack, needle)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testStrStr_TC8(self):
        # arrange
        haystack="mississippi"
        needle="issip"
        expRslt = 4

        # act
        actRslt= self.testedobj.strStr(haystack, needle)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
