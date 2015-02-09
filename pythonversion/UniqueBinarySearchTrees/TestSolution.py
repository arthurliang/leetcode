'''
Created on Feb 9, 2015

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


    def testNumTrees_TC1(self):
        # arrange
        n = 0
        expRslt = 0

        # act
        actRslt = self.testedobj.numTrees(n)

        # assert
        self.assertEqual(expRslt, actRslt)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()