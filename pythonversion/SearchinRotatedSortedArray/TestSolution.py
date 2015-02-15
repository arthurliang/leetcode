'''
Created on Feb 15, 2015

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


    def testSearch_TC1(self):
        # arrange
        A = []
        target = 0
        expRslt = -1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()