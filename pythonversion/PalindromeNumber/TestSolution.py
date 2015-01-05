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


    def testIsPalindromeWhenXis0(self):
        # arrange
        x = 0
        expRslt = True

        # act
        actRslt = self.testedobj.isPalindrome(x)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsPalindromeWhenXis11(self):
        # arrange
        x = 12
        expRslt = False

        # act
        actRslt = self.testedobj.isPalindrome(x)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsPalindromeWhenXis123(self):
        # arrange
        x = 123
        expRslt = False

        # act
        actRslt = self.testedobj.isPalindrome(x)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsPalindromeWhenXisNeg123(self):
        # arrange
        x = -123
        expRslt = False

        # act
        actRslt = self.testedobj.isPalindrome(x)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()