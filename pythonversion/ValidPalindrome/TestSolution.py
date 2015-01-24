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
        s = ''
        expRslt = True

        # act
        actRslt = self.testedobj.isPalindrome(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC2(self):
        # arrange
        s = "A man, a plan, a canal: Panama"
        expRslt = True

        # act
        actRslt = self.testedobj.isPalindrome(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC3(self):
        # arrange
        s = "race a car"
        expRslt = False

        # act
        actRslt = self.testedobj.isPalindrome(s)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
