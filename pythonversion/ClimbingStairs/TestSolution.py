'''
Created on Feb 5, 2015

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


    def testClimbStairs_TC1(self):
        #arrange
        n = 1
        expRslt = 1

        #act
        actRslt = self.testedobj.climbStairs(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testClimbStairs_TC2(self):
        #arrange
        n = 2
        expRslt = 2

        #act
        actRslt = self.testedobj.climbStairs(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testClimbStairs_TC3(self):
        #arrange
        n = 3
        expRslt = 3

        #act
        actRslt = self.testedobj.climbStairs(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testClimbStairs_TC4(self):
        #arrange
        n = 4
        expRslt = 5

        #act
        actRslt = self.testedobj.climbStairs(n)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testClimbStairs_TC5(self):
        #arrange
        n = 5
        expRslt = 8

        #act
        actRslt = self.testedobj.climbStairs(n)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
