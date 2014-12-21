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
        pass


    def testConvertToTitleWhenNumIsNotValid(self):
        # arrange
        num = 0
        expRslt = None

        # act
        actRslt = self.testedobj.convertToTitle(num)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
