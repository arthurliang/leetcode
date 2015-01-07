'''
Created on Jan 6, 2015

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


    def testlongestCommonPrefix_TC1(self):
        # arrange
        strs = []
        expRslt = ""

        # act
        actRslt = self.testedobj.longestCommonPrefix(strs)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testlongestCommonPrefix_TC2(self):
        # arrange
        strs = ["a"]
        expRslt = "a"

        # act
        actRslt = self.testedobj.longestCommonPrefix(strs)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testlongestCommonPrefix_TC3(self):
        # arrange
        strs = ["c","c"]
        expRslt = "c"

        # act
        actRslt = self.testedobj.longestCommonPrefix(strs)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testlongestCommonPrefix_TC4(self):
        # arrange
        strs = ["c","ca"]
        expRslt = "c"

        # act
        actRslt = self.testedobj.longestCommonPrefix(strs)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testlongestCommonPrefix_TC5(self):
        # arrange
        strs = ["ca","c"]
        expRslt = "c"

        # act
        actRslt = self.testedobj.longestCommonPrefix(strs)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testlongestCommonPrefix_TC6(self):
        # arrange
        strs = ["ca","cb"]
        expRslt = "c"

        # act
        actRslt = self.testedobj.longestCommonPrefix(strs)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testlongestCommonPrefix_TC7(self):
        # arrange
        strs = ["ca","cbd"]
        expRslt = "c"

        # act
        actRslt = self.testedobj.longestCommonPrefix(strs)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testlongestCommonPrefix_TC8(self):
        # arrange
        strs = ["cae","cadf","cag"]
        expRslt = "ca"

        # act
        actRslt = self.testedobj.longestCommonPrefix(strs)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()