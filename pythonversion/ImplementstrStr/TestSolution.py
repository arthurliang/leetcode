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


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
