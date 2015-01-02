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


    def testLengthOfLastWordWhenLastWordDosntExist_TC1(self):
        # arrange
        s = ""
        expRslt = 0

        # act
        actRslt = self.testedobj.lengthOfLastWord(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testLengthOfLastWordWhenLastWordDosntExist_TC2(self):
        # arrange
        s = "    "
        expRslt = 0

        # act
        actRslt = self.testedobj.lengthOfLastWord(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testLengthOfLastWord_TC1(self):
        # arrange
        s = "Hello World"
        expRslt = 5

        # act
        actRslt = self.testedobj.lengthOfLastWord(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testLengthOfLastWord_TC2(self):
        # arrange
        s = " World"
        expRslt = 5

        # act
        actRslt = self.testedobj.lengthOfLastWord(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testLengthOfLastWord_TC3(self):
        # arrange
        s = "hello "
        expRslt = 5

        # act
        actRslt = self.testedobj.lengthOfLastWord(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testLengthOfLastWord_TC4(self):
        # arrange
        s = " test "
        expRslt = 4

        # act
        actRslt = self.testedobj.lengthOfLastWord(s)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
