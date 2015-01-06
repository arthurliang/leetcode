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


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()