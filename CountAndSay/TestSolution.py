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


    def testCountAndSayWhenNis1(self):
        #arrange
        n = 1
        expRslt = "11"

        #act
        actRslt = self.testedobj.countAndSay(n)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
