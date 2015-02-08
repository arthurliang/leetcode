'''
Created on Feb 8, 2015

@author: Arthur
'''
import unittest
import Solution
from utility import BinTree


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testBuildTree_TC1(self):
        # arrange
        preorder = []
        inorder = []
        expRst = None

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        self.assertEqual(expRst, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()