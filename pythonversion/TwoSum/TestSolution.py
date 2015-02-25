'''
Created on Feb 25, 2015

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


    def testTwoSum_TC1(self):
        # arrange
        num = [2,7,11,15]
        target = 9
        expRslt = (1,2)

        # act
        actRslt = self.testedobj.twoSum(num, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testTwoSum_TC2(self):
        # arrange
        num = [2,5,7]
        target = 9
        expRslt = (1,3)

        # act
        actRslt = self.testedobj.twoSum(num, target)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
