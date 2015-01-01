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


    def testMajorityElement_TC1(self):
        #arrange
        num = [1]
        expRslt = 1

        #act
        actRslt = self.testedobj.majorityElement(num)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
