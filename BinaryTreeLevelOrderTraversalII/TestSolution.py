'''
Created on Dec 13, 2014

@author: Arthur
'''
import unittest
import Solution
import BinTree


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        pass


    def testlevelOrderForNullTree(self):
        # arrange
        expRst = []

        # act
        actRslt = self.testedobj.levelOrder(None)

        # assert
        self.assertEqual(expRst, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()