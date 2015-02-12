'''
Created on Feb 12, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.BinTree import BinTree


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testIsValidBST_TC1(self):
        # arrange
        expRslt = True

        # act
        actRslt = self.testedobj.isValidBST(None)

        # assert
        self.assertEqual(expRslt, actRslt)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()