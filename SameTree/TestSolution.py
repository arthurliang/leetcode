'''
Created on Dec 14, 2014

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


    def testIsSameTreeWhen2NoneTree(self):
        # arrange

        # act
        actRslt = self.testedobj.isSameTree(None, None)

        # assert
        self.assertEqual(True, actRslt)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()