'''
Created on Jan 1, 2015

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


    def testReverseWhenXis0(self):
        # arrange
        x = 0
        expRslt = 0

        # act
        actRslt = self.testedobj.reverse(x)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testReverseWhenXis123(self):
        # arrange
        x = 123
        expRslt = 321

        # act
        actRslt = self.testedobj.reverse(x)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testReverseWhenXisNeg123(self):
        # arrange
        x = -123
        expRslt = -321

        # act
        actRslt = self.testedobj.reverse(x)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testReverseWhenXis1534236469(self):
        # arrange
        x = 1534236469
        expRslt = 0

        # act
        actRslt = self.testedobj.reverse(x)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testReverseWhenXisNeg2147483648(self):
        # arrange
        x = -2147483648
        expRslt = 0

        # act
        actRslt = self.testedobj.reverse(x)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()